# Evaluator: a language model separate from the writer

Evaluation date: 2026-11-27. Target: Moses, Mesgarani, Leonard, Chang, "Neural speech recognition: continuous phoneme decoding using spatiotemporal representations of human cortical activity", J Neural Eng 13(5):056004 (epub 2016-08-03, PMC5031534; ppub 2016-10). Sources checked: wiki `doi-10.1088-1741-2560-13-5-056004/source/text.txt` (OSTI PDF, header "AUTHOR SUBMITTED MANUSCRIPT - JNE-101252.R1"), cross-checked against `pmc-5031534-phoneme/source/text.txt` (NIHMS809223); the comparator folders in the wiki; the three audit JSONs in the work folder.

Dating: first public 2016-08 is right (PMC epub 2016-08-03; no preprint found). Prior cutoff 2016-02 and concurrent window 2016-02 to 2017-02 are applied correctly; Herff 2015 (June) and Heger 2015 (Interspeech, September) are true priors; nothing within the window is treated as prior.

## Claim table

| No | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Decoder = LDA likelihoods + phoneme 4-gram + Viterbi over HGWs (Verdict) | target Abstract, §2.2.1–2.2.3 | correct | |
| 2 | Same ASR chain on ECoG in Herff 2015 and Heger 2015; first cited by the authors (Verdict, M06) | target §1 ref [9]; Herff §2.10; Heger §2.7 | correct | Heger is not cited by the target, as stated. The two are one experiment (same seven Albany patients), see fix M3. |
| 3 | Multi-lag features earlier in the same group, Pasley 2012, 100 lags of 10 ms (Verdict, M06) | Pasley Methods; Mesgarani and E. F. Chang are co-authors | correct | |
| 4 | "the priority claim rests on its 'single-speaker' qualifier (§1)" (Verdict) | target §1 lines on refs [9], [10] | partly correct | The qualifier is "perceived continuous speech … in a single-speaker environment". Against Herff it is "perceived" that matters; against ref [10] it is "single-speaker". Ref [10] is from the same group (Mesgarani, E. F. Chang) and the target says it "focused primarily" on multi-speaker. See H2. |
| 5 | "continuous phoneme output from heard speech is the real step" (Verdict) | target ref [10]; Abdelaziz et al. 2019 (wiki `arxiv-1912.05869`, §3, §4.5) | wrong as stated | Ref [10] (ICSI TR 2015, same group) already did HMM phone recognition from perceived-speech ECoG. Abdelaziz et al. describe [10] as their "recently published framework", with flat-start HMMs, and report single- and mixed-speaker results that show "similar behavior to that observed in [9]". So [10] probably had a single-speaker condition too (inference). |
| 6 | 8 of 18 prior decoders do closed-set classification (Verdict, M06, Appendix) | M06 audit `prior_tally` | correct as a slot-filled tally, but the denominator is wrong | The 18 double-count Herff and Heger and leave out some same-group decoders (M3). In the prose, the slot-filled 8 and 1 read as the whole population's design counts, but 7 of the 18 have no route value (M5). |
| 7 | Electrodes chosen by a speech-versus-silence t-test on the whole Gump set; 95/89/74 channels; threshold "qualitatively chosen" (Verdict, M12) | target §2.1.4 | correct | Whether this is "the strongest confound" is a separate question, see M1. |
| 8 | "no zero-weight decoding is reported (§2.2.3)"; "phonotactics are not separated from HMM smoothing" (Verdict, M07) | target §2.2.3 grid "L ∈ {0, 1/5, 1/4, 1/3, 1/2, 1, 2, 3, 4, 5}"; Table 4 | misleading | L = 0 was in the tuning grid and lost for every feature set. The chosen L is 2 for MFCC, A, B and All, and 3 for C. A Gump PER at L = 0 is the only thing missing. See H3. |
| 9 | Authors credit the gain to temporal smoothing (Verdict, M07) | target §4 "temporal smoothing of the phoneme likelihoods is the primary benefit…" | correct | Credited properly. |
| 10 | Best neural PER 70.47%, averaged and pooled, "upper limits"; infeasible for a prosthesis (Verdict) | Table 5 (Averaged HGW, All, decoding PER 70.47 ± 16.77); §4 | correct | Matches the OSTI and PMC texts. |
| 11 | iPhoneme: 7.86% WFST, 10.62% greedy, 9.98% with the 6-gram LM, T15, offline (M06, M07) | wiki `arxiv-2604-16441-iphoneme` Table IV | correct | Attempted speech, intracortical: not like-for-like with heard-speech ECoG. |
| 12 | Willett 2023: 19.7% online PER before the LM (M06) | Willett Table 1 and text ("computed on the raw RNN output were 19.7%") | correct | Attempted speech, intracortical. |
| 13 | "no heard-speech PER is among the ledger candidates" (M06) | M06 audit `sota_candidates`, entry `arxiv-1912.05869` | wrong | Abdelaziz et al. 2019 (same group, with Moses and E. F. Chang as co-authors) is in the candidates, but under its audio-ASR value of 4.01. Its neural values: perceived-speech ECoG, DNN/HMM, biphone LM, 12-word CRM corpus, one subject, single-speaker PER 56.75% (mixed-speaker 64.54%), 8 Monte Carlo CV folds (Table 1). See H1. |
| 14 | Matthews 2012 Viterbi-decoded HMMs over intracortical firing rates; Mugler 2014 LDA (M06) | the two wiki folders | correct | |
| 15 | HGW beats HGS, p < 0.005 (M06) | target §3.2 | correct | |
| 16 | Herff: 200 ms context per side; selects features on training data only (M06, M12) | Herff §2.6, §2.8 | correct | |
| 17 | 15 of 18 name no LM; two use word bigrams on read texts (M07) | M07 audit; Herff §2.10; Heger §2.7 | correct (pattern match, labelled) | |
| 18 | 4.3 M SUBTLEX-US sentences; Gump sequences removed (M07) | target §2.2.2 | correct | Only exact full-stimulus matches were removed. The corpus is film and TV subtitles, so Forrest Gump n-grams may remain (unverified, low). |
| 19 | 142.96% to 70.47%, about 51% relative (inference) (M07) | Table 5 | arithmetic correct | The authors say estimation PERs "tend to be relatively large and are primarily included … for completeness; typically, PERs are only informative for decoding results" (§3.1.1). The baseline is one the authors themselves set aside, see M1. |
| 20 | Moses 2021: 60.5% / 25.6% median WER without/with LM, 50 words (M07) | NEJM Results | correct | Attempted speech; labelled. |
| 21 | 11 of 18 use k-fold (pattern match); ten stimulus folds (M12) | M12 audit; target §2.1.5 | correct (pattern match) | |
| 22 | Chen 2024: held-out participants, PCC 0.765 (M12) | Chen Abstract | correct | Produced speech, spectrogram PCC; it is a partition comparator only. |
| 23 | "the paper tests new stimuli of the same two speakers (§2.1.5)" (M12) | target §3.4 | incomplete | The paper also trains on one speaker's stimuli and tests on the other's, in both directions (§3.4). See M2. |
| 24 | "Window and Viterbi parameters were tuned on TIMIT test folds without a validation set" (Outrun) | target §2.1.6, §2.2.3, §3 ("Each evaluation used all 10 of the Gump cross-validation folds") | wrong in effect | TIMIT is a separate development set, and all reported results are on Gump. See H4. |
| 25 | "Speaker independence … rests on two Gump speakers; the authors note it" (Outrun) | target §3.4, §4 | wrong attribution | §4 concludes "speaker identity does not significantly affect our system" and gives no two-speaker caveat. |

