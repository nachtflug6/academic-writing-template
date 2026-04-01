# Venue Operations Guide

This folder is the single operational area for venue-aligned thesis requirements and readiness checks.

## File Roles

- [requirements.md](requirements.md)
	- Index and governance file.
	- Explains the split between formal requirements and empirical benchmarks.
	- Defines precedence when guidance conflicts.

- [formatting-requirements.md](formatting-requirements.md)
	- Official, template-derived, and handbook-derived rules.
	- Use this for all compliance and submission decisions.

- [benchmark-requirements.md](benchmark-requirements.md)
	- Structural and chapter-role benchmarks derived from representative theses.
	- Use this for diagnosis, prioritization, and readiness shaping.

- [checklist.md](checklist.md)
	- Compact pre-handoff and pre-submission checklist.
	- Confirms both compliance and benchmark readiness were reviewed.

- [feedback/](feedback/)
	- Traceable log of supervisor and examiner feedback rounds.
	- Each file is dated and records raw feedback, derived rules, and where each was applied.
	- Naming convention: `YYYY-MM-DD_<source>.md`

## Precedence Rule

If benchmark guidance conflicts with official/template requirements, official/template requirements always win.

## How To Operate (Recommended Workflow)

1. Confirm source of truth for formal constraints
	 - Fill or update [formatting-requirements.md](formatting-requirements.md) from handbook/template sources.

2. Maintain benchmark baseline
	 - Keep [benchmark-requirements.md](benchmark-requirements.md) aligned with current representative-thesis analysis.
	 - Update ranges and chapter expectations only when the sample basis changes.

3. Run review and feedback using both sources
	 - Review method/output format: [../.github/instructions/review.instructions.md](../.github/instructions/review.instructions.md)
	 - Compliance criteria source: [formatting-requirements.md](formatting-requirements.md)
	 - Structural benchmark criteria source: [benchmark-requirements.md](benchmark-requirements.md)

4. Close readiness before handoff/submission
	 - Complete [checklist.md](checklist.md)
	 - Resolve any conflicts in favor of [formatting-requirements.md](formatting-requirements.md)

## Update Rules

- Update [formatting-requirements.md](formatting-requirements.md) when:
	- institution handbook changes,
	- official template changes,
	- submission office instructions change.

- Update [benchmark-requirements.md](benchmark-requirements.md) when:
	- benchmark sample set changes,
	- program conventions shift in recent theses,
	- chapter-role expectations are recalibrated.

- Add a file to [feedback/](feedback/) when:
	- a new supervisor or examiner feedback round is received.
	- Link each feedback item to where the derived rule was applied.

- Keep [requirements.md](requirements.md) stable and short.

## What Not To Put Here

- Do not store manuscript prose drafts.
- Do not store raw evidence extraction notes.
- Do not duplicate agent prompt execution format here; keep operational review format in [../.github/instructions/review.instructions.md](../.github/instructions/review.instructions.md).

## Ownership Suggestion

- Formal requirements owner: thesis author (with advisor confirmation).
- Benchmark owner: thesis author (with periodic recalibration from representative theses).
- Final compliance sign-off: advisor/program process as applicable.