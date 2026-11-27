# Evaluation: Audio-visual speech recognition using deep learning (Noda et al., Appl. Intell. 2015)

Evaluator: a language model separate from the writer

Date: 2026-11-27. Inputs: `compact.md`, `audio-visual-speech-recognition-using-deep-learning.md`, `slots.json`, `verdict.json`, the four topic audits, `reader1/*.txt`, and the wiki source texts of the target (`doi-10.1007-s10489-014-0629-7/source/sc_text.txt`), [2] (`isca-noda14-cnnlip`), [5] (`arxiv-2406.10082`), [7] (`arxiv-2406.12233`), [9] (`arxiv-2602.19316`), plus `isca-duchnowski94_icslp`, `isca-heckmann01-annhmm`, `isca-watanabe90_icslp` and `oa-W3099202502`. I rebuilt the prior populations with the writer's `dated_counts.py` logic, read-only. I modified nothing.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Denoising AE on 11-frame MFCC windows, five hidden layers | target Sec. 5.1, Table 1, Sec. 6.5 | correct | 429-in/429-out, 300-150-80-40-80-150-300 |
| 2 | Stream weights 0 to 1.0 in 0.1 steps; "best ... over all stream weight pairs" | target Sec. 5.3 | correct | 11 weights, so "best-of-11" holds (inference) |
| 3 | AE depth picked on the test words | target Sec. 6.1 (40 test words), Fig. 4 | correct | "five hidden layers obtained the best ... among all SNR ranges", on the 40-test-word evaluation |
| 4 | Gaussian noise only; train 10 dB steps, test 5 dB steps | target Sec. 5.1, 6.1, 6.5 | correct | Train and test both use superimposed Gaussian noise (see F6) |
| 5 | 45.87% phonemes at 32×32 (Table 4); ~22.5% words (Sec. 6.4) | target Table 4, Sec. 6.4 | correct | 22.5% is for 16×16 and 64×64 with 32 Gaussians, 40 test words, closed-speaker |
| 6 | [2]: 58% phonemes, ~37% words, 84 test words, 6×6 and PCA baselines | [2] Sec. 6.1, 6.3 | correct | The protocol differs, and the review does not say so (F3) |
| 7 | "unaddressed" (Sec. 2.2); 52 references; [2] not cited | target Sec. 2.2, reference list | correct (fact), unfair (use) | [2] is absent from refs 1–52. It is [concurrent] (F1) |
| 8 | 24000 recordings vs 400 × 6; 216 vs 360 training words | target Sec. 4, 5.2, 6.4 | correct | |
| 9 | Authors concede that adaptive weighting is missing | target Sec. 7.2, Sec. 8 | correct | Sec. 8 also says "automatic selection of stream weight was not attained". The review cites only Sec. 7.2 |
| 10 | Papandreou: 0–1 grid in 0.1 steps on a reserved group, NOISEX babble, held-out speakers | reader1 TASL text, Sec. VI.A/C | correct | The weights are chosen on a reserved repetition (first six speakers), and results are averaged over the other five |
| 11 | Potamianos & Neti: exponent tuned on a held-out set, babble, unseen speakers | reader1 Eurospeech text, Sec. 2.2, 4.1 | correct | Also reports MS (seen-speaker) results, so seen-speaker testing is not by itself behind practice |
| 12 | Miyajima: GPD-trained weights, jackknife held-out speaker | reader1 ICSLP text, Sec. 3.2, 4.1 | correct | M2VTS French digits. Not among the 9 "held-out set" pattern hits |
| 13 | Yoshida & Nakadai sweep plus SNR regression | quote y5/y6 | correct | |
| 14 | LP Conformer 1.9% WER, LRS3, babble 0 dB, 100k h | Whisper-Flamingo Table 3 | correct, condition incomplete | The table warns that noisy WER from different noise datasets is "not directly comparable" |
| 15 | VIT 3D 6.1% → 2.9%, 52% relative | Whisper-Flamingo Table 3 | correct | (6.1−2.9)/6.1 = 52.5% |
| 16 | SyncVSR 93.2% LRW top-1 | SyncVSR Table 1 | correct, condition incomplete | No word-boundary input, LRW only (157 h). 95.0% with boundaries |
| 17 | USR 2.0 reports AVSR WER as mean and SD over three seeds | USR 2.0 Table 13 | insufficient condition | Seeds appear only in appendix Table 13 (LRS3 low-resource, 50-epoch runs, clean). Main results have no SD |
| 18 | Prior AVSR 65: MFCC 33, enhancement 9, learned denoiser 0 | M06 denoising audit, rebuilt population | correct as tally, population flawed | Duplicates and off-population items (F4) |
| 19 | Prior lip-reading 127 "with a recognizer": HMM 102, CNN 0 | lipreading audit, rebuilt population | partly wrong | The raw regex gives CNN 1, and the audit removes it by hand as a false hit (JSALT 2000 report, "CNN broadcast news"; confirmed). At least 13 members have no automatic recognizer (F5) |
| 20 | Fusion: multi-stream HMM 29 of 65 usual | fusion audit | correct as tally | It includes the huang09b and wu07d duplicate pairs, so 27 unique |
| 21 | M12: held-out set 9 of 65 | M12 audit prior_pids | correct as tally | It includes the huang09b pair, so 8 unique. Contains [3] and [4] but not [10] |
| 22 | Dating: [2] Interspeech 2014-09 is [concurrent]; target online 2014-12-20 | [2] header, target p. 1, Crossref | label correct, body use wrong | Crossref: created 2014-12-19, online 2014-12-20, print 2015-06. No received date in the PDF text, and Springer's page could not be fetched, so submission date unverified |
| 23 | Noda 2014 "three months older" | as above | correct arithmetic, wrong role | See F1 |

