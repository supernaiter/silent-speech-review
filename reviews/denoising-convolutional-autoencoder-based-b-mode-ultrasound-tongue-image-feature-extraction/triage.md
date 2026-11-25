# Triage of the evaluation (11 findings)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Code notes t53 (directory split, first 10 directories train) and t56 (validation data scored as test) contradict the "neighbouring frames" inference; t4 gives the paper's "randomly selected". | M12 body: neighbour inference replaced by the text/code disagreement and the validation-as-test finding; M11 note; row evaluation_limits. |
| 2 | applied | t34/t42 (0.41 at length 60), t35/t43 (0.21 at length 30). | Verdict, M06 verdict line, M12 state-of-the-art line (now matched-length), first claims bullet, verdict.short, slots M06 note, row position_in_field and key_result. |
| 3 | applied | No run count in the paper (t44: no seeds or repetitions reported); non-integer error counts may mean averaging. | Verdict ("number of runs not reported"), M06 and M12 verdict lines, claims bullet, M12 table cell, row fields; averages question kept. |
| 4 | applied | k4: 18.7 is CER without SpecAugment (Table 1); best WER 20.5% (k5, Table 2) with a 65k LM (k2). | M07 state-of-the-art cell set to "-" with the condition in the note; M06 state-of-the-art line says "best is 20.5% WER" with the 65k LM. |
| 5 | applied | t62 ("competitive results [12, 13]", Sec. 1) and t63 (reference [13] = Jaumard-Hakoun 2016). | Claims bullet 2 now names reference 13 and its use in §1. |
| 6 | partly applied | M12 tally: "Li 2019" in the published note is this paper (the published table's target was Ji et al.); the 8 candidates contain no second version of the target, so no double count. ICASSP 2019 version: not in the wiki, unverified, kept in verification_status; review cites arXiv v1. Tatulli and Hueber 2017 is in the wiki (icassp2017-tatulli-multimodal-cnn-vsr), read (Abstract, Sec. 3.1): supervised CNN features from raw tongue ultrasound and video, uncited by the target. Xu et al. 2017 not in the wiki: unverified. | "First" restricted to the combination of denoising and a convolutional autoencoder (Verdict, M06, claims bullet); Tatulli added as deciding prior in M06 text, Appendix and audit read_fulltext; refs.json. |
| 7 | applied | Same as 6 (Tatulli prior). | As in 6. |
| 8 | rejected | Optional; other-corpus numbers (TaL1 3.42%) are not comparable and the body limit leaves no room. | - |
| 9 | applied | Claim 6: Hueber quotes c17/c18 plus audit; claim 13 (now 12): t44 for the noise; claim 17: SSR7000 quote s1 added; claim 25: t64 quotes "K = 60 and 30". | claims.md regenerated and refilled; notes entries t62-t64, a1-a3, k4-k5, s1 added (verify_quotes: 89 found, 0 missing). |
| 10 | applied | Same as 4: 18.7% is a CER. | As in 4. |
| 11 | applied | t17 ("except with DCT"). | DCT bullet now says the authors flag the exception without explaining it. |

Counts: 10 applied (one partly), 1 rejected, 0 unverified findings left open in the text; ICASSP-version venue and Xu et al. 2017 recorded as unverified in verification_status.
