# Evaluator: a language model separate from the writer

Review checked: `towards-reconstructing-intelligible-speech-from-the-human-auditory-cortex.md` (and `compact.md`, `claims.md`, `slots.json`, `verdict.json`, both topic audits). Sources opened: the target in the wiki (`pmc-6351601-intelligible/source/sc_text.txt`, `doi-10.1038-s41598-018-37359-z/source/text.txt`), Martin 2017 thesis, Matthews 2012 thesis, Chakrabarti 2015 thesis, Berezutskaya 2022, Wairagkar et al. 2025 (`doi-10.1038-s41586-025-09127-3`), bioRxiv 10.1101/2024.12.16.628596, Mesgarani & Chang 2012 (`doi-10.1038-nature11020`), Moses et al. 2016. The supplementary PDF of the target is not in the wiki, so the Supplementary Table values can only be checked against `notes.json`. Date: 2026-11-26.

## Claim table

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Network decodes a 256-node autoencoder code of 516 WORLD parameters (Verdict) | Target, Fig. 1 caption; Methods, DNN architecture | correct | |
| 2 | Model ordering repeats in each of five patients (Verdict, Fig. 4) | Target, Results: "the relative performance of the four models was the same in all subjects" | correct | The repetition covers the four models (LR/DNN × spectrogram/coded vocoder). It does not cover the raw-vocoder control. |
| 3 | "this has not been attempted previously" is contradicted by Guenther 2009 and Chakrabarti 2015 (Verdict; Where) | Target Introduction; Guenther 2009 Introduction/Methods; Chakrabarti 2015 Ch. 4 | correct | The quotes support formant decoding (Kalman filter, F1/F2) and ten LPC coefficients from ECoG, both in production. |
| 4 | "a lineage the paper does not cite" (M06 body) | Target reference list: ref 7 (Chakrabarti, Sandberg, Brumberg, Krusienski 2015, review of ECoG speech decoding) and ref 59 (Herff et al. 2016 EMBC, "Towards direct speech synthesis from ECoG: A pilot study") | wrong | The target cites a production-side direct-synthesis pilot from ECoG and a review of that lineage. It does not cite Guenther 2009 or Chakrabarti's thesis by name. |
| 5 | All 4 earlier heard-speech intracranial reconstruction studies decode a spectrogram, 3 linear and 1 DNN (M06 Usual approach; Appendix) | M06 audit `prior_time_tally_…`: Pasley 2012, Yang 2015, Leonard 2016, Martin 2017 thesis; wiki `doi-10.1038-nature11020` | insufficient evidence (population incomplete) | Mesgarani & Chang 2012 (Nature 485:233; heard two-talker mixtures, ECoG, linear spectrogram reconstruction) is in the wiki and missing from the 4. With it the count is 5 of 5, 4 of them linear. Pasley 2012 also decoded a modulation-energy target, so a non-spectrogram heard-speech target existed before 2018. |
| 6 | First public date bioRxiv 2018-06 (M06; ref 1) | Review text; `prep/target.json` | correct in the review; internal inconsistency in the files | `prep/target.json` gives `first_public: 2019-01`. The review uses 2018-06 consistently. The counted window ends at 2017, not at 2018-06 (see fix L2). |
| 7 | ESTOI raw vocoder 0.30, network spectrogram 0.40, coded vocoder 0.47, linear 0.31 (Verdict; M06; Where) | `notes.json` (Supplementary Table 2); target text says only "significantly better" (t56) | insufficient quote | The numbers are in `notes.json` only. Another `notes.json` entry says Supplementary Table 2 "was not supplied", which contradicts it. The claim-table quote has no numbers. |
| 8 | +17.5% and +52% relative ESTOI (inference) | Arithmetic: 0.47/0.40 = 1.175; 0.47/0.31 = 1.516 | correct | |
| 9 | Bottleneck: 32, 128, 256 tie at 0.47, yet 256 "said to maximize accuracy" (Where) | Target Methods: "maximized both the objective reconstruction accuracy (Supp. Table 3), and the subjective assessment" | correct but incomplete | The authors also cite a subjective criterion that could break the tie. The review leaves it out. |
| 10 | 65% (Abstract) vs 67% (Results) (Where) | Target Abstract; Results, Subjective evaluation | correct | |
| 11 | 11 listeners vs "all the ten listeners" (Where) | Target Results; Fig. 3 caption ("Eleven subjects"); Methods ("11 participants") | correct | |
| 12 | Sentences averaged over six repetitions (Results) vs presented eight times (Methods) (Where) | Target Results, Neural recordings; Methods, Stimulus | correct | |
| 13 | Digits repeated six times; patient behind the 40 tokens not stated (M12) | Target Methods, Stimulus; Results, Subjective evaluation | correct | No sentence names the subject or the aggregation used for the listener tokens. |
| 14 | 128 electrodes pooled across five patients; authors call this an upper bound (Where) | Target Results, "combined the electrodes of all five subjects"; Discussion | correct | The training-duration sweep (Fig. 5C) also uses 128 pooled electrodes. The review does not say so. |
| 15 | Yang 2015: network vs linear, two patients (M06) | Yang 2015 Abstract, Sec. 2.1 | correct | |
| 16 | SOTA: best listener score from neural signals is 80% (Angrick 2024, 6 keywords) (M06, M12, table) | Wairagkar et al. 2025 Nature (`doi-10.1038-s41586-025-09127-3`, Results): transcript matching among 6 sentences, mean 94.34%, median 100%; open transcription median WER 43.75% | wrong | A later neural listener score from the M12 candidate list is higher under the same 1-in-6 chance. Both are production studies, not heard speech. |
| 17 | "closest later heard-speech design" is Berezutskaya 2022, correlations only (M06 SOTA) | bioRxiv 10.1101/2024.12.16.628596 (wiki; in the M12 audit candidates) | wrong | That study records ECoG from 9 participants listening to TIMIT sentences. It maps the recordings to a frozen pre-trained wav2vec 2.0 latent and synthesizes speech with HiFi-GAN. Four listeners transcribed 71.6% of words, PER was 28.6%, and ESTOI is reported. It is closer to the target than Berezutskaya 2022 on every axis: heard speech, a pre-trained latent target, a listener test and ESTOI. |
| 18 | Berezutskaya 2022: 9 subjects, movie, GAN latent, mel decoding correlates better | Berezutskaya 2022 Sec. II–III | correct | It has only an informal listening remark and no formal listener test. |
| 19 | Anumanchipalli 2019 [concurrent], median 31% WER with a 25-word pool | Fig. 2b quote; bioRxiv 2018-11 | correct | Chronology label right (5 months after the target). |
| 20 | 18 studies decoding synthesizer-like parameters from neural signals, all production or imagery (M06 body) | M06 audit `recall_check_…synthesizer_parameter_decoding` | wrong as worded | The audit counts 18 keys, with versions not merged. Only some are neural decoders. The rest are "reviews or non-neural synthesis". The cutoff (≤ 2018) takes in a [concurrent] work (Brumberg 2018). The Appendix wording is right and the body wording is not. |
| 21 | All 14 pre-2018 reconstruction evaluations score correlation; listener rating 0 (M12) | M12 audit `prior_time_tally_…` (19 unique keys, 5 named exclusions, no pids for the 14); candidate list | insufficient evidence / likely inflated | Subtracting the 5 named exclusions from the 19 pre-2018 unique keys leaves 14 that must include cEEGrid target-speaker detection (2016). The topic's inclusion rule excludes that design ("attention decoding that only tracks an envelope to select a talker … not a reconstruction study"). The 14 also hold the AV-speech MEG encoding study (2017) and the EEG hierarchical-entrainment study (2017), which the M06 audit classes as off-population. The listener-rating count of 0 is unaffected. |
| 22 | No listener rating of neural reconstructions before 2018 (M12) | Whole-wiki check; Guenther 2009; Matthews 2012; Chakrabarti 2015; own knowledge | correct as far as I can check | I know of no pre-2018 formal listener test of audio decoded from neural signals. Guenther 2009 used closed-loop auditory feedback to the participant, not listener scoring. Listener tests were routine before 2018 in non-neural synthesis from articulatory, EMG or video input (e.g. the 85% 2017 visual-to-speech candidate in the Appendix). The authors make the same claim themselves (Introduction: "previous studies have been evaluated only using objective measures such as correlation or recognition accuracy"). |
| 23 | "The paper changes one component" (Verdict) and "departs in the target only" (M06) | Target Results: models vary in "1) regression technique … 2) the representation … 3) the neural frequency range"; "The input to all models was … both low frequency and the high-gamma envelope"; Fig. 5A | wrong | The paper also changes the evaluation (M12, which the review calls its "most useful change") and the input bands (M05, low frequency plus high gamma, with a gain shown in Fig. 5A). |
| 24 | M06 `ahead`: ledger count, deciding priors read, repetition (rule check) | SKILL.md verdict rule; audit `read_fulltext` (Yang, Guenther, Chakrabarti read, role prior) | mostly meets the rule | The count is in the Appendix and the priors were read and cited. Repetition across five patients is shown for the coded target only. The prior population misses Mesgarani & Chang 2012, which does not change the verdict. |
| 25 | M12 `standard` | SKILL.md: "standard = matches the usual approach, or the difference is not supported well enough to call" | inconsistent wording | The target's design plainly differs from the usual approach (listener test vs 0 of 14). Calling it "standard" can only rest on the second clause, and the text does not say so. Instead it calls the listener test "the paper's most useful change". |

