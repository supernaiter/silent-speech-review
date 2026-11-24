# Triage of the independent evaluation (12 findings)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | The three GRID listener-test priors fit only GRID. Lip2Wav (arXiv 2005.08209, Sec. 6.3.2) was read: 15 raters, single-speaker open-vocabulary data. The multi-speaker LRW baseline (end-to-end GAN, arXiv 2104.13332) reports no listener test. No earlier multi-speaker LRW/LRS3 prior read meets the condition, so the behind rule is not met for the main settings. The 85% result was dropped from the basis. | M12 verdict changed from behind to standard (section, slots, extra.json); Lip2Wav added as a reference; Verdict sentence on M12 removed |
| 2 | applied | LipVoicer Sec. 5 and 5.1, Tables 2 and 4: SVTS files were supplied by the SVTS authors; LRS3 WER 82.4% (LipVoicer 21.4% in the same table); intelligibility MOS 2.17 (LipVoicer 3.44); 16 annotators per sample. | Verdict, M06 state of the art, M12 state of the art, claims section; notes l1–l6 |
| 3 | applied | V2SFlow Sec. III-B compares against ground-truth text labels (r3_13); SVTS Sec. 3.4 uses the real-audio transcript; neither later paper names the SVTS checkpoint in the passages read. | Claims section, bullet 1 |
| 4 | applied | LipSound2 Abstract names VoxCeleb2 in the same sentence; quote extended. | notes w1 |
| 5 | applied | Target Sec. 3.1: "for this corpus we generate the speaker embeddings using the audio clip from the corresponding video", which the authors call consistent with earlier LRW work [32]. | notes t12, t74; M07 text credits the authors' reason |
| 6 | applied | The quoted sentence ends the LRW paragraph of Sec. 4.1. | Claims bullet 2 now tied to LRW (larger LRW model, Table 1; own-clip embedding, Sec. 3.1) |
| 7 | applied | Table 4: "w/o Spec. Conv. 1.97 0.705 0.523 2.90" against "L1+Spec. Conv. 1.97 0.705 0.523 2.36". | Claims bullet 4 |
| 8 | applied | Table 2 caption (no LRS3 WER) and Sec. 3.4 (objective metrics do not match perception) are the authors' own caveats. | Verdict ("as the authors note"), M12 usual-approach paragraph |
| 9 | applied | Kefalas et al. share an author (Pantic) with SVTS. | Verdict: "when the same group re-scores them" |
| 10 | applied in part | Whole-system comparison noted. The recognizer-overlap concern is rejected: LipVoicer Sec. 5.1 uses "a different ASR (Ma et al., 2023) to evaluate the WER" (r4_02). | M06 state-of-the-art line ("both replace the whole generator, so this is not a vocoder gap") |
| 11 | rejected | Row labels are the fixed slot names inserted by render_review.py; section headings name the topic. | – |
| 12 | rejected | The audit state-of-the-art records and sota candidates (M06, M02, M12 published tables) list no LRS3 WER below LipVoicer; the lowest is LipVoicer re-scored at 20.62% in a [later] 2026 table, the same system. | – |

Counts: 10 applied (one in part), 2 rejected, 0 unverified.
