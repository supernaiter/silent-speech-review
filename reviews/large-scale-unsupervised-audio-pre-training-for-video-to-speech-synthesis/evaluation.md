# Evaluation: Large-scale unsupervised audio pre-training for video-to-speech synthesis

Date: 2026-11-22. Fallback evaluator (claim table only): one pass over the claim table, the Verdict and the component sections; no sources were opened. Items marked "inference" rest on the evaluator's own knowledge, not on a checked source.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Decoder pre-trained on 3,572 h of audio alone | Claim 1; Table III, Abstract | correct | "Total 3,572" and "more than 3,500 hours of audio" support it. |
| 2 | Decoder transfer without the input signal dates from 2021 [2] | Claim 2; [2] Abstract | insufficient evidence | The quote supports that TaLNet transfers a TTS decoder. "Dates from 2021" is a first-use claim, and no deciding earlier works are named as checked. |
| 3 | Transfer lowers WER in 7 of 16 pairs and raises it in 9 | Claim 3; Tables IV, V, VII, VIII | insufficient evidence | The claim table records only "counted by the reviewer". The 16 pairs and their values are not listed, so the central count cannot be checked. |
| 4 | Earlier systems have lower WER on all four WER splits | Claim 4; Tables IV, V, VII | partly correct | 4.07, 16.05 and 2.37 are quoted. The LRW 12.90 is cited (t66) but no quote is shown. |
| 5 | Extra training stage only for pre-trained variants (§V-C1); single runs; no listener test | Verdict; "Where the claims outrun" | insufficient evidence | This is the review's main confound, but the claim table has no quote for §V-C1, for single runs or for §V-E. |
| 6 | Authors concede that scratch mel models beat fine-tuned ones on GRID seen and LRW (§VI) | "Where the claims outrun" | insufficient evidence | No quote. The review does attribute this to the authors, which is fair. |
| 7 | §VI's claim of better results on all reconstruction metrics holds for PESQ, STOI and ESTOI | "Where the claims outrun", bullet 1; Claims 4, 10, 11 | wrong | The review's own TCD-TIMIT figures contradict it: VCA-GAN 0.595 STOI and 0.420 ESTOI against the paper's 0.568 and 0.405 (Table VI). On TCD-TIMIT, STOI and ESTOI trail. |
| 8 | Pretrained vocoder only is the most common design, 9 of 30 | Claim 5; ledger tally | correct (tally) | The count comes from the ledger and is outside this check. |
| 9 | TaLNet decoder trained on 460 h of LibriTTS | Claim 6; [2] Sec. 4 | correct | The quote matches. |
| 10 | LipSound2 pre-trains on about 2400 h of paired audio-visual data | Claim 6; [5] | insufficient evidence | The quote ("is firstly pre-trained") gives no hours. |
| 11 | TaLNet WER drops from 55.9% to 36.5%, 34.7% relative | Claim 7; [2] Table 1 | correct | (55.9 − 36.5) / 55.9 = 34.7%. The quote shows ±9.9 and ±10 spreads, which the review does not mention. |
| 12 | TaLNet gains at every training-set size from 75 speakers down to 1 | Claim 7; [2] Table 2 | insufficient evidence | The quote says "consistently improved ... when varying the amount of train[ing data]". It does not give 75 or 1. |
| 13 | Best gain 25.75% to 18.57% on GRID unseen speakers, 27.9% relative | Claim 8; Table VII | correct | 7.18 / 25.75 = 27.9%. |
| 14 | GRID seen speakers: 2.66% to 3.66% | Claim 8; Table V | correct | The quote matches. |
| 15 | LRW: 14.96% to 18.70% | Claim 8; Table VIII | insufficient evidence | Cited (t64, t65), but no quote text is shown. |
| 16 | GRID four speakers: 4.07% against 4.54% | Claim 10; Table IV | correct | The quote matches. |
| 17 | GRID unseen speakers: 16.05% against the paper's best 17.08% | Claim 10; Table VII | partly correct | 16.05 is quoted. 17.08 is not. M03 calls 18.57 the "best single gain" endpoint, so 17.08 must come from another row, which is not shown. |
| 18 | TCD-TIMIT: VCA-GAN STOI 0.595 beats the paper's best 0.568 | Claim 11; Table VI | partly correct | Both numbers are quoted, but nothing shows that 0.568 is the best row in Table VI. |
| 19 | PESQ and ESTOI gains lie within a single-run spread the paper never measures | M06 verdict | wrong (judgment) | An unmeasured spread cannot place gains inside it. The defensible statement is that the gains cannot be separated from run-to-run variation. |
| 20 | 83 of 165 studies run a listener test, so the verdict is "behind, against the typical study" | Claim 12; M12 | partly correct | 83 of 165 is 50.3%, barely half, so "typical" overstates it. The count itself comes from the ledger. |
| 21 | Listener tests date from 2017, with 85% listener word accuracy [7] | Claim 13 | insufficient evidence | The 85% is quoted, but its condition (corpus, speaker-dependent or not) is missing. "Date from 2017" may be too late. Inference: Le Cornu and Milner, Interspeech 2015, already reconstructed speech from visual features and may have run listening tests. |
| 22 | State of the art for M03 and M06 | M03, M06 | insufficient evidence | Both lines name only 2021–2022 prior work, mostly from the target's own group. Later work is not considered. Inference: ReVISE (CVPR 2023), unit-based lip-to-speech (Interspeech 2023), DiffV2S (ICCV 2023) and LipVoicer (ICLR 2024). Several of these are within 6 months of the target and must be labelled [concurrent] or [later], not treated as missed priors. Values were not checked. |
| 23 | The strongest confound is unequal training | Verdict | correct (handled) | The review names it and proposes the fix. Two further confounds go unstated: the ASR model used for WER is not named, and test speakers may overlap with the pre-training corpora. The overlap is raised in the bullets but not weighed in the Verdict. |
| 24 | M03 "standard" verdict | M03 | partly correct | The verdict is reasonable, but the boundary is undefined. A pretrained HiFi-GAN in the paper's own mel route is also an audio-only pre-trained decoder stage, which blurs the split between "pretrained vocoder only" and "decoder transfer". |

