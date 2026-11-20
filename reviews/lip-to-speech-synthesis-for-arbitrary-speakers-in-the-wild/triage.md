# Triage: Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild

Each fix in the evaluation was checked against notes.json, the source text and the topic tables. Result: 13 of 13 applied (7 correct, 6 partly correct, 0 wrong, 0 unverifiable). After the changes: check_review 0 FAIL, body 6,966 characters.

1. Correct. The M08 audit labels the 48-study design "speaker label or reference-audio speaker embedding", and the Appendix and table use that label. The M08 text now says that this design appears in 48, with 23 naming reference audio and 23 a face image.
2. Partly correct. The source does say "We choose 15 random samples from the LRS2 dataset" (Sec. 4.3), but notes.json had no quote for it. Added notes entry t105. The Verdict now reads "a listener test on 15 LRS2 samples (Sec. 4.3)".
3. Correct. The Verdict now gives the condition of the [later] test (10 LRS3 sentences of 10 s or longer, a harder test) and the successor's 3.49. Added c21 for the Table 2 column header ((A) Intelligibility). The 3.49 value was already quoted in c6.
4. Correct. M02 now calls the 72.5% to 50.7% result an ablation. M06 states that Faces-to-Voices' 30.45% uses Whisper Medium and a voice inferred from the face, while V2SFlow's 28.5% uses an audio-derived voice and another ASR (c25, c26). The M02 table cell now shows the V2SFlow 28.5% figure, as the M12 cell does.
5. Correct. The authors themselves say lip-to-text plus TTS is more accurate on words (Sec. 4.2.3). The FDSD sentence now says that FDSD ignores sync and does not score words, so closeness on FDSD is not content evidence (t107).
6. Correct. LSE-C improves (2.507 vs 1.991, Table 3). The Verdict now says the model beats the baseline on FDSD and sync but not on PESQ and STOI, and that content is unmeasured.
7. Correct. The abstract says "outperform all baselines by a large margin" (t4). The quotation in the outrun section is replaced with this wording.
8. Partly correct. The source supports both points: the KL loss appears in Sec. 3.2.3 (Eq. 1), and the ablation's encoder is "a standard speech encoder trained from scratch" (Sec. 4.2.1). Only the notes quotes were missing. Added t106 and t104. The text now names the "w/o Content Encoder" label and gives section locators.
9. Partly correct. SED is defined only as a distance between speaker embeddings, and no encoder is named (Sec. 4.1.2). The claim was reworded as "not shown to be independent" in the Verdict and marked "(inference)" in M08 (t108). The test-time reference is now located at Sec. 3.2.4 (t96).
10. Partly correct. "L1" is supported by Sec. 4.2.1 ("only L1 reconstruction loss"). Added t103 and the locator. The wording is kept.
11. Partly correct. The absences are recorded (t87 seeds/variance, t85 test sizes), and Table 4 has 7 systems on 4 criteria (t47, t49-t55). Locators were added: Sec. 4.2.3, Table 3 caption, Sec. 4.3 and Table 4.
12. Correct. DiffV2S is ICCV 2023 (wiki CVF record; DOI 10.1109/ICCV51070.2023.00618, pp. 6692-6701). V2SFlow is ICASSP 2025 (Crossref DOI 10.1109/ICASSP49660.2025.10889780). refs.json was updated and the references and .bib were rebuilt.
13. Correct. LipVoicer (ICLR 2024, [later]) reports a WER of 21.4% on LRS3 and 17.8% on LRS2 with lip-read text guidance under a different ASR (Tables 3-4; c22-c24). It was added to M12 State of the art, the M12 audit read_fulltext, the Appendix and the references. The read count is now 9 for this review, so the gate gives a WARN only.

Also changed: the M12 verdict now says "on protocol; no deficit is measured", verdict.json was regenerated, the row fields were updated through fix_row.py, and claims.md was remapped (45 rows, none flagged).
