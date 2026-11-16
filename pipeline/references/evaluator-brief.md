# Brief for the independent evaluation pass

You did not write this review. Trust nothing in it.

The evaluator is a top-tier model that is **separate from the writer model**. It is called once, without tools, and it receives exactly two things: this brief (the instruction block below) and the output of `scripts/compact_for_chat.py` (the review without Questions and Appendix, the reference list, and the claim table with each claim's source quote and location). It writes `<slug>.eval.md`.

The review follows the format in `pipeline/SKILL.md` (step 5): English only, no paper summary, no process disclaimers, a clear position, and two differences per component (usual approach, state of the art).
The field comparison (usual approach, counts) comes from the wiki ledger tallies (slot-filled / pattern match, unique studies); the candidate papers were not read one by one, and only the target and the papers the review names were read in full. Do not ask for candidate-by-candidate audits, confirmed counts or recall estimates; check the claims that are made.

Check, in this order (at most 25 claims):
1. **Target paper (6–8 claims).** Each statement about the target in the Verdict and in "Where the claims outrun the evidence": does the claim-table quote and location support it? Internal inconsistencies in the target and caveats the authors state themselves that the review missed.
2. **Usual approach and state of the art (per component section).** Is the stated usual approach plausibly the typical design for this task? Is the stated state of the art really the best work today, including later work, with the year, metric and value its source reports? Name any better or more recent work you know of.
3. **Comparators (8–12 claims).** All comparators that carry the central claim: is the number in the quoted passage, with the condition the review attaches to it?
4. **Central claim and position.** Name the strongest confound (different starting point, baseline strength, task, absolute vs relative change) and say whether the review handled it. Is every position backed by a citation, a location in the paper or an Appendix number? Flag any position stronger than that evidence, and any hedged wording where the evidence allows a plain statement.
5. **Fairness.** Is any work the authors could not have read (within 6 months of the target, or later) treated as prior work or as a missed citation? Does the review present as its own finding something the authors report themselves?
6. **Absence and novelty claims.** For each "none of the N ledger papers" or "first / only" sentence: does it name the deciding prior works, and do you know of an earlier work with the same design? Report it with year and locator.
7. **Verdicts.** For each slot verdict that is not `standard`: does it follow the verdict rules in `pipeline/SKILL.md` (for `ahead`: ledger count in the Appendix, deciding priors named, effect repeated)?

Output (English): a table (claim, where checked, correct / wrong / insufficient evidence, note), then a list of required fixes ordered by impact, then two scores out of 10 (procedure, final text). No praise section longer than five lines.

## Instruction block (send exactly, replacing the target line)

The call is one message: this block, then a line `=====REVIEW TEXT=====`, then the full output of `compact_for_chat.py <slug>.md compact.md --claims claims.md`.

```
You are a detail checker. Below is an expert review (in English) of <title, authors, arXiv/DOI, year of the target paper>, with a compact reference list and a claim table (each number or citation in the review, the source quote and its location). Do not judge the prose; find errors of detail. You have no tools: work from the quotes in the claim table and from what you know of the literature, and mark anything you cannot check from these as "insufficient evidence".

Please check:
1. Bibliographic errors in the reference list (authors, title, venue, year, volume and pages, DOI, arXiv id). Check as many as possible.
2. Whether numbers in the text (error rates, accuracy, sensor counts, ratios, counts) match what the cited papers report, especially for the target paper and the main comparators. Use the claim table's quote and location as the starting point.
3. Whether each citation number [n] points to a work that actually supports the claim.
4. Calculation errors (relative change etc.) and internal contradictions (the same quantity given different values in different places).
5. Chronology: is any work published after the target treated as prior work? Is each [concurrent] / [later] label right?
6. For each "Usual approach" and "State of the art" line: is that really the usual design for this task, and is there better or more recent work than the stated state of the art? Give the work, its year, metric and value.
7. Any judgment in the review that its cited evidence does not support.
8. For each claim-table row: does the quote (and its location) support the claim as written, including number, unit and condition? Answer match / mismatch / no quote.

Answer in English. Output format: a table (No. | Location (section and first words of the sentence) | Type (bibliographic / number / citation / calculation / contradiction / chronology / state of the art / judgment / quote match) | What is wrong | Value you believe correct | Evidence (locator or location in the source) | Confidence (high / medium / low)). Then the required fixes ordered by impact, then two scores out of 10 (procedure, final text). At the end, list the items you could not check. Mark inference as inference.
```

The evaluator cannot see the wiki; counts derived from the wiki (scan totals, tiers) are outside its check. Save its answer verbatim to `<slug>.eval.md` with the date and the evaluator label "a language model separate from the writer". Its answer and the triage log (`<slug>.triage.md`, verdicts applied / rejected / unverified) stay in English; neither is published as review text.
