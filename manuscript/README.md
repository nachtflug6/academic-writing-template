# Manuscript Drop-In Workspace

This folder is intentionally empty and unconstrained.

Use it as a drop-in area for any LaTeX project, for example:

- a conference paper template,
- a journal template,
- a thesis template,
- or multiple manuscript subprojects.

## How to use

1. Copy your venue template/project into this folder.
2. Identify the entry `.tex` file.
3. Compile with:

```bash
bash ./scripts/compile-thesis.sh quick manuscript/path/to/entry.tex
bash ./scripts/compile-thesis.sh full manuscript/path/to/entry.tex
```

If you compile often from the same entry, set:

```bash
export MANUSCRIPT_ENTRY=manuscript/path/to/entry.tex
```

Then you can run:

```bash
bash ./scripts/compile-thesis.sh quick
```
