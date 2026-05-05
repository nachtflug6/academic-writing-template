# Handoff

This folder holds timestamped export bundles used for evidence work, review, and submission handoffs.

## Structure

```
handoff/
├── YYYYMMDD_HHMMSS/             # Timestamped bundle (one per handoff run)
│   ├── manuscript_no_refs.md    # Citation-free manuscript export (LaTeX → Markdown)
│   ├── references.bib           # Filtered bibliography (cited entries only)
│   └── claim_evidence_report.md # Claim-to-evidence mapping and strength audit
└── iterations/                  # Archived or consumed bundles
```

## Workflow

1. **Generate a bundle** — run the handoff script to produce a new timestamped folder:
   ```bash
   python3 scripts/generate_handoff.py
   ```
2. **Work from the bundle** — agents and reviewers read from the latest `YYYYMMDD_HHMMSS/` folder. The citation-free manuscript (`manuscript_no_refs.md`) and evidence report (`claim_evidence_report.md`) are the primary inputs.
3. **Archive when done** — once a bundle has been consumed (feedback integrated, review complete), move it to `iterations/` to keep the root clean.

## Bundle Contents

| File | Purpose |
|---|---|
| `manuscript_no_refs.md` | Full manuscript as readable Markdown; all `\cite{}` commands stripped; figures and tables replaced with placeholders |
| `references.bib` | BibTeX subset containing only the entries actually cited in the manuscript |
| `claim_evidence_report.md` | Paragraph-level claim audit with evidence strength ratings (Strong / Moderate / Weak / No match) |

## Authority

Handoff files are the **highest authority** for research content. When agents work on evidence, claim support, or review tasks, they should read from the most recent bundle in this folder rather than the raw LaTeX sources.
