# Evidence Editing Instructions

Apply these guidelines when editing files under `evidence/`.

## Purpose

The purpose of `evidence/` is to preserve, organize, and interpret support material without collapsing it into final manuscript claims.

Treat evidence work as structured scientific traceability, not as polished prose writing. The main goals are:
- preserve what the source actually supports,
- make support relationships explicit,
- retain uncertainty, scope, and attribution,
- distinguish strong evidence from weak evidence,
- separate extracted evidence from synthesis, interpretation, and manuscript-ready claims.

Do not turn provisional evidence into settled conclusions unless explicitly instructed.

---

## 1. Core principles

### A. Separation of evidence from manuscript prose
Keep evidence distinct from final paper language.
- Do not silently merge evidence notes into manuscript files.
- Do not rewrite working evidence into publication-style claims unless explicitly asked.
- Keep extraction, interpretation, and final argumentation separate.

### B. Traceability over polish
Prioritize source traceability, claim linkage, and epistemic clarity over smooth writing.
A useful evidence note should make it easy to answer:
- what the claim is,
- what supports it,
- how directly it is supported,
- where the support comes from,
- how strong the support is,
- what remains uncertain.

### C. Preserve epistemic discipline
Do not flatten or strengthen evidence.
Preserve:
- uncertainty,
- qualifiers,
- attribution,
- scope,
- conditions,
- contradictions,
- null findings,
- reviewer-relevant caveats.

Evidence notes should distinguish:
- observation vs inference,
- direct support vs indirect support,
- present-paper claim vs cited-background claim,
- general claim vs single example,
- support vs qualification vs dispute.

### D. No invented support
Never invent:
- citations,
- quoted passages,
- results,
- metadata,
- page numbers,
- evidence links,
- factual claims not grounded in retrieved material.

If verification is incomplete, mark it clearly.

---

## 2. Evidence areas

Use the following file roles consistently:

- `evidence/literature/extracts/`
	Close-to-source notes, quoted or near-source passages, retrieval logs, local interpretations tied tightly to source text.

- `evidence/literature/summaries/`
	Synthesized literature summaries that combine multiple sources while preserving attribution and uncertainty.
	
	**Note on canonical books**: Summaries of canonical textbooks (e.g., Box-Jenkins time series, Montgomery DOE, Goodfellow deep learning) are separately maintained in `2026-03-28_canonical_books_summaries.md`. When citing these books for background framing, reference both the bibliography entry and this summary document for examiner context. Canonical-book citations are appropriate for establishing frameworks and standard terminology, not for empirically precise or contested claims—use article/proceedings sources for those.

- `evidence/claims/`
	Claim-support notes, evidence mapping, citation-needed material, support gaps, and defensibility checks.

- `evidence/reports/`
	Supporting reports, white-paper style documents, structured internal summaries, or evidence-based background documents.

- `evidence/experiments/run-notes/`
	Execution notes, experiment logs, procedural notes, anomalies, deviations, and unresolved issues.

- `evidence/experiments/result-summaries/`
	Interpreted result summaries with explicit distinction between result, interpretation, and limitation.

---

## 3. What counts as scientific evidence

Do not assume that only explicit sentence-level claims count as evidence.

Relevant evidence may include:
- direct explicit claims,
- empirical findings,
- definitional or taxonomic statements,
- methodological use of X for Y,
- operationalisation or measurement language,
- mechanism or explanatory links,
- examples or case instances,
- comparative statements,
- review or synthesis statements,
- contextual field-positioning statements,
- qualified, conditional, or boundary-limited claims,
- negative, null, mixed, or contested evidence,
- metadata-level evidence from titles, abstracts, keywords, or section headings.

A passage may support different relation types, for example:
- causal,
- correlational,
- predictive,
- definitional,
- taxonomic,
- methodological,
- operational,
- comparative,
- contextual,
- exemplifying,
- contested.

Always try to preserve what kind of relation the source actually supports.

---

## 4. Evidence classification rules

When useful, classify evidence using these dimensions:

### A. Relation type
Label the kind of relation supported, such as:
- causal,
- correlational,
- predictive,
- definitional,
- taxonomic,
- methodological,
- operational/measurement,
- comparative,
- contextual,
- example/case,
- dispute/null/mixed.