## Required fixes, ordered by severity

### High

**H1. Like-for-like state of the art is missing for M06 and M07, and one stated absence is false.**
- Location: M06 "State of the art", M06 sentence "no heard-speech PER is among the ledger candidates", M07 "State of the art", and table rows M06 and M07.
- Evidence: Abdelaziz et al. 2019 (arXiv:1912.05869, wiki `arxiv-1912.05869`; authors include D. A. Moses and E. F. Chang) decodes phones from perceived-speech ECoG over pSTG. It uses DNN/HMM 3-state monophones and a biphone LM, on the 12-word CRM corpus with one subject. Single-speaker PER is 56.75% (SD 1.10) and mixed-speaker PER 64.54% (Table 1). It is in this audit's `sota_candidates` under the audio-ASR value of 4.01, so it was missed.
- Further evidence: later same-group perceived-speech decoders that continue this paper's phone-level Viterbi approach are also in the wiki and go unmentioned:
  - Moses et al. 2018 (J Neural Eng 15:036005, `doi-10.1088-1741-2552-aaab6f`): real-time, 10-sentence classification, 90% or higher per subject, and 98% with the HMM scheme offline for subject A.
  - Moses et al. 2019 (Nat Commun, `doi-10.1038-s41467-019-10994-4`): phone-level Viterbi decoding with context priors; perceived questions 76% (chance 20%), produced answers 61% (chance 7%).
