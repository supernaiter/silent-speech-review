# Evaluator: a language model separate from the writer

Date: 2026-11-27. Review evaluated: `a-neural-speech-decoding-framework-leveraging-deep-learning-and-speech-synthesis.md` (Chen et al., Nat Mach Intell 6, 467–480, 2024; doi:10.1038/s42256-024-00824-8; first public bioRxiv 10.1101/2023.09.16.558028 v1, 2023-09-17). The evaluator changed none of the review or work files.

Sources checked:
- Target: wiki `doi-10.1038-s42256-024-00824-8/source/text.txt` and `paper.xml`.
- Target Supplementary Information: Springer ESM `42256_2024_824_MOESM1_ESM.pdf`, fetched 2026-11-27, sha256 2ec46e48…72f. Table S1 and Fig. S10 were read.
- Released code: `flinkerlab/neural_speech_decoding` tag v1.0.1, `train_e2a.py`, sha256 d9bbff7d…2ed.
- Same-group prior [2]: wiki `pmc-10589651-ffwd`, the PNAS 2023 text, and the bioRxiv API record for 10.1101/2021.12.06.471521. The record shows only v1, dated 2021-12-07, plus its abstract.
- Comparators [3], [5] and Herff 2019 from wiki sources. Metzger 2023 and Wairagkar 2025 from the wiki. Crossref dates for the 2023 ledger items.
- The four topic audits in `.audit/`.

What the evaluator could not check: the full text of the 2021 bioRxiv v1. bioRxiv returned 429 and the web archive is blocked by egress policy. Claims about what v1 contains are therefore checked against the PNAS version, the v1 abstract and the target's own statements about its prior work. They are marked "insufficient evidence" where v1 alone decides.

## Claim table

