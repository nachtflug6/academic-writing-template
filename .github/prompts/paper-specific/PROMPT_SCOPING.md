# Prompt Scoping (Canonical)

This file defines canonical usage and duplication control.

## Canonical thesis-specific set

- Use `.github/prompts/paper-specific/compact/` as the only thesis-specific prompt pack.
- It contains 12 prompts total:
  - 6 whole-thesis prompts
  - 6 chapter prompts (one per chapter)

## Cross-project set

- Keep `.github/prompts/universal/` for generic checks reusable across projects.

## Duplication policy

- Do not add a new prompt if its purpose is already covered in `compact/`.
- Prefer extending an existing compact prompt over creating a sibling variant.
- Keep one canonical prompt per chapter.
- Keep whole-thesis prompts targeted and non-overlapping.

## Residue policy

- Remove obsolete prompt variants once consolidated.
- Avoid placeholder prompts in active folders.