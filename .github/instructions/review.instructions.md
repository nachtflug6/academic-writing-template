# Review Instructions

Use these guidelines when reviewing the workspace before major handoff, internal review, defense preparation, or submission.

## Purpose

The goal of review is not only to catch formatting problems. It is to identify weaknesses that could cause trouble during supervision, opponent review, examination, peer review, or submission.

A good review should assess:
- technical integrity,
- manuscript-evidence separation,
- argument clarity,
- scope discipline,
- claim defensibility,
- likely reviewer or opponent challenges,
- and submission readiness.

Keep the review structured. Distinguish clearly between:
- format/integrity issues,
- writing/clarity issues,
- evidence/claim issues,
- argument/content issues,
- and handoff/submission issues.

Do not silently rewrite during review unless explicitly asked. Review should primarily identify, classify, and prioritize issues.

---

## 1. Review modes

### A. Format and integrity review
Check technical and workspace consistency.
Focus on:
- LaTeX integrity,
- file structure,
- references,
- includes,
- package consistency,
- venue requirement alignment,
- submission-package readiness.

### B. Content and argument review
Check whether the manuscript's reasoning is clear, complete enough, and defensible within its stated scope.
Focus on:
- missing motivations,
- unexplained choices,
- weak transitions in argument,
- unclear contribution framing,
- missing definitions,
- unsupported reasoning jumps,
- scope inconsistencies,
- unaddressed alternatives or omissions.

### C. Opponent / examiner challenge review
Read like a skeptical but fair opponent, reviewer, or examiner.
Ask:
- Why was X not discussed?
- Why was Y chosen instead of Z?
- What assumptions does this depend on?
- Is this claim too broad?
- Is the limitation acknowledged clearly enough?
- Is the contribution distinct and justified?
- Would a reviewer ask for comparison, citation, or clarification here?
- Is one case being stretched into a general claim?
- Is this statement vulnerable to an obvious counterexample?
- Where would an opponent push on novelty, rigor, generality, or interpretation?

### D. Evidence and defensibility review
Check whether claims are supported at the right strength.
Focus on:
- traceability from claims to evidence,
- distinction between evidence and interpretation,
- bounded wording,
- preservation of uncertainty,
- causal precision,
- novelty bounding,
- citation gaps,
- overclaim risk,
- mismatch between wording and support.

### E. Delivery and handoff review
Check whether the workspace is ready for the next person or next phase.
Focus on:
- current task state,
- known open issues,
- ambiguous files,
- packaging readiness,
- visible next actions,
- unresolved risk items.

---

## 2. Scope checks

Confirm that:
- manuscript and evidence boundaries are respected,
- bibliography files remain in `refs/`,
- cite keys are unchanged,
- standards constraints in `standards/requirements.md` are considered (formal/template rules in `standards/formatting-requirements.md`, benchmark baseline in `standards/benchmark-requirements.md`),
- files are located and named consistently,
- ambiguous materials are explicitly identified rather than silently reclassified.

---

## 3. LaTeX integrity checks

Check that:
- no `\label{}`, `\ref{}`, or `\cite{}` commands are broken,
- include/input paths remain valid,
- figure/table references still resolve correctly,
- environments remain intact,
- no accidental package additions were made unless requested,
- section structure remains coherent after edits,
- comments and important annotations were not removed.

---

## 4. Manuscript editing compliance checks

Verify that edits to manuscript files followed the guidelines in `.github/instructions/manuscript.instructions.md`.

Check that:
- minimum intervention was applied: changes are targeted rather than wholesale rewrites,
- the author's scientific intent, results, and argument structure are unchanged,
- no new theoretical content or claims were introduced,
- no sections were restructured without explicit instruction,
- the author's voice has not been distorted,
- equations, notation, symbols, and formal derivations were not altered,
- author comments and annotations were not removed,
- bibliography metadata was not changed,
- edits favor clarity and flow improvements: sentence simplification, stronger topic sentences, better transitions, sharper paragraph unity,
- epistemic status is visible: distinctions between observation, inference, interpretation, and hypothesis are preserved or clarified,
- claim scope and certainty are aligned with the evidence described,
- language-risk edits softened or flagged overclaims, absolutes, causal overreach, novelty inflation, and vague evaluative language.

Ask:
- Were edits minimal and targeted?
- Was anything added that was not already supported by the source material?
- Were any conditions, limitations, or distinctions erased?
- Does the edited text satisfy the strength-mismatch principle: is the wording no stronger than the evidence, and is the scope no broader than what was shown?

---

## 5. Writing and readability checks

Review whether the manuscript is readable and scientifically well-formed.

Check for:
- unclear or overloaded sentences,
- weak topic sentences,
- abrupt paragraph transitions,
- unclear referents,
- excessive abstraction,
- unnecessary jargon density,
- vague evaluative language,
- poor paragraph unity,
- missing explanation of why one idea follows another,
- formal but cognitively difficult prose.

Also check whether the prose remains:
- precise without being opaque,
- rigorous without being stiff,
- concrete without becoming informal,
- accessible without losing substance.

---

## 6. Content and argument review checks

Review the manuscript's reasoning, not just its wording.

Check for:
- unclear problem framing,
- weak statement of contribution,
- unclear research gap,
- unexplained design or method choices,
- missing rationale for important decisions,
- unsupported argumentative jumps,
- concepts introduced without definition,
- distinctions that should be explicit but are blurred,
- discussion sections that summarize without interpreting,
- limitations that are missing or too weakly stated,
- conclusions that extend beyond the actual evidence.