## Findings, ordered by impact

**F1. High. Concurrent work is treated as prior work and as a missed citation.**
- Location: Verdict sentence 3 ("the authors' own uncited Interspeech 2014 design, three months older"), M06 visual paragraph ("The departure belongs to [2], three months earlier"), Priority bullet ("contradicted by [2], absent from the 52-item reference list"), and the ref 2 note ("published three months before the target; not in the target's reference list").
- Evidence: SKILL.md lines 88 and 115 say that "Neither [concurrent] nor [later] counts as prior work and neither can be a 'missed citation'." The draft's own Appendix puts [2] in [Concurrent] (11), CNN 1. Interspeech 2014 is 14–18 Sept 2014, which is inside the 2014-06 to 2015-06 window. The journal's submission date is unknown: no "Received" line in the text, and the Springer page could not be fetched. The manuscript may predate the conference, so "uncited" is not a fair charge. The visual verdict "standard" rests entirely on [2]. Once [2] is removed, the prior count is CNN 0 of 127.
- Fix:
  - Rebase the visual verdict on prior evidence only. Prior CNN is 0 of 127. Name the real deciding priors (F2). Keep `standard` because the word-level effect is pooled, from one run and on seen speakers. Alternatively, test `ahead` explicitly: Table 4 gives per-speaker phoneme rates, but there is no per-speaker or repeated word-level comparison against the baselines.
  - Restate [2] as overlap, not priority: "The same authors' [concurrent] Interspeech 2014 paper [2] reports the same seven-layer CNN on the same six speakers; the journal text does not mention the overlap."
  - Delete "uncited" and "three months older/earlier" from the Verdict and the M06 visual paragraph.
  - Delete the Priority bullet, or rewrite it against prior work (see F2).
  - Change the ref 2 note to "[concurrent]; same authors".

