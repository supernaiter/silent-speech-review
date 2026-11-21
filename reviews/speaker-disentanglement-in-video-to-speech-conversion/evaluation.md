# Evaluation: Speaker disentanglement in video-to-speech conversion

Date: 2026-11-21. Fallback evaluator (claim table only). Input: the compact review (Verdict, component sections, "Where the claims outrun the evidence", component table) and its claim table. No sources were opened. Ledger counts (slot-filled and pattern-match tallies) are taken as given and not re-audited. Judgments of my own beyond the claim table are marked (inference).

## Claim check

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target adds an identity vector or a frozen audio speaker embedding, plus adversarial losses on the lip encoder (Verdict) | CT 1: t2, t4, t21 | correct | Quotes support both inputs, the adversarial losses and the 512-to-32 projection. |
| 2 | The stripping device is Wand and Schmidhuber's inverted-gradient speaker classifier [2] (Verdict) | CT 2: p5; CT 1: t4 | insufficient evidence | p5 supports what [2] does. No quote shows that the target uses gradient reversal: t4 says only "adversarial losses", and the Table II rows quoted show "dispel MLP / dispel linear". |
| 3 | [2] is "uncited" by the target (Verdict) | none | insufficient evidence | The claim table has no row for this. A location is needed, e.g. the target's reference list or Sec. II. |
| 4 | Lip2Wav fed a speaker embedding a year earlier; the paper calls it concurrent (Sec. II) (Verdict) | CT 2: p4, t77 | partly correct | p4 supports the speaker-embedding input. The t77 excerpt does not contain the word "concurrent". t77 also shows that the authors set Lip2Wav apart because it uses no disentanglement. |
| 5 | The claim to be first with voice control and unseen identities (Abstract) fails (Verdict) | CT 1–2 | wrong as stated (stronger than the evidence) | The table does not quote the target's "first" sentence. [2] is lipreading (recognition), not synthesis. [3] has no disentanglement, which is the distinction the authors draw themselves (t77). The evidence shows that each part of the design has a precedent. It does not show that the combined claim fails. |
| 6 | EER is scored with the same embedding network that conditions the SE models (Verdict; Where the claims outrun the evidence) | CT 20: t83, t21 | correct | This is a well-chosen confound, quoted with its location. |
| 7 | Seven of 18 speaker-conditioned Table II rows exceed the 41.9% baseline WER, so "all these variants maintain or improve the content intelligibility" is wrong (Verdict) | CT 3, 21: t27–t33, t42, t79 | partly correct | The six SI rows (42.7–50.2) and SE-norm dispel-MLP (49.6) do exceed 41.9. The total of 18 rows and the wording of the conclusion are not visible in the quoted excerpts. The comparison uses B (41.9) as the reference. Compared with the matched non-adversarial variant, the result is worse still for SE with frame dropping (31.2 rises to 41.9), so the point is stronger than stated. Labelling a table count "(inference)" is an unnecessary hedge. |
| 8 | 20 of 42 pattern-match studies compute the speaker embedding from reference audio (M03 identity) | CT 4 (audit) | correct (ledger) | This is plausible as the typical design. |
| 9 | Lip-derived speaker vectors [4] and x-vector conditioning [5] [concurrent] "came earlier" (M03 identity) | CT 6 | contradiction | [5] is labelled concurrent and is then presented as prior work. TaL (arXiv Nov 2020, SLT Jan 2021) falls within 6 months of the target. |
| 10 | V2SFlow raised LRS3 unseen-speaker SECS from 0.587 to 0.664 [6] [later] (M03 identity SOTA) | CT 7 (audit) | correct (audit only) | No source quote is in the table. The condition behind 0.587 (which ablation) should be named. |
| 11 | 6 of 18 adversarial or disentangling studies use gradient reversal (M03 adversarial) | CT 8 (audit) | correct (ledger) | This is plausible. |
| 12 | [2] learns "to confuse speakers", gaining about 40% relative accuracy between speakers | CT 9: p5, p6 | condition missing | p6 reads "a relative accuracy improvement of around 40% with only 15 to 20 seconds of untranscribed target speaker data". The gain comes from adaptation with untranscribed target-speaker data. This condition has to be stated. |
| 13 | ZS Lip2Speech: EER 36.72% against 43.13% without the split, on 13 unseen GRID speakers [7] | CT 10: p7, p8, p9 | wrong / no quote | 36.72 does not appear in the quoted Table 1 rows. The "Proposed" row has 26.57 in the column where "Proposed-VAE" has 43.13. Either the value or the column is wrong. p9 supports the 13 unseen speakers. |
| 14 | SE with frame dropping: dispel-MLP takes EER from 48.6 to 7.1 (85% relative) and WER from 31.2 to 41.9 (34% relative) | CT 11: t35, t36 | correct | The arithmetic checks out (85.4%, 34.3%). It is plain arithmetic, so the "(inference)" tag is not needed. |
| 15 | SI EER stays at 6.8–7.5% against 7.1% without removal | CT 12: t29–t33 | correct | Row 3 (6.9) also falls inside the range. |
| 16 | 48 of 93 studies set the voice by speaker label or reference-audio embedding (M08) | CT 13 (audit) | correct (ledger) | This is plausible. |
| 17 | DiffV2S: voice-match MOS 3.91 on LRS3 unseen speakers [8] (M08 SOTA) | CT 14 (audit) | insufficient evidence | The table has no source quote. It needs to confirm that 3.91 is the voice-similarity MOS and not naturalness. |
| 18 | Row 10 is the most intelligible system in the listening test (word accuracy 73.7) and has the lowest similarity (33.5 against 99.3 for real speech) (M08) | CT 15: t54 | partly correct | The pairing (third system: 33.5 / 73.7; real speech: 99.3 / 93.2) and the minimum are consistent. The mapping to Table II row 10 is not in the quote. |
| 19 | 78 / 65 / 52 / 2 of 165 studies (listener test / WER / unseen speakers / repeated runs) (M12) | CT 16 (audit) | correct (ledger) | — |
| 20 | The paper reports one run without seeds (M12) | CT 23: t68 | insufficient evidence | t68 describes random hyperparameter search on validation. It does not show a single run. |
| 21 | V2SFlow 28.5% WER on LRS3 [6]; Lip2Wav 14.08% on 4 seen GRID speakers [3] (M12 SOTA) | CT 17: p1, p2 | numbers correct; SOTA questionable | Lip2Wav (2020) predates the target, so it cannot be the current state of the art for GRID. Later GRID video-to-speech work exists, for example VCA-GAN (Kim et al., 2021) and end-to-end GAN V2S (Mira et al., 2022). Their GRID WERs should be checked, ideally on the unseen-speaker split this paper uses (inference, not verified). On LRS3, check later systems such as LipVoicer (Yemini et al., ICLR 2024) against 28.5% (inference). |
| 22 | Table I omits Lip2Wav; Lip2Wav's WER is under Google ASR, not the paper's Kaldi model with GRID grammar (2.8% on real speech) | CT 18: p1, p3, t12, t17 | partly correct | Google ASR (p3) and B-spk 17.8 (t12) are supported. No quote shows the omission, the Kaldi grammar or the 2.8%. |
| 23 | Table II row 1 gives the GAN 41.9%, identical to B and without the recompute mark; the GAN paper reports 40.5% on 10 held-out subjects [9] | CT 19: t26, t27, t84, p11, p12 | partly correct | The 41.9 / 41.9 and the dagger rule are supported. The p11/p12 text (40.5%, 10 subjects) is not shown. |
| 24 | "Best results in terms of PESQ and WER" (Sec. IV.A) holds for WER only without Lip2Wav | CT 22: t14, p1, t11 | no quote / contradiction | The quoted t14 reads "competitive results", not "best results". Under M12 the review itself says the WERs are not comparable (different ASR, seen speakers). Here it treats them as a plain failure of the authors' claim. |
| 25 | M11 verdict "not reported" while "This paper" reads "GRID" (component table) | Component table | contradiction | The corpus is reported. Either the verdict or the cell is wrong. |

