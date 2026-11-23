# Triage: NaturalL2S (arXiv:2502.12002)

Date: 2026-11-23. Input: `naturall2s-end-to-end-high-quality-multispeaker-lip-to-speech-synthesis-with-differential-digita.eval.md` (fallback evaluator, claim table only), 11 required fixes. Findings were checked against notes.json and, where needed, the source passages: NaturalL2S Sec. V-B and Table III; SLD-L2S Table 1 and Results and Discussion; Mira et al. Sec. IV; the LightL2S abstract; and the M06 and M07 topic audits.

Result: 7 correct, 4 partly correct, 0 wrong, 0 unverifiable; 11 of 11 applied.

| # | Finding | Verdict | Evidence | Where applied |
|---|---|---|---|---|
| 1 | The "excludes LipVoicer" bullet is contradicted by the review's own quality numbers | correct (applied) | LipVoicer DNSMOS 3.11 against 3.23 (l1, t41); [later] naturalness 2.51 against 3.54 (s4, s9). The gap is WER (21.4% against 30.4%), not quality. | "Where the claims outrun the evidence", bullet 3 rewritten: the quality claim holds against LipVoicer, and the omission hides intelligibility. |
| 2 | M07 Appendix bin lists DiffV2S as "no speaker embedding stated" | partly correct (applied) | The contradiction is real. But the bin is a full-text pattern count of studies that state reference audio is unnecessary (`no_speaker_embedding_claimed`), and a study counts under every design it names. So DiffV2S stays in the bin and the tally is not changed. | Appendix M07 bin relabelled "reference audio stated as unnecessary 2 (the target, and DiffV2S, whose embedding is video-derived)". The M07 text now says the verdict rests on DiffV2S needing no reference audio. |
| 3 | "Without statistical tests" is wrong because Table III gives intervals | partly correct (applied) | The ± values are standard deviations, not intervals: "Table III reports the MOS scores and standard deviations" (Sec. V-B, t66). No significance test or interval appears anywhere (t62). The wording was still too terse. | M12 "Usual approach": "a 15-listener test with MOS standard deviations, but no confidence intervals or significance tests (Tables I–IV, §V-B)". |
| 4 | "Single-run" (M06) and "One run" (M03) are unsupported | correct (applied) | The paper gives no seeds or run count (t58). It does not say there was one run. | M06 text: "with no run count or seeds stated". M03 `choice` in slots: "Runs not stated; GT F0 in training". Row `limitations` changed to match (fix_row.py). |
| 5 | Name the [concurrent] DDSP study; harmonic-plus-noise vocoders are not new | correct (applied) | The M06 joint-training audit lists LightL2S (Interspeech 2025, same group) and four 2008–2015 harmonic-plus-noise studies. The LightL2S abstract states a DDSP vocoder (new entry g1). | M06 text names LightL2S [7] and the four earlier studies; novelty is narrowed to a differentiable prior trained with the vocoder. New reference with DOI. Appendix entry names it. |
| 6 | Summary table: M07 row label and M12 state-of-the-art cell | partly correct (applied) | The M07 row label "Lexicon and LM" is the fixed slot name printed by the shared renderer (spec slot "use-time lexicon and auxiliary information"), so it was not changed. The M12 cell "[5] (2026): re-score" did not match the text. | M12 `sota` in slots: "LipVoicer (2024): LRS3 WER 21.4%". |
| 7 | Give SLD-L2S's own LRS3 row | correct (applied) | SLD-L2S Table 1: Proposed LRS3 WER 30.22% with a reference speaker embedding; its authors state "LipVoicer achieves the lowest WER" (new entries s11, s12). LipVoicer remains the state of the art on WER. | M06 "State of the art": "SLD-L2S itself reaches 30.22%". |
| 8 | Attach the ASR condition to LipVoicer's 21.4% in the Verdict | correct (applied) | LipVoicer scores WER with the ASR of Ma et al. (2023) (Sec. 5.1, l3). | Verdict: "21.4% under its own ASR". M12 "State of the art": "with its own ASR". The one-ASR pair is kept in M06 and M12 to stay within the length limit. |
| 9 | The Verdict should credit the authors' own WER concession | correct (applied) | The authors concede "slightly higher WER scores compared to the Lip2Speech Unit" (§V-B, t9). | Verdict sentence 4: "as the authors concede (§V-B)". The duplicate clause in bullet 3 was removed. |
| 10 | Claim-table rows lack quotes for four statements | correct (applied) | Notes already held t31–t34 and t43–t44 (the other two systems), t13 (supplied samples), t30 and t66 (pooling), and t26 (§IV-D). | Claim row 3 now maps all four systems. Rows 44–46 were added for the supplied samples, MOS pooling and §IV-D, since those sentences have no number or citation and are not extracted by the script. |
| 11 | Make the "first attempt" rebuttal precise | partly correct (applied) | Mira et al. use LRW, "(500 words, ...) uttered by hundreds of different speakers" (new entry m3); Facetron uses 33 GRID speakers (f2). The proposed residual novelty (sentence-level joint training on LRS2/LRS3) was not adopted. Other joint-training hits in the audit (for example arXiv 2306.15464 on LRS3) were not read, so that claim would not be supported. | Verdict: "on word-level LRW and 33-speaker GRID ... fails as worded". M06 text: "LRW (500 words, hundreds of speakers)". |

## Reruns

- Steps 6–8 were rerun after the edits: render_review, build_refs, fill_row, then fix_row.py, check_review, verify_quotes and audit_tally (all four audits). The reviews.jsonl input came from origin/main of the review repository.
- Gates: check_review 0 FAIL, 1 WARN. The WARN (17 papers read in full besides the target) comes from the reused published M06 and M12 tables. verify_quotes: 107 found, 0 missing, 11 unchecked. audit_tally: all four pass.
- Topic tables: the M06 and M12 tables are the published ones, with their published tallies unchanged. The M12 audit was brought up to the current published table by appending the entries published since (one review's tallies and two `read_fulltext` entries). Nothing was removed.
- Body: 6,999 characters (limit 7,000). Four sentences were shortened to make room.
- New notes entries: s11, s12, m3, g1. New reference: LightL2S (DOI 10.21437/Interspeech.2025-1478).
- claims.md was regenerated (43 claims plus 3 rows added by triage) and every mapping refilled, with no "?" left. compact.md was regenerated.
- `verdict.position` follows the revised Verdict. `verification_status` in extra.json records the triage and the open items.

## Not acted on (outside the required fixes)

- Claim check 12: "instead" in the M06 usual-approach line is slightly loose. The verdict is unaffected, so the line was kept.
- Claim check 16: whether 2025 video-to-speech systems report a lower LRS3 WER than LipVoicer is unverified. The item is recorded in `open_items`.
- Claim check 21: "cannot rank systems" was shortened to "a ceiling (inference)" to save length. This also answers the evaluator's point about over-wording.
