# Evaluation: Modeling Coarticulation in EMG-based Continuous Speech Recognition

Evaluator: a language model separate from the writer. Date: 2026-11-27.

What was read: the review (`modeling-coarticulation-in-emg-based-continuous-speech-recognition.md`), `compact.md`, `claims.md`, `slots.json`, `verdict.json`, both topic audits, the target source text (`papers/doi-10.1016-j.specom.2009.12.002/source/text.txt`, accepted manuscript), the five reader-prior texts in `reader-priors/`, and the Benster 2024 source text. Spot checks of the M06 population used wiki source texts.

## Claim table

| # | Claim (location in review) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Nine PF streams bundled by decision trees beside a phone stream (Verdict) | Target §3.1, §3.3 | correct | Nine PFs with >50,000 frames; 70 leaves per stream; weights 0.11 per PF and 0.01 for the phone stream. |
| 2 | Dating: target first public 2009-12, prior means before 2009-06, Interspeech 2009 is [concurrent] (Appendix, refs 4) | Target front matter (received 15 Nov 2009, accepted 2 Dec 2009, manuscript dated 1 Dec 2009); Wand et al. 2009, ref [7] | correct | The first public BDPF papers are Wand et al. and Toth et al., Interspeech 2009 (Sept 2009). Both cite the target ("to appear") as their source, so they are [concurrent], not a same-group precedent. BIOSIGNALS 2009 [3] (Jan 2009) has no PF streams. Wand & Schultz 2009a (CCIS, "to appear") is [later]; I could not check its content. Jou's 2008 thesis is not in the wiki, so I could not check it. The bundling dates hold. |
| 3 | "None of the 12 prior non-acoustic-signal recognizers bundles features" (Verdict, M06) | M06 audit `dated_counts`; bundling full-text pattern | correct within the stated setting | No prior design in the wiki uses bundling. But the setting leaves out acoustic ASR, where the authors themselves name a similar design (finding 1). |
| 4 | "8 of 12 ... use phone or word HMM units with no feature stream, 4 name feature streams" (M06 Usual approach) | Source texts of `pmc-25146-brainwave`, `isca-manabe03_eurospeech`, `isca-meltzner08-subvocal`, `isca-wrench00_icslp`, `doi-10.1109-asru.2005.1566521` | wrong | Suppes 1997 (EEG) and Manabe 2003 contain no HMM. Meltzner 2008 matches "feature stream" only through its reference list. The audit itself says "PF streams confirmed in Jou 2007 only". |
| 5 | Population of 12 is complete and deduplicated (Appendix) | Wiki folders | insufficient | Duplicates are handled (isca-wand07_emgwav is not counted twice). Missing: Hueber et al. Interspeech 2007 and Interspeech 2008, both continuous HMM phone recognizers from ultrasound and lip video ("monophone only", 2008). They fall inside the inclusion rule. They would not change bundled = 0. |
| 6 | Group tried the ingredients separately: Jou 2007 AF streams 33.9→29.9% on one speaker; Wand 2009b clustered triphones 68.92→60.97% (M06) | Jou 2007 abstract, §4.3, §5; Wand 2009b §4.5 | correct, one condition missing | Jou 2007 picked the AF subset on half of the *test set* (two-fold cross-validation), not on a separate development set. Wand 2009b's 68.92→60.97% system was trained "on all available data (including the training data of the speaker to be tested)". |
| 7 | "Clustered sub-word units go back to [5]", "[6] used context-independent phones" | Walliczek 2006 §4.3; Jou 2006 §2.3 | correct | See finding 17: this contradicts the target's "first time" claim in §4. |
| 8 | Ablation 41.99 / 35.78 / 31.49 (Table 3); pooled 45.24 → 44.95, not significant (Table 4) | Target Table 3, Table 4, §4 | correct | |
| 9 | Confound: 290 → 2,489 Gaussians and no CD-phone control in the speaker-dependent tables (M06) | Target Table 2, §3.4, §4 | correct but incomplete | The review leaves out the authors' own partial control. One BDPF stream has a Gaussian count comparable to the phone system and is 10.6% relative better (§3.4). The authors also say speaker-dependent CD phone models cannot be trained on this data (§4). |
| 10 | Repetition "over 28 sessions of 14 speakers and under pooled training" (Verdict, M06) | Target §3.4 (α ≤ 0.07%), §4, Figs. 5–6; notes t47 | insufficient | The paper reports only means with paired t-tests. There is no per-session gain count and no variance. The pooled regime reuses the same 28 test sessions (10 utterances each), so it is not an independent repeat. |
| 11 | M06 state of the art: Benster 2024, 12.2% WER, silent, open vocabulary, one speaker, LLM decoding | arXiv 2403.05583, Abstract, Table 3, App. A.3 | correct, but the mode is mismatched | The same table gives 3.7% WER on vocal EMG, which matches the target's audible mode. The 12.2% comes from the validation-selected ensemble; a test-selected ensemble reached 8.0% (A.3). The gain comes from LLM rescoring and ensembling, not from the acoustic-unit design. |
| 12 | M03 is "weaker than the group's earlier held-out-speaker design on the same corpus [3]" (Verdict) | Wand 2009b §3.4, §4.5 | partly wrong | In [3] only the CI cross-speaker and MLLR experiments hold the speaker out. [3]'s own context-dependent "Speaker-Independent Training" includes the test speaker's data, which is the target's design. |
| 13 | "About 28%" speaker-independent claim is pooled (62.15→44.95%) | Target §4, §5, Table 4 | correct | 27.7% relative (inference). |
| 14 | M03 state of the art: Scheck 2024, one-session adaptation beats training from scratch | M03 audit `state_of_the_art` | insufficient | The task is sEMG-to-speech synthesis, not recognition. The value field is "p < 0.01", with no metric value. The audit labels the timing "prior", while the review says [later]. |
| 15 | M03 Usual approach "Per-speaker models" | M03 audit tally | insufficient | No count or tier is given. The Appendix gives the usual design as "held-out-speaker test of a pooled model 40 (pattern match, all years)", which conflicts with this line. |
| 16 | M12: three of four read priors give no development set; [2] uses a development subset | Jou 2006 §4–5; Walliczek 2006 §5.1.1; Wand 2009b §4.5; Jou 2007 §4.3 | correct | [2]'s "development subset" is half of the test set. |
| 17 | Target tunes the weights and the 70-leaf size on the test set (§3.3); the data for the 220 leaves is not named (§4) | Target §3.2, §3.3, §4 | correct | The authors state this themselves. The bullet credits them; the Verdict does not. |
| 18 | Concurrent silent test: above 80% WER for most speakers; 30.10% for the speaker with earlier silent sessions [4] | Wand et al. 2009 §3.1, §4.1, Fig. 2 | correct, selectively reported | Speakers 6 and 11 are "in a reasonable range". Speaker 15 is an extra speaker outside EMG-PIT (500-sentence session, 250 silent). The vocabulary is 108 words. |
| 19 | Silent speech "claimed in §1, scored nowhere (§2.2)" | Target §1, §2.2, §5 | correct, weak location | The strongest overclaim is in §5: "bringing EMG-based speech recognition within useful range for silent speech applications". |
| 20 | Five streams 31.25%, nine 31.49% (Fig. 7) | Target §3.4 | correct number, not an overreach | The authors say the two are "essentially the same". |
| 21 | α = 0.7% (§3.2) against α ≤ 0.07% (Table 3) | Target §3.2; end of §3.4 | correct | A real contradiction: the 3.5* row (CI PF vs baseline) falls under both statements. |
| 22 | Lattice 18.76% at density 100 is an oracle bound (inference) | Target §3.4, Fig. 8, Table 3 | correct | The authors present it as "an estimate of how much information is available". The only overreach is listing it as a row in the system table. |
| 23 | §3.2 credits [2] with "up to 10%" while [2] reports 11.8% | Target §3.2; Jou 2007 abstract, §4.3 | correct number, wrong category | This understates a prior. It is not a claim that outruns evidence. |
| 24 | Verdict M06 ahead: zero of 12 priors, four read priors, repetition | SKILL.md verdict rule | correct only inside the non-acoustic setting | See findings 1, 2 and 4. |
| 25 | M03 standard and M12 standard, with reasons | SKILL.md rules | correct | M03: one confirmed prior is below the three-paper rule for `behind`. M12: the target matches the typical practice of the read priors. |

