# Academic Writing Template

This repository is a reusable thesis template workspace.
It separates manuscript text, evidence, planning, and submission assets so writing decisions remain traceable.

## Template Goal

Use this template to start a new thesis project with a structured workflow.

Replace placeholders in:

- `manuscript/TexFiles/settings.tex` (title, author, institution metadata)
- `manuscript/TexFiles/*.tex` (chapter/front-matter content)
- `refs/references.bib` (your bibliography)
- `standards/formatting-requirements.md` (official venue rules)
- `tasks/status.md` (your real progress state)

## How This Repository Works

The workflow is intentionally evidence-first:

1. Define scope and priorities in `project/` and `tasks/`.
2. Collect and synthesize sources in `evidence/`.
3. Write and revise thesis text in `manuscript/`.
4. Keep references in one canonical file: `refs/references.bib`.
5. Check standards and constraints in `standards/`.
6. Prepare packaging and final checks in `submission/`.

The practical rule is simple: final claims belong in `manuscript/`, while supporting reasoning and source work stay in `evidence/`.

## Repository Structure

```
.
├── manuscript/                    # Thesis LaTeX sources, figures, tables, appended papers
├── refs/                          # Bibliography and reference management artifacts
├── evidence/                      # Source extracts, summaries, claims, reports, experiment notes
├── project/                       # Scope, outline, and project-level framing
├── tasks/                         # Status and backlog tracking
├── standards/                     # Institutional requirements, benchmarks, and feedback logs
├── submission/                    # Submission checklist and packaging notes
├── scripts/                       # Build and utility scripts
├── .github/                       # Agent/editor instructions and prompt assets
└── AGENTS.md                      # Template agent behavior
```

### Key Folders

- `manuscript/`
	- Main thesis file and chapter files under `manuscript/TexFiles/`.
	- Figures and tables are maintained as LaTeX inputs under `manuscript/TexFiles/figures/` and `manuscript/TexFiles/tables/`.
	- Appended paper materials are under `manuscript/papers/`.

- `refs/`
	- Canonical bibliography file: `refs/references.bib`.
	- Keep citation keys stable unless intentionally harmonized across the manuscript.

- `evidence/`
	- `evidence/literature/extracts/`: close-to-source excerpts.
	- `evidence/literature/summaries/`: synthesis notes.
	- `evidence/claims/`: claim-to-evidence mapping notes.
	- `evidence/reports/`: thematic analyses and evidence runs.

- `project/`
	- Research brief, dependencies, and outline.

- `tasks/`
	- `tasks/status.md`: current thesis status and milestones.
	- `tasks/backlog.md`: prioritized next actions.

- `standards/`
	- Formatting requirements, structural benchmarks, and feedback logs.
	- Validate assumptions against official institutional guidelines before submission.

- `submission/`
	- Final packaging and checklist artifacts.

## Source of Truth and Editing Boundaries

- Manuscript text source of truth: `manuscript/`.
- Bibliography source of truth: `refs/references.bib`.
- Evidence source of truth: `evidence/`.

Do not mix these roles:

- Do not store draft argumentation in chapter files if it is still evidence work.
- Do not treat evidence notes as final prose.
- Do not rewrite or invent bibliography metadata from memory.

## Build and Compile

Common commands:

```bash
# Quick single-pass compile
bash ./scripts/compile-thesis.sh quick

# Full compile (bib pass included)
bash ./scripts/compile-thesis.sh full

# Clean build artifacts
bash ./scripts/compile-thesis.sh clean
```

If using VS Code tasks, equivalent tasks are available in the workspace task list.

## Smart Library Integration

This repo does not host Smart Library.
It consumes Smart Library over HTTP when available.

Configuration:

```bash
export SMARTLIB_API_URL=http://localhost:8001
```

Smoke test:

```bash
python3 scripts/smartlib_smoke_test.py
```

This checks service health and confirms document listing access.

## Build and Compile

Common commands:

```bash
# Quick single-pass compile
bash ./scripts/compile-thesis.sh quick

# Full compile (bib + glossary + reruns)
bash ./scripts/compile-thesis.sh full

# Clean build artifacts
bash ./scripts/compile-thesis.sh clean
```

## Recommended Working Loop

1. Confirm current priorities in `tasks/status.md`.
2. Pull supporting evidence from `evidence/` (or run a new evidence pass).
3. Apply focused edits in a specific chapter file under `manuscript/TexFiles/`.
4. Compile (`quick`, then `full` when citations/references changed).
5. Update `tasks/status.md` and `submission/package-checklist.md` when milestones shift.

## Notes on Venue Files

`standards/requirements.md` is the index for the standards folder.
Use `standards/formatting-requirements.md` for official/template constraints and `standards/benchmark-requirements.md` for representative-thesis structural benchmarks.
Before submission, replace placeholders with institution-specific constraints and confirm all checklist items.
