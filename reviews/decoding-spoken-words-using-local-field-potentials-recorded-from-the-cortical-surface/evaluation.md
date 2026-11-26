# Evaluator: a language model separate from the writer

Independent evaluation, 2026-11-26. Inputs: `compact.md`, the review `.md`, `slots.json`, `verdict.json`, the three topic audits, the target source text (`papers/doi-10.1088-1741-2560-7-5-056007/source/text.txt`, PMC author manuscript), Guenther 2009 (`pmc-2784218-wirelesssynth`), Brumberg 2009 (`isca-brumberg09_bcisynth/source/sc_text.txt`), Brumberg 2011 (`pmc-3096823-phonintent`), wiki manifests for the prior and [concurrent] hits, and a scan of all wiki folders dated 2011 or earlier (plus PMC ids below 3,200,000) for intracranial speech material. Wiki and review files were not modified.

## Claim table

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | First public 2010-09; prior < 2010-03; [concurrent] 2010-03 to 2011-03 | target text.txt l.4 "J Neural Eng. 2010 Sep 1"; wiki manifest `published 2010-10-01` | correct | The wiki manifest carries the issue date (2010-10-01); the Appendix should name the basis (PMC/PubMed epub 2010-09-01). |
| 2 | Prior population 2 (Guenther 2009, Brumberg 2009), one participant lineage | M05/M06/M12 audits `prior_tally`; wiki scan | correct as a wiki count; see F2 | No other pre-2010-03 intracranial speech decoder is in the wiki (only Guenther 2009 PMC/DOI folders, Brumberg 2009, Brumberg 2010 review, Towle 2008, Sahin 2009, a perception study). Brumberg 2009 reports the same participant and the same 25 online sessions over 5 months as Guenther 2009, so "2 of 2" is one experiment reported twice. |
| 3 | Known pre-2010-03 intracranial speech classification outside the wiki | target reference list; Brumberg 2011 Introduction | partly handled | Blakely et al. 2008 (EMBC, micro-ECoG phoneme classification) is the only one found; it is not in the wiki and was not read. Leuthardt 2009 and Kellis 2009 (Neurosurgical Focus, micro-ECoG, motor/non-speech; target refs 26, 43) and Wang/Schalk/Kubanek motor ECoG are outside the speech setting. Formisano 2008 is fMRI listening and outside the setting. Tankus 2012, Pei 2011, Leuthardt 2011 are [later]. |
| 4 | Brumberg 2011 names Blakely 2008 and the target as earlier micro-ECoG speech work | Brumberg 2011 text | correct | "closely spaced micro-ECoG arrays (<3 mm spacing) ... four phonemes in Blakely et al., 2008; 10 words in Kellis et al., 2010". |
| 5 | "more than half discarded for some words" (Sec. 2.2); "yes" 81 of 166 (Table 1) | target Sec. 2.2, Table 1 | correct | "hot" 31 of 65 also. |
| 6 | Best five FMC electrodes chosen "with best overall accuracy" with "no separate selection set (Sec. 3.3)" | target Sec. 2.6, 3.3 | insufficient evidence as stated | Sec. 3.3 does not mention a selection set. The inference rests on Sec. 2.6 (per-electrode accuracies come from the classifier) and Sec. 2.2 (only 30 trials per word). The review's own Question 1 shows it is unconfirmed. See F5. |
| 7 | Gains 4.0 points (89.6%, two words) to 20.0 points (48%, ten words); 13.5 ± 5.2 average; all 16 FMC about 28% on ten words (inference) | target Sec. 3.3 | correct | 48 − 20 = 28. Ten-word is one combination (k = n, Sec. 2.6), so the 48% has no spread. |
| 8 | Joint FMC + Wernicke changed accuracy by 0.40 ± 0.43 points | target Sec. 3.2 | correct | See F4 for the inference built on it. |
| 9 | "more input lowered accuracy, the signature of an under-regularised classifier (inference)" | target Sec. 3.2, 3.3 | wrong (contradicted by the paper) | Doubling inputs with the Wernicke array did not lower accuracy (+0.40); selecting best five on Wernicke gave only +1.3 ± 0.7 (Sec. 3.3). The FMC gain is the selection effect the review itself names as the main confound. |
| 10 | Unused macro grid: "the clinical grid in the same patient was not decoded (Sec. 2.1, 2.3)" | target Sec. 2.1, 2.3 | correct | Neuroport recorded only the 32 micro channels; reference tied to the clinical lead. |
| 11 | No significance tests (Sec. 2.6) | target Sec. 2.6, 4.3 | correct | Only comparison with uniform chance; Sec. 4.3 still writes "did not change accuracy significantly". |
| 12 | "nearly 30% at 1 mm" (Sec. 4.2); "hot" 84.4% vs 56.7% (Sec. 3.5) | target | correct | Percentage points. |
| 13 | 500-ms delay slow for conversation (Sec. 4.4.3); prior feedback within 50 ms | target Sec. 4.4.3; Guenther 2009 abstract | correct numbers, caveat missed | The authors themselves compare with a 30-ms trajectory decoder (ref. 9) and call it "a different problem than the decision-based algorithm". See F8. |
| 14 | Guenther 2009 hit rate 45% to 70% between first and last blocks | Guenther 2009 text | correct | "from 45% on the first block to 70% on the last block across sessions". |
| 15 | M12 prior counts: online 2 of 2, held-out session or subject 0, "slot-filled" | M12 audit, both prior tallies | tier wrong; count inconsistent | Held-out zeros are pattern-match counts. The published M12 table (2013-11 tally) lists Guenther 2009 (`doi-10.1371-journal.pone.0008218`) under the same `held_out_session_or_day` regex and under k-fold, so the pattern-match value for this base is 1 of 2, not 0. See F6. |
| 16 | M06 prior counts: formant regression 2, word classification 0, phoneme 0 | M06 audit | correct | Tier slot-filled. |
| 17 | Duraivel 2023: four patients, up to 57% vs 11.11% chance; 20–35% median at standard spacing | claim table d1–d3 | correct | Appropriate state of the art for M05 (micro-ECoG, explicit spacing comparison). |
| 18 | Card 2024: 99.6% with 50-word vocabulary | claim table r1 | correct number, condition missing | First day of use, sentence decoding with a language model over a 50-word vocabulary; not isolated-word closed-set classification. See F7. |
| 19 | Chen 2024: PCC 0.765 on unseen participants | claim table ch1 | correct | Reconstruction metric on another task; acceptable only as partition state of the art. A journal version may exist (unverified). |
| 20 | Appendix: high-density or 1–4 mm wording before 2012 "only [concurrent] studies without a speech decoder" | M05 audit `recall_check`, `concurrent_pids` | wrong wording | Chang 2010 (`doi-10.1038-nn.2641`, 4-mm grid) has a classifier of perceived syllables. |
| 21 | `verdict.short`: "departs from the 2010 intracortical formant decoders" | Guenther 2009 (PLoS ONE 2009), Brumberg 2009 (Interspeech 2009) | wrong | Both are 2009. |

