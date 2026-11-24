# Triage of the evaluation (2026-11-24)

Evaluator: fallback language model over compact.md (15 findings plus claim-check rows). Each finding checked against notes.json and, where needed, the specific source passage (new notes entries s1-s8, verify_quotes 148 found, 0 missing).

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | r1, r2: Hegde et al. 2022 run lip-to-text plus TTS as a baseline (Table 3), so lip-reader text at inference predates LipVoicer; the novel part is conditioning a video-to-speech synthesizer on it (t1). | Verdict sentence 2 narrowed to "condition a video-to-speech synthesizer on lip-reader text", with [hegde2022arbitrary] as the boundary. |
| 2 | applied | SKILL.md `ahead` rule needs the effect shown; no cascade control (t83, r1); LipVoicer output WER tracks the lip reader (t40-t42). Coordinator instruction concurs. | M07 verdict ahead -> standard in Verdict, M07 section, slots.json, extra.json, verdict.json short, row position_in_field. |
| 3 | applied | All M07 numbers are LRS3. | "(LRS2, LRS3, GRID)" removed with the ahead verdict. |
| 4 | applied | r15-r17: LipAdapter scores its output with Whisper-Large; its LipVoicer row equals the target's own 21.4% (t26); re-scoring not stated in its Table 1 caption or results text. | M07 state of the art rewritten: LipVoicer itself; LipAdapter gap marked cross-evaluator (inference). |
| 5 | applied | Appendix C quote added (s7); the code-config claim (t72) has no locally verifiable code quote. | Config clause dropped from "Where the claims outrun"; App. C item kept; question kept. |
| 6 | applied | ReVISE-protocol ASR (t57) and later re-scores exist. | Verdict: "the main tables score words with an ASR from the same work as the lip reader". |
| 7 | applied | s6: Table 11 caption "Inferior ASR WER achieved by early stopping" (same ASR, less training). | M02 sentence reframed as sensitivity; contradiction framing with the "re-training" quote removed. |
| 8 | applied | s1, s2: SLD-L2S LRS3 WER column: Proposed 30.22, V2SFlow 27.55, Intelligible 27.73 (r19), LipVoicer 20.62 (r18). | M07 state of the art cites "20.62% against 27.55% to 30.22%". |
| 9 | applied | 165 minus 15 text-naming studies (audit pattern counts). | Appendix M07 adds "at least 150 name no use-time text (165 minus 15, inference)". |
| 10 | applied | s4: Hegde et al. 2023 Table 3 header "Method L2T-WER PESQ STOI ESTOI LSE-C LSE-D"; r11-r12. Absence confirmed. | M07: "report only the lip reader's WER (Table 3)". |
| 11 | applied | t1 (authors' "first" claim), s5 (authors' own ReVISE caveat). | Verdict attributes the first claim to the authors; ReVISE item attributes the 6.4%/5.6% caveat to the authors. |
| 12 | applied | r23, r46: WYS 23.73% vs LipVoicer 22.24%; no later listener-transcription test among read papers. | M02 and M12 state-of-the-art lines say plainly that no later work beats or re-tests it; slots.json M02/M07 sota cells updated. |
| 13 | applied | t60, s8 (E.5 naturalness and synchronization lapses), s5 (5.6%). | Claim table rows 26-27 and E.5 row carry quotes. |
| 14 | applied | Spec slot name M07 = use-time lexicon and auxiliary information. | Heading renamed "M07 Lexicon and auxiliary information: lip-reader text guidance". |
| 15 | applied | Duplicate labels came from refs.json notes repeating the build_refs label; "has both" ambiguous. | refs.json notes cleaned; M12 says "a listener test and ASR WER". |
| C25 | unverified | Venue updates for 2026 items and V2SFlow (possibly ICASSP 2025) not checked; refs keep the versions in the wiki. | none |

Counts: 15 applied, 0 rejected, 1 unverified (C25, bibliographic). Gate after triage: check_review.py 0 FAIL, 1 WARN (papers read counted from reused published tables), body 6,997 characters.
