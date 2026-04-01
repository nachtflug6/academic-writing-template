#!/usr/bin/env bash
set -euo pipefail

mode="${1:-full}"

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
manuscript_dir="$repo_root/manuscript"

if [[ ! -d "$manuscript_dir" ]]; then
  echo "Error: manuscript directory not found at $manuscript_dir" >&2
  exit 1
fi

cd "$manuscript_dir"

case "$mode" in
  full)
    pdflatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
    bibtex main
    makeglossaries main
    pdflatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
    pdflatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
    ;;
  quick)
    pdflatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
    ;;
  clean)
    rm -f *.aux *.log *.synctex.gz *.bbl *.blg *.out *.toc *.lof *.lot *.run.xml *.fls *.fdb_latexmk *.bcf *.acn *.acr *.alg *.glg *.glo *.gls *.ist
    ;;
  *)
    echo "Usage: $0 [full|quick|clean]" >&2
    exit 1
    ;;
esac
