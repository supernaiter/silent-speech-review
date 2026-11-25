# Triage of the evaluation (12 findings)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Abstract: "for the first time ... from intracranial electrocorticographic (ECoG) recordings" (t1); the claim is scoped to ECoG. | Outrun bullet rebutting a broader claim removed; Verdict keeps the EMG point as design lineage only. |
| 2 | applied | Metzger 2023 Abstract: 25% median WER (c3), 1,024 unique words (c4); Card 2024 Results: 2.5% WER (c1). | M07 State of the art and M07 table row; Moses 2021 dropped from the review and references. Small-set Metzger result (unverified) not added. |
| 3 | applied | Published table ledger_tally.pattern_counts: n-gram LM 134, LLM rescoring 14 over 1,162 pattern-match studies; its usual_approach field (152) disagrees with its own pattern counts. | M07 Usual approach and Appendix now share one population definition and name the plurality (134); slots M07 field; open item noted in verification_status. |
| 4 | applied | Slot verdict is about design vs the field (Jou 2006: 108-word test-covering vocabulary, p3; Schultz and Wand: 101 words, s4); LM exclusion is unstated (t41), not shown absent. | One sentence in M07 explaining why "standard" holds; closed-set consequence stays in Verdict and Outrun. |
| 5 | applied | §4.4: "Despite the fact that the evaluations in this article have been performed offline" (t33). | Outrun bullet now says the authors state it and that real-time use is untested. |
| 6 | applied | Fig. 4 caption describes the 100 ms panel ("yield different models in auditory regions ... 100 ms after production", t46); §3.1 says discriminability increases until ~150 ms (t30). Compatible. | Bullet removed. |
| 7 | applied | §3.2: "For all dictionary sizes, the performance is significantly better than randomized results" (t47, new notes entry). | M12 body quotes it. |
| 8 | applied | §3.2 defines WER with substitutions, deletions and insertions; 75% correct (t21) does not by itself give 25% WER. | Outrun bullet: "consistent with ... if insertions are few (inference)". |
| 9 | applied | Audit counts: 21 of 145, 45 of 132 are pluralities, not majorities. | M12 Usual approach says "most named". |
| 10 | applied | Target: overt read-aloud (t3); Metzger: severe paralysis (c9); Card: advanced ALS (c10). | Verdict sentence and a new Outrun bullet name the task difference. Intracortical nature of Card/Willett already stated. |
| 11 | applied | Target author list ends with Schultz; Jou 2006 and Schultz and Wand 2010 list Schultz; the target's reference list has no EMG recognition paper (t48). | Verdict: "co-authored by Schultz ... uncited by the paper"; M06 table note. |
| 12 | rejected (unverified) | No later benchmark or Chang-lab bilingual paper was located and read for this review; Card 2024 (2.5%) remains the lowest-WER read state of the art for M06. | Not applied. |
