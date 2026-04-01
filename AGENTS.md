---
name: Thesis Template Copilot Configuration
description: Template-specific instructions for Copilot editing and assistance.
---

# Thesis Template: Copilot Agent Configuration

This file customizes Copilot's behavior for this licentiate thesis project.

## Project Type: Thesis Template

This template supports thesis projects with:
- Core thesis chapters (introduction, background, methodology, discussion, conclusion)
- Multiple included research papers (appended or integrated)
- Comprehensive bibliography
- Support materials (figures, tables, appendices, glossary)

## Materials Hierarchy

Treat information sources in this priority order:

1. **University requirements** (`standards/requirements.md`): Thesis formatting and submission rules are non-negotiable
2. **Thesis guidelines**: Your specific institution's thesis handbook or style guide
3. **Source material** (`evidence/literature/extracts/`): Highest authority for research content
4. **Included papers** (`manuscript/papers/`): Published or submitted work with verified citations
5. **Main thesis chapters** (`manuscript/TexFiles/`): Your thesis prose
6. **Figures and tables**: Visual support material

## Core Rules

### Preservation
- Never modify: LaTeX `\label{}`, `\ref{}`, `\cite{}` commands
- Never alter: Bibliography entries or cite keys
- Never remove: Existing citations or cross-references
- Never invent: Experimental results, citations, or factual claims

### Template Considerations
- **Multiple papers**: If your thesis includes appended papers, treat them as already-vetted content
- **Long document**: Break changes into manageable edits per chapter/paper
- **University compliance**: Always check `standards/requirements.md` before major structural changes
- **Glossary and macros**: Preserve custom LaTeX commands and definitions

### Chapter/Section Edits
- Prefer editing individual chapter files in `manuscript/TexFiles/`
- Make targeted improvements to clarity and flow
- Preserve your voice and narrative choices
- Flag structural changes that might affect cross-references

## Venue Compliance

This thesis targets: **[University Name / Degree Program]**

Before suggesting major changes, check `standards/requirements.md` for:
- Page limits and formatting rules
- Citation style requirements
- Figure/table guidelines
- Anonymity or confidentiality rules
- Submission deadline and process

## Status and Milestones

For current thesis status, consult `tasks/status.md`:
- Completion status of each chapter
- Known issues or blockers
- Important deadlines
- Priority next actions

Reference this file when deciding which chapters need work.

## Example Workflows

### Refactor a thesis chapter
1. Read the chapter target and context
2. Check `.github/instructions/manuscript.instructions.md` for guidelines
3. Make targeted clarity improvements
4. Verify all labels and citations remain intact
5. Test compilation for LaTeX errors

### Integrate a new paper or appendix
1. Ask about the paper's role in the thesis
2. Verify it uses consistent citations with main bibliography
3. Integrate carefully to avoid breaking cross-references
4. Check formatting consistency with thesis style

### Update bibliography
1. Ask for complete publication details
2. Verify all entries match `\cite{}` commands in text
3. Ensure consistent formatting across entries
4. Test BibTeX compilation

## Questions Before Major Edits

- What is the current completion status of the thesis?
- Which university/institution is this for?
- Are there any specific formatting constraints?
- Are included papers already finalized?
- What is the submission deadline?

## Contact and Review

Treat this file as the source of truth for template-specific editing rules.
If you have questions about edits, refer back to these principles.
