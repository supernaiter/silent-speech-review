# Triage of the evaluation: RESOUND review

Date: 2026-11-23. The ten required fixes were checked against notes.json and, where needed, against specific source passages in the wiki.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied (partly) | vid2voc (Michelsanti et al., Interspeech 2020, wiki `isca-michelsanti20-vid2voc`, first public 2020-04, prior) predicts F0, voicing, aperiodicity and spectral envelope from silent video for WORLD: "we predict all the vocoder features (not only SP) directly from raw video frames" (Sec. 1). Le Cornu & Milner (TASLP 2017, `doi-10.1109-taslp.2017.2716178`) generate F0 and aperiodicity artificially ("Speech excitation information is not available from the visual signal"), so they are not a closer prior and are not cited. | Verdict sentence 2; M06 evidence paragraph; Appendix M06 read list; M06 audit (read_fulltext prior, deciding-priors note); notes mi1, mi2 |
| 2 | applied | Auto-AVSR [22] is the L2T model (Sec. 2.2.1, w1) and the WER scorer (Sec. 3.2, t48). The cross-paper part was not applied: LipVoicer scores with the ASR of Ma et al. (2023) and SLD-L2S with AUTO-AVSR (n_l3, n_s6), the same family. | M12 evidence paragraph, first sentence |
| 3 | applied | 28.55 against 17.04 on LRS2 (t31, t30) contradicts "matches the field's best" across both datasets. | Verdict sentence 4 split into LRS3 level / LRS2 behind |
| 4 | applied | No quote shows how Intelligible L2S gets speaker identity at inference; LipVoicer uses a face image and mouth video (lv1). | Verdict sentence 5 narrowed to LipVoicer |
| 5 | applied | RESOUND follows [27] (t9), which is SVTS (w14); V2SFlow uses the SVTS unseen-speaker split (v4). | M12 usual-approach line; author question narrowed to AV-HuBERT pre-training |
| 6 | rejected (as a fix), stated | V2SFlow also computes SECS with Resemblyzer (v5), so the values share an encoder. The shared encoder is now stated. | M07 state-of-the-art line |
| 7 | applied | Table 2 header "Naturalness↑Intelligibility↑ Similarity↑" (w15). | M07 evidence ("Similarity column"); claim row 20 |
| 8 | applied (claim table) | "Table 2 presents the MOS results along with their 95% confidence intervals." (t49) | Claim row 23 mapping |
| 9 | rejected / unverified | The M06 state of the art stays on LRS3 WER, the metric of the published M06 topic table and of the target's own comparison. AlignDiT (arXiv 2504.20629) is not in the wiki index at commit 730b0b4, so its values remain unverified. | none; noted in verification_status |
| 10 | rejected | The row label is the fixed spec slot name rendered by render_review.py (M07 = use-time lexicon and auxiliary information, which covers the prompt and lip-reader text); the same mapping is used in the published reviews. | none |

Counts: 7 applied (two of them partly or claim-table only), 3 rejected (one of these unverified). Gate after rewrite: 0 FAIL, 1 WARN (papers read count inherited from the published topic tables).