### B. Support polarity
Indicate whether the source:
- supports,
- qualifies,
- disputes,
- reports mixed evidence,
- or merely mentions the relation.

### C. Explicitness
Indicate whether support is:
- explicit,
- implicit but well-supported,
- weakly suggestive,
- or ambiguous.

### D. Scope
Distinguish:
- general field-level claim,
- domain-specific claim,
- method-specific claim,
- condition-specific claim,
- single-case or example-level evidence.

### E. Provenance
Distinguish:
- current-paper finding,
- current-paper interpretation,
- cited-background claim,
- review synthesis,
- author framing or motivation.

Do not collapse these distinctions unless explicitly instructed.

---

## 5. Evidence strength guidance

Assess evidence strength relative to the claim being supported.

A useful practical scale:

- **Strong direct evidence**
	Clear, explicit, well-scoped support directly matching the target claim.

- **Clear support**
	Explicit support, but backgrounded, narrower, or not the paper’s main result.

- **Moderate support**
	Good example, operationalisation, mechanism, or condition-specific support.

- **Weak but relevant support**
	Suggestive, implicit, or contextual support that helps but does not settle the claim.

- **Mention only**
	X and Y co-occur or are discussed, but relational support is weak or unclear.

- **Not valid evidence**
	No defensible support for the target claim.

Remember:
- a definitional statement may be strong for taxonomy questions,
- but weak for causal questions;
- a case example may be strong for existence-of-use,
- but weak for broad generalization.

### F. Canonical Books vs. Article-Level Evidence

**Use canonical textbooks for**:
- Establishing widely accepted frameworks and terminology (e.g., "ARIMA models follow Box & Jenkins methodology")
- Explaining standard modeling procedures or architectural conventions
- Providing foundational background that does not need primary-source anchoring
- Defining a field's consensus on a particular method or approach
- Framing your problem within established disciplinary practice

**Use article/proceedings evidence for**:
- Empirical findings, experiments, or results that support or contradict a claim
- Precise assertions about performance, capability, or limitation
- Contested or novel claims that would benefit from current peer-reviewed support
- Quantitative or qualitative evidence (numbers, percentages, outcomes)
- Claims about what is new, unsolved, or uncertain in the field

**Citation strategy**:
1. **Background framing**: Cite canonical books liberally; examine the canonical-books summary document (`evidence/literature/summaries/2026-03-28_canonical_books_summaries.md`) to confirm scope match
2. **Precise claims**: Follow with article/proceedings citations (via SmartLibrary extraction logs or direct evidence files)
3. **Examiner guidance**: Do not assume all readers have read every canonical book; brief context (from the summary) may help justify textbook-only citations in some contexts

See `evidence/claims/` for mapping specific manuscript claims to their evidence anchors across both book and article sources.

---

## 6. Editing priorities

Prioritize the following when editing evidence files:

1. organization and traceability over polish,
2. explicit links from claims to support,
3. preservation of qualifiers such as “suggests,” “may,” “preliminary,” “under these conditions,”
4. accurate distinction between evidence and interpretation,
5. clear notation of support strength and uncertainty,
6. clear TODO markers where verification, metadata, or follow-up retrieval is still needed,
7. preservation of contradictory, limiting, or null evidence.

---

## 7. Smart Library access and retrieval workflow

This environment has access to a Smart Library service for literature search and document retrieval.
Treat Smart Library as the primary retrieval tool for research and literature-discovery tasks before falling back to general web search.

**Base URL**: `http://localhost:8001`

### Preferred use cases
Use Smart Library when you need to:
- search a local research corpus,
- find relevant papers or passages,
- retrieve metadata and citation details,
- recover chunk context,
- build evidence packages,
- verify whether a source supports a specific claim.

### Corpus coverage note
Treat the current Smart Library corpus as primarily containing journal articles and conference proceedings.
Do not assume strong coverage for books, monographs, standards, or technical reports.
If a canonical book/report source is required and Smart Library retrieval fails, mark it explicitly as a corpus-coverage gap and use a documented fallback path.

### Verified API endpoints

**Search**
- `GET /api/search/?q=<query>&top_k=<number>`
	Semantic literature search returning chunk matches with metadata.

