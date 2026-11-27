# Evaluator: a language model separate from the writer

Date: 2026-11-27. Target: Angrick et al., "Online speech synthesis using a chronically implanted brain–computer interface in an individual with ALS", Sci Rep 14, 9617 (2024), doi:10.1038/s41598-024-60277-2. First public medRxiv 10.1101/2023.06.30.23291352 v1. The review file is the same as `draft-before-evaluation/review.md` (byte-identical).

Sources checked: wiki `papers/doi-10.1038-s41598-024-60277-2/source/text.txt` (wiki commit 730b0b4a); Fig. 2 image from the Sci Rep article page; the medRxiv API (v1 posted 2023-07-01); Crossref for dates of Luo 2023, Wairagkar NER 2023 and Littlejohn 2025; wiki texts of [5], [6], [8], [10] and of doi-10.1109-icassp43922.2022.9747300; the M06 and M13 audit JSONs; `notes.json`. Repository files fetched from `cronelab/delayed-speech-synthesis` branch `main` on 2026-11-27 (the commit SHA could not be read: the GitHub API was not reachable from this session). SHA-256: replicate.sh 10ebf618…7651, train_unidirectional_vad.py 9c1fc0f1…f7f3a, train_bidirectional_model.py d9d71088…1ea1c2.

## Claim table

