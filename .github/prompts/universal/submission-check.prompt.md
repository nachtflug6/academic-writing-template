---
name: Submission Check
description: Verify manuscript meets venue requirements and is ready for submission review.
applyTo: manuscript/**/*.tex
---

# Submission Check

## Goal
Ensure the manuscript complies with all venue-specific requirements before final submission.

## Instructions

1. **Load venue requirements**: Open `venue/requirements.md` (index), then use `venue/formatting-requirements.md` for official/template rules and `venue/benchmark-requirements.md` for empirical structural expectations.
2. **Check compliance**:
   - Length limits (page count, word count): measure PDF or count words
   - Formatting rules: margins, fonts, spacing, line numbering (if required)
   - Citation style: verify all `\cite{}` commands use correct style
   - Anonymous submission: check for author identifications if required
   - Figure/table limits: count and verify against rules
   - Supplementary material: confirm what's allowed/required
   - Header/footer rules: check if venue-specific formatting needed
   - File naming and structure: verify submission format
3. **Check manuscript integrity**:
   - All citations compile correctly
   - All `\ref{}` commands resolve to valid labels
   - No orphaned sections or missing includes
   - Abstract present and within limits
   - Keywords present (if required)
4. **Verify metadata**:
   - Title, author names (or "Anonymous" if required)
   - Email address (hidden if anonymous)
   - Institutional affiliations (if not anonymous)
5. **Red flags to check**:
   - Incomplete sections (comments, placeholders, `TODO` items)
   - Orphaned citations (`\cite{}` with no bibliography entry)
   - Broken cross-references
   - Missing or miscaptioned figures/tables
   - Inconsistent formatting

## Output Format

Provide:
- **Compliance checklist**: ✓ or ✗ for each requirement
- **Issues found**: Problems preventing submission
- **Warnings**: Items that should be reviewed before final submission
- **Estimated metrics**: Page count, word count, figure/table counts
- **Ready for submission**: Yes/No with conditions

## Do Not

- Make edits; only audit and report
- Assume venue rules; always reference the stated requirements
- Suggest changes beyond what requirements specify

## Before Running This Check

- Ensure `venue/formatting-requirements.md` is complete and current (and `venue/requirements.md` still reflects the split model)
- Compile the manuscript successfully to PDF first
- Have the complete venue submission guidelines available for reference