**F2. Medium. The visual absence claim and the Priority critique lack the deciding priors in the population.**
- Location: M06 visual Usual approach line and paragraph, Priority bullet, Appendix lipreading entry.
- Evidence: the 127-study prior population contains neural visual front ends that work on mouth pixels and output phonetic units:
  - Duchnowski et al., ICSLP 1994 (`isca-duchnowski94_icslp`) feed 24×16 normalized lip pixels into a visual MS-TDNN, a weight-shared time-delay network. It outputs viseme units, which are combined with acoustic phoneme units.
  - Watanabe & Kohda, ICSLP 1990 (`isca-watanabe90_icslp`) use layered neural networks for lip-reading.
  - Heckmann et al., 2001 (`isca-heckmann01-annhmm`) fuse audio and video phoneme a-posteriori probabilities in an ANN/HMM.

  The regex "(phone|phoneme|viseme) posterior" gives 0 prior hits, and it misses these. "0 a CNN" holds literally only for 2D CNNs. The design the paper adds is "network on raw mouth images → phonetic posteriors → HMM", and that has precedents.
- Fix: in the visual section, write "None of the 127 prior lip-reading studies (pattern match, Appendix) applies a 2D CNN; neural networks on lip pixels with phonetic outputs date to the MS-TDNN of [Duchnowski 1994] and ANN/HMM posterior fusion of [Heckmann 2001]". Cite both and read the first. Recast the Sec. 2.2 criticism as narrow: "unaddressed" holds for 2D CNNs but omits the TDNN lineage.

**F3. High. "Unexplained" is wrong: the two papers' protocols explain the word-rate gap.**
- Location: M06 visual paragraph ("about 22.5% words, unexplained") and Question 3.
- Evidence:
  - In [2], Sec. 5, the CNN is trained on frames from all 300 words, shuffled, with 5/6 used for training. The 84 test words are among them. In the target, Sec. 6.4, the VSR features come from a CNN "trained with 360 training words", so the test words are excluded.
  - The splits also differ: 216/84 in [2] against 360/40 in the target.
  - The ~37% in [2] is therefore not comparable to the target's 22.5%, and is likely inflated by test-word frames seen in CNN training (inference).
  - Both papers also measure phoneme rates on randomly shuffled 100 Hz frames, where adjacent frames fall in train and test (target Sec. 5.2, "shuffled and 5/6 of the data were used for training"). So the 45.87% of Table 4 is a frame-level within-word score (inference).
- Fix: replace "unexplained" with the protocol difference. Add a bullet under "Where the claims outrun the evidence": "Phoneme rates (Table 4) come from a random frame split (Sec. 5.2), so neighbouring frames of the same word sit in training and test." Drop Question 3, or ask whether the 2014 CNN saw the test words.

**F4. Medium. The AVSR denominator 65 contains duplicates and off-population items.**
- Location: Appendix, all three AVSR topics, and every "of 65" in the body.
- Evidence:
  - Two version pairs are counted twice, because grouping is by ledger key and not by ISCA id: `isca-huang09b-cdt`/`isca-huang09b_interspeech` and `isca-wu07d-2dpca`/`isca-wu07d_interspeech`.
  - Unlike the lipreading population, there is no recognizer filter (`excluded_no_automatic_recognizer: null`). The 65 includes non-recognizer studies: `pmc2700967_avstats` (natural statistics), `openaccess_avsp_barker99` (acoustics from visual features), `avsp-mccotter01_luminance` (perception), `isca-walsh05_avsp` (agent framework), `isca-ozgur08_avsp` (lip segmentation), `isca-gurbuz05_interspeech` (lip tracking), `doi-10.63317-26hq9jzng47p` (corpus) and `isca-xie12-avfusion` (pattern discovery).
  - Unique counts change: MFCC 33→31, multi-stream 29→27, held-out 9→8, out of 63 before the off-population exclusions. The usual designs stay the same.
- Fix: deduplicate by ISCA paper id or title, apply the same recognizer filter used for lipreading, and restate the counts and denominators.