| # | Claim (location in review) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | First public 2023-07, medRxiv v1 2023-07-01; prior < 2023-01, concurrent 2023-01 to 2024-01 (plan, Appendix) | medRxiv API | correct | v1 date 2023-07-01. The ±6-month window is applied correctly. |
| 2 | Word played after it ends; bidirectional decoder (Verdict, M06) | text §Methods "feedback from each synthesized word began after he spoke"; §Discussion "bidirectional LSTM imposed a delay" | correct | |
| 3 | 5.5 months after training, 3 sessions (Verdict, M13) | §Results "approximately 5 and a half months… 3 sessions across 3 different days" | correct | |
| 4 | 80% vs 16.7% chance; 21 listeners; six choices (Verdict, M12) | §Results; §Methods listening test | correct | The diagonal of Fig. 2C averages 79.7%, which matches 80%. |
| 5 | Natural speech 99.8% (Verdict, bullets) | §Results | correct | Same listeners and test, with natural and synthesized samples mixed. A like-for-like comparison except that exclusions apply only to the synthesized side. |
| 6 | "about 100 times the error (inference)" | 20/0.2 | correct (inference) | Because 99.8% is rounded, the ratio could be roughly 80–130×. Acceptable because the review labels it as inference. |
| 7 | "Back" 37.3% (Fig. 2C) | Fig. 2C image | correct | Back was chosen as "Left" in 51.6% of cases. |
| 8 | 180 samples, 2 excluded, "a few" false detections uncounted; no interval (bullets) | §Results | correct | The final denominator is not given anywhere in the text. |
| 9 | Stability: no pre-gap listener score, no statistic, no per-day value; authors ask for longer testing (bullets, M13) | §Discussion "produced similar results over 3 separate days… longitudinal testing over longer time periods will be needed to explicitly test this" | correct | The authors' caveat is credited in the bullet but not in the Verdict sentence. |
| 10 | No synthesis of unseen words; word-specific dynamics, as the authors state (M06) | §Discussion | correct, credited | |
| 11 | "Closed-loop neural synthesis existed in 3 of 50 prior studies" [2][3][4] (Verdict) | M06 audit `tally_at_target_time_…` | wrong denominator | The 50 is a pattern-match population over all signals. It includes reviews and an ethics paper (the audit lists 4 reviews in the 44-key basis plus doi-10.1007-s13311-022-01190-2 (review) and doi-10.1093-jmp-jhac011 (ethics)) and non-neural signals (EMA, PMA, rtMRI, lip). The numerator 3 is neural only, so it does not share a population with the denominator. |
| 12 | "5 of 50 played audio back in closed loop, all frame by frame" (M06 usual approach, table) | same audit | insufficient evidence for the denominator | The tier is labelled "pattern match", but the population still contains non-decoders, against the population rule. The classification of the 5 is plausible: Guenther 2009, Berry 2014 (EMA), Bocquelet 2016 (EMA), Brumberg 2018 and Angrick 2021. |
| 13 | Neural closed loops then gave vowel formants within 50 ms (2009) [2] or unintelligible words (2021) [4] | audit read_fulltext quotes | correct | Brumberg 2018 [3] (EEG, formants) is also a deciding prior. It is cited in the Verdict, but this line leaves it out. |
| 14 | "earliest intelligible closed-loop neural synthesis in the prior set" (Verdict) | audit; general knowledge | plausible | I know of no earlier intelligible closed-loop neural synthesis. The authors also claim online intelligible synthesis themselves: their v1 abstract states that synthesis "until now… has only been done using retrospective analyses… able-bodied patients", a claim that [2] and [4] contradict. |
| 15 | SOTA M06: [5] causal within 10 ms, 43.75% median WER (2025); [6] 5.24% offline with simulated real-time inference (2026) | wiki texts of [5], [6] | correct | In [6], 5.24% is reported as "average WER" in Results and as the abstract WER. Littlejohn et al. 2025 is missing (fix 4). |
| 16 | M13: 8 of 10 prior acute with intact speech; chronic 2 ([2], [11]); speech-impaired 1 | M13 audit | insufficient evidence | The audit says participant and implant were "classified from ledger text and titles", with only the two chronic studies checked in text. The published text does not say this. Two intracranial synthesis works cited in the target's own reference list are not in the ledger and are not named: Herff et al. 2016 EMBC (prior, acute ECoG) and Wairagkar et al. 2023 NER, doi:10.1109/ner52421.2023.10123880 (issued 2023-04-24, [concurrent], chronic intracortical). The direction of the usual approach would not change. |
| 17 | Wilson 2020 [11] chronic, intact speech | audit; title | plausible | The BrainGate participants had tetraplegia with intact speech, and the synthesis was offline. |
| 18 | SOTA M13: [5] chronic intracortical, ALS, closed-loop 43.75% median open-transcription WER | wiki text [5] | correct | Littlejohn et al. 2025 (chronic ECoG, anarthria, streaming synthesis) is the closest later work on the same implant type and is missing (fix 4). |
| 19 | [12] Metzger 2023 [concurrent], "as the target describes it" | target §Introduction | correct | Published Aug 2023, so the concurrent label holds. |
| 20 | [7] Luo 2023 [concurrent]; "commands were already classified" | Crossref: Adv Sci issued 2023-10-24 | label correct, wording off | "already" suggests priority over the target, but the work is concurrent. The target calls it "our prior work". |
| 21 | M12: closed-set identification in all 3 prior intracranial studies [8][9][10] (confirmed) | wiki texts: [8] single-word identification with 10/25/50 choices plus pool-restricted transcription; [10] binary forced choice; target says its test is "similar to Herff et al." | correct; insufficient quote | Claim row 14 quotes the [8] transcription WER. That passage does not show closed-set identification. |
| 22 | SOTA M12: [5] 94.34% six-choice sentences | wiki text [5] "choosing from 6 possible sentences of the same length… 94.34%" | correct | |
| 23 | "Error is 20% here against 5.66%… not like-for-like" | — | correct but low value | The sentence is flagged as not like-for-like. It adds a number the review then says cannot be compared. |
| 24 | Target omits [4] and calls prior ECoG synthesis offline except Metzger (Lineage) | target §Discussion; reference list (60 entries) | correct | Angrick 2021 Commun Biol does not appear in the reference list, and neither does Brumberg 2018. |
| 25 | Replication script and training defaults swap test/validation days; no seed (Reproducibility) | repository `main` fetched 2026-11-27 | facts correct, impact misframed, not pinned | replicate.sh passes `--test_day 2022_11_03 --val_day 2022_11_04` explicitly, while the argparse defaults are the reverse. No `manual_seed` or `seed` call is present. The 80% comes from online sessions, so the test/validation choice does not touch any claim in the paper. |

## Required fixes (by severity)

1. **High: Verdict and M06 usual approach, "3 of 50" and "5 of 50 prior studies".** Evidence: the M06 audit basis keeps reviews (specom 2010, erd 2010, access 2020, innerspeech review 2018, doi-10.1007-s13311-022-01190-2) and an ethics paper (doi-10.1093-jmp-jhac011) in the 50. The neural numerator (3) is set against an all-signal denominator. Fix: remove non-decoders and report the decoder denominator at the target's time. Give the neural closed loops against the neural (or intracranial) prior decoders, or state the all-signal boundary explicitly with per-signal numerators. Keep the "pattern match" label, or set `matched=null` if the population cannot be cleaned.

