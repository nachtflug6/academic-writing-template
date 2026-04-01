#!/usr/bin/env python3
"""Generate citekey -> anchored claims report from thesis LaTeX sources.

Stage-1 scope only:
- Extract citation occurrences and local claim snippets.
- No bibliography metadata enrichment.
- No online verification or support-quality assessment.
"""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT_ROOT = ROOT / "manuscript"
MAIN_TEX = MANUSCRIPT_ROOT / "main.tex"
OUTPUT_DIR = ROOT / "evidence" / "claims"


INCLUDE_RE = re.compile(r"\\(include|input)\s*\{([^}]+)\}")
# Common LaTeX citation forms. This repo mostly uses \cite{}, but we support variants.
CITE_CMD_RE = re.compile(r"\\([A-Za-z]*cite[A-Za-z*]*)\s*((?:\[[^\]]*\]\s*)*)\{")

SENT_BOUNDARY = ".!?"


@dataclass
class Occurrence:
    file_path: str
    line: int
    column: int
    macro: str
    citekey: str
    grouped_citation: bool
    raw_context: str
    claim: str
    flags: List[str] = field(default_factory=list)


@dataclass
class CitekeyBucket:
    occurrence_count: int = 0
    claims: List[str] = field(default_factory=list)
    claim_locations: Dict[str, List[str]] = field(default_factory=lambda: defaultdict(list))
    claim_flags: Dict[str, Set[str]] = field(default_factory=lambda: defaultdict(set))


def strip_comments_preserve(text: str) -> str:
    """Strip LaTeX comments while preserving text length and line positions."""
    out_chars: List[str] = []
    i = 0
    length = len(text)
    while i < length:
        ch = text[i]
        if ch == "%":
            # Count backslashes immediately before % to determine escaping.
            backslashes = 0
            j = i - 1
            while j >= 0 and text[j] == "\\":
                backslashes += 1
                j -= 1
            escaped = (backslashes % 2) == 1
            if not escaped:
                # Replace comment text with spaces until newline so offsets stay stable.
                while i < length and text[i] != "\n":
                    out_chars.append(" ")
                    i += 1
                continue
        out_chars.append(ch)
        i += 1
    return "".join(out_chars)


def normalize_include_target(target: str) -> str:
    target = target.strip()
    if not target.endswith(".tex"):
        target = f"{target}.tex"
    return target


def resolve_tex_path(current_file: Path, include_target: str) -> Optional[Path]:
    target = normalize_include_target(include_target)

    # Try relative to current file first, then manuscript root.
    candidates = [
        (current_file.parent / target).resolve(),
        (MANUSCRIPT_ROOT / target).resolve(),
        (ROOT / target).resolve(),
    ]

    for path in candidates:
        try:
            path.relative_to(ROOT)
        except ValueError:
            continue
        if path.exists() and path.is_file():
            return path
    return None


def discover_include_graph(root_file: Path) -> List[Path]:
    ordered: List[Path] = []
    visited: Set[Path] = set()

    def walk(path: Path) -> None:
        path = path.resolve()
        if path in visited:
            return
        visited.add(path)
        ordered.append(path)

        text = path.read_text(encoding="utf-8", errors="replace")
        text = strip_comments_preserve(text)

        for match in INCLUDE_RE.finditer(text):
            include_target = match.group(2)
            included = resolve_tex_path(path, include_target)
            if included is not None:
                walk(included)

    walk(root_file)
    return ordered


def line_starts(text: str) -> List[int]:
    starts = [0]
    for m in re.finditer(r"\n", text):
        starts.append(m.end())
    return starts


def pos_to_line_col(starts: List[int], pos: int) -> Tuple[int, int]:
    lo = 0
    hi = len(starts) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if starts[mid] <= pos:
            lo = mid + 1
        else:
            hi = mid - 1
    line_idx = max(0, hi)
    line_start = starts[line_idx]
    return line_idx + 1, (pos - line_start) + 1


