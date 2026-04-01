# Academic Writing Workspace Template

This repository is a reusable workspace for academic writing projects.
It is intentionally neutral: thesis, paper, report, survey, or mixed projects are all valid.

## Core Idea

- `manuscript/` is a drop-in area for whatever LaTeX project/template you use.
- `evidence/` stores source-oriented notes and claim support.
- `refs/` stores bibliography sources.
- `project/`, `tasks/`, `standards/`, and `submission/` support planning and compliance.

## Manuscript Folder Is Unconstrained

Put any LaTeX structure inside `manuscript/`:

- a conference paper template,
- a journal submission template,
- a thesis template,
- or multiple drafts in separate subfolders.

The repository does not assume chapter files, `TexFiles/`, or a fixed entry filename.

## Build and Compile

Use the build script with an explicit entry file:

```bash
# Quick single-pass compile
bash ./scripts/compile-thesis.sh quick manuscript/main.tex

# Full compile (pdflatex + optional bib/glossary + pdflatex x2)
bash ./scripts/compile-thesis.sh full manuscript/main.tex

# Clean LaTeX artifacts recursively under manuscript/
bash ./scripts/compile-thesis.sh clean
```

You can also set a default entry:

```bash
export MANUSCRIPT_ENTRY=manuscript/path/to/entry.tex
bash ./scripts/compile-thesis.sh quick
```

## Repository Structure

```
.
├── manuscript/                    # Drop-in LaTeX project workspace
├── refs/                          # Bibliography and reference management artifacts
├── evidence/                      # Source extracts, summaries, claims, reports, experiment notes
├── project/                       # Scope, outline, and project-level framing
├── tasks/                         # Status and backlog tracking
├── standards/                     # Institutional requirements, benchmarks, and feedback logs
├── submission/                    # Submission checklist and packaging notes
├── scripts/                       # Build and utility scripts
├── .github/                       # Agent/editor instructions and prompt assets
└── AGENTS.md                      # Workspace agent behavior
```

## Smart Library Integration

This repo can consume Smart Library over HTTP when available.

```bash
export SMARTLIB_API_URL=http://localhost:8001
python3 scripts/smartlib_smoke_test.py
```