## Findings, ordered by impact

1. **Critical. Location:** Verdict, sentence 2; M06 section ("Verdict: ahead ..."); Appendix M06 inclusion rule.
   **Evidence:** The setting leaves out acoustic ASR without saying so in the body. The authors themselves credit acoustic ASR for every part of the design:
   - PF streams beside phone models: Kirchhoff 1999; Metze and Waibel 2002; Metze 2005 (§3.1–3.2).
   - The decision-tree clustering mechanism: Bahl et al. 1991 (§3.3).
   - A single-stream form of bundling: "using only one BDPF stream ... is an approach similar to the one described in (Yu and Schultz, 2003)" (§3.4).
   - CD-BDPF clustering "adds significant flexibility to phoneme context clustering ..., a fact which has also been described in (Yu and Schultz, 2003)" (§4).

   Published practice counts precedents from any signal. Under that rule, Yu and Schultz 2003 (Proc. Eurospeech, pp. 1869–1872) is a deciding prior that was not read, so the `ahead` rule (deciding priors read in full) is not met.

   **Fix:** In the M06 section and the Verdict, state the boundary and the reason: "ahead among non-acoustic recognizers; the clustering mechanism, the feature streams and a one-stream form of bundling come from acoustic ASR [Bahl 1991; Kirchhoff 1999; Metze and Waibel 2002; Yu and Schultz 2003], as the authors state (§3.1–3.4)". Read Yu and Schultz 2003 as a deciding prior.
   - If it already bundles features per stream across several streams, set M06 to `standard` and call the contribution a transfer to EMG.
   - If it uses a single tree only, keep `ahead` for the multi-stream form. Cite Fig. 7: one stream gives 42.16%, against 31.49% for nine streams.

