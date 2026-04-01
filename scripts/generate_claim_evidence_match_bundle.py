#!/usr/bin/env python3
"""Generate timestamped claim-evidence match bundle.

This script builds a dated folder in evidence/claims containing:
- consolidated claim-evidence reports,
- per-citekey markdown and json files,
- bibliography metadata extracted from refs/references.bib,
- linked-file references (symlinks where possible) to relevant evidence files.
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
CLAIMS_DIR = ROOT / "evidence" / "claims"
CLAIM_REPORT_JSON = CLAIMS_DIR / "citekey_claim_report.json"
CLAIM_REPORT_MD = CLAIMS_DIR / "citekey_claim_report.md"
CLAIM_REPORT_CSV = CLAIMS_DIR / "citekey_claim_report.csv"
BIB_FILE = ROOT / "refs" / "references.bib"

EVIDENCE_DIRS = [
    ROOT / "evidence" / "literature" / "extracts",
    ROOT / "evidence" / "literature" / "summaries",
    ROOT / "evidence" / "reports",
]


@dataclass
class BibEntry:
    citekey: str
    entry_type: str
    fields: Dict[str, str]


def collapse_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def strip_wrapping(s: str) -> str:
    s = s.strip()
    while True:
        if len(s) >= 2 and ((s[0] == "{" and s[-1] == "}") or (s[0] == '"' and s[-1] == '"')):
            s = s[1:-1].strip()
            continue
        break
    return collapse_ws(s)


def parse_bib_fields(body: str) -> Dict[str, str]:
    parts: List[str] = []
    buf: List[str] = []
    depth = 0
    in_quotes = False
    i = 0
    while i < len(body):
        ch = body[i]
        if ch == '"' and (i == 0 or body[i - 1] != "\\"):
            in_quotes = not in_quotes
            buf.append(ch)
        elif not in_quotes and ch == "{":
            depth += 1
            buf.append(ch)
        elif not in_quotes and ch == "}":
            depth = max(0, depth - 1)
            buf.append(ch)
        elif not in_quotes and depth == 0 and ch == ",":
            part = "".join(buf).strip()
            if part:
                parts.append(part)
            buf = []
        else:
            buf.append(ch)
        i += 1
    tail = "".join(buf).strip()
    if tail:
        parts.append(tail)

    out: Dict[str, str] = {}
    for p in parts:
        if "=" not in p:
            continue
        k, v = p.split("=", 1)
        key = k.strip().lower()
        val = strip_wrapping(v.strip())
        out[key] = val
    return out


def parse_bib_file(path: Path) -> Dict[str, BibEntry]:
    text = path.read_text(encoding="utf-8", errors="replace")
    entries: Dict[str, BibEntry] = {}

    i = 0
    n = len(text)
    while i < n:
        at = text.find("@", i)
        if at < 0:
            break

        m = re.match(r"@([A-Za-z]+)\s*\{", text[at:])
        if not m:
            i = at + 1
            continue
        entry_type = m.group(1).lower()
        open_brace = at + m.end() - 1

        depth = 0
        j = open_brace
        while j < n:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        if j >= n:
            break

        content = text[open_brace + 1 : j].strip()
        comma = content.find(",")
        if comma == -1:
            i = j + 1
            continue

        citekey = content[:comma].strip()
        body = content[comma + 1 :].strip()
        fields = parse_bib_fields(body)

        if citekey:
            entries[citekey] = BibEntry(citekey=citekey, entry_type=entry_type, fields=fields)

        i = j + 1

    return entries


def load_claim_report(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def first_author_surname(author_field: str) -> Optional[str]:
    if not author_field:
        return None
    first = author_field.split(" and ")[0].strip()
    if not first:
        return None
    if "," in first:
        return first.split(",", 1)[0].strip()
    tokens = first.split()
    return tokens[-1].strip() if tokens else None


def line_number_from_pos(text: str, pos: int) -> int:
    return text[:pos].count("\n") + 1


def collect_snippets_for_direct(text: str, key: str, max_hits: int = 2) -> List[dict]:
    snippets = []
    pattern = re.compile(re.escape(key), flags=re.IGNORECASE)
    for idx, m in enumerate(pattern.finditer(text)):
        if idx >= max_hits:
            break
        line = line_number_from_pos(text, m.start())
        start = max(0, text.rfind("\n", 0, m.start()) + 1)
        end_nl = text.find("\n", m.end())
        if end_nl == -1:
            end_nl = len(text)
        snippet = collapse_ws(text[start:end_nl])
        snippets.append({"line": line, "text": snippet})
    return snippets


def collect_snippets_for_author_year(text: str, surname: str, year: str, max_hits: int = 2) -> List[dict]:
    snippets = []
    lines = text.splitlines()
    surname_l = surname.lower()
    year_l = year.lower()
    for i, ln in enumerate(lines):
        low = ln.lower()
        if surname_l in low and year_l in low:
            snippets.append({"line": i + 1, "text": collapse_ws(ln)})
            if len(snippets) >= max_hits:
                break
    return snippets


def scan_evidence_files() -> List[Path]:
    files: List[Path] = []
    for base in EVIDENCE_DIRS:
        if not base.exists():
            continue
        files.extend(sorted(base.rglob("*.md")))
    return files


def safe_rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def match_evidence_for_citekey(citekey: str, bib: Optional[BibEntry], evidence_files: List[Path]) -> List[dict]:
    matches: List[dict] = []

    surname = None
    year = None
    if bib:
        surname = first_author_surname(bib.fields.get("author", ""))
        year = bib.fields.get("year", "")

    for f in evidence_files:
        text = f.read_text(encoding="utf-8", errors="replace")
        direct = re.search(re.escape(citekey), text, flags=re.IGNORECASE) is not None
        ay = False
        if not direct and surname and year:
            low = text.lower()
            ay = surname.lower() in low and year.lower() in low

        if not direct and not ay:
            continue

        if direct:
            method = "direct-citekey-token"
            confidence = "high"
            snippets = collect_snippets_for_direct(text, citekey)
        else:
            method = "author-year-heuristic"
            confidence = "medium"
            snippets = collect_snippets_for_author_year(text, surname or "", year or "")

        matches.append(
            {
                "file": safe_rel(f),
                "method": method,
                "confidence": confidence,
                "snippets": snippets,
            }
        )

    return matches


def bib_metadata(bib: Optional[BibEntry]) -> dict:
    if bib is None:
        return {
            "metadata_status": "missing_bib_entry",
            "entry_type": None,
            "author": None,
            "year": None,
            "title": None,
            "venue": None,
            "doi": None,
            "url": None,
        }

    venue = (
        bib.fields.get("journal")
        or bib.fields.get("booktitle")
        or bib.fields.get("publisher")
        or bib.fields.get("institution")
        or bib.fields.get("series")
    )

    return {
        "metadata_status": "ok",
        "entry_type": bib.entry_type,
        "author": bib.fields.get("author"),
        "year": bib.fields.get("year"),
        "title": bib.fields.get("title"),
        "venue": venue,
        "doi": bib.fields.get("doi"),
        "url": bib.fields.get("url"),
    }


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, data: dict | list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def render_per_citekey_md(obj: dict) -> str:
    lines: List[str] = []
    lines.append(f"# {obj['citekey']}")
    lines.append("")
    lines.append("## Claim Stats")
    lines.append(f"- Occurrence count: {obj['occurrence_count']}")
    lines.append(f"- Distinct claim count: {obj['distinct_claim_count']}")
    lines.append("")

    bm = obj["bibliography_metadata"]
    lines.append("## Bibliography Metadata")
    lines.append(f"- Metadata status: {bm['metadata_status']}")
    lines.append(f"- Entry type: {bm['entry_type']}")
    lines.append(f"- Author: {bm['author']}")
    lines.append(f"- Year: {bm['year']}")
    lines.append(f"- Title: {bm['title']}")
    lines.append(f"- Venue: {bm['venue']}")
    lines.append(f"- DOI: {bm['doi']}")
    lines.append(f"- URL: {bm['url']}")
    lines.append("")

    lines.append("## Claims")
    for cl in obj.get("claims", []):
        lines.append(f"- {cl['text']}")
        if cl.get("locations"):
            lines.append(f"  - locations: {', '.join(cl['locations'])}")
        if cl.get("flags"):
            lines.append(f"  - flags: {', '.join(cl['flags'])}")
    lines.append("")

    lines.append("## Related Evidence")
    if not obj.get("related_evidence"):
        lines.append("- No related evidence file match found.")
    else:
        for ev in obj["related_evidence"]:
            lines.append(f"- file: {ev['file']}")
            lines.append(f"  - match_method: {ev['method']}")
            lines.append(f"  - confidence: {ev['confidence']}")
            for sn in ev.get("snippets", []):
                lines.append(f"  - snippet (line {sn['line']}): {sn['text']}")

    return "\n".join(lines) + "\n"


def create_symlink(link: Path, target: Path) -> bool:
    try:
        if link.exists() or link.is_symlink():
            link.unlink()
        link.parent.mkdir(parents=True, exist_ok=True)
        rel_target = os.path.relpath(target, link.parent)
        os.symlink(rel_target, link)
        return True
    except OSError:
        return False


def build_bundle() -> None:
    if not CLAIM_REPORT_JSON.exists():
        raise FileNotFoundError(f"Missing claim report: {CLAIM_REPORT_JSON}")

    date_prefix = dt.date.today().isoformat()
    bundle = CLAIMS_DIR / f"{date_prefix}_claim-match"
    per_key_dir = bundle / "per-citekey"
    linked_dir = bundle / "linked-files"
    metadata_dir = bundle / "metadata"

    bundle.mkdir(parents=True, exist_ok=True)
    per_key_dir.mkdir(parents=True, exist_ok=True)
    linked_dir.mkdir(parents=True, exist_ok=True)
    metadata_dir.mkdir(parents=True, exist_ok=True)

    claim_report = load_claim_report(CLAIM_REPORT_JSON)
    bib_index = parse_bib_file(BIB_FILE)
    evidence_files = scan_evidence_files()

    # Keep canonical claim files linked in bundle.
    fixed_claim_files = [CLAIM_REPORT_MD, CLAIM_REPORT_JSON, CLAIM_REPORT_CSV]

    all_citekeys = claim_report.get("citekeys", [])
    consolidated: List[dict] = []
    bibliography_extract: Dict[str, dict] = {}
    citekey_to_evidence_index: Dict[str, dict] = {}
    symlink_results: List[dict] = []

    csv_rows: List[dict] = []

    for item in all_citekeys:
        key = item["citekey"]
        bib = bib_index.get(key)
        bm = bib_metadata(bib)
        bibliography_extract[key] = bm

        claim_details = item.get("claim_details", [])
        related = match_evidence_for_citekey(key, bib, evidence_files)

        obj = {
            "citekey": key,
            "occurrence_count": item.get("occurrence_count", 0),
            "distinct_claim_count": item.get("distinct_claim_count", 0),
            "bibliography_metadata": bm,
            "claims": claim_details,
            "related_evidence": related,
            "notes": {
                "stage": "claim-evidence-match",
                "quality_assessment": "not_performed",
                "online_verification": "not_performed",
            },
        }
        consolidated.append(obj)

        md_path = per_key_dir / f"{key}.md"
        json_path = per_key_dir / f"{key}.json"
        write_text(md_path, render_per_citekey_md(obj))
        write_json(json_path, obj)

        citekey_to_evidence_index[key] = {
            "evidence_files": [r["file"] for r in related],
            "match_methods": sorted({r["method"] for r in related}),
            "max_confidence": "high" if any(r["confidence"] == "high" for r in related) else ("medium" if related else "none"),
        }

        for r in related:
            csv_rows.append(
                {
                    "citekey": key,
                    "occurrence_count": obj["occurrence_count"],
                    "distinct_claim_count": obj["distinct_claim_count"],
                    "evidence_file": r["file"],
                    "match_method": r["method"],
                    "confidence": r["confidence"],
                }
            )

    # Build symlinks for canonical claim files and all matched evidence files.
    linked_index = {
        "claims": [],
        "evidence": [],
        "symlink_creation": "attempted",
    }

    for cf in fixed_claim_files:
        if not cf.exists():
            continue
        rel = safe_rel(cf)
        link = linked_dir / rel
        ok = create_symlink(link, cf)
        linked_index["claims"].append({"source": rel, "link": safe_rel(link), "symlinked": ok})
        symlink_results.append({"source": rel, "link": safe_rel(link), "symlinked": ok})

    matched_files = sorted({m["file"] for o in consolidated for m in o.get("related_evidence", [])})
    for rel in matched_files:
        src = ROOT / rel
        if not src.exists():
            linked_index["evidence"].append({"source": rel, "link": None, "symlinked": False})
            continue
        link = linked_dir / rel
        ok = create_symlink(link, src)
        linked_index["evidence"].append({"source": rel, "link": safe_rel(link), "symlinked": ok})
        symlink_results.append({"source": rel, "link": safe_rel(link), "symlinked": ok})

    write_json(metadata_dir / "bibliography_extract.json", bibliography_extract)
    write_json(metadata_dir / "citekey_to_evidence_index.json", citekey_to_evidence_index)
    write_json(linked_dir / "linked_files_index.json", linked_index)

    summary = claim_report.get("summary", {})
    unresolved = [o["citekey"] for o in consolidated if o["bibliography_metadata"]["metadata_status"] != "ok"]
    no_evidence = [o["citekey"] for o in consolidated if not o.get("related_evidence")]

    consolidated_json = {
        "bundle_name": bundle.name,
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "source_claim_report": safe_rel(CLAIM_REPORT_JSON),
        "summary": {
            "total_citekeys": len(consolidated),
            "total_citation_occurrences": summary.get("total_citation_occurrences"),
            "total_extracted_claim_snippets": summary.get("total_extracted_claim_snippets"),
            "citekeys_missing_bibliography_entry": len(unresolved),
            "citekeys_with_no_related_evidence_match": len(no_evidence),
        },
        "citekeys": consolidated,
    }
    write_json(bundle / "consolidated_claim_evidence_report.json", consolidated_json)

    # Consolidated markdown.
    md_lines: List[str] = []
    md_lines.append("# Claim-Evidence Match Bundle")
    md_lines.append("")
    md_lines.append(f"- Bundle: {bundle.name}")
    md_lines.append(f"- Total citekeys: {len(consolidated)}")
    md_lines.append(f"- Total citation occurrences: {summary.get('total_citation_occurrences')}")
    md_lines.append(f"- Total extracted claim snippets: {summary.get('total_extracted_claim_snippets')}")
    md_lines.append(f"- Citekeys missing bibliography entries: {len(unresolved)}")
    md_lines.append(f"- Citekeys with no related evidence file match: {len(no_evidence)}")
    md_lines.append("")
    md_lines.append("## Citekey Overview")
    for o in sorted(consolidated, key=lambda x: x["distinct_claim_count"], reverse=True):
        ev_count = len(o.get("related_evidence", []))
        status = o["bibliography_metadata"]["metadata_status"]
        md_lines.append(
            f"- {o['citekey']}: claims={o['distinct_claim_count']}, occurrences={o['occurrence_count']}, evidence_files={ev_count}, bibliography={status}"
        )
    md_lines.append("")
    md_lines.append("## Missing Bibliography Entries")
    if unresolved:
        for key in unresolved:
            md_lines.append(f"- {key}")
    else:
        md_lines.append("- None")
    md_lines.append("")
    md_lines.append("## No Evidence Match")
    if no_evidence:
        for key in no_evidence:
            md_lines.append(f"- {key}")
    else:
        md_lines.append("- None")
    md_lines.append("")
    md_lines.append("## Notes")
    md_lines.append("- Bibliography metadata was extracted locally from refs/references.bib.")
    md_lines.append("- Matching methods include direct citekey token and author-year heuristic.")
    md_lines.append("- No online verification or source-quality assessment was performed.")

    write_text(bundle / "consolidated_claim_evidence_report.md", "\n".join(md_lines) + "\n")

    # Consolidated CSV.
    csv_path = bundle / "consolidated_claim_evidence_report.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "citekey",
                "occurrence_count",
                "distinct_claim_count",
                "evidence_file",
                "match_method",
                "confidence",
            ],
        )
        writer.writeheader()
        writer.writerows(csv_rows)

    readme_lines = [
        "# Claim-Evidence Match Bundle",
        "",
        f"This bundle was generated from {safe_rel(CLAIM_REPORT_JSON)} and {safe_rel(BIB_FILE)}.",
        "",
        "## Contents",
        "- consolidated_claim_evidence_report.md/json/csv",
        "- per-citekey/: one markdown and one json file per citekey",
        "- metadata/bibliography_extract.json",
        "- metadata/citekey_to_evidence_index.json",
        "- linked-files/: symlink/index references to claim and related evidence files",
        "",
        "## Matching",
        "- high: direct citekey token match in evidence files",
        "- medium: author-year heuristic match in evidence files",
        "- none: no related evidence file match found",
        "",
        "## Constraints",
        "- No online verification performed.",
        "- No source-quality assessment performed.",
        "",
    ]
    write_text(bundle / "README.md", "\n".join(readme_lines))

    manifest = {
        "bundle": bundle.name,
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "inputs": [
            safe_rel(CLAIM_REPORT_JSON),
            safe_rel(CLAIM_REPORT_MD),
            safe_rel(CLAIM_REPORT_CSV),
            safe_rel(BIB_FILE),
            *[safe_rel(p) for p in EVIDENCE_DIRS if p.exists()],
        ],
        "outputs": [
            safe_rel(bundle / "consolidated_claim_evidence_report.md"),
            safe_rel(bundle / "consolidated_claim_evidence_report.json"),
            safe_rel(bundle / "consolidated_claim_evidence_report.csv"),
            safe_rel(bundle / "README.md"),
            safe_rel(bundle / "MANIFEST.json"),
            safe_rel(metadata_dir / "bibliography_extract.json"),
            safe_rel(metadata_dir / "citekey_to_evidence_index.json"),
            safe_rel(linked_dir / "linked_files_index.json"),
        ],
        "counts": {
            "per_citekey_markdown_files": len(list(per_key_dir.glob("*.md"))),
            "per_citekey_json_files": len(list(per_key_dir.glob("*.json"))),
            "symlink_attempts": len(symlink_results),
            "symlink_failures": sum(1 for x in symlink_results if not x["symlinked"]),
        },
    }
    write_json(bundle / "MANIFEST.json", manifest)

    print(f"Bundle: {bundle}")
    print(f"Citekeys: {len(consolidated)}")
    print(f"Missing bib entries: {len(unresolved)}")
    print(f"No evidence matches: {len(no_evidence)}")
    print(f"Per-citekey files: {len(list(per_key_dir.glob('*.md')))} md, {len(list(per_key_dir.glob('*.json')))} json")


if __name__ == "__main__":
    build_bundle()