## Required fixes, ordered by impact

**H1 (high). State of the art for M06 and M12 is not the best work and is the wrong setting.**
- Location: M06 "State of the art"; M12 "State of the art"; 13-components table, M06 and M12 rows; Appendix "Listener scores among sota candidates".
- Evidence:
  - The 80% figure is from Angrick et al. 2024 (ALS, attempted production, 6 keywords). It is not the best listener score from neural signals. Wairagkar et al. 2025 (Nature; wiki `doi-10.1038-s41586-025-09127-3`, Results) reports a mean 94.34% transcript match among 6 sentences, with the same 1-in-6 chance, and an open-transcription median WER of 43.75%. That study is in the M12 audit candidates.
  - For heard speech, the closest later design is not Berezutskaya 2022. bioRxiv 10.1101/2024.12.16.628596 (2024) uses ECoG from 9 participants listening to TIMIT sentences and a frozen pre-trained wav2vec 2.0 latent target with a HiFi-GAN decoder. Four listeners transcribed 71.6% of words, PER was 28.6%, and ESTOI is reported.
- Fix:
  - M06 SOTA: name bioRxiv 2024.12.16.628596 [later] as the heard-speech heir of the latent-target idea (71.6% open word recognition, sentence material). Keep Berezutskaya 2022 only as a secondary correlation-only result.
  - Drop "the best listener score from neural signals … is 80%". If a production comparator is kept, use Wairagkar 2025 (94.34% 6-choice match; median WER 43.75%) and say plainly that it is production, not heard speech.
  - M12 SOTA: replace with the same two works. Keep Anumanchipalli as [concurrent].
  - Update the table cells, refs and the Appendix to match.

