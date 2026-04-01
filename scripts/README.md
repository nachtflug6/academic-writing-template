# Scripts

Automation scripts for build, checks, and maintenance tasks.

Available scripts:

- `compile-thesis.sh` — generic LaTeX build helper for any entry `.tex` file in `manuscript/`
- `smartlib_smoke_test.py` — minimal Smart Library API smoke test against an external running instance

## compile-thesis.sh

Usage:

```bash
bash ./scripts/compile-thesis.sh <quick|full|clean> [entry_tex]
```

Examples:

```bash
bash ./scripts/compile-thesis.sh quick manuscript/main.tex
bash ./scripts/compile-thesis.sh full manuscript/venue-template/paper.tex
bash ./scripts/compile-thesis.sh clean
```

Default entry behavior:

- If `[entry_tex]` is provided, it is used.
- Else if `MANUSCRIPT_ENTRY` is set, that is used.
- Else fallback is `manuscript/main.tex`.

Mode behavior:

- `quick`: one `pdflatex` pass.
- `full`: one `pdflatex` pass, optional `bibtex`/`makeglossaries` when relevant files exist, then two more `pdflatex` passes.
- `clean`: recursively removes LaTeX artifacts under `manuscript/`.

## Smart Library smoke test

This repo accesses Smart Library through its HTTP API, not through a direct database connection.
If Smart Library is already running elsewhere, no extra infrastructure is needed here beyond network reachability to that API.

Configuration:

- Base URL comes from `SMARTLIB_API_URL`
- Default base URL is `http://localhost:8001`

Recommended shell setup:

```bash
export SMARTLIB_API_URL=http://localhost:8001
```

Run:

```bash
python3 scripts/smartlib_smoke_test.py
```

Example with explicit base URL:

```bash
SMARTLIB_API_URL=http://localhost:8001 python3 scripts/smartlib_smoke_test.py
```

Success looks like:

- A JSON health response such as `{"status": "healthy"}`
- A formatted summary of `GET /api/documents/` including `total` and a small document preview
- A final `Smoke test passed` line

For ad hoc access from this repo, use the same base URL with standard HTTP tools, for example:

```bash
curl -fsS "$SMARTLIB_API_URL/health"
curl -fsS "$SMARTLIB_API_URL/api/documents/?limit=3&offset=0"
```

This folder is intentionally lightweight and can evolve with project needs.