## Required fixes, ordered by impact

**F1. Major. M05 compares against the wrong axis.**
Location: Verdict sentence 2; M05 "Usual approach"; Appendix M05; table row M05.
Evidence: the slot is "electrode scale", but the only prior design, the Neurotrophic Electrode, records single units through a penetrating electrode. That is a finer scale than 1-mm micro-ECoG, so "replace a penetrating intracortical electrode with 1-mm surface micro-ECoG" describes a change in invasiveness, not in scale. The paper's own scale argument is against clinical millimetre electrodes at centimetre spacing (Sec. 1: "millimetre-scale electrodes and centimetre-scale inter-electrode spacing are too coarse"). The intracranial speech recordings in the ledger before 2010-03 used clinical grids or depth electrodes: Towle 2008 (`doi-10.1093-brain-awn147`) and Sahin 2009 (`doi-10.1126-science.1174481`). They were excluded only for having no decoder, a criterion that matters for M06 and M12 but not for a sensor slot. The authors also cite earlier non-speech micro-ECoG BCI recordings (refs. 26, 43: Kellis 2009, Leuthardt 2009; Sec. 1 "extends previous studies").
Fix: for M05, report two counts with denominators: decoders, 1 experiment (2 reports) intracortical; intracranial speech recordings, clinical macro grid or depth in 2 of 2 off-population priors (pattern match, named). State the departure as "surface micro-ECoG instead of clinical macro-ECoG, with intracortical as the only decoded precedent". Name refs. 26/43 as the authors' own non-speech micro-ECoG precedent. Rewrite Verdict sentence 2 to match.