- Fix:
  - Add Abdelaziz 2019 [later, same group] as the like-for-like heard-speech ECoG PER line, with its conditions (12-word vocabulary, one subject, biphone LM).
  - Keep iPhoneme and Willett only as attempted-speech intracortical references, labelled not like-for-like.
  - Add Moses 2018 and 2019 as the same group's later continuation, under M06, and under M07 (context priors as use-time language information).
  - Delete the false absence sentence.

**H2. The novelty and priority framing ignores the same-group deciding prior, ref [10].**
- Location: Verdict ("priority claim rests on its 'single-speaker' qualifier"; "continuous phoneme output from heard speech is the real step"); M06 usual approach ("none of the 3 prior perception-only decoders uses an HMM or LM"); Appendix ("Outside the ledger: Chang et al. 2015").
- Evidence:
  - Target ref [10] is S.-Y. Chang, Edwards, Morgan, Ellis, Mesgarani and E. F. Chang (ICSI TR 2015): phone recognition from perceived-speech ECoG, by the target's own group.
  - Abdelaziz et al. 2019 (§3, §4.5) call it "our recently published framework" with HMMs, and say their single- and mixed-speaker results show "similar behavior to that observed in [9]". So [10] likely also had a single-speaker condition (inference).
  - The target itself says [10] "focused primarily" on multi-speaker (§1).
- Fix:
  - Label ref [10] as a same-group prior. Describe it through the target's citation and through Abdelaziz 2019, labelled as inference.
  - Count it as a prior perception decoder with HMM decoding.
  - Drop "the real step", or limit it to the open-vocabulary phoneme LM with Gump as the test set.
  - State that the priority claim rests on two qualifiers: "perceived" against Herff, and "single-speaker" against a same-group report that likely included single-speaker phone recognition. That qualifier is thin.
  - Qualify "none of the 3 prior perception-only decoders" with "in the ledger".

**H3. The M07 criticism ignores that L = 0 was in the tuning grid.**
- Location: Verdict ("no zero-weight decoding is reported"); M07 body ("no L = 0 decoding is reported … phonotactics are not separated"); What the field needs next ("M07: decode at L = 0").
- Evidence:
  - §2.2.3 searched "all possible combinations of L ∈ {0, 1/5, 1/4, 1/3, 1/2, 1, 2, 3, 4, 5}".
  - Table 4 optimum: L = 2 for MFCC, A, B and All; L = 3 for C. L = 0 lost on the TIMIT tuning metric for every feature set.
  - The authors' smoothing attribution rests on posteriogram accuracy being similar with basic priors (§4). The review credits that.
- Fix:
  - Say that zero LM weight was tried in the TIMIT grid and never chosen, which is evidence the phoneme LM adds something beyond smoothing on the tuning data.
  - Say that what is missing is a reported Gump PER at L = 0 against L*, and a uniform-prior control.
  - Rewrite the field-needs item to "report Gump PER at L = 0 and with a uniform prior".
  - Soften "not isolated" accordingly.