| # | Claim (location in review) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | 18 speech parameters; differentiable synthesizer; speech-autoencoder guidance (Verdict) | Target Results: ECoG-to-speech framework; Methods: Summary of speech parameters | correct | |
| 2 | The 2021 preprint "already had the pipeline, with causal and anticausal decoders, on five participants" (Verdict) | PNAS text (Intro; Fig. 1; Methods: Speech decoder); v1 abstract ("interpretable representational space", "disentangle feedforward vs. feedback"); target Methods: Speech encoder; target Discussion | correct at design level; insufficient evidence for v1 wording | The target itself says this. Methods: Speech encoder: "unlike our previous work in ref., which completely relied on unsupervised training, we provided supervision for some speech parameters". Discussion: "multiple improvements … over our previous approach on the subset of participants with hybrid-density grids". The review does not credit these disclosures (Fix M1). Differences the authors claim (Praat supervision; synthesizer, decoder and training changes) go unmentioned. The claims-table quotes for [2] are PNAS-section quotes but are attributed in the text to "the 2021 preprint" (Fix M9). |
| 3 | "What it adds is scale: 48 participants, three decoders, both hemispheres and a held-out-word test (5 of 202 prior studies, Appendix)" (Verdict) | Target Methods: Experiments design; PNAS Results ("stricter cross-validation … unseen words (SI Appendix, Fig. S7)"); PNAS Methods ("implanted on the left hemisphere in all participants"); M12 audit | partly wrong | 48 participants, three decoders and both hemispheres are new against [2]: PNAS has five participants, ResNet only, all left hemisphere, hybrid-density grids. The held-out-word test is not new against [2]: PNAS reports a stricter unseen-word cross-validation. That paper is cited here for its chance level but not for this test. "5 of 202" is a regex mention count (`(unseen|held-out|novel|new) words`) with no tier label, in a population that is not filtered to decoders. Low-density decoding is a real addition the Verdict omits. |
| 4 | Waveform from Griffin–Lim; no listener rating; listeners rated ECoG synthesis in 2019 [3] (Verdict) | Target Results; no listener test anywhere in text or Supplementary Information; [3] Results, Fig. 2b | correct; comparison not like-for-like | [3] had listeners transcribe synthesized sentences with 25- and 50-word pools. Herff et al. 2019 (Front Neurosci, doi:10.3389/fnins.2019.01267, in the ledger) ran a forced-choice listening test with 55 listeners on synthesized single words from ECoG. That is the closer protocol precedent for a single-word study (Fix M4). |
| 5 | Advantage over direct spectrogram or GAN decoding rests on three participants (Supp. Fig. 10) (Verdict) | Supplementary Information §9, Fig. S10 caption | correct | Caption: "applied … to speech production data in three of our HB participants". The figure shows one baseline only: the group's earlier model, described as "a direct ECoG to spectrogram model (with WaveNet as a vocoder)" and labelled GAN. The main text claims two baselines and "significantly". Fig. S10 reports no test. The review could state both points (Fix M5). |
| 6 | The causal PCC of 0.797 is within-participant reconstruction of 50 trained words (Verdict) | Target Results: Fig. 2a; Methods: Data collection | correct but one-sided | The authors report that held-out-word performance is "comparable to our standard trial-based held-out approach" (Results; Fig. 2b). The Verdict sentence should say so (Fix M7). |
| 7 | M06 usual approach: of 63, 12 spectrogram regression, 27 vocoder or formant parameters | M06 audit `prior_time_tally`, candidate list | numbers match audit; population wrong | Of the 73 candidate rows indexed 2022 or earlier, many are not intracranial synthesis. Examples: talking-face synthesis (isca-agelfors98, isca-blanco98, isca-arb01), ultrasound or lip silent speech interfaces (isca-hueber07/08, sottovoce), permanent-magnet articulography, EEG (arxiv-1908.05743), perception studies (doi-10.1126-sciadv.abc6348), reviews, datasets and an ethics paper (doi-10.1093-jmp-jhac011). The figure 27 also picks up waveform "vocoder" mentions. The table labels 12 as the usual approach although 27 is larger (Fixes H2, M3). |
| 8 | M06 state of the art: SwinTW PCC 0.817 (N=43, grid only), "non-causal by its description (inference)", 0.838 (N=39) [5] | [5] wiki text | numbers correct; causality claim insufficient evidence; wrong step | The [5] text never uses "causal". "Non-causal" cannot be inferred from windowed temporal attention, so it should read "causality not stated". The same source gives 0.825 for grid-only SwinTW in its detailed Results. The result changes decoder and electrodes, not the intermediate representation, so it is not a state-of-the-art result on M06's own step (Fix M2). |
| 9 | Formants drove a synthesizer in 2009 [6]; differentiability absent from 63 priors, named in 5 from 2024 on | [6] Abstract; M06 audit | correct for [6]; absence claim weak | No wiki-wide full-text step: `fulltext_pattern` is null and `recall_sample` is empty. The population is not intracranial-only. The DDSP lineage that the target itself cites ("Unlike the differentiable digital signal processing (DDSP) in ref.", Engel et al. 2020) goes unmentioned (Fix M10). |
| 10 | "New here: causal ResNet and Swin match their non-causal versions (P=0.093, P=0.196)" | Target Results, Fig. 2a; PNAS Results, Fig. 2E | P values correct; "new" overstated; "match" overstated | PNAS already compared causal, anticausal and noncausal ResNet ("slight decrease … performs close"). What is new is Swin and LSTM, and 48 participants. A non-significant Wilcoxon test is not an equivalence test (Fix M6). |
| 11 | M02 usual approach: 5 of 11 name an autoencoder latent; Lip2AudSpec 2017 [7] | M02 audit; [7] Sec. 3.3 | numbers match audit; population mixed | The 11 mix ultrasound, NAM whisper, lip video, auditory-perception reconstruction (Akbari 2019) and acoustic-to-articulatory inversion (isca-xie15). That is a different setting from the intracranial M06 and M12 populations. Known-item recall is 0.2 (Fix H2). |
| 12 | M02 state of the art: "same guidance trains" [5], PCC 0.838 | [5] Method: speech decoding framework (c25); Results Fig. 4 | quote correct; wrong step | 0.838 is the gain from extra electrodes. No result isolates the guidance loss (Fix M2). |
| 13 | 2021 encoder "generates reference speech parameters…" [2] | PNAS Methods: Speech encoder | correct in PNAS; insufficient evidence for v1 | Same issue as row 2. |
| 14 | M08: 7 neural vocoder, 4 Griffin–Lim of 63; Angrick used WaveNet [4] | M08 audit; [4] Abstract | numbers match audit; incomplete | The Appendix gives unit selection 17, the largest category, but the component line and table omit it. Same population problem as row 7. |
| 15 | Target and [2] use Griffin–Lim | Target Results; PNAS Methods | correct | |
| 16 | M08 state of the art: median 31% WER, 25-word pool (2019) [3] | [3] Results, Fig. 2b | number correct; conditions incomplete; not current | Missing conditions: sentences, closed pools, offline, five participants. Later listener results exist in other settings. Metzger et al. 2023 (Nature, doi:10.1038/s41586-023-06443-4; [concurrent]; cited by the target): median perceptual WER 8.20% (50-phrase-AAC) and 54.4% (1024-word-General), attempted silent speech. Wairagkar et al. 2025 (Nature, doi:10.1038/s41586-025-09127-3; [later]): transcript matching mean 94.34% (6 choices), open-transcription median WER 43.75%, intracortical, attempted speech (Fix M4). |
| 17 | M12: of 202, 76 k-fold, 39 random split, 7 held-out subject, 5 held-out words | M12 audit | numbers match audit; population wrong; dating slip | About 95 of 258 rows indexed 2022 or earlier have titles of EEG reviews, audiovisual-perception iEEG studies, datasets and similar. Brain2Char (J Neural Eng, online 2020-12-16, doi:10.1088/1741-2552/abc742) sits in the "2023" bucket and is a prior. |
| 18 | Five-fold test with 10 words withheld from all training (Fig. 2b) | Target Results; Fig. 2b caption | correct | |
| 19 | M12 state of the art: PCC 0.765 on unseen participants (2024, [concurrent]) [5] | [5] Main Results | correct | [concurrent] is right: 2024-03-11 is within 6 months of 2023-09-17. [5] calls it leave-one-out in Main Results but describes 5-fold sex-split cross-validation in the detailed Results; state the condition. The M12 audit note saying [5] "predates the target" is wrong, but it is not in the published text. |
| 20 | Eight productions per word, so test trials repeat trained words (inference) | Target Methods: "once in the AN and SC tasks and twice in the others" | correct | 1+1+2+2+2 = 8, and 50 × 8 = 400. |
| 21 | "The held-out-word result has no fold values (Fig. 2b)" | Fig. 2b caption: "performance … from five folds"; "performance across all five validation folds was comparable" | wrong as written | Fig. 2b plots each fold. What is missing is numeric fold means in the text (Fix M8). |
| 22 | No chance level; the 2021 preprint reported one [2] | Target text (no "chance"); PNAS Results ("estimated using shuffled data") | correct for target and PNAS; insufficient evidence for v1 | |
| 23 | Split 80/20 vs 350/50 = 87.5/12.5% | Target Results: Data collection; Methods | correct | |
| 24 | Released script tests every epoch with no validation set (train_e2a.py:770-825); no seeds | Code v1.0.1: loop at line 770, `epoch % 10` checkpoint at line 791; no `seed` or validation in file | correct; not pinned; framed beyond the evidence | The script evaluates the test set each epoch and saves every 10th epoch. It does not show test-based selection, yet the heading "Selection" implies it. The published text gives no tag or commit (Fix M11). |
| 25 | Causal ResNet 43.99 ± 1.09 ms; causal Swin 59.13 ± 0.74 ms; real time not the focus (authors) | Supplementary Table 1 (RTX-3060, N_FFT=256); Discussion | correct, credited | |
| 26 | Density: "no consistent gain" rests on five people (Fig. 3d) | Target Results; Fig. 3d | misquote | "No consistent gain" is not in the paper. The paper says "not significantly different from each other (with the exception of participant 2)". The five participants are the authors' own N (Fix M12). |
| 27 | Right hemisphere untested in left-damaged patients, as the authors concede | Target Discussion | correct, credited | |
| 28 | Loss weights tuned on three participants, split unstated | Target Methods: Model training | correct | |

