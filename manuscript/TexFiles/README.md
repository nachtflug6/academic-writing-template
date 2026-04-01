# TexFiles

This folder contains the authored LaTeX source for thesis core text, plus local figure and table inputs used by chapters.

## Default chapter structure

1. `1_introduction.tex` — problem framing, aim, research questions, scope.
2. `2_background.tex` — conceptual and literature background.
3. `3_methodology.tex` — thesis-level design and method boundaries.
4. `4_papers.tex` — results/included work and thesis-level reporting.
5. `5_discussion.tex` — synthesis, implications, limitations.
6. `6_conclusion.tex` — concise thesis closure.

Supporting front/back matter in this folder includes:

- `abstract.tex`
- `summary.tex`
- `firstpage.tex`
- `acknowledgment.tex`
- `dedication.tex`
- `publicationsList.tex`
- `appendedPapers.tex`
- `0_glossary.tex`
- `00_macros_equations.tex`
- `settings.tex`

## How the chapter files are assembled

- `summary.tex` inputs the six main chapter files in order.
- `figures/` contains figure inputs referenced by the chapters.
- `tables/` contains thesis tables used in the chapter files.
- `*.aux` files are build artifacts, not source files.

## Chapter-role boundaries

Keep each chapter serving its thesis role.

- Introduction: move from broad motivation to a specific problem, then state aim, research questions, scope, and roadmap.
- Background: synthesize the concepts and related work needed by the thesis; avoid drifting into a generic survey.
- Methodology: describe the thesis design and rationale without over-claiming method superiority.
- Results/Papers chapter: report findings with clear provenance.
- Discussion: interpret and synthesize findings at thesis level.
- Conclusion: keep it short, direct, and thesis-level.

## Language, citations, and evidence policy

To avoid duplicated rule sets, this file does not restate full language-risk and evidence-discipline policies.

- For manuscript wording, claim discipline, and LaTeX integrity: `.github/instructions/manuscript.instructions.md`
- For evidence traceability and support-strength discipline: `.github/instructions/evidence.instructions.md`
- For chapter-role benchmarks and language flags used in review: `standards/benchmark-requirements.md`

Use this `TexFiles/README.md` as a local map for file roles and chapter boundaries in this folder.

## Editing notes

- Keep changes targeted; do not rewrite whole chapters unless there is a clear reason.
- Check that new prose still fits the chapter's role in the overall thesis architecture.