**H2 (high). Wrong statement about the target's citations.**
- Location: M06 body, "a lineage the paper does not cite"; Where, Priority bullet.
- Evidence: the target cites ref 7, Chakrabarti, Sandberg, Brumberg & Krusienski 2015 (Biomed. Eng. Lett.), a review of ECoG speech decoding. It also cites ref 59, Herff et al. 2016 EMBC, "Towards direct speech synthesis from ECoG: A pilot study", a production-side direct synthesis from ECoG listed among the linear-regression methods.
- Fix: replace with "a lineage the paper cites only through a review [its ref 7] and a direct-synthesis pilot [its ref 59], yet still calls synthesizer-parameter estimation unattempted". This sharpens the overreach finding, because the authors had the counter-example in their own reference list.

**M1 (medium). M06 prior population is incomplete, and "all decode a spectrogram" leaves out modulation targets.**
- Location: Verdict ("all 4 earlier …"); M06 Usual approach; Appendix M06 tally.
- Evidence:
  - Mesgarani & Chang 2012 (Nature 485:233–236; wiki `doi-10.1038-nature11020`) reconstructs auditory spectrograms by linear decoding from ECoG during heard two-talker mixtures. Its Abstract reads: "speech spectrograms reconstructed based on cortical responses to the mixture of speakers". It is first public 2012 and absent from the 4 and from the audit candidates.
  - Pasley 2012 also decoded a modulation-energy representation, which was its best-performing model.
