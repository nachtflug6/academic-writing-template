# Thesis Template Brief

## Purpose

This repository provides a reusable structure for academic thesis writing.
It is intended to be customized for your institution, degree level, and research domain.

## First Customization Steps

1. Update thesis metadata in `manuscript/TexFiles/settings.tex`.
2. Replace placeholder chapter text in `manuscript/TexFiles/*.tex`.
3. Populate `refs/references.bib` with your citations.
4. Fill venue constraints in `standards/formatting-requirements.md`.
5. Track progress in `tasks/status.md` and `tasks/backlog.md`.

## Build Workflow

Use the provided script:

```bash
bash ./scripts/compile-thesis.sh quick
bash ./scripts/compile-thesis.sh full
bash ./scripts/compile-thesis.sh clean
```

## Scope

This template intentionally separates:

- Manuscript source in `manuscript/`
- Evidence work in `evidence/`
- Planning in `project/` and `tasks/`
- Venue rules in `standards/` and `venue/`
- Submission readiness in `submission/`

## Notes

- Validate all institution-specific requirements before submission.
- Keep all placeholder markers until replaced with your real content.