**F5. Medium. The 127 "lip-reading studies with a recognizer" still include studies with no recognizer.**
- Location: M06 visual Usual approach line and Appendix.
- Evidence: the lexical recognizer filter keeps at least 13 perception, synthesis or neuroimaging studies, for example `doi-10.1016-j.bandl.2013.05.009` (fMRI), `pmc-3689691-avcortex` (fMRI), `pmc-pmc3155585` (normative lip-reading skills), `isca-tiippana10_avsp` (McGurk), `isca-siciliano03_avsp`, `isca-agelfors98_icslp`, `isca-pelachaud01-italian`, `isca-eger09_avsp`, `isca-wik08_aughead`, `isca-zelezny08_avsp`, `doi-10.1016-j.specom.2010.09.003`, `avsp-mccotter01_luminance` and `openaccess_avsp_barker99`.
- Fix: exclude these, or drop "with a recognizer" from the label, and restate HMM n/N.

**F6. Medium. The main confound of the denoiser is missed: the noise type is matched between training and test.**
- Location: M06 audio paragraph ("Training uses 10 dB steps, testing 5 dB steps").
- Evidence: the AE is trained on the same synthetic Gaussian noise used in testing (Sec. 5.1, 6.1, 6.5). The ~65% gain at 10 dB (Sec. 6.1) is therefore in-distribution. The step sentence states a fact and takes no position.
- Fix: replace that sentence with "The denoiser is trained and tested on the same synthetic Gaussian noise (Sec. 5.1, Sec. 6.1), so the ~65% gain at 10 dB is a matched-noise result; only the 5 dB intermediate levels are unseen."

**F7. Medium. Precedents are handled inconsistently between the two front ends, and the "new to AVSR" headline overstates.**
- Location: Verdict sentence 2 and M06 audio paragraph.
- Evidence: the denoiser is audio-only and is applied before fusion. The authors themselves present it as an adoption of Vincent's denoising AE (Sec. 2.1) and cite Feng, Zhang & Glass, ICASSP 2014 (May 2014, prior; target ref 13) and Maas et al. 2013 (target ref 32). "New to AVSR" is a property of the population, not of the method. Feng 2014 is mentioned in the review only as "its reference 13", without a reference entry. The visual side, by contrast, loses novelty to a same-group concurrent paper.
- Fix: use one basis for both front ends: new to the prior AVSR or lip-reading population, not shown with repetition, so `standard`. Name the out-of-population precedent for each: Feng et al. 2014 as a numbered prior reference with its DOI from the paper's ref 13, and Duchnowski 1994 per F2. Reword Verdict sentence 2 to "No prior AVSR study applies a learned audio denoiser (0 of N, pattern match, Appendix); the denoiser is the audio-only design of Feng et al. [n] moved unchanged in front of the fusion".

**F8. Medium. M12 behind: the yardstick is explicit, but the count is not tied to the verdict and the slot bundles typical practice.**
- Location: M12 section, Verdict sentence 4, slots.json M12.
- Evidence:
  - "Against best comparable work" is stated, which satisfies the rule's yardstick clause.
  - The ≥3 count comes from "named held-out set 9 of 65" (8 unique). It contains [3] and [4], but not [10], whose condition is training-set GPD weights plus jackknife. This is a different condition, and the text does not distinguish it.
  - The slot cell "Gaussian noise, seen speakers, test-set tuning" reads as if all three are behind. Gaussian or white noise is as common as babble (24 against 23 of 65), and [4] itself reports multi-speaker (seen-speaker) results.
- Fix: restrict `behind` to choosing weights and depth on the test words. State "8 of 63 prior AVSR studies name a held-out tuning set (pattern match, Appendix), including [3] and [4]". Describe [10] as "weights trained on training data". Present Gaussian noise and closed-speaker testing as typical and not decisive.