**Document lookup**
- `GET /api/documents/{doc_id}`
	Retrieve metadata such as title, authors, year, abstract, DOI, and source path.

- `GET /api/documents/search/?title_contains=<text>&author_contains=<text>&year=<year>&id=<id>`
	Metadata-filtered document search.

**Text and context retrieval**
- `GET /api/documents/text/{text_id}`
	Retrieve a specific chunk.

- `GET /api/documents/text/{text_id}/context?before=<n>&after=<n>`
	Retrieve chunk plus surrounding context.

- `GET /api/documents/{doc_id}/pages/{page_number}/text`
	Retrieve full page text.

**Bootstrapping**
- `GET /api/agent/instructions`
- `GET /llms.txt`

### Preferred workflow

1. **Search**
	 Use `/api/search/?q=...&top_k=10` with a descriptive natural-language query.

2. **Inspect results**
	 Review chunk text, title, score, and page number.

3. **Recover context**
	 Use `/api/documents/text/{text_id}/context?before=1&after=1` when a single chunk is insufficient.

4. **Verify metadata**
	 Use `/api/documents/{doc_id}` to capture citation details.

5. **Extract and record**
	 Store evidence with traceable identifiers such as:
	 - `document_id`
	 - `chunk_id`
	 - page number
	 - title
	 - quoted or paraphrased support
	 - local note on what relation is supported
	 - strength/polarity if relevant

### Retrieval behavior
- Prefer descriptive natural-language queries over sparse keyword strings.
- Start with semantic search.
- Use metadata search when searching by title, author, year, or incomplete citation details.
- Use context retrieval before drawing conclusions from short excerpts.
- Reformulate and retry if results are weak.
- Preserve document title, `document_id`, `chunk_id`, and page number for traceability.

---

## 8. File-writing guidance

### General prose guidance
- In evidence files, preserve source-backed facts and traceability first; readability is secondary.
- Prefer prose over bullets for ordinary explanation and interpretation, but use bullets when they preserve source structure, factual distinctions, or claim-to-evidence mapping.
- Enumerate as many items as needed when the source material itself provides substantive, distinct facts that must be retained.
- Do not mechanically enumerate long strings only for style; enumerate when the breadth is evidentially important or needed for faithful capture.
- Prefer compact parenthetical examples where suitable, for example "this appears in several settings (e.g. X and Y)," but expand to longer lists when that is required for factual completeness.

### For extracts
- stay close to source wording,
- preserve attribution,
- avoid overstating,
- note whether the passage is direct evidence, contextual framing, or only partial support,
- include retrieval metadata.

### For summaries
- synthesize carefully across sources,
- do not erase disagreement,
- separate consensus from isolated findings,
- distinguish repeated patterns from single examples,
- preserve scope and qualifiers.

### For claim-support notes
- state the target claim explicitly,
- list supporting sources separately,
- indicate strength and limits of support,
- mark gaps, uncertainties, and citation needs,
- note if support is only indirect or example-based.

### For experiment notes and results
- separate raw observation from interpretation,
- preserve provisional status where relevant,
- mark anomalies, deviations, failed runs, or unresolved issues,
- do not convert exploratory notes into validated findings.

---

## 9. Prohibited changes

Do not:
- invent citations, quotations, results, or claims,
- silently merge evidence into manuscript prose,
- remove attribution,
- remove uncertainty qualifiers,
- strengthen suggestive evidence into definitive claims,
- turn a single example into a general conclusion,
- convert association into causation,
- suppress contradictory or null evidence,
- present cited-background claims as if they were directly established by the current source.

---

## 10. Comments, uncertainty, and TODOs

Use explicit markers where verification or interpretation is incomplete.

Examples:
- `% TODO: verify page range and exact wording`
- `% TODO: support appears indirect; check surrounding context`
- `% TODO: evidence supports methodological use, not causal claim`
- `% TODO: current note may overgeneralize from a single case`
- `% TODO: citation metadata incomplete`

When unsure, preserve the uncertainty rather than resolving it by guesswork.

---

## 11. Standard for success

A successful edit makes evidence files:
- better organized,
- more traceable,
- more explicit about what supports what,
- clearer about strength, scope, and uncertainty,
- more faithful to source meaning,
- better separated from manuscript-ready prose,
- and more useful for later claim construction, review, and citation checking.