2. **Major. Location:** M06 Usual approach, "8 of 12 ... use phone or word HMM units with no feature stream, 4 name feature streams".
   **Evidence:** Suppes 1997 and Manabe 2003 contain no HMM. Meltzner 2008 matches "stream" only through its reference list. The audit's own note says "PF streams confirmed in Jou 2007 only".
   **Fix:** "8 of 12 name no feature stream (pattern match); PF streams confirmed in one (Jou 2007 [2]), three further pattern hits unconfirmed". Drop "HMM".

3. **Major. Location:** Verdict, "the gain holds over 28 sessions of 14 speakers and under pooled training"; M06, "repetition over 14 speakers and two training regimes".
   **Evidence:** The paper reports only averages with paired t-tests (α ≤ 0.07%, §3.4). There is no per-session gain count and no variance (notes t47). The pooled regime is tested on the same 28 sessions of 10 utterances. The tuning was done on that same test set, so the t-tests are optimistic too.
   **Fix:** "Averaged over 28 sessions (10 test sentences each), paired t-tests significant; per-session results only in Figs. 5–6; the pooled result reuses the same test sessions." Keep `ahead` only if per-subject repetition is accepted at this strength, and say so.

4. **Major. Location:** M06, "Two confounds remain: the model grows from 290 to 2,489 Gaussians ... with no context-dependent phone control".
   **Evidence:** The authors' own control goes unreported. One BDPF stream has a Gaussian count comparable to the phone system and is 10.6% relative better (§3.4, discussion of Table 2). The authors also say speaker-dependent CD phone models cannot be trained on this data (§4). Pooled training does give a CD-phone control: 56.55% against 45.24% (Table 4).
   **Fix:** Report these first. Then narrow the confound: the parameter growth of the 10-stream system is matched only at one stream. Drop "the phone stream keeps weight 0.01" as a confound, or explain what it confounds.

5. **Major. Location:** Verdict, "weaker than the group's earlier held-out-speaker design on the same corpus [3]"; M06, "tree-clustered triphones in a speaker-independent recognizer".
   **Evidence:** Wand 2009b §4.5 trains its triphone "Speaker-Independent Training" on "all available data (including the training data of the speaker to be tested)". That is the target's design. Only the CI cross-speaker experiments in [3] (with MLLR) hold the speaker out. The target's §4 states its design plainly ("trained with the combined training data ... then tested for each speaker").
   **Fix:** "The target, like [3]'s triphone experiment, calls pooled training that includes the test speaker 'speaker-independent'; §4 states this, and the term in §5 ('about 28% in the speaker-independent system') overstates it. [3] held the speaker out only for context-independent models with MLLR." In the M06 sentence, mark the 68.92→60.97% system as pooled with the test speaker included.

6. **Major. Location:** M06 State of the art, "12.2% WER on open-vocabulary silent EMG ... against the target's 31.49% on audible EMG".
   **Evidence:** The SOTA source reports 3.7% WER on vocal EMG in the same Table 3. That number matches the target's mode. The gain comes from LLM rescoring and ensembling (the decoder), not from the acoustic-unit design this slot reviews.
   **Fix:** "3.7% WER on vocal EMG and 12.2% on silent EMG, open vocabulary, one speaker, LLM-rescored ensemble [7]; no unit-level comparison to bundling exists." Optionally add that 12.2% is the validation-selected ensemble (8.0% for a test-selected one, App. A.3). This also makes the M12 point about test-set selection.

7. **Major. Location:** M03 State of the art, and the table row for [8].
   **Evidence:** The audit's SOTA is an sEMG-to-speech synthesis model, which is a different task from recognition. Its "value" is "p < 0.01", with no metric value. The audit records the timing as "prior", against [later] in the review.
   **Fix:** Give the metric and value reported in Scheck 2024 §IV-B and say it is a synthesis model. Otherwise choose a cross-speaker EMG recognition result. Correct the audit timing to later.

8. **Major. Location:** M03 Usual approach, "Per-speaker models".
   **Evidence:** There is no ledger count or tier. The Appendix says the usual design is "held-out-speaker test of a pooled model 40 (pattern match, all years)", which contradicts this line.
   **Fix:** Give a dated count for per-speaker training at the target's time, with its tier, or align the line with the Appendix tally and say whose time it describes.

