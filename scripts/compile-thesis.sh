#!/usr/bin/env bash
set -euo pipefail

mode="${1:-full}"
entry_arg="${2:-}"

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
manuscript_dir="$repo_root/manuscript"

if [[ ! -d "$manuscript_dir" ]]; then
  echo "Error: manuscript directory not found at $manuscript_dir" >&2
  exit 1
fi

default_entry="${MANUSCRIPT_ENTRY:-manuscript/main.tex}"
entry_rel="${entry_arg:-$default_entry}"

# Normalize the entry path from repo root.
if [[ "$entry_rel" = /* ]]; then
  entry_abs="$entry_rel"
else
  entry_abs="$repo_root/$entry_rel"
fi

entry_dir="$(dirname "$entry_abs")"
entry_file="$(basename "$entry_abs")"
entry_stem="${entry_file%.tex}"

print_usage() {
  cat <<'EOF'
Usage:
  bash ./scripts/compile-thesis.sh <quick|full|clean> [entry_tex]

Examples:
  bash ./scripts/compile-thesis.sh quick manuscript/main.tex
  bash ./scripts/compile-thesis.sh full manuscript/paper.tex
  MANUSCRIPT_ENTRY=manuscript/template/main.tex bash ./scripts/compile-thesis.sh quick

Notes:
  - If [entry_tex] is omitted, MANUSCRIPT_ENTRY is used.
  - If MANUSCRIPT_ENTRY is unset, manuscript/main.tex is used.
EOF
}

case "$mode" in
  full)
    ;;
  quick)
    ;;
  clean)
    ;;
  -h|--help|help)
    print_usage
    exit 0
    ;;
  *)
    echo "Error: unknown mode '$mode'." >&2
    print_usage
    exit 1
    ;;
esac

if [[ "$mode" = "clean" ]]; then
  find "$manuscript_dir" -type f \( \
    -name '*.aux' -o -name '*.log' -o -name '*.synctex.gz' -o -name '*.bbl' -o -name '*.blg' -o -name '*.out' -o \
    -name '*.toc' -o -name '*.lof' -o -name '*.lot' -o -name '*.run.xml' -o -name '*.fls' -o -name '*.fdb_latexmk' -o \
    -name '*.bcf' -o -name '*.acn' -o -name '*.acr' -o -name '*.alg' -o -name '*.glg' -o -name '*.glo' -o -name '*.gls' -o \
    -name '*.ist' -o -name '*.dvi' -o -name '*.ps' \
  \) -delete
  exit 0
fi

if [[ "$entry_file" != *.tex ]]; then
  echo "Error: entry file must end with .tex. Got: $entry_rel" >&2
  print_usage
  exit 1
fi

if [[ ! -f "$entry_abs" ]]; then
  echo "Error: entry file not found: $entry_abs" >&2
  print_usage
  exit 1
fi

cd "$entry_dir"

pdflatex -synctex=1 -interaction=nonstopmode -file-line-error "$entry_file"

if [[ "$mode" = "full" ]]; then
  if [[ -f "$entry_stem.aux" ]]; then
    if grep -qE 'citation|bibdata|bibstyle' "$entry_stem.aux" 2>/dev/null; then
      bibtex "$entry_stem" || true
    fi
  fi

  if [[ -f "$entry_stem.glo" || -f "$entry_stem.acn" ]]; then
    makeglossaries "$entry_stem" || true
  fi

  pdflatex -synctex=1 -interaction=nonstopmode -file-line-error "$entry_file"
  pdflatex -synctex=1 -interaction=nonstopmode -file-line-error "$entry_file"
fi