- Fix: report 5 of 5 heard-speech intracranial studies with a spectrogram target (4 linear, 1 DNN). Add "Pasley 2012 also decoded modulation energy; no study decoded vocoder parameters or a learned latent". Note the recall miss in the Appendix. The verdict is unchanged.

**M2 (medium). The M12 denominator of 14 is not reproducible and appears to include designs the inclusion rule excludes.**
- Location: M12 Usual approach; table M12 ("pattern match 14"); Appendix M12.
- Evidence: the audit lists no pids for the 14. The 19 pre-2018 unique keys minus the 5 named exclusions must include:
  - cEEGrid target-speaker detection 2016, which is excluded by the M12 rule;
  - the 2017 AV-speech MEG and EEG hierarchical-entrainment studies, which the M06 audit classes as off-population;
  - Cheung et al. 2016 (motor-cortex auditory representation, an encoding study).
- Fix: list the 14 pids in the audit and re-tally after applying the rule (likely about 9 to 11 unique reconstruction studies). Restate as "correlation in all N of N". The listener-rating count stays 0.

**M3 (medium). The M12 verdict contradicts the Verdict and the M12 prose.**
- Location: Verdict ("changes one component … The listener test (M12) is standard"); M12 closing paragraph ("most useful change … Verdict: standard").
- Evidence: SKILL.md allows `standard` for a differing design only when "the difference is not supported well enough to call". The review's own count shows the design differs (0 of N earlier studies use listener rating).
- Fix: say "M12 departs from the field (listener scoring, 0 of N before 2018) but is not called `ahead` because the tokens come from one unnamed patient or aggregation, likely from six-repetition averages, with closed-set digits, so the result has no repetition across subjects". Change "changes one component" to "changes the decoding target (M06) and adds listener scoring (M12)". Credit the authors' own statement (Introduction) that prior work used only objective measures; see L3.

**M4 (medium). The confound is stated more strongly than the evidence allows, and the `ahead` credit rests on the wrong element.**
- Location: Verdict ("so the gain belongs to a compression trained on 80 hours of external speech"); M06 body ("The heard-speech vocoder target is new in its setting").
- Evidence: Supplementary Table 2 (via `notes.json`) shows that raw vocoder parameters (0.30) score below the network spectrogram (0.40), and that coded parameters reach 0.47. This isolates the coding step. It does not isolate the external corpus from dimensionality reduction or from the tanh, noise-trained bottleneck (Methods). No coded spectrogram was tested. The per-patient repetition (Fig. 4) covers the coded target only.
- Fix:
  - Verdict: "the gain comes from the autoencoder code (raw parameters 0.30 vs coded 0.47); whether the 80-hour external corpus, the compression or the vocoder parameterization carries it is untested (inference)".
  - M06 body: credit `ahead` to "an externally pretrained compressed target" and not to "the vocoder target". The raw vocoder target was worse than the spectrogram.

**M5 (medium). The input-band change (M05) is omitted from the changed components.**
- Location: Verdict ("changes one component"); M06 ("departs in the target only"); table M05 (standard, no count).
- Evidence: the target lists the neural frequency range as one of its three design factors (Results). All four models take low frequency (0–50 Hz) plus the high-gamma envelope, and Fig. 5A shows the combination beats either band alone. The heard-speech priors (Pasley, Yang, Leonard) use high gamma.
- Fix: add M05 as an incidental change in one sentence, with a reason or count for the verdict. State that the 65–67% and +52% gains over the linear baseline are measured with both bands in every model, so they do not mix the band change with the target change.