## Usual approach and state of the art

- The usual approaches given (audio-embedding conditioning, gradient reversal, label or audio voice control, listener test plus ASR WER) are plausible typical designs.
- The M03 adversarial SOTA (ZS Lip2Speech VAE split) uses a different technique from adversarial removal. It is acceptable as "best identity/content split", but the value is wrong (row 13).
- The M12 GRID SOTA is not current (row 21).

## Confound and position

- The strongest confound, EER measured with the training-time embedding network, is identified and handled.
- A second confound is not handled: the WER baseline. Each adversarial variant should also be compared with its own non-adversarial counterpart, not only with B.
- The Lip2Wav WER comparison is a cross-ASR, cross-speaker-set comparison. The review notes this in M12 but drops it in "Where the claims outrun the evidence".
- The novelty position (Verdict) goes beyond its evidence (row 5).

## Fairness and novelty

- [5] is concurrent but is treated as earlier work (row 9).
- [3] is 12 months before the target, so it is fair to treat it as prior work.
- For the "first" claim, a further deciding prior for adversarial speaker removal in synthesis is Chou et al., "Multi-target Voice Conversion without Parallel Data by Adversarially Learning Disentangled Audio Representations", Interspeech 2018, arXiv:1804.02812 (audio input, not video; medium confidence).

