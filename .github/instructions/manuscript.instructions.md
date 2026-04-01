# LaTeX Manuscript Editing Instructions

Apply these guidelines when editing manuscript files, especially LaTeX sources in `manuscript/` and related evidence text in `evidence/`.

## Purpose

Improve the manuscript's writing quality, readability, and defensibility without changing the author's scientific intent, technical meaning, mathematical content, citation structure, or LaTeX validity.

Treat scientific writing as guided reasoning. Your job is to help the reader see:
- what the topic is,
- why it matters,
- what is being claimed,
- on what basis,
- under what conditions,
- how the ideas connect,
- and what remains uncertain or limited.

The text should become clearer, more precise, more logically connected, more rigorous, and more concrete where useful, without becoming simplified, inflated, or stylistically distorted.

---

## 1. Core editing goals

### A. Clarity and flow
Improve readability and argument flow without changing meaning.
- simplify convoluted sentences,
- improve transitions,
- strengthen topic sentences,
- improve paragraph openings and closings,
- make reasoning steps easier to follow,
- reduce ambiguity in pronouns and references,
- flag circular reasoning or unsupported argumentative moves.

### B. Scientific writing quality
Edit toward prose that is:
- clear,
- precise,
- coherent,
- concise,
- logically staged,
- epistemically careful,
- and graspable through mechanisms, variables, conditions, or examples where appropriate.

Accessibility is not simplification. Do not remove technical distinctions, conditions, or mechanisms just to make the prose sound easier.

Rigor is not stiffness. Do not replace weak prose with ceremonially formal, noun-heavy, or inflated language.

Tangibility is not informality. Where the prose becomes too abstract, prefer operational, mechanistic, or concrete wording that is already supported by the text.

### C. Language defensibility
Reduce language that is easy for an examiner, reviewer, or opponent to challenge.
Focus especially on:
- overclaims,
- absolute statements,
- causal overreach,
- novelty inflation,
- vague evaluative language,
- imprecise quantifiers,
- thesis-wide generalisations from narrow evidence,
- rhetorical or adversarial phrasing.

---

## 2. LaTeX integrity rules

All edits must preserve valid LaTeX.

You must:
- preserve all `\cite{}` commands exactly,
- preserve all `\label{}` commands,
- preserve all `\ref{}` and related cross-references,
- preserve sectioning structure unless explicitly instructed otherwise,
- keep environments intact,
- respect the existing package setup,
- never add packages unless explicitly requested.

You must not:
- remove author comments,
- alter equations, notation, symbols, or formal derivations,
- change bibliography metadata,
- break compilation structure.

---

## 3. Content preservation rules

You are editing language, not changing the science.

Do not:
- add new theoretical content,
- change results, findings, or substantive claims,
- change the paper's overall argument,
- restructure sections without explicit instruction,
- rewrite large passages unless explicitly asked,
- significantly alter the author's voice.

Default to the minimum intervention needed for a real improvement.

When a substantial rewrite seems needed, flag or suggest it instead of imposing it.

---

## 4. Preferred edits

Prefer edits such as:
- fixing grammar and syntax,
- simplifying dense sentences,
- improving passive-to-active voice when helpful,
- replacing weak verbs with stronger verbs,
- reducing unnecessary nominalization,
- clarifying pronoun antecedents,
- removing redundancy,
- sharpening topic sentences,
- improving paragraph unity,
- adding brief transitions or bridge phrases,
- making claim scope clearer,
- clarifying whether a sentence reports observation, inference, interpretation, or hypothesis,
- making abstract claims more concrete where the text already supports that move,
- flagging unclear or missing citation support.

---

## 5. Sentence and paragraph guidance

### Sentence-level guidance
Prefer sentences that are easy to parse on first read.
- favor clear subject–verb structure,
- keep one main conceptual move per sentence where possible,
- avoid stacked modifiers and long prepositional chains,
- prefer explicit referents over vague "this," "it," or "they,"
- use connective words when logic would otherwise remain implicit,
- split overloaded sentences when necessary.

Prefer wording that makes relations visible:
- cause,
- contrast,
- consequence,
- condition,
- example,
- limitation,
- comparison.

### Paragraph-level guidance
Treat each paragraph as a unit of thought.
A strong paragraph usually:
- has one main purpose,
- begins with an orienting sentence,
- develops through explanation, evidence, mechanism, contrast, or example,
- ends with an implication, interpretation, limitation, or transition.

Improve local coherence across sentences and make the paragraph's role in the broader argument easier to see.

Prefer prose over enumeration for ordinary explanatory material.
- Do not overuse bullet lists for generic points or routine exposition.
- Enumerate only when the listed items carry real argumentative weight, mark a genuine distinction, or will be referred back to later.
- Avoid long fact strings such as "X happens in A, B, C, D, and E" unless the breadth of the set is itself important.
- When giving examples, prefer compact parenthetical illustration where possible, for example "this is a problem (e.g. in X and Y)."
- Prefer one or two strong examples over three or more weaker ones unless completeness is necessary to the argument.