2. **High: M13 usual approach and Appendix, 8 of 10 classification and missing priors.** Evidence: the audit states the classification comes "from ledger text and titles"; the published Appendix does not say so. The target's own reference list contains Herff et al. 2016 EMBC ("Towards direct speech synthesis from ECoG", prior, acute) and Wairagkar, Hochberg, Brandman, Stavisky 2023 NER, doi:10.1109/ner52421.2023.10123880 (2023-04-24, [concurrent], chronic intracortical synthesis). Neither is in the ledger or named in the review. Fix: name both through the target's citation, labelled (prior / [concurrent]). State in the Appendix that the 8 acute studies were classified from ledger text and titles, or check each in its text. Update counts if Herff 2016 is added (likely 9 of 11 acute).

3. **Medium: "Where the claims outrun the evidence", Reproducibility bullet.** Evidence: the findings are not pinned to a commit. At `main` (2026-11-27) the facts hold, but replicate.sh sets the days explicitly, and the headline 80% comes from separate online sessions. The default swap therefore does not undercut any claim. Fix: pin a commit SHA and move this to Questions for the authors as a minor reproducibility note ("training-script defaults differ from replicate.sh; no training seed"), or drop it. Do not present it as a claim outrunning the evidence.

4. **Medium: State-of-the-art lines for M06 and M13.** Evidence: Littlejohn, Cho, Liu, Silva, Yu, et al., "A streaming brain-to-voice neuroprosthesis to restore naturalistic communication", Nature Neuroscience 2025 (issued 2025-03-31), doi:10.1038/s41593-025-01905-6. This is chronic ECoG in a participant with anarthria, with streaming closed-loop synthesis, the same implant class as the target. It is not in the wiki and the review does not mention it. Its metrics are unverified here. Fix: read it and either cite its result with conditions (vocabulary, latency, metric, closed or open set) on the M06 and M13 lines, or state why [5] stays the better reference.

5. **Medium: M12 setting boundary.** Evidence: M06 uses an all-signal population, M13 is justified as intracranial in the plan, and M12 narrows to "3 prior intracranial production studies" out of 23 without a justification in the text. Fix: give the usual approach over the 23 confirmed studies, or state why M12 uses the M13 boundary.

6. **Low: Verdict, "bought by dropping the real-time constraint".** Evidence: the authors chose delayed feedback deliberately (§Introduction, "We chose to provide delayed rather than simultaneous auditory feedback…"; §Discussion, "the bidirectional LSTM imposed a delay"). Fix: credit their rationale with the locations, then state the cost.

7. **Low: Verdict, stability sentence.** Evidence: the authors write "longitudinal testing over longer time periods will be needed to explicitly test this" (§Discussion). Fix: credit this caveat in the Verdict as well, not only in the bullet.

8. **Low: M06, "the same participant's commands were already classified [7] ([concurrent])".** Evidence: Adv Sci issued 2023-10-24, so the work is concurrent. Fix: replace "already" with "as the target cites from its own prior work".

9. **Low: claims.md row 14 (M12 usual approach) quote.** Evidence: the quote is the [8] transcription WER. Fix: quote [8]'s single-word identification task ("number of choices (10, 25, and 50 words)") and [10]'s forced-choice test.

10. **Low: Lineage bullet, optional strengthening.** Evidence: the medRxiv v1 abstract claims synthesis "until now… has only been done using retrospective analyses… able-bodied patients temporarily implanted… for epilepsy surgery", which [2] (online, locked-in) and [4] (online sEEG) contradict. The published version softened the claim. Fix: cite the v1 wording if the lineage point is kept.

11. **Low: M12, "Error is 20% here against 5.66% (inference)…".** Fix: drop the number pair, since the review itself says it is not like-for-like, or keep only the qualitative statement.

12. **Low: process wording.** Examples: "Both are standard by our rules" (Verdict) and "(reused topic table)" / "(new topic)" (Appendix). Fix: state the rule ("one participant, no repetition") and drop the process labels.

13. **Low: Reference 10 (Kohler).** The venue mixes arXiv and NBDT. Fix: cite one version (NBDT 2022, first public arXiv 2021-11).

## Scores

- Procedure: 6/10. The dating and window are correct, the deciding priors were read, and the numbers check out. However, the population includes non-decoders, the M13 classification rests on titles and ledger text without saying so, the target's reference list was not mined for missing priors, the code findings are not commit-pinned, and a directly relevant later work is missing.
- Final text: 7/10. The text has a clear position, and the target numbers are accurate (80%, 99.8%, 37.3%, 180/2, 5.5 months, 21 listeners, 16.7%). Most author caveats are credited. Weak points: the headline count mixes populations, the reproducibility bullet is overstated, and two credit or wording issues remain.

## Counts by severity

High 2 · Medium 3 · Low 8 · Total 13.