**M6 (medium). The whole-wiki synthesizer-parameter count is misstated in the body.**
- Location: M06 body, "A whole-wiki full-text check to 2018 finds 18 studies … from neural signals, all in production or imagery".
- Evidence: the audit counts 18 keys, with versions not merged. It says "the rest are reviews or non-neural synthesis". The cutoff ≤ 2018 takes in Brumberg 2018, which is [concurrent].
- Fix: "18 full-text keys to 2018 (versions not merged); the neural decoders among them (Guenther 2009 and its lineage, Chakrabarti 2015; Brumberg 2018 [concurrent]) are all production or imagery". Also apply L4.

**L1 (low). The bottleneck tie leaves out the authors' second criterion.**
- Location: Where, Bottleneck.
- Fix: "objective scores tie at 0.47 for 32, 128 and 256 nodes; the subjective comparison the authors cite to pick 256 is not reported".

**L2 (low). The cutoff wording is loose.**
- Location: M06 Usual approach, "before the target's first public date (bioRxiv, 2018-06)".
- Evidence: the counted window is "first public 2017 or earlier", and 2018-01 to 2018-12 is treated as [concurrent].
- Fix: say "first public 2017 or earlier (target bioRxiv 2018-06; 2018 works counted as [concurrent])". Also correct `prep/target.json` `first_public` (2019-01) to 2018-06 so later runs stay consistent.

**L3 (low). Fairness: the authors already state the M12 absence.**
- Location: M12 Usual approach.
- Evidence: target Introduction, "previous studies have been evaluated only using objective measures such as correlation or recognition accuracy".
- Fix: add "as the authors note (Introduction)". Present the ledger count as confirming their claim, not as the review's own discovery.

**L4 (low). Method restatement and process narration in the body.**
- Location: M12 ("The paper adds 11 listeners, 40 TI-46 digit tokens per model, MOS and speaker gender beside ESTOI."); M06 ("A whole-wiki full-text check to 2018 finds …").
- Fix: cut the first sentence to the contrast that matters ("listener digit identification and MOS beside ESTOI, against correlation-only practice"). Move the search narration to the Appendix and keep only the finding in the body.

**L5 (low). The Supplementary Table numbers lack a quotable source.**
- Location: claim table rows 4, 11, 17–19; `notes.json`.
- Evidence: the target text gives no values. `notes.json` holds both the values and an entry saying Supplementary Table 2 "was not supplied".
- Fix: add a `notes.json` quote from the supplementary PDF with table and row labels, and delete the contradictory "not supplied" condition.

**L6 (low). The training-duration sweep also uses pooled electrodes.**
- Location: Where, Electrodes.
- Evidence: target Results: "We used 128 randomly chosen electrodes and trained several neural network models … from 10 to 30 minutes".
- Fix: extend the bullet to say that the duration sweep (Fig. 5C) uses the same pooled, cross-patient set.

## Strongest confound and whether it is handled

The coded target versus the spectrogram mixes three things: the vocoder parameterization, the dimensionality reduction, and an external 80-hour speech prior. The review names the confound and proposes the right control (a coded spectrogram). It overstates which factor is responsible (M4) and still credits the vocoder in the M06 body.

## Scores

- Procedure: 6/10. The deciding priors were read and the chronology labels are right. But the heard-speech population misses Mesgarani & Chang 2012, the M12 denominator is not reproducible, and the state-of-the-art search missed two in-wiki later works that beat or fit better than the chosen ones.
- Final text: 6/10. The positions are clear and the target-internal inconsistencies are all correct. The state of the art is wrong for both audited slots, one factual claim about the target's citations is wrong, and the M12 verdict wording contradicts itself.

Counts by severity: high 2, medium 6, low 6.