## Required fixes, ordered by severity

**H1. High: Verdict, "What it adds … and a held-out-word test (5 of 202 prior studies, Appendix)".**
- Evidence: [2] (PNAS Results) reports "stricter cross-validation providing a similar performance" for unseen words (SI Appendix, Fig. S7). The review relies on [2] for its chance level but ignores this. "5 of 202" is an unlabelled regex mention count used as a design count in the Verdict, and the ledger missed [2] (known-item recall miss in M12).
- Fix: check 2021 v1 for the unseen-word test.
  - If it is there, remove the held-out-word test from the novelty list. What remains new is the scale of that test: ten-word folds across the cohort for causal ResNet.
  - If it is only in the PNAS version, cite it as [concurrent].
- Either way, label "5 of 202" as pattern match or drop it from the Verdict.
- Add low-density clinical grids (43 of 48 participants; [2] used hybrid-density grids only) to the list of what is new.

**H2. High: M06, M08, M02 and M12 usual-approach lines, the Verdict "none of 63 prior intracranial-synthesis ledger studies", and the Appendix.**
- Evidence: the populations named "intracranial-synthesis" (63) and "intracranial speech decoding" (202) contain talking-face synthesis, lipreading and ultrasound silent speech interfaces, EEG work, perception studies, reviews, datasets and an ethics paper (row 7 and row 17 examples). The M02 population (11) mixes five modalities and includes perception and inversion studies. This breaks the decoders-only population rule and the one-setting rule.
- Fix: filter each population to decoders or systems in the stated setting and recount. Or relabel the counts as "ledger rows matching the pattern, unfiltered" and remove them from the Verdict.
- Restate the absence sentence on the filtered intracranial set and name the deciding priors in it: [2], [3], [4], Herff 2019, Angrick 2021.

