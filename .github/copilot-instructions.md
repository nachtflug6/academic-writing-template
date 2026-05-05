# Copilot Instructions for Academic Writing

This repository is an **academic manuscript workspace**, not a software codebase. Apply these principles consistently across all edits.

## Core Principles

### 1. Preserve Structure and Metadata
- **Never remove or modify**: LaTeX commands, labels, `\ref{}` calls, `\cite{}` calls, or bibliography cite keys
- **Maintain environments**: Preserve `\begin{} \end{}` structures, section hierarchies, and formatting
- **Keep package imports**: Do not add new packages unless explicitly requested
- **Preserve comments**: Author notes and editorial comments in LaTeX comments are working material

### 2. Never Invent Facts or Citations
- **Do not create bibliography entries** from memory or inference
- **Do not invent experimental results, numbers, or claims** not present in source material
- **Do not hallucinate citations** or attribute claims to authors without verification
- **Flag uncertainty**: If a claim needs verification, mark it with a comment like `% TODO: verify from source`

### 3. Distinguish Between Material Types
- **Handoff bundles** (`handoff/`): Highest authority for research content — citation-free manuscript export, filtered bibliography, and claim-evidence reports
- **Final manuscript** (`manuscript/`): Polished LaTeX prose; must be factual and properly cited
- **Bibliography** (`refs/references.bib`): Authoritative cite key source; never modify entries without explicit instruction

### 4. Edit Targeting
- **Prefer section edits**: Edit individual source files in the active manuscript project under `manuscript/` rather than rewriting whole documents
- **Keep changes focused**: Make targeted improvements to clarity, structure, or argument flow
- **Avoid wholesale rewrites**: Preserve author's voice and editorial decisions

### 5. LaTeX Best Practices
- **Respect formatting**: Maintain consistent indentation and line breaks where sensible
- **Validate syntax**: Ensure edits do not break LaTeX compilation
- **Use appropriate environments**: Preserve the author's choice of structural elements (sections, subsections, etc.)
- **Comment thoughtfully**: Add clarifying comments only when the code is genuinely ambiguous

## When to Ask for Clarification

- If a citation appears incomplete or incorrect
- If a claim seems to lack supporting evidence
- If structural edits might break cross-references
- If the scope of a requested edit is ambiguous

## Workflow Support

### Instruction files
- `.github/instructions/manuscript.instructions.md` — LaTeX editing rules, language-risk checks, claim discipline, operational workflows (explore, draft, refactor)
- `.github/instructions/evidence.instructions.md` — rules for working with handoff files and evidence classification (see deprecation notice inside)
- `.github/instructions/review.instructions.md` — full review framework: modes, output templates, compliance checks, examiner challenge checks
- `AGENTS.md` — thesis-specific agent configuration and materials hierarchy

### Standards folder
- `standards/requirements.md` — index: defines precedence between formal rules and benchmarks
- `standards/formatting-requirements.md` — official/template-derived formatting and submission rules
- `standards/benchmark-requirements.md` — structural benchmarks and chapter expectations from representative theses; includes supervisor/examiner language flags and terminology accessibility rules
- `standards/feedback/` — traceable log of supervisor and examiner feedback rounds (dated files)

### Key folder map
- Manuscript source projects: `manuscript/`
- Figures and tables: use paths defined by your chosen venue template inside `manuscript/`
- Appended papers (if used): paths defined by your active manuscript project
- Bibliography: `refs/references.bib`
- Handoff bundles: `handoff/` (latest timestamped folder)
- Task tracking: `tasks/status.md`, `tasks/backlog.md`