def find_matching_brace(text: str, open_idx: int) -> Optional[int]:
    depth = 0
    for i in range(open_idx, len(text)):
        ch = text[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i
    return None


def find_prev_boundary(text: str, pos: int) -> int:
    i = max(0, pos)
    while i > 0:
        ch = text[i]
        prev = text[i - 1] if i - 1 >= 0 else ""
        if ch in SENT_BOUNDARY and prev != "\\":
            return i + 1
        if ch == "\n" and i - 1 >= 0 and text[i - 1] == "\n":
            return i + 1
        i -= 1
    return 0


def find_next_boundary(text: str, pos: int) -> int:
    i = min(len(text) - 1, max(0, pos))
    while i < len(text):
        ch = text[i]
        prev = text[i - 1] if i - 1 >= 0 else ""
        if ch in SENT_BOUNDARY and prev != "\\":
            return i + 1
        if ch == "\n" and i + 1 < len(text) and text[i + 1] == "\n":
            return i
        i += 1
    return len(text)


def simplify_latex(text: str) -> str:
    text = text.replace("~", " ")
    text = text.replace("\n", " ")

    # Remove citations from snippets to avoid noise and duplication.
    text = re.sub(r"\\[A-Za-z]*cite[A-Za-z*]*\s*(?:\[[^\]]*\]\s*)*\{[^{}]*\}", " ", text)

    # Unwrap one-argument commands repeatedly, e.g. \emph{...}, \gls{...}
    unwrap_re = re.compile(r"\\[A-Za-z*]+\s*(?:\[[^\]]*\]\s*)?\{([^{}]*)\}")
    for _ in range(6):
        new_text = unwrap_re.sub(r"\1", text)
        if new_text == text:
            break
        text = new_text

    # Remove remaining command names and braces.
    text = re.sub(r"\\[A-Za-z*]+", " ", text)
    text = text.replace("{", " ").replace("}", " ")

    # Keep punctuation but normalize whitespace.
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def canonical_for_dedup(text: str) -> str:
    t = text.lower()
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def is_near_duplicate(a: str, b: str) -> bool:
    if not a or not b:
        return False
    if canonical_for_dedup(a) == canonical_for_dedup(b):
        return True
    return SequenceMatcher(None, canonical_for_dedup(a), canonical_for_dedup(b)).ratio() >= 0.92


def extract_claim_window(text: str, cite_start: int, cite_end: int) -> Tuple[str, List[str], str]:
    flags: List[str] = []

    sent_start = find_prev_boundary(text, cite_start)
    sent_end = find_next_boundary(text, cite_end)
    sentence = text[sent_start:sent_end]

    # Keep a local raw window for debugging/traceability.
    context_start = max(0, sent_start - 220)
    context_end = min(len(text), sent_end + 220)
    raw_context = text[context_start:context_end]

    # Include previous sentence if cite appears near sentence start.
    lead = text[sent_start:cite_start]
    if len(simplify_latex(lead)) <= 20 and sent_start > 0:
        prev_start = find_prev_boundary(text, max(0, sent_start - 2))
        prev = text[prev_start:sent_start]
        if simplify_latex(prev):
            sentence = prev + " " + sentence
            flags.append("claim likely spans multiple sentences")

    # Include next short sentence if cite is at sentence end and next appears tightly coupled.
    tail = text[cite_end:sent_end]
    if len(simplify_latex(tail)) <= 18 and sent_end < len(text):
        next_end = find_next_boundary(text, min(len(text) - 1, sent_end + 1))
        nxt = text[sent_end:next_end]
        if 0 < len(simplify_latex(nxt)) <= 160:
            sentence = sentence + " " + nxt
            flags.append("claim likely spans multiple sentences")

    claim = simplify_latex(sentence)

    # Boundary ambiguity heuristics.
    if not claim or len(claim.split()) < 5:
        flags.append("ambiguous claim boundary")

    if len(claim) > 450:
        flags.append("ambiguous claim boundary")

    return claim, sorted(set(flags)), raw_context


def parse_citations_in_file(path: Path) -> Tuple[List[Occurrence], int]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    text = strip_comments_preserve(raw)
    starts = line_starts(text)

    occurrences: List[Occurrence] = []
    unresolved = 0

    for m in CITE_CMD_RE.finditer(text):
        macro = m.group(1)
        open_brace_idx = m.end() - 1
        close_brace_idx = find_matching_brace(text, open_brace_idx)
        if close_brace_idx is None:
            unresolved += 1
            continue

        payload = text[open_brace_idx + 1 : close_brace_idx]
        keys = [k.strip() for k in payload.split(",") if k.strip()]
        if not keys:
            unresolved += 1
            continue

        line, col = pos_to_line_col(starts, m.start())
        grouped = len(keys) > 1

        claim, claim_flags, raw_context = extract_claim_window(text, m.start(), close_brace_idx + 1)

        line_text = raw.splitlines()[line - 1] if line - 1 < len(raw.splitlines()) else ""
        context_flags: Set[str] = set(claim_flags)

        if grouped:
            context_flags.add("grouped citation")

        # Lightweight location/context flags.
        window = text[max(0, m.start() - 240) : min(len(text), close_brace_idx + 240)].lower()
        if "\\caption{" in window:
            context_flags.add("citation in caption/footnote/table")
        if "\\footnote{" in window:
            context_flags.add("citation in caption/footnote/table")
        if "\\begin{table" in window or "/tables/" in str(path).replace("\\", "/"):
            context_flags.add("citation in caption/footnote/table")
        if line_text.lstrip().startswith("\\item"):
            context_flags.add("citation in list item")

        for key in keys:
            occurrences.append(
                Occurrence(
                    file_path=str(path.relative_to(ROOT)).replace("\\", "/"),
                    line=line,
                    column=col,
                    macro=macro,
                    citekey=key,
                    grouped_citation=grouped,
                    raw_context=simplify_latex(raw_context),
                    claim=claim,
                    flags=sorted(context_flags),
                )
            )

    return occurrences, unresolved


def build_reports(occurrences: List[Occurrence], unresolved_count: int) -> Tuple[dict, str, List[dict]]:
    by_key: Dict[str, CitekeyBucket] = defaultdict(CitekeyBucket)
    csv_rows: List[dict] = []

    ambiguous_cases = 0
    total_claim_snippets = 0

    for occ in occurrences:
        bucket = by_key[occ.citekey]
        bucket.occurrence_count += 1

        claim_text = occ.claim.strip()
        if not claim_text:
            claim_text = "[No clean claim text extracted]"
            if "ambiguous claim boundary" not in occ.flags:
                occ.flags.append("ambiguous claim boundary")

        added = False
        duplicate_match: Optional[str] = None
        for existing in bucket.claims:
            if is_near_duplicate(existing, claim_text):
                duplicate_match = existing
                break

        if duplicate_match is None:
            bucket.claims.append(claim_text)
            added = True
            target_claim = claim_text
        else:
            target_claim = duplicate_match
            bucket.claim_flags[target_claim].add("repeated near-duplicate claim collapsed")

        location = f"{occ.file_path}:{occ.line}"
        if location not in bucket.claim_locations[target_claim]:
            bucket.claim_locations[target_claim].append(location)

        for fl in occ.flags:
            bucket.claim_flags[target_claim].add(fl)

        if "ambiguous claim boundary" in occ.flags:
            ambiguous_cases += 1

        if added:
            total_claim_snippets += 1

    citekey_items = []
    for key in sorted(by_key):
        bucket = by_key[key]
        claim_entries = []
        for claim in bucket.claims:
            flags = sorted(bucket.claim_flags.get(claim, set()))
            locs = bucket.claim_locations.get(claim, [])
            claim_entries.append(
                {
                    "text": claim,
                    "locations": locs,
                    "flags": flags,
                }
            )
            csv_rows.append(
                {
                    "citekey": key,
                    "claim": claim,
                    "occurrence_count": bucket.occurrence_count,
                    "distinct_claim_count": len(bucket.claims),
                    "locations": " | ".join(locs),
                    "flags": " | ".join(flags),
                }
            )

        citekey_items.append(
            {
                "citekey": key,
                "occurrence_count": bucket.occurrence_count,
                "distinct_claim_count": len(bucket.claims),
                "claims": [c["text"] for c in claim_entries],
                "claim_details": claim_entries,
            }
        )

    top20 = sorted(citekey_items, key=lambda x: x["distinct_claim_count"], reverse=True)[:20]

    summary = {
        "total_citation_occurrences": len(occurrences),
        "total_unique_citekeys": len(citekey_items),
        "total_extracted_claim_snippets": total_claim_snippets,
        "ambiguous_extraction_cases": ambiguous_cases,
        "unresolved_citation_syntax_cases": unresolved_count,
        "top_20_citekeys_by_distinct_claims": [
            {
                "citekey": item["citekey"],
                "distinct_claim_count": item["distinct_claim_count"],
                "occurrence_count": item["occurrence_count"],
            }
            for item in top20
        ],
    }

    report = {
        "summary": summary,
        "citekeys": citekey_items,
        "notes": [
            "Stage-1 extraction only: no bibliography metadata enrichment.",
            "No online verification or source-quality assessment performed.",
        ],
    }

    md = render_markdown(report)
    return report, md, csv_rows


def render_markdown(report: dict) -> str:
    lines: List[str] = []
    summary = report["summary"]

    lines.append("# Citekey to Anchored Claims Report")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- Total citation occurrences: {summary['total_citation_occurrences']}")
    lines.append(f"- Total unique citekeys: {summary['total_unique_citekeys']}")
    lines.append(f"- Total extracted claim snippets: {summary['total_extracted_claim_snippets']}")
    lines.append(f"- Ambiguous extraction cases: {summary['ambiguous_extraction_cases']}")
    lines.append(f"- Unresolved citation syntax cases: {summary['unresolved_citation_syntax_cases']}")
    lines.append("")
    lines.append("## Top 20 Citekeys by Distinct Claims")
    for item in summary["top_20_citekeys_by_distinct_claims"]:
        lines.append(
            f"- {item['citekey']}: {item['distinct_claim_count']} distinct claims ({item['occurrence_count']} occurrences)"
        )

    lines.append("")
    lines.append("## Citekey Blocks")

    for item in report["citekeys"]:
        lines.append("")
        lines.append(f"### {item['citekey']}")
        lines.append(f"- Occurrence count: {item['occurrence_count']}")
        lines.append(f"- Distinct claim count: {item['distinct_claim_count']}")
        for claim in item.get("claim_details", []):
            lines.append(f"- {claim['text']}")
            if claim.get("locations"):
                lines.append(f"  - locations: {', '.join(claim['locations'])}")
            if claim.get("flags"):
                lines.append(f"  - flags: {', '.join(claim['flags'])}")

    lines.append("")
    lines.append("## Notes")
    for note in report.get("notes", []):
        lines.append(f"- {note}")

    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    scoped_files = discover_include_graph(MAIN_TEX)
    # Keep only TeX files under manuscript root from the include graph.
    scoped_files = [p for p in scoped_files if p.suffix == ".tex" and MANUSCRIPT_ROOT in p.parents or p == MAIN_TEX]

    all_occurrences: List[Occurrence] = []
    unresolved_total = 0

    for path in scoped_files:
        occs, unresolved = parse_citations_in_file(path)
        all_occurrences.extend(occs)
        unresolved_total += unresolved

    report, markdown_text, csv_rows = build_reports(all_occurrences, unresolved_total)

    json_path = OUTPUT_DIR / "citekey_claim_report.json"
    md_path = OUTPUT_DIR / "citekey_claim_report.md"
    csv_path = OUTPUT_DIR / "citekey_claim_report.csv"

    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    md_path.write_text(markdown_text, encoding="utf-8")

    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "citekey",
                "claim",
                "occurrence_count",
                "distinct_claim_count",
                "locations",
                "flags",
            ],
        )
        writer.writeheader()
        writer.writerows(csv_rows)

    print(f"Wrote: {md_path}")
    print(f"Wrote: {json_path}")
    print(f"Wrote: {csv_path}")
    print(
        "Summary: "
        f"occurrences={report['summary']['total_citation_occurrences']}, "
        f"unique_citekeys={report['summary']['total_unique_citekeys']}, "
        f"distinct_claims={report['summary']['total_extracted_claim_snippets']}"
    )


if __name__ == "__main__":
    main()