9. **Minor. Location:** Verdict, last sentence; bullet "Silent speech".
   **Evidence:** [4] Fig. 2 and §4.1:
   - Speakers 6 and 11 are "in a reasonable range".
   - Speaker 15 (30.10%) is an extra speaker outside EMG-PIT, with a 500-sentence session, 250 of them silent.
   - The vocabulary is 108 words, and the best audible WER there is 30.19%.

   The overclaim the review targets is in §5, not §1.
   **Fix:** "Above 80% WER for most of the 14 pilot speakers; only one silent-experienced speaker from outside the corpus reached 30.10% [4]." Cite §5's "within useful range for silent speech applications".

10. **Minor. Location:** "Where the claims outrun the evidence", bullet "Prior work".
    **Evidence:** "Up to 10%" against 11.8% understates a prior work. It is not an overreach by the target. The 11.8% in Jou 2007 is the peak on cross-validated halves of the test set for one session.
    **Fix:** Move it to Questions, or drop it.

11. **Minor. Location:** bullet "Stream count".
    **Evidence:** The authors themselves call 31.25% and 31.49% "essentially the same" (§3.4). The bullet restates them and names no overreach.
    **Fix:** Drop it.

12. **Minor. Location:** bullet "Lattice".
    **Evidence:** §3.4 presents the lattice WER as an information estimate.
    **Fix:** "Table 3 lists the 18.76% lattice oracle as a system row (inference: an oracle bound, not a result)."

13. **Minor (missed).** Table 3's relative gains form a ladder over systems that are not nested. "Bundled PFs 14.8%" is measured against the CD-PF row (41.99%), but the bundled system is not built on that row. §3.3 gives 24.1% against the baseline, and the end of §3.4 calls 14.8% the gain "by bundling".
    **Fix:** Add a bullet: the gain attributed to bundling alone is 21.4% against CI PFs (inference).

14. **Minor (missed).** §4 says Wand and Schultz 2009b applied CD phone modelling to EMG "for the first time". Walliczek 2006 [5] had already trained clustered CD triphones on EMG (§4.3–5). The review cites [5] for clustered units but does not flag the priority claim.
    **Fix:** Add one bullet.

15. **Minor. Location:** M06 body, "A full-text search for feature bundling over the whole wiki returns only ...".
    **Evidence:** This is a process statement in the body.
    **Fix:** Move it to the Appendix and keep only "no prior work (Appendix)" in the body.

16. **Minor. Location:** M03, "The target pools the 14 pilot speakers and tests each of them (§4)"; M12, "the target decodes 10 sentences per speaker with the 101 test words (§2.2)"; M06, the full Table 3 ladder.
    **Evidence:** These restate the method and results.
    **Fix:** Keep only the numbers that carry a comparison, such as 35.78 against 41.99.

17. **Minor. Location:** Verdict, "Its size is an upper bound, because stream weights and tree size were tuned on the test set (§3.3)".
    **Evidence:** Test-set tuning biases the result but does not make it a strict upper bound. The Verdict also does not say the authors state this themselves.
    **Fix:** "Its size is optimistic: as the authors state (§3.3), stream weights and tree size were tuned on the test set."

18. **Minor. Location:** M06 Usual approach, "chosen on development data"; M12, "the lineage's best protocol [2]".
    **Evidence:** Jou 2007 §4.3 splits the test set into two halves for cross-validation.
    **Fix:** "chosen on halves of the test set in two-fold cross-validation".

19. **Minor. Location:** M06 audit (affects the Appendix "read in full ... (prior)" count).
    **Evidence:** isca-wand09_interspeech appears under `read_prior` with role "prior" and timing "concurrent". The review labels it correctly, but the audit mixes the roles.
    **Fix:** Give it a concurrent role in the audit.

20. **Minor. Location:** Appendix, M06 population.
    **Evidence:** Hueber et al. 2007 and 2008 (ultrasound and lip HMM phone recognizers, in the wiki, inside the inclusion rule) are missing.
    **Fix:** Add both (14 prior, both context-independent), or state why they are excluded.

Unverified, not required: whether Wand and Schultz 2009a (CCIS) or Jou's 2008 thesis contain bundled features, and whether any work after Benster 2024 beats 12.2% (silent) or 3.7% (vocal) on the Gaddy benchmark. The exact online date of the target, 2009-12 or 2010-01, does not change any window.

## Scores

- Procedure: 6/10. The dating, the deciding-prior reads within EMG and the number checks are sound. The any-signal deciding prior (Yu and Schultz 2003) was not read, and the pattern-match labels were overstated.
- Final text: 6/10. Most numbers check out. The `ahead` setting is unstated, the SOTA mode is mismatched, the M03 comparison with [3] is misread, and three "outrun" bullets are not overreaches.

Counts by severity: critical 1, major 7, minor 12.
