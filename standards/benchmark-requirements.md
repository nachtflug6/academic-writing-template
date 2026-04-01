# Venue Structural Benchmarks

Use this file for empirical chapter and whole-thesis benchmarks derived from representative theses in your venue/program.

## Purpose and Limits

These benchmarks are for diagnosis and prioritization, not rigid rules.

- Use benchmarks to identify structural gaps and examiner-risk patterns.
- Do not treat ranges as hard constraints when the manuscript has clear rationale.
- If benchmark expectations conflict with formal requirements, formal requirements win.

---

## Whole-Thesis Architecture

Expected structural flow:

Introduction -> Background -> Methodology -> Results/Papers -> Discussion -> Conclusion

Structural signals for a strong thesis:

- Aim and research questions are visible early and answered explicitly late.
- Chapter weight is balanced; synthesis and closure are not underdeveloped.
- Thesis-level synthesis across studies/papers is visible.
- Navigation is clear via section contracts and heading hierarchy.

Common structural risks:

- Research questions are introduced but not explicitly answered.
- Discussion becomes only a recap rather than synthesis.
- Conclusion introduces new material instead of closing the argument.
- Method chapter becomes an extended defense rather than design description.

---

## Chapter Benchmark Table (Fill With Local Baselines)

| Chapter | Target length | Typical subsection count | Typical citation density | Notes |
|---------|---------------|--------------------------|--------------------------|-------|
| 1. Introduction | [placeholder] | [placeholder] | [placeholder] | [placeholder] |
| 2. Background | [placeholder] | [placeholder] | [placeholder] | [placeholder] |
| 3. Methodology | [placeholder] | [placeholder] | [placeholder] | [placeholder] |
| 4. Results/Papers | [placeholder] | [placeholder] | [placeholder] | [placeholder] |
| 5. Discussion | [placeholder] | [placeholder] | [placeholder] | [placeholder] |
| 6. Conclusion | [placeholder] | [placeholder] | [placeholder] | [placeholder] |

---

## Must-Have Signals by Chapter

### Chapter 1 - Introduction

- Problem framing is explicit.
- Aim and research questions are clearly stated.
- Scope and delimitations are visible.
- Roadmap for the thesis is included.

### Chapter 2 - Background

- Key concepts are defined.
- Related work is synthesized, not listed source-by-source.
- Clear bridge to methodology and research questions.

### Chapter 3 - Methodology

- Research design and rationale are explicit.
- Mapping from research questions to methods/evidence is visible.
- Method boundaries and limitations are acknowledged.

### Chapter 4 - Results/Papers

- Findings are organized by thesis logic (e.g., RQ/contribution).
- Provenance of each finding is clear.
- Reporting remains descriptive; interpretation is mainly in Chapter 5.

### Chapter 5 - Discussion

- Findings are interpreted at thesis level.
- Contributions, limitations, and implications are explicit.
- Each research question is revisited and discussed.

### Chapter 6 - Conclusion

- Concise thesis-level closure.
- Direct answers to research questions.
- No major new content.

---

## Review Usage

- Review method and output format: `../.github/instructions/review.instructions.md`
- Formal compliance source: `formatting-requirements.md`
- Structural benchmark source: this file

Use these benchmarks to prioritize revisions and highlight risk areas before handoff.

### Chapter 3 - Methodology
- RQ coherence,
- framing clarity,
- design transparency,
- mapping clarity (aim/RQs -> studies -> methods -> evidence),
- thesis-vs-study method distinction,
- descriptive discipline (description vs debate),
- boundary compliance (method chapter vs discussion role),
- limitation explicitness,
- quality reflection,
- citation sufficiency,
- skim-read citation anchoring for rationale/quality-criteria claims,
- skim legibility.

### Chapter 4 - Results / Papers
- RQ coherence,
- thesis-level organization,
- provenance/mapping clarity,
- results-vs-discussion boundary discipline,
- synthesis quality,
- evidence presentation clarity,
- visual support usefulness,
- citation sufficiency,
- skim legibility.

### Chapter 5 - Discussion
- aim/RQ closure coherence,
- synthesis quality,
- interpretation depth,
- contribution clarity,
- implication quality,
- limitation maturity,
- quality reflection,
- future-work quality,
- citation sufficiency,
- skim legibility.

### Chapter 6 - Conclusion
- fit with aim/RQs,
- thesis-level closure quality,
- directness of answering,
- contribution clarity,
- distinction from discussion,
- adherence to expected internal structure (opening paragraph + 3-4 bullets + closing paragraph),
- word count within ~250 words,
- absence of future work (must not appear here),
- claim discipline and scope control,
- citation discipline (none),
- skim legibility.

---

## Supervisor and Examiner Language Flags

The following words and phrases were specifically scrutinised in feedback from the supervisor and examiner. Treat these as high-priority language-risk items throughout the manuscript.

| Word / phrase | Risk | Safer direction |
|---------------|------|----------------|
| `foundational` | Overclaim; implies the work underpins the field | Use `contributes to`, `provides a basis for`, or describe the specific contribution directly |
| `methodological role` | Vague evaluative label; invites challenge on what the role actually is | Specify the actual function, e.g., `used to structure`, `used to map`, `applied to` |

Apply the general language-risk guidance in `.github/instructions/manuscript.instructions.md` §7 alongside these venue-specific flags.

---

## Terminology Accessibility Rule

**Context (supervisor/examiner feedback):** The thesis is cross-disciplinary. Not all readers will be familiar with AI/ML terminology. Technical terms must be briefly inline-defined the first time they appear in any section a general reader is likely to encounter — particularly Chapter 1 (Introduction) and Chapter 2 (Background).

**Rule:** The first use of any AI, ML, or domain-specific technical term in a cross-disciplinary context must include a brief inline definition. Use the pattern:
> "X, which is a [brief description of what it is/does]"

**Scope:**
- Mandatory in Chapter 1 and Chapter 2.
- Apply in Chapter 5 (Discussion) if a term is reintroduced after a long absence.
- Not required in Chapter 3 (Methodology) or Chapter 4 (Results) where the reader is assumed to have read Chapters 1–2.

**Examples of correctly handled terms:**
- "a large language model (LLM), which is a neural network trained to generate and process text"
- "fine-tuning, which is the process of adapting a pre-trained model to a specific task using a smaller dataset"

**Should not:**
- Use acronyms without expansion on first use.
- Assume the reader knows AI/ML vocabulary because the thesis uses AI tools or methods.
- Add definitions so lengthy they interrupt the argument flow; keep inline definitions to one clause.