Typical review questions include:
- Why is this problem important in this specific scope?
- Why was this method, dataset, case, or comparison chosen?
- Why are some related approaches not discussed?
- What would a critical reader say is missing?
- What alternative interpretation exists?
- Does the manuscript answer the questions it raises?

---

## 7. Opponent / examiner challenge checks

Read parts of the manuscript as if preparing challenges for a defense or peer review.

Look for places where an opponent could reasonably ask:
- Why is X excluded?
- Why is Y included?
- Why this framing and not another?
- Why is this comparison sufficient?
- Why should this result generalize?
- What exactly is new here?
- What is the evidence for that wording?
- Is this correlation being presented as causation?
- Is the novelty claim bounded enough?
- Is this claim true only in this setting?
- What would happen if a contrary example were raised?

Flag sentences or sections that are easy to challenge because they are:
- too broad,
- too absolute,
- under-cited,
- poorly bounded,
- weakly motivated,
- or unclear about assumptions.

---

## 8. Evidence integrity checks

Check that:
- claims remain traceable to evidence notes,
- uncertainty is marked rather than erased,
- no invented data, figures, or outcomes appear,
- evidence files do not get silently turned into manuscript claims,
- limitations, null results, and contradictory evidence are not suppressed,
- claim wording matches the strength of support,
- cited-background claims are not presented as if directly established by the current work.

---

## 9. Language-risk checks

Review for wording likely to invite reviewer or examiner attack.

Flag:
- absolute formulations,
- overclaims,
- causal overreach,
- novelty inflation,
- vague quantifiers,
- promotional wording,
- rhetorical dismissal of alternatives,
- scope creep from one case to many.

Ask:
- Is the wording stronger than the evidence?
- Is the scope broader than what was shown?
- Would one counterexample damage the sentence badly?
- Would this survive a skeptical "how do you know?" question?

---

## 10. Delivery checks

Confirm that:
- `tasks/status.md` reflects the current state,
- `tasks/backlog.md` reflects next actions,
- `submission/package-checklist.md` reflects packaging readiness,
- unresolved issues are visible,
- ambiguous files are explicitly listed rather than force-classified,
- known risks are documented rather than left implicit.

---

## 11. Review output format

When producing a review, structure it as:

1. **Overall verdict**  
   - Ready / Nearly ready / Needs revision / High risk

2. **Top issues first**  
   - most important problems affecting defensibility, clarity, integrity, or submission readiness

3. **Issues by category**  
   - format/integrity
   - manuscript editing compliance
   - writing/readability
   - content/argument
   - opponent/examiner vulnerability
   - evidence/claim support
   - delivery/submission

4. **Questions a reviewer or opponent is likely to ask**  
   - list the strongest likely challenges

5. **Priority fixes**  
   - what should be fixed first before handoff or submission

Keep the review diagnostic and prioritized. Do not drown major risks in minor cosmetic comments.

---

## 12. Standard for success

A successful review should make it clear:
- whether the workspace is technically sound,
- whether manuscript edits followed the guidelines in `manuscript.instructions.md`,
- whether the manuscript is readable and coherent,
- whether the argument is defensible,
- where an examiner or reviewer is most likely to attack,
- whether claims are properly supported and bounded,
- and what must be fixed before the next handoff or submission.

---

## 13. Operational review templates

Use these templates for consistent review outputs.

### A. Whole-thesis structure/readiness template
1. Verdict: Strong / Adequate / Weak / At Risk.
2. Dense summary.
3. Top strengths (5).
4. Top weaknesses (5).
5. Missing core vs optional elements.
6. Top 10 fixes first (`issue | why | first fix`).

### B. Blockers and priority plan template
1. Blockers by category (`research | writing | structure | compliance | technical | external`) with impact and owner.
2. Dependency-aware sequencing.
3. Next 7 concrete actions.
4. Time estimates.
5. Escalations/questions for advisor or co-authors.

### C. Feedback integration template
1. Feedback matrix (`chapter | issue | priority | owner`).
2. Integration order with rationale.
3. Conflicts and clarification questions.
4. Cross-chapter consistency risks.
5. Verification checklist after implementation.

### D. Citation/reference audit template
1. Missing/unmatched cite keys.
2. Under-cited hotspots by chapter.
3. Bibliography data-quality issues.
4. Orphaned references.
5. Priority fixes.

### E. Compliance/figures/format template
1. Requirement-by-requirement compliance status (`pass/fail` + evidence note).
2. Figure/table findings.
3. Formatting/navigation risks.
4. Submission blockers.
5. Final preflight checklist.

### F. Language-risk template
1. Overall language-risk verdict.
2. Dense risk-profile summary.
3. Repeated risky patterns and safer wording direction.
4. Category findings (absolutes, overclaims, causal overreach, novelty inflation, vague quantifiers/evaluation, rhetorical tone, first-person risk).
5. Top language fixes first (`pattern | why risky | first wording move`).

### G. Chapter benchmark template
Use this chapter-level structure when reviewing a single chapter:
1. Verdict: Meets / Nearly meets / Below expectations.
2. Dense summary.
3. Top strengths (5).
4. Top weaknesses (5).
5. Missing core vs optional chapter elements.
6. Boundary issues.
7. Reviewer-risk issues.
8. Rubric notes by chapter role criteria.
9. Top 10 fixes first (`issue | why | first fix`).

Chapter-specific expectations and rubric anchors are defined in `standards/benchmark-requirements.md`.

---

## 14. Constraints during review execution

When operating in review mode:
- do not rewrite manuscript sections unless explicitly asked,
- do not invent evidence, citations, or metadata,
- do not replace high-impact risks with cosmetic comments,
- do not claim full compliance without requirement-level evidence,
- prioritize defensibility and submission risk over style preference.