**F2. Major. A "usual approach" built from one experiment.**
Location: M05, M06 and M12 "Usual approach" lines ("2 of 2"); table "slot-filled 2"; Appendix "population 2".
Evidence: Brumberg 2009 (Interspeech) and Guenther 2009 (PLoS ONE) report the same participant, the same Neurotrophic Electrode and the same 25 online sessions over 5 months. Brumberg 2009 states "25 sessions over a 5 month period" and "first ever neural prosthesis for speech restoration". The brief's rule "versions count once" makes this one study. A two-report base from one system is not evidence of a field default, and "standard" by matching it is empty.
Fix: write "1 prior experiment (2 reports, one participant)" wherever "2 of 2" appears, and replace "Usual approach" content with "Only prior system: ...". State in each changed slot that `standard` follows from the second clause of the rule ("difference not supported well enough to call") and not from matching a usual approach.

**F3. Major. The M06 (and partly M05) verdict reasoning uses works the rules do not allow.**
Location: Verdict sentence 3; M06 closing sentence "Verdict: standard; the authors' concurrent report ... (ref. 47) shares the design"; `slots.json` M06 note.
Evidence: ref. 47 (Kellis et al., EMBC 2010, Buenos Aires, held at the end of August and start of September 2010) is the same group's conference version of this work. It is [concurrent] at best, and under "versions count once" it is not a separate prior, so it cannot show the design is "not new". Blakely 2008 classified four phonemes, not words, is not in the wiki and was not read, so it cannot be a deciding prior for word classification (SKILL.md: deciding priors named and read). Under the rules, M06 is a different design from the single prior (word classification 0 of 2). `ahead` fails only on the repetition clause: one patient, one 15/15 split, no reruns, selection on evaluation data. That is the protocol reason for `standard`.
Fix: M06 closing should read along these lines: "Verdict: standard. Word classification is absent from the only prior system (0 of 2 reports, Appendix), but the effect is shown in one patient on one split with electrodes and trials selected on evaluation data (Sec. 2.2, 3.3), so the departure is not supported well enough to call." Move ref. 47 to a [concurrent] same-group note. In the Verdict, drop "Neither is new as a design, since ..." for M06. Keep it for M05 only with Brumberg 2011 (read) as the support. Optionally add that closed-set word classification from non-invasive signals predates the target (Suppes et al. 1997, PNAS, wiki `pmc-25146-brainwave`), outside the intracranial setting.

**F4. Major. The under-regularisation inference contradicts the paper's data and the review's own confound.**
Location: M06, sentence "Adding the Wernicke's array ... the signature of an under-regularised classifier (inference)".
Evidence: adding 16 Wernicke electrodes, which doubles the features, changed accuracy by +0.40 ± 0.43 points and did not lower it (Sec. 3.2). Choosing the best five Wernicke electrodes gained only 1.3 ± 0.7 points (Sec. 3.3). The 13.5-point FMC gain comes from electrodes ranked by accuracy on the evaluation data, which the Verdict already calls the strongest confound. The data do not show that "more input lowered accuracy".
Fix: delete the inference, or replace it with: "The best-five gain (13.5 ± 5.2 points, FMC) cannot be separated from selection on the decode trials. The same selection on Wernicke's area gained 1.3 ± 0.7 points (Sec. 3.3), and adding the whole Wernicke array changed nothing (0.40 ± 0.43, Sec. 3.2)."