**H4. The test-set tuning criticism is wrong for the reported results.**
- Location: "Where the claims outrun the evidence", bullet 3.
- Evidence:
  - The HGW grid used "one arbitrarily-chosen TIMIT cross-validation fold" (§2.1.6), and the Viterbi grid used TIMIT likelihoods (§2.2.3).
  - All reported evaluations "used all 10 of the Gump cross-validation folds" (§3).
  - TIMIT therefore acts as a separate development set, so Gump results are not tuned on their test folds.
- Fix: delete the bullet. If anything is kept, use the authors' own caveat, "the relatively small amount of data used during the grid search" and one shared HGW parameterization for all electrodes (§4), credited to them.

### Medium

**M1. The "strongest confound" is misidentified.**
- Location: Verdict; M12 body; M07 relative-change sentence.
- Evidence:
  - Electrode selection uses speech-versus-silence labels (stimulus presence), not phoneme identity (§2.1.4).
  - The same electrode set serves every within-paper comparison (HGW against HGS, estimation against decoding, the speaker tests). So it can shift absolute PER but cannot produce the paper's central relative claims. PER removes silence anyway (§3.1.1).
  - The stronger confound for the central claim (decoding improves PER) is the baseline: framewise estimation PERs above 100%, which the authors call "primarily included … for completeness; typically, PERs are only informative for decoding results" (§3.1.1). The "about 51% relative" reduction is measured against that baseline.
- Fix:
  - Demote the electrode overlap to a limitation on absolute PER.
  - Name the inflated estimation baseline as the main confound and credit the authors' own §3.1.1 caveat.
  - Report the relative change only alongside that caveat, or use the confusion-accuracy and posteriogram comparisons instead.

**M2. The speaker evidence is misreported.**
- Location: M12 State of the art ("tests new stimuli of the same two speakers"); Outrun bullet 4 ("the authors note it"); field needs ("hold out speakers").
- Evidence: §3.4 trains on 90% of one speaker's stimuli and tests on all of the other speaker's, in both directions, with no significant neural difference. §4 concludes "speaker identity does not significantly affect our system" with no two-speaker caveat.
- Fix:
  - State that cross-speaker train/test was done.
  - Make the limitation the review's own point: two stimulus speakers, one male and one female.
  - Remove "the authors note it".
  - Change the field-needs item to held-out subjects and sessions, since stimulus speakers were already held out.

