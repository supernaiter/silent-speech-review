# Triage: SLD-L2S review

Date: 2026-11-23. Input: `sld-l2s-hierarchical-subspace-latent-diffusion-for-high-fidelity-lip-to-speech-synthesis.eval.md` (fallback evaluator, 12 required fixes). Each finding was checked against the wiki source text of the paper concerned, and only for the passage it needs.

Result: 12 findings; 6 correct, 4 partly correct, 2 wrong, 0 unverifiable. 10 applied.

| # | Finding | Verdict | Evidence | Where applied |
|---|---|---|---|---|
| 1 | Claim-table quotes do not hold the values for 27.55, 20.62, 0.618, 30.70, 29.70, 0.627/0.588/0.628, 4.36, 3.65/3.77/3.69/3.90, 4.2885/29.99 and "1 NFE" | correct, applied | All values are in the target's Tables 1-3. The earlier quotes held only the first cell of each row. | notes.json: full-row quotes for t33-t39, t44, t46-t51; new t76 (ground-truth MOS 4.36) and t77 (57.7M vs 57.8M); claims.md rows 5, 12, 16, 17, 19, 20, 22 |
| 2 | ImaginTalk [3] may be continuous, not discrete | wrong, rejected | ImaginTalk formulates generation "as a discrete token diffusion process using" RVQ, with 12 RVQ levels and codebook size 1,024 (its Secs. 1 and 4.4). The "discrete" description and the n=1 count stand. | Not applied. The c10 quote was replaced with the explicit sentence so the claim table shows the evidence. |
| 3 | Faces-to-Voices and HiCoDiT numbers lack dataset, column and "video alone" context | correct, applied | Faces-to-Voices Table 2 header gives LRS3-TED first, then UTMOS, DNSMOS, RMSEf0, WER. The HiCoDiT Table 1 caption says LRS3 and defines the A/V columns; its own row is A no, V yes; the dagger marks models not trained on LRS3. | notes.json c8 (row quote), new c15, c16, c17; M06 text now adds "without LRS3 training" for HiCoDiT; claims.md rows 4, 8, 9, 10 |
| 4 | "Cited but missing from Table 1" is unsupported; t74 quotes V2SFlow | correct, applied | The target's related work says "More recent works, including V2SFlow ... and From Faces to Voices (Kim et al. 2025) introduce flow matching". Faces-to-Voices is not among the Table 1 baselines. | notes.json t74 quote, text and location; claims.md row 4 |
| 5 | M07 is "Lexicon and LM", so a speaker embedding is the wrong slot | wrong, rejected | Slot M07 is "use-time lexicon and auxiliary information" (spec v2.1, slot notes). A reference-audio speaker embedding supplied at inference is use-time auxiliary information. The table header is the renderer's short label. | Not applied |
| 6 | M12 verdict differs between section and table | partly correct, applied | Both already gave `standard`. The qualifier "not in the conclusions drawn" read like a second verdict value. | M12 section: "Verdict: standard; the overreach is in the conclusions (next section), not the protocol." |
| 7 | Add the pretrained codec decoder and the re-scored baselines as confounds | partly correct, applied | The X-Codec decoder is pretrained on LibriSpeech (target, Implementation Details). Whether the decoder raises UTMOS is not tested, so this is stated as inference. Re-scoring is supported: the target computes WER with AUTO-AVSR, and its ground truth scores 0.71% WER against 2.5% in V2SFlow's Table I. The baselines were re-scored with that ASR (inference). V2SFlow scores 27.55% in the target's table and 28.5% in its own. | Verdict sentences 2 and 6; M12 section (new sentence on AUTO-AVSR and ground-truth WER); claims.md rows 2, 6, 18 |
| 8 | NaturalL2S and Intelligible do not contradict a claim about diffusion methods | partly correct, applied | The point is fair as framing. Their architectures were not re-read, so the review now states only their one-step NFE (Table 1). | Efficiency bullet: the claim "holds within Table 1 but omits the cited 10-step Faces-to-Voices; 10 NFE remains ten times the one-step Intelligible and NaturalL2S" |
| 9 | Quote both Table 3 "w/o Lsem" rows | correct, applied | Table 3 has "w/o Lsem" with 4.1859 ... 0.795 and again with 4.2507 ... 0.771. | notes.json t49, t51; claims.md row 21 |
| 10 | Locate the absence claims (unseen speakers; no comment on scores above ground truth) | correct, applied | The Datasets section names only "pre-defined splits for training, validation, and testing". The results discussion says the model "substantially outperforms all baselines ... in the reference-free quality metrics" and does not mention ground truth. | M12 text names the Datasets section and the results discussion; claims.md rows 14, 17 |
| 11 | V2SFlow year differs: 2024 in the text and table, 2025 in the reference | partly correct, applied | Not an error: 2024 is the first-public arXiv month (2024-11) and 2025 is the ICASSP publication. The label was ambiguous. | M12 State of the art and table now read "arXiv 2024"; the reference keeps ICASSP 2025 |
| 12 | M13 "Step count only" ignores the reported training hardware | correct, applied | Training on one H100 for about five days is reported (Implementation Details). Inference runtime is not. | slots.json M13 choice "Training compute; no runtime", note "Efficiency claimed without inference runtime"; Verdict sentence 6 |

## Other observations

- The evaluator notes NaturalSpeech 2 as a text-to-speech precedent for continuous codec latents. The target cites it as its inspiration (Related Work, Neural Audio Codec), and the review makes no novelty claim for the design. No change; recorded in `verification_status`.
- Row field `en.limitations` said "WER worse than baselines". In Table 1 the target's WER is better than DiffV2S and NaturalL2S, so it now reads "LRS3 WER trails V2SFlow, LipVoicer and Intelligible in its own table" (via `fix_row.py`). The other legacy fields were already English and agree with the revised review.

## Gates after triage

- `check_review.py`: 0 FAIL, 1 WARN (15 papers read in full besides the target). The count comes from the `read_fulltext` entries of the two reused published topic tables. This review read 5 papers.
- `verify_quotes.py`: 73 found, 0 missing.
- `audit_tally.py`: both audits pass. The topic tables are unchanged: every published entry is kept and this review's entries are only appended.
- Body: 6,656 characters.