**F5. Moderate. The selection-on-test claim is stated more firmly than its evidence, and the paper's internal control is missing.**
Location: Verdict sentence 4 ("chosen by overall accuracy with no separate selection set (Sec. 3.3)"); "Where the claims outrun the evidence", bullet 1.
Evidence: Sec. 3.3 says only "with best overall accuracy". Selection on decode trials is inferred from Sec. 2.6, where single-electrode accuracies come from the train/decode classifier, and Sec. 2.2, which gives only 30 trials per word. The review's Question 1 asks exactly this. The Wernicke result (+1.3 ± 0.7 with the same procedure) suggests the inflation is limited and belongs next to the claim.
Fix: cite Sec. 2.6 with Sec. 3.3, add "(inference)" to "no separate selection set", and add the Wernicke control in one clause.

**F6. Moderate. M12 prose goes past its verdict; tier and count are inconsistent.**
Location: M12 "Usual approach" ("held-out session or subject 0, slot-filled") and the closing "Verdict: standard for 2010, and weaker than its only prior, which tested online".
Evidence: `standard` is correct under the rules. `behind` needs at least 3 earlier ledger papers, and there are 2 reports of one experiment. "Weaker than its only prior" is a `behind` judgement in prose, and it is confounded. Online closed-loop formant control measures a participant learning with feedback (hit rate 45% to 70% across sessions), not how an offline classifier generalizes. The held-out zeros are pattern-match counts, and the published M12 table (2013-11 tally) puts Guenther 2009 under the same `held_out_session_or_day` regex (and k-fold).
Fix: change "slot-filled" to "online 2 of 2 slot-filled; held-out session wording 1 of 2, held-out subject 0 (pattern match, wording only)". Replace the closing with "Verdict: standard. The only prior system was tested online in closed loop, a different task, so it gives no partition yardstick for an offline classifier." Back the day-wise point with the authors' own Sec. 3.1 ("Variability in the task-correlated power was present between sessions") and Sec. 4.4.2.

**F7. Moderate. The M06 state of the art omits Card 2024's condition and starting point.**
Location: M06 "State of the art"; table row M06.
Evidence: the 99.6% is first-day sentence decoding through a language model limited to 50 words, from intracortical arrays. The target classifies isolated words with no language model from surface LFPs. "On one fifth the vocabulary" invites a direct comparison that SKILL.md (starting points) does not allow.
Fix: "Card et al. (2024) [later] reach 99.6% word accuracy on the first day of use, decoding sentences with a language model limited to 50 words, from intracortical arrays [5]; task, sensor and language model all differ from the target's isolated ten-word classification." If one exists in the wiki, add a closed-set isolated-word ECoG classifier as a closer comparator.

**F8. Moderate. The latency comparison drops the authors' own caveat.**
Location: M06, "The 500-ms decision delay ... the prior decoder gave feedback within 50 ms [2]".
Evidence: Sec. 4.4.3 already compares against the 30-ms trajectory decoder (ref. 9) and says it is "a different problem than the decision-based algorithm presented in this study"; rapid feedback "is not as important for discrete word classification". The review presents the comparison as its own and leaves out the caveat (brief item 5).
Fix: attribute the comparison to the authors (Sec. 4.4.3), keep their caveat, and state the reviewer's position after it, or drop the 50-ms clause.

**F9. Minor. Wrong year in `verdict.short`.**
Location: `verdict.json` `short`.
Evidence: Guenther 2009 and Brumberg 2009 are both 2009 publications.
Fix: change "the 2010 intracortical formant decoders" to "the 2009 intracortical formant decoder (one participant)".

**F10. Minor. The Appendix M05 recall line mislabels Chang 2010 and leaves Blakely's status unstated.**
Location: Appendix M05, "high-density or 1–4 mm wording before 2012 only [concurrent] studies without a speech decoder".
Evidence: the audit lists `doi-10.1038-nn.2641` as "perception classifier; 4 mm grid".
Fix: write "only [concurrent] studies without a production decoder (Chang 2010 classifies perceived syllables on a 4-mm grid)". Add "Blakely et al. 2008 (cited by the target) is not in the wiki".