**M3. The 18-study prior population needs correction.**
- Location: Verdict, M06/M07/M12 usual approach, Appendix counts.
- Evidence:
  - **Double count.** Herff 2015 (U17) and Heger 2015 (U18) report the same seven Albany patients. The wiki's published M12 tally for the Mugler-group review merges them (P15, "one study, two reports"). The rules require deduplicating reports of one experiment.
  - **Bouchard & Chang 2014.** It is listed as mapping without a decoder, but it is J Neurosci (wiki `pmc-4166154-vowelvsmc`) with an explicit "acoustic feature decoding model" (linear prediction of formants and pitch from vSMC, five-fold CV). It is a decoder from the same group, and the other published tally includes it (P11).
  - **Chang et al. 2010.** Nat Neurosci (`doi-10.1038-nn.2641`) is listed as mapping, but it trains a single-trial L1 logistic-regression classifier of perceived syllables, with "feature selection and classifier training … performed in the cross-validation loop". It is a same-group perception decoder, and also a same-group precedent for fold-internal selection, relevant to M12.
  - **Mesgarani & Chang 2012.** Nature (`doi-10.1038-nature11020`, the target's ref [37], which the target also uses for its electrode-selection method) is in the wiki but not among the candidates. It is a same-group perception decoder (stimulus reconstruction).
  - **Correct exclusions.** Leuthardt 2012 (`pmc-3342676-gammaev`, mapping), the Greenlee and Nourski mapping papers, and Flinker 2015 are rightly excluded.
  - **Present as expected.** Kellis 2010, Pei 2011, Brumberg 2011, Guenther 2009, Martin 2014, Mugler 2014 and Pasley 2012 are all in the population.
- Fix:
  - Recount the population: about 20 unique experiments (merge Herff/Heger; add Bouchard 2014, Chang 2010, Mesgarani 2012). Perception-only decoders become 5 in the ledger, plus ref [10] outside it.
  - Restate the HMM/LM count as one experiment in two reports.
  - Name the same-group priors explicitly (Chang 2010, Pasley 2012, Mesgarani 2012, Bouchard 2014, ref [10]).
  - The direction of the usual-approach conclusion probably holds.

**M4. The authors' own points are presented without credit.**
- Location: Verdict and M06 (closed-set against continuous contrast); field needs M06 ("sub-phone or recurrent models"; "compare … with multi-lag regression").
- Evidence: in §4 the authors write that Kellis [66] and Mugler [67] "did not perform continuous speech decoding". They also propose "sub-phone modeling [18,21] or recurrent neural network (RNN) modeling", and call for comparisons of a discrete-state decoder with "continuous-valued reconstruction methods … [5]".
- Fix: credit these to the authors with §4, and keep only what the review adds (a fixed electrode set; multi-lag regression features).

**M5. Slot-filled design counts read as population design counts.**
- Location: M06 usual approach ("8 classify … 1 regresses acoustics").
- Evidence: 7 of the 18 have no decoder-route value. Guenther 2009 (continuous formant decoding), Martin 2014 and Yang 2015 (spectrotemporal reconstruction) regress acoustics; with Bouchard 2014 added, acoustic regression is at least 4 to 5.
- Fix: present 8 and 1 as lower bounds of the slot-filled field, or recount from the full texts.

**M6. State-of-the-art cells lack the deciding conditions.**
- Location: the 13-component table, M06, M07 and M12 rows.
- Evidence:
  - "[5] (2026): PER 7.86%" and "PER 10.62% to 9.98%" carry no conditions (attempted speech, intracortical, one participant, offline, WFST/6-gram).
  - "[10] (2024): held-out subjects" omits produced speech and the spectrogram PCC metric.
  - The rules require the conditions that decide the result.
- Fix: add the conditions, and put a like-for-like perceived-speech entry first (H1).

### Low

**L1. A process note sits in the published reference list.**
- Location: Ref 1, "Read as the accepted manuscript."
- Evidence: this is a process note. The OSTI text is headed "AUTHOR SUBMITTED MANUSCRIPT - JNE-101252.R1", while the wiki manifest says version_of_record. The numbers checked (Table 4, Table 5, the 2.54 threshold, the L grid) match the PMC author manuscript NIHMS809223, so there is no content mismatch.
- Fix: drop the note; record the version in the work-folder metadata only.

**L2. The LM-corpus exclusion is described as stricter than it is.**
- Location: M07 usual approach ("with Gump sequences removed … stricter than read-text bigrams").
- Evidence: §2.2.2 removes only "any phoneme sequence which exactly matched the phoneme sequence associated with any of the Gump stimuli". SUBTLEX-US comes from film subtitles, so partial overlap with re-enacted Forrest Gump lines is possible (unverified).
- Fix: say "exact Gump sentences removed".

## Scores

- **Procedure: 5/10.**
  - Done well: correct dating and window, the read deciding priors (Herff, Heger), the audits and labelled tiers.
  - The candidate set held a like-for-like, same-group, heard-speech comparator (Abdelaziz 2019) that was missed.
  - The population double-counts one experiment and drops three same-group decoders.
  - Same-group later work (Moses 2018/2019) was not searched.
  - The target's own grid and data split were not read closely enough before criticising them (H3, H4).
- **Final text: 5/10.**
  - Numbers are accurate throughout, and the authors' temporal-smoothing attribution and their infeasibility caveat are properly credited.
  - But two of the four "outrun" bullets are wrong (TIMIT tuning; "the authors note it").
  - The M07 criticism ignores L = 0 in the grid.
  - The novelty framing ignores the same-group ref [10].
  - The state-of-the-art lines are not like-for-like and say so only in passing.

## Final counts by severity

- High: 4 (H1–H4)
- Medium: 6 (M1–M6)
- Low: 2 (L1–L2)