## Required fixes (ordered by impact)

1. Correct bullet 1 of "Where the claims outrun the evidence". On TCD-TIMIT, STOI (0.568 against 0.595) and ESTOI (0.405 against 0.420) trail VCA-GAN, so §VI's claim holds for PESQ on every set and for STOI and ESTOI only on the GRID splits. As written, it contradicts M06.
2. List the 16 model and split pairs behind "7 of 16" in the Appendix or claim table, with the scratch and transferred WER for each. The central verdict rests on this count.
3. Add claim-table quotes for §V-C1 (the extra training stage), for single runs, for §V-E (metrics and the perception concession), for §V-A2 (corpus overlap) and for the §VI concession. The main confound currently has no quoted support.
4. Rewrite "PESQ and ESTOI gains lie within a single-run spread the paper never measures" as "cannot be separated from run-to-run variation, which the paper does not measure".
5. Add quotes for LRW 12.90, 14.96 and 18.70 and for GRID unseen 17.08. Show that 0.568 is the best TCD-TIMIT STOI row in Table VI.
6. Support or remove "from 75 speakers down to 1" (TaLNet) and "about 2400 hours" (LipSound2). Neither appears in the quoted passages.
7. M12: state the condition of the 85% listener word accuracy. Check whether listener tests predate 2017 (for example, Le Cornu and Milner, Interspeech 2015). Replace "against the typical study" with "about half of studies (83 of 165)".
8. M03 and M06 state of the art: consider later and concurrent video-to-speech systems (for example, ReVISE 2023, unit-based lip-to-speech 2023, DiffV2S 2023, LipVoicer 2024), labelled [concurrent] or [later], with metric and value from their sources. Or say explicitly that the line is limited to the paper's reported comparators.
9. "Dates from 2021 [2]": name the earlier works checked that decide this, or soften to "at least since 2021".
10. Define how "decoder pre-trained on audio alone" differs from "pretrained vocoder only". The paper's mel route itself uses a pretrained vocoder.
11. TaLNet comparison: add the reported spread (36.5 ± 10) and the absolute changes (19.4 points against 7.18 points) next to the relative figures.

## Scores

- Procedure: 6/10. The arithmetic checks out and the main confound is named. But the central count and the confound lack quoted evidence, and several numbers are cited without quote text.
- Final text: 6/10. The position is clear and fair to the authors. One internal contradiction (TCD-TIMIT STOI and ESTOI) and one overreaching judgment (the unmeasured spread) need fixing.
