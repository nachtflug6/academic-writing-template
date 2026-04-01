# VS Code Workspace Configuration

This directory contains VS Code settings and recommendations for the academic writing project.

## Files

### `settings.json`
Core editor and extension configuration:
- **Word wrap**: Enabled for comfortable editing of Markdown/LaTeX.
- **File exclusions**: LaTeX build artifacts automatically hidden.
- **LaTeX Workshop**: Compile recipes and PDF viewer configuration.
- **Code Spell Checker**: Thesis-specific term dictionary.
- **Markdown Linting**: Relaxed rules for academic prose.
- **LTeX**: Grammar checking disabled by default (opt-in for polish phase).

### `extensions.json`
Recommended extensions for this workspace:
- **james-yu.latex-workshop** (ESSENTIAL): LaTeX compilation, PDF viewer, syntax highlighting.
- **streetsidesoftware.code-spell-checker** (ESSENTIAL): Spell checking across LaTeX/Markdown.
- **davidanson.vscode-markdownlint** (ESSENTIAL): Linting for operational Markdown files.
- **yzhang.markdown-all-in-one** (Core): Markdown authoring helpers and shortcuts.
- **valentjn.vscode-ltex** (Optional): Grammar checking; enable when polishing.
- **eamodio.gitlens** (Optional): Git authorship and history tracking.

To install all recommendations, run: `code --install-extension <id>` for each ID above.

### `tasks.json`
Pre-configured build tasks:
- **LaTeX: Compile main.tex** (Cmd+Shift+B default): Single pdflatex pass.
- **LaTeX: Full compile**: Complete cycle (pdflatex → bibtex → pdflatex × 2).
- **LaTeX: Clean build artifacts**: Remove .aux/.log/.synctex.gz etc.
- **LaTeX: View main.pdf**: Open compiled PDF in default viewer.

### `cspell.json`
Spell checker domain dictionary with academic/thesis terms. Add new technical terms or author names here to prevent false positives.

## Quick Start

1. Open Extensions panel (Cmd+Shift+X).
2. Search "Recommended" to see suggested extensions.
3. Install the core 3 extensions (LaTeX Workshop, Code Spell Checker, Markdown Lint).
4. Open `manuscript/main.tex` and press Cmd+Shift+B to compile.
5. View the compiled PDF in the right-pane tab.

## Customization

- **Spell check**: Edit `cSpell.ignoreWords` in `settings.json` or add journal acronyms to `cspell.json`.
- **Compile recipe**: Modify LaTeX tools in `settings.json` to use `lualatex` or other engines.
- **File exclusions**: Extend `files.exclude` for any additional build artifacts.
- **Build tasks**: Add tasks in `tasks.json` for other LaTeX targets (inlaga.tex, errata.tex).

## Tips

- **Preserve Markdown/LaTeX boundaries**: The instructions files enforce manuscript/evidence separation. Spell checker and linting respect these domains.
- **Sync PDF viewer**: LaTeX Workshop's PDF reader syncs with editor via Cmd+Shift+V (SyncTeX).
- **Search patterns**: Use the Search Editor (Cmd+K Cmd+O) with patterns like `\cite\{\}` to audit citation usage.
- **Git blame**: With GitLens, hover over a line to see who edited it and when (useful for collaborative review).

## Troubleshooting

- **"pdflatex not found"**: Ensure TeX Live is installed (`brew install basictex` on macOS, `apt install texlive-full` on Linux).
- **Font errors**: Install `cm-super` package for scalable Computer Modern fonts.
- **PDF won't open**: Check build panel for errors; ensure `manuscript/main.pdf` exists.
- **Spell check too aggressive**: Add words to `cspell.json` `ignoreWords` array.

## See Also

- `.github/copilot-instructions.md`: Overview of repo structure and editing rules.
- `.github/instructions/`: Detailed guidance for working with evidence, manuscript, notes, and review tasks.
- `tasks/status.md`: Chapter completion tracking.