**M1. Medium: Verdict and M02 section (fairness and credit).**
- Evidence: the authors state the precedent themselves and say what changed. Methods: Speech encoder: Praat supervision "unlike our previous work in ref., which completely relied on unsupervised training". Discussion: "multiple improvements … over our previous approach on the subset of participants with hybrid-density grids".
- Fix: credit these statements with their locations instead of presenting the 2021 precedent as the reviewer's finding. Name Praat-supervised (semi-supervised) autoencoder pretraining as the authors' stated change on M02.
- Note that the five hybrid-density participants are probably the earlier cohort; the Discussion wording implies it.

**M2. Medium: State of the art on M06 and M02.**
- Evidence: SwinTW 0.817 and 0.838 come from a different decoder and extra electrodes. Neither isolates the intermediate representation or the guidance loss. "Non-causal by its description" is not supported, because [5] never mentions causality.
- Fix: write "causality not stated". Either give a result on each slot's own step, or say that no result isolates it. For M06, a representation-level comparator is Metzger et al. 2023 (HuBERT units; [concurrent]; cited by the target). For M02, no published ablation of the guidance loss exists, as the review's own question implies.

**M3. Medium: M06 and M08 usual-approach labels.**
- Evidence: the table names "Spectrogram regression (12)" as usual although "vocoder or formant parameters" counts 27. That 27 also counts waveform vocoder mentions, so it overlaps M08. M08 omits unit selection (17), its largest Appendix category.
- Fix: after the H2 recount, name the largest design or justify the choice. List unit selection in the M08 line and in the table.

**M4. Medium: M08 state of the art and the Verdict listener comparison.**
- Evidence: [3] is sentence transcription with closed 25- and 50-word pools. The like-for-like precedent for a single-word ECoG study is Herff et al. 2019, which ran a forced-choice listening test with 55 listeners. Later listener results exist (row 16).
- Fix:
  - Add the conditions to the [3] line: sentences, closed pool, offline, five participants.
  - Cite Herff 2019 as the closer listener-test precedent.
  - Add the most recent listener result with its conditions, labelled [concurrent] or [later].

**M5. Medium: Verdict, Supplementary Fig. 10 sentence.**
- Evidence: Fig. S10 shows one baseline, the group's own earlier direct-spectrogram/GAN model with a WaveNet vocoder, in three hybrid-density participants. No test is reported, although the main text says "significantly" and names two baselines.
- Fix: say "one baseline (the group's earlier model), three participants, no test reported".

**M6. Medium: M06, "New here: causal ResNet and Swin match their non-causal versions".**
- Evidence: [2] already compared causal and non-causal ResNet, finding a "slight decrease". The test is a non-significant Wilcoxon, not an equivalence test.
- Fix: write "no significant difference (P=0.093, P=0.196; not an equivalence test)". Restrict "new" to Swin, LSTM and the 48-participant scale.

**M7. Medium: Verdict, last sentence ("50 trained words").**
- Evidence: the authors report that held-out-word performance is comparable (Results; Fig. 2b).
- Fix: add that clause. The remaining criticism is that no numeric fold values or chance level are given (see M8).

