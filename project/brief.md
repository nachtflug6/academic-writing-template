# Academic Writing Workspace Brief

## Purpose

This repository provides a reusable structure for academic writing projects.
It is designed for flexible use across thesis, paper, report, and mixed writing workflows.

## First Customization Steps

1. Place your venue template or manuscript project under `manuscript/`.
2. Identify your LaTeX entry file path (for example, `manuscript/main.tex`).
3. Compile with `bash ./scripts/compile-thesis.sh quick <entry.tex>`.
4. Populate `refs/references.bib` if you keep bibliography centrally.
5. Fill venue constraints in `standards/formatting-requirements.md`.
6. Track progress in `tasks/status.md` and `tasks/backlog.md`.

## Build Workflow

Use the provided script:

```bash
bash ./scripts/compile-thesis.sh quick manuscript/main.tex
bash ./scripts/compile-thesis.sh full manuscript/main.tex
bash ./scripts/compile-thesis.sh clean
```

## Scope

This workspace intentionally separates:

- Manuscript source in `manuscript/`
- Evidence work in `evidence/`
- Planning in `project/` and `tasks/`
- Venue rules in `standards/` and `venue/`
- Submission readiness in `submission/`

## Notes

- Validate all institution-specific requirements before submission.
- Keep `manuscript/` structure aligned with your chosen venue template.
