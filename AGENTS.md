---
name: Thesis Template Copilot Configuration
description: Template-specific instructions for Copilot editing and assistance.
---

# Academic Writing Workspace: Copilot Agent Configuration

This file customizes Copilot's behavior for this academic writing workspace.

## Project Type: Flexible Academic Writing Workspace

This workspace supports:
- Thesis projects
- Conference and journal papers
- Technical reports and mixed manuscript collections
- Flexible bibliography and support-material structures

## Materials Hierarchy

Treat information sources in this priority order:

1. **University requirements** (`standards/requirements.md`): Thesis formatting and submission rules are non-negotiable
2. **Thesis guidelines**: Your specific institution's thesis handbook or style guide
3. **Source material** (`evidence/literature/extracts/`): Highest authority for research content
4. **Manuscript project files** (`manuscript/`): Venue template and source files for your current writing target
5. **Main manuscript text**: Your authored prose and structure
6. **Figures and tables**: Visual support material

## Core Rules

### Preservation
- Never modify: LaTeX `\label{}`, `\ref{}`, `\cite{}` commands
- Never alter: Bibliography entries or cite keys
- Never remove: Existing citations or cross-references
- Never invent: Experimental results, citations, or factual claims

### Workspace Considerations
- **Template-first**: Preserve structure of the selected venue template inside `manuscript/`
- **Long documents**: Break changes into manageable edits
- **Venue compliance**: Always check `standards/requirements.md` before major structural changes
- **LaTeX integrity**: Preserve custom commands and definitions

### Manuscript Edits
- Prefer editing source files belonging to the active manuscript target in `manuscript/`
- Make targeted improvements to clarity and flow
- Preserve your voice and narrative choices
- Flag structural changes that might affect cross-references

## Venue Compliance

This manuscript targets: **[Venue / Institution / Program]**

Before suggesting major changes, check `standards/requirements.md` for:
- Page limits and formatting rules
- Citation style requirements
- Figure/table guidelines
- Anonymity or confidentiality rules
- Submission deadline and process

## Status and Milestones

For current project status, consult `tasks/status.md`:
- Completion status of major manuscript components
- Known issues or blockers
- Important deadlines
- Priority next actions

Reference this file when deciding which chapters need work.

## Example Workflows

### Refactor a manuscript section
1. Read the target section and context
2. Check `.github/instructions/manuscript.instructions.md` for guidelines
3. Make targeted clarity improvements
4. Verify all labels and citations remain intact
5. Test compilation for LaTeX errors

### Integrate a venue template or section package
1. Confirm the role of the imported template/package in the current manuscript
2. Verify bibliography and cross-reference compatibility
3. Integrate carefully to avoid breaking cross-references
4. Check formatting consistency with target venue style

### Update bibliography
1. Ask for complete publication details
2. Verify all entries match `\cite{}` commands in text
3. Ensure consistent formatting across entries
4. Test BibTeX compilation

## Questions Before Major Edits

- What is the current completion status of the manuscript target?
- Which venue or institution rules apply?
- Are there any specific formatting constraints?
- Is the template fixed or still negotiable?
- What is the submission deadline?

## Contact and Review

Treat this file as the source of truth for template-specific editing rules.
If you have questions about edits, refer back to these principles.