**F11. Minor. The first-public date basis is not stated.**
Location: Appendix setting.
Evidence: the review's 2010-09 is right (PMC header: "J Neural Eng. 2010 Sep 1"). The wiki manifest says 2010-10-01 (issue date).
Fix: write "first public 2010-09-01 (epub; wiki manifest gives issue date 2010-10-01)".

**F12. Minor. Process language in the body.**
Location: Verdict sentence 1 ("both standard under the verdict rules"); M12 "Two prior studies are below the 3 needed for behind."
Evidence: review-format bans process statements. These sentences describe the protocol, not the field.
Fix: replace them with substantive reasons: "both standard: each departs from the single prior system but is shown in one patient on one split". In M12, use the reason given in F6.

**F13. Minor. Table counts lack denominators and base.**
Location: the 13-components table, rows M05, M06, M12 ("slot-filled 2"), and M04 and M13 ("(prior)").
Evidence: counts must be design counts with their denominator at the target's time.
Fix: write "2 of 2 prior reports, one experiment (slot-filled)". For M04 and M13, write "one prior system, not audited".

**F14. Minor. An inconsistency in the target is missed.**
Location: M06 "the authors draw this contrast themselves (Sec. 1)".
Evidence: Sec. 1 cites ref. 31 (Blakely 2008) for phoneme discrimination and also among studies "decoding continuous, dynamic speech from ... formant frequencies [9, 10, 31]".
Fix: optional one clause noting that the authors' own contrast misfiles Blakely 2008, which classified phonemes.

**F15. Minor. M12 state-of-the-art condition.**
Location: M12 "State of the art"; table row M12.
Evidence: PCC 0.765 is a spectrogram-reconstruction correlation under leave-one-subject-out testing. The task differs, and the review does not give the number of participants or the signal type. A later journal version of Chen et al. may exist (unverified).
Fix: add the task, the metric and the cohort in one clause. For the target's day-wise weakness, also consider naming a held-out-day or months-later evaluation (for example Card 2024 [later], already cited).

## Answers to the specific checks

- Population: for the stated setting, the 2-report prior population is a correct wiki count. No pre-2010-03 intracranial speech decoder in the wiki was missed. Blakely 2008 is the only known item outside the wiki. Leuthardt/Schalk, Wang and Kubanek pre-2010 work is motor ECoG or micro-ECoG and outside the speech setting. Formisano 2008 is fMRI. The setting was applied consistently. However, the 2 reports are one experiment, so "usual approach" is not meaningful (F2), and the decoder requirement is wrong for the sensor slot (F1).
- First public 2010-09 and the concurrent window: correct (F11 for the basis).
- M06 `standard`: correct as an outcome, but only via "not supported well enough to call" (fails the repetition clause of `ahead`). The present justification through ref. 47 and Blakely is not protocol-based (F3).
- M12 `standard` with 2 priors: correct under the `behind` rule. The prose must not imply `behind` (F6).
- Paper claims: electrode selection with numbers, 81 of 166, the unused macro grid, the missing significance tests, +0.40 vs +13.5 and 28% (inference) are all supported by the text. The under-regularisation inference is not (F4). The selection claim needs "(inference)" and the Wernicke control (F5).
- State-of-the-art comparators: Duraivel 2023 fits M05. Card 2024 needs its condition (F7). Chen 2024 is acceptable for partition only, with its condition stated (F15).
- Summary restatement: the body has no paper summary. There are two process sentences (F12).

## Scores

- Procedure: 6/10. The ledger tallies, recall check and chronology were done carefully. One experiment was counted twice, a sensor slot was gated on having a decoder, and verdict reasons appeal to unread and same-group concurrent work.
- Final text: 6/10. The checks on the target are accurate and specific. The M05 axis, the M06 verdict reasoning and one inference contradicted by the paper need rewriting.

Counts by severity: Major 4, Moderate 4, Minor 7.