Prefer lexical and citation variation in expository prose.
- Avoid repeating the same wording or sentence template many times in close proximity; vary word choice and formulation while preserving meaning.
- Avoid repeatedly attaching the same single citation to nearby generic statements when those statements are broadly supported in the literature.
- For generic background claims, prefer a defensible mix of relevant sources rather than citation monoculture.
- Reuse the same citation repeatedly in close proximity only when a specific fact depends primarily on that source or that source is uniquely authoritative for the point.

---

## 6. Claim discipline and rigor

Strengthen the writing by making epistemic status visible.

Where relevant, preserve or clarify distinctions such as:
- observation vs inference,
- evidence vs interpretation,
- correlation vs causation,
- hypothesis vs supported conclusion,
- mechanism vs speculation,
- local finding vs broader generalisation.

Improve claims by:
- specifying conditions or scope when needed,
- avoiding overstatement,
- calibrating certainty to the support described,
- keeping limitations visible,
- making assumptions explicit when they matter for interpretation.

A stronger sentence is often one that more clearly shows:
- what was observed,
- what is inferred,
- what conditions matter,
- what is still uncertain.

---

## 7. Language-risk checks

Review wording for examiner/reviewer vulnerability.

### Flag or soften:
- absolutes such as: all, always, never, every, none, impossible, completely, proves, guarantees, ensures, foundational, universal
- broad superiority claims from limited evidence
- strong real-world impact claims without demonstration
- causal language when only association is shown
- novelty claims such as: the first, the only, unprecedented, unique, no prior work
- vague praise such as: highly important, outstanding, remarkable, revolutionary, extremely effective
- unclear quantifiers such as: many, most, several, widely, commonly, often, typically, in general
- defensive or self-promotional first-person phrasing
- dismissive or rhetorical wording such as: clearly, obviously, of course, undeniably, merely, simply, fails to, is flawed

### Strength-mismatch principle
For any risky sentence, ask:
- Is the wording stronger than the evidence?
- Is the scope broader than what is shown?
- Would one counterexample weaken it badly?
- Would it survive a reviewer asking "always?", "how do you know?", or "in what exact scope?"

If not, narrow, soften, or flag the wording.

Do not flag normal academic hedging or clear, well-bounded claims.

---

## 8. Commenting and flagging

When a problem cannot be safely fixed without changing scientific intent, use concise inline comments rather than silent rewriting.

Examples:
`% EDITOR: This claim appears broader than the evidence stated here.`
`% EDITOR: Consider narrowing the scope or adding support.`
`% EDITOR: Causal wording may be stronger than the evidence described.`
`% EDITOR: Transition between these paragraphs is weak.`
`% EDITOR: This sentence seems to mix result and interpretation.`

Do not remove existing author comments.

---

## 9. What to avoid

Avoid or flag rather than silently performing:
- rewriting full paragraphs without consultation,
- changing section order,
- merging sections,
- introducing stronger claims,
- converting association into causation,
- expanding local results into field-wide statements,
- adding decorative examples,
- replacing precise technical language with vague readability-oriented wording,
- making the prose more formal without making it clearer.

---

## 10. Standard for success

A successful edit makes the manuscript:
- easier to read on first pass,
- easier to follow logically,
- more precise about what is claimed,
- more explicit about scope and uncertainty,
- more concrete where abstraction had become unhelpful,
- less vulnerable to reviewer challenge,
- and still fully faithful to the original science, citations, equations, comments, and LaTeX structure.

---

## 11. Operational workflows (global)

Use these workflows for manuscript work that is not chapter-specific benchmarking.

### A. Explore manuscript (read-only)
Use when you need a structural status snapshot before edits.

Steps:
- read the active entry file(s) and included source files within `manuscript/`,
- map section hierarchy and file organization,
- identify completion state (drafted vs stub/placeholder),
- flag missing transitions, unsupported claims, weak passages,
- check consistency of labels, refs, and cite keys,
- do not edit while running this mode.

Recommended output:
1. Structure overview,
2. section-by-section completion status,
3. key gaps and weak spots,
4. cross-reference/citation integrity notes,
5. prioritized next revision targets.

### B. Draft from evidence notes
Use when converting evidence into manuscript-ready draft prose.

Rules:
- every factual statement must trace to source notes,
- preserve attribution and uncertainty,
- do not invent claims or citations,
- prepare `\cite{}` placeholders using existing keys,
- mark unresolved support with concise TODO/editor flags.

Recommended output:
1. draft LaTeX section text,
2. citation placeholder map,
3. uncertainty flags,
4. paragraph-to-source traceability notes.

### C. Section refactor
Use for targeted clarity/flow improvement in existing text.

Rules:
- preserve `\cite{}`, `\label{}`, `\ref{}` integrity,
- keep section hierarchy unchanged unless explicitly requested,
- do not alter equations or scientific claims,
- prioritize transitions, topic sentences, and paragraph unity.

Recommended output:
1. edited section text,
2. brief change summary,
3. integrity confirmation (`\cite{}`, `\label{}`, `\ref{}` preserved).