**F9. Medium. Process disclaimers appear in the body.**
- Location: M06 audio ("in a whole-wiki check (Appendix)"), M06 visual ("the only hit of a whole-wiki CNN-lipreading check"), Priority bullet ("the only earlier CNN lipreading hit (Appendix)"), M06 audio SOTA ("that English, speaker-independent sentence test allows no single gap").
- Evidence: SKILL.md line 110 bans "within the wiki search"-type wording and "cannot be judged here"-type statements.
- Fix: write plain, Appendix-backed facts, for example "[6], the one earlier audio-visual denoising autoencoder (Appendix), trains ...". For the gap, state the conditions that differ (language, task, speaker independence) as facts, without saying the gap cannot be computed.

**F10. Low. The state-of-the-art lines omit conditions their sources attach.**
- Location: all four SOTA lines.
- Evidence and fix:
  - [5]: Table 3 says noisy WER across noise datasets is "not directly comparable" (LP Conformer uses NoiseX babble). Add this. "Robust AVSR now uses no denoiser" is a generalization the Appendix does not support (later: learned denoiser 12 of 274). Write "the best tabulated result uses no separate denoiser". For the audio front-end step, an audio-only figure from the same table (VIT 3D ASR 6.1% at 0 dB babble) matches the step better than an AVSR WER.
  - [7]: add "without word-boundary input, LRW training only (157 h)".
  - [9]: add "in appendix Table 13, LRS3 low-resource, 50-epoch runs". Better still, choose a protocol source whose main results carry run variability.

**F11. Low. Fairness: the authors' own disclosures are not credited.**
- Location: Test-set selection bullet and Verdict.
- Evidence: Sec. 5.3 openly states the best-over-weights selection. Sec. 8 states that "automatic selection of stream weight was not attained."
- Fix: write "The paper reports the best result over all weight pairs (Sec. 5.3) and says automatic selection was not attained (Sec. 8); the 'additional 10%' is therefore an oracle upper bound". This separates honest reporting from overstatement.

**F12. Low. The Appendix hides a manual correction.**
- Location: Appendix lipreading entry, "CNN 0".
- Evidence: the raw regex count is 1 (`oa-W3099202502`, a JSALT 2000 report whose "CNN" is the broadcaster). The audit records the correction, but the Appendix does not.
- Fix: "CNN 0 (one regex hit, the broadcaster name, removed)".

**F13. Low. The Ngiam reference note and the deep-fusion tally do not match.**
- Location: ref 6 note ("deciding prior for ... deep fusion") and Appendix fusion "deep fusion 0".
- Evidence: the body never uses [6] for fusion. [6] is outside the 65 (a missed known item). The target's own related work (Sec. 2.3) cites Ngiam 2011 and Huang & Kingsbury, ICASSP 2013 (target ref 19, a prior DBN audio-visual study not in the wiki) as deep feature-fusion precedents.
- Fix: add one Appendix clause, "deep fusion 0 in the population; outside it, [6] and Huang & Kingsbury 2013 (cited by the target)". Alternatively, drop the "deep fusion" role from the ref 6 note.

**F14. Low. Wording and restatement.**
- Location and fix:
  - Verdict sentence 1 restates the pipeline. Compress it to the changed components.
  - "hand-set weights" is inaccurate: the weights are swept and chosen per SNR on the test words. Use that wording.
  - "no per-speaker breakdown" should read "no per-speaker word results for the denoiser", because Table 4 gives per-speaker visual phoneme rates.
  - The M06 visual clause "same authors, six male ATR speakers, one CNN per speaker, 6 × 6 and PCA baselines" summarises [2]. Keep only what carries the overlap point.

## Scores

- Procedure: 6/10. The sources were read and the quotes are accurate. The concurrent-dating rule is broken in the body, the populations are not deduplicated or filtered for AVSR, and the deciding priors for the visual absence claim are missing.
- Final text: 6/10. The target numbers, test-set-selection findings and comparators check out. The central visual argument rests on concurrent work, and "unexplained" ignores a protocol difference documented in both papers.

Counts by severity: High 2, Medium 7, Low 5.