**M8. Medium: M12, "The held-out-word result has no fold values (Fig. 2b)".**
- Evidence: Fig. 2b plots five folds.
- Fix: write "no numeric fold means in the text".

**M9. Medium: M02 and M06 quotes attributed to "the 2021 preprint".**
- Evidence: the claim-table quotes and locations come from the PNAS 2023 text (pmc-10589651-ffwd). The evaluator could not obtain v1 to confirm the wording.
- Fix: give v1 locators (page and section) for the quoted sentences in the claim table. Or attribute the quotes to the PNAS version and add "first described in the 2021 preprint".

**M10. Medium: M06 absence sentence ("differentiability is absent from the 63 prior studies").**
- Evidence: there was no wiki-wide full-text step (`fulltext_pattern` null, `recall_sample` empty). The target cites DDSP (Engel et al., ICLR 2020) as the source of differentiable synthesis.
- Fix: run the full-text step on the filtered population, and name DDSP as the lineage the authors credit.

**M11. Medium: "Where the claims outrun the evidence", Selection item.**
- Evidence: in the v1.0.1 code, the test set is evaluated each epoch and checkpoints are saved every 10 epochs. No test-based checkpoint choice is visible, and the paper does not say which epoch is reported.
- Fix: pin the code reference as "flinkerlab/neural_speech_decoding v1.0.1, train_e2a.py:770–825". Reword to "the test set is evaluated every epoch; which epoch is reported is not stated".

**M12. Medium: Density item, quoted "no consistent gain".**
- Evidence: the phrase is not in the paper.
- Fix: quote the paper ("not significantly different … with the exception of participant 2", Fig. 3d) or remove the quotation marks. Credit N=5 as the authors' own figure.

**L1. Low: Appendix dating.**
- Evidence: the cutoff is year-only ("2022 or earlier"). Under the ±6-month rule, prior means before 2023-03-17. Brain2Char (2020) is misfiled in the M12 "2023" bucket. Undated rows are large: 39 against 63 in M06, 109 against 202 in M12.
- Fix: use the date cutoff, refile Brain2Char, and state the share of undated rows next to each count. Impact on the decoder counts is small; the 2023 items before 2023-03-17 are mostly not decoders.

**L2. Low: M03.**
- Evidence: the verdict is "not reported" while the cell says "Per-participant" (reported). This conflicts with the checklist rule against "not_reported with a filled cell".
- Fix: make it "standard", and move the tuning-split gap to the note.

**L3. Low: Verdict, "Both are standard for this paper".**
- Evidence: both designs depart from the stated usual approach. They are "standard" only because of a same-group precedent.
- Fix: say "standard (not new: same-group 2021 precedent), departing from the usual approach".

**L4. Low: References.**
- Evidence: process notes appear in the published references: "Read as the Version of Record (PMC OA BioC XML)" and "read as the PNAS version".
- Fix: drop them or reduce them to version labels.

**L5. Low: M12 state of the art.**
- Evidence: [5] is internally inconsistent: leave-one-out in Main Results, 5-fold sex-split cross-validation in Results.
- Fix: state the protocol behind 0.765.

## Scores

- **Procedure: 5/10.** The target numbers, Supplementary Table 1, Fig. S10, the code lines and the comparators' values check out, and the same-group precedent was found and read. But the populations are not filtered to decoders, and the absence claim has no full-text step. The 2021 v1 is cited through PNAS quotes, and [2]'s own unseen-word test was missed.
- **Final text: 6/10.** It takes a clear, mostly well-located position. The authors' caveats on real time and the right hemisphere are credited, and the 80/20 vs 350/50 and test-word-recurrence points are correct. Against that, the Verdict's novelty list contains one item that [2] already reports. Two state-of-the-art lines are not on their slot's step, and the text has one misquote, one wrong statement about Fig. 2b and uncredited author disclosures about the precedent.

## Final counts by severity

- High: 2 (H1, H2)
- Medium: 12 (M1–M12)
- Low: 5 (L1–L5)
- Claim-table results (28 rows):
  - correct: 11
  - numbers correct, but incomplete, one-sided, on the wrong step or framed beyond the evidence: 11
  - wrong or partly wrong: 3 (rows 3, 21, 26)
  - insufficient evidence for the 2021 v1 wording: 3 (rows 2, 13, 22; these share the PNAS-verified part)
