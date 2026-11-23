# Triage: LipDiffuser (arXiv:2505.11391)

Date: 2026-11-23. Input: `lipdiffuser-lip-to-speech-generation-with-conditional-diffusion-models.eval.md` (fallback evaluator, claim table only), 7 required fixes. Each finding was checked against the target source text (v3) and, where needed, against the comparator passages (Kefalas et al. Sec. IV and Tables V, VII; V2SFlow Sec. IV-B and Table I; Faces-to-Voices Sec. 4.4 and Table 2).

Result: 4 correct, 3 partly correct, 0 wrong, 0 unverifiable; 7 of 7 applied.

| # | Finding | Verdict | Evidence | Where applied |
|---|---|---|---|---|
| 1 | Cross-dataset absence rests on "We begin with in-domain results" | partly correct (applied) | The whole v3 text was checked. Sec. 5 has three results only: Table 1 (LRS3-CHiME3, -10 dB), the listening test (Fig. 1, LRS3-CHiME3 samples at -10 dB) and WER over input SNR (Fig. 2). No cross-dataset or enrollment-scenario result appears, so the absence holds. The evaluator's guess that "begin" means more results follow is wrong. The weak support is real. | Notes t50 restated with the Sec. 5 contents; new entry t61 (Fig. 2 sentence). "Where the claims outrun the evidence", bullet 1, now names Table 1 and Figs. 1-2. Claim rows 6 and 23 remapped. |
| 2 | Quality-lead sentence omits NISQA below the clean reference and the SD yardstick | correct (applied) | Table 1: NISQA 4.57 for LipDiffuser against 4.65 for Clean; the DNSMOS gap of 0.08 is smaller than either SD (0.30, 0.36). | Verdict sentence 3 rewritten: quality matches the clean recordings rather than exceeding them. `verdict.position` and the row fields `axes_moved` and evidence 9 changed to match (fix_row.py). |
| 3 | M06 state of the art (Faces-to-Voices 30.45%) not reconciled with V2SFlow 28.5% | correct (applied) | Faces-to-Voices computes WER with Whisper Medium (Sec. 4.4). V2SFlow uses the conformer recognizer of Ma et al. [40] (Sec. IV-B). DiffV2S scores 41.07% in the Faces-to-Voices Table 2 and 39.2% in the V2SFlow Table I, so the two scales differ. | One sentence added under M06 "State of the art". New notes entries v4 and f5. Slot M06 `sota` names Whisper Medium. |
| 4 | Kefalas numbers lack column header, split labels and the meaning of "basic fine-tuning" | correct (applied) | Table VII is "GRID (33 speakers, unseen)" and Table V is "GRID (33 speakers, seen)", both with a WER (%) column. Sec. IV defines basic fine-tuning as initializing the decoder and discriminator from the pretrained A2A-WaveGAN. | M02 "State of the art" sentence names the 33-speaker split, the initialization and the frozen decoder. New notes entries k4, k5 and k6. |
| 5 | "Within one standard deviation" for WER; the authors call it comparable | partly correct (applied) | The authors do say "comparable WER and LPS" (Sec. 5), and Table 1 gives SDs of 0.33-0.35 with no interval or test. The evaluator's "per-utterance SD" is not stated in the paper: notes t48 records that the unit of the SD is not given. So that part was not adopted. | Verdict sentence 5 credits the authors' "comparable" and states the SDs with no interval or test. Row evidence 10 changed to match (fix_row.py). |
| 6 | Single-table and no-ablation claims cite the pretraining quote | partly correct (applied) | Table 1 is the only table in the paper, so the claim holds. But Fig. 2 is a second quantitative result: WER over SNR for SGMSE+, AV-Gen and LipDiffuser, with no ablation. The cited quote was the wrong support. | Verdict sentence 2 names Table 1 and Fig. 2. Notes t55 now quotes the Sec. 5 sentence on Table 1 and lists the checked experiments. Claim rows 2, 12 and 16 remapped. |
| 7 | Listening-test absence not shown from the Fig. 1 caption | correct (applied) | The Fig. 1 caption states only the rating task and the 0-100 scale against a reference. Sec. 4.3 gives 15 participants and randomly selected samples. No sample count, interval or test is given. | Notes t58 now quotes the Fig. 1 caption. Bullet 3 cites "Fig. 1 caption, Sec. 4.3". Claim row 25 remapped. |

## Reruns

- Steps 6-8 were rerun after the edits: render_review, build_refs, fill_row, then fix_row.py, check_review, verify_quotes and audit_tally (all three audits). The reviews.jsonl input came from origin/main of the review repository.
- Gates: check_review 0 FAIL, 1 WARN. The WARN (17 papers read in full besides the target) comes from the reused published M06 and M12 tables. This review read 3 comparators. verify_quotes: 86 found, 0 missing, 13 unchecked. audit_tally: all three pass. Topic tables were not modified.
- Body: 6,928 characters (limit 7,000). Three sentences were tightened to make room for the additions.
- claims.md was regenerated (39 claims) and every mapping refilled, with no "?" left. compact.md was regenerated from the revised review.
- extra.json `verification_status` records the triage and the open items.

## Not acted on (outside the required fixes)

- Claim check 24: the evaluator says a later journal version of Kefalas et al. may exist. This is unverified and was added to `open_items`; the reference keeps the arXiv locator.
- Claim check 9: a FiLM-style modulation in speaker-conditioned systems would not change the `standard` verdict for M06, so nothing was changed.