## Verdicts

- No slot is rated `ahead`.
- "not applicable" for M09/M10 is consistent.
- "not reported" for M11 contradicts the cell (row 25).

## Required fixes (ordered by impact)

1. Correct the ZS Lip2Speech EER: 36.72% is not in the quoted Table 1. Give the right value from the right column (the "Proposed" row shows 26.57 where "Proposed-VAE" shows 43.13), with its metric name.
2. Restate the novelty position. Quote the target's Abstract "first" sentence. Then say that the adversarial device [2] (lipreading) and the speaker-embedding input [3] each have precedents, without saying the combined claim "fails". Acknowledge that the authors distinguish [3] by its lack of disentanglement (t77). Consider adding Chou et al. 2018 as a synthesis-side prior.
3. Remove "came earlier" for [5], or drop the [concurrent] label. As written, they contradict each other.
4. Add the condition to Wand and Schmidhuber's 40%: it comes with 15–20 s of untranscribed target-speaker data.
5. Replace the "Best results in terms of PESQ and WER" quote with the actual wording (t14: "competitive results") or quote the right location. Carry the ASR and speaker-set caveat from M12 into this bullet.
6. In the Verdict WER point, show the conclusion sentence and the count of 18 rows in the quotes. Add the matched non-adversarial comparison (e.g. SE frame-drop: 31.2 rises to 41.9). Drop the "(inference)" tag here and in the SE arithmetic.
7. Fix M11: the verdict "not reported" contradicts "GRID".
8. Supply quotes or locations for the following unquoted statements: [2] "uncited", Lip2Wav called "concurrent", Table I omitting Lip2Wav, Kaldi grammar and 2.8% on real speech, the GAN's 40.5% on 10 held-out subjects, Fig. 3 system = Table II row 10, and "one run without seeds".
9. Show that the target actually uses gradient reversal (a Table II row or Sec. III), or describe its adversarial loss as the paper names it.
10. Update the M12 state of the art: replace or supplement Lip2Wav (2020) with later GRID results (e.g. VCA-GAN 2021, Mira et al. 2022) on a matching split. Check later LRS3 systems (e.g. LipVoicer 2024) against V2SFlow's 28.5%.
11. Name the metric behind DiffV2S's 3.91 (voice-similarity MOS or naturalness MOS) with a source location. Name the ablation behind V2SFlow's 0.587.
12. State which Table II reference each "exceeds 41.9%" row is measured against (B on unseen speakers). Note that Table I's B (21.8%) is a different test condition, so readers do not mix the two tables.

## Scores

- Procedure: 6/10
- Final text: 5/10
