# Triage of the independent evaluation (2026-11-27)

Evaluator: a language model separate from the writer. 18 required fixes (High 3, Medium 9, Low 6). Applied 17, partly applied 1, rejected 0. No verdict changed: M06, M03 and M12 stay standard and M13 stays not reported.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Whisper-Flamingo arXiv v1 (2024-06-14) and the Interspeech version (wiki isca-rouditchenko24_interspeech) have only the 433 h AVSR row (1.5%). The 0.76/0.86/0.68 rows appear in the November 2024 revisions (v3 dated 19 Nov 2024, notes c27), after the target's v1 (2024-09). | Verdict sentence 4; M12 State of the art (Whisper-Flamingo line removed); claims bullet 2 reframed as later rows the 2025 revision did not add; Question 2; reference [3] note |
| 2 | applied | WF v3 Table 3: 0.76% is clean-trained at beam 1 (1.8% at beam 15, c29); noise-trained gives 0.86% (c9). The target trains with babble and decodes with beam 15 (t46, t58). | Verdict: the VSP-LLM(FT) omission is now the clearest overreach, and the 0.77% is stated to lead the noise-trained row; claims bullet 2 |
| 3 | applied | MMS-LLaMA Table 1: the 0.72% row is "Whisper AV-HuBERT LLaMA 3.2 3B 1759" (c24). | M03 State of the art; notes c13/c20 corrected; M03 audit |
| 4 | applied | WF v3 Table 3 has noise-trained greedy ASR rows 1.1/0.85 (c26); the 2.3% row is noise-trained with beam 15 (c10); the target samples SNR including clean, uses Whisper-medium and temperature 0.6 (t46, t58). | M03 paragraph: "close to", rows marked as November 2024, noise-trained greedy row added |
| 5 | applied | Target ref. [39] is "Robust speech recognition via large-scale weak supervision" (t144); 680k h (c12); LP Conformer 100K h (t91). | M03 paragraph |
| 6 | applied | New family counts over the same 407 prior studies (tools/m06_families_2024-09.json): HMM 180, CTC 146, attention 136, transducer 80, hybrid 55. "Trained end to end" dropped. | M06 Usual approach, Verdict sentence 2, slots M06 (matched 146), audit usual_approach_<slug>, Appendix |
| 7 | applied | The regex matches "end-to-end" as an architecture term. | M03 Usual approach ("mention ... upper bound"); audit design label; slots field |
| 8 | partly applied | The target places itself after LLM-ASR [31]-[35] (t143) and names VSP-LLM as the only prior LLM-based method (t8); VSP-LLM merges tokens by unit deduplication (c7). The LLM-ASR papers are outside the VSR/AVSR ledger and were not read, so they are described through the target's citation and not added as references. | Verdict sentences 2-3 (credit, novelty = one frozen LLM for audio, video and both); M06 paragraphs |
| 9 | applied | The M12 state of the art is now protocol: USR 2.0 reports LRS3 low-resource AVSR WER as mean ± SD over three seeds, 2.9 ± 0.1 (c21; published table quote). | M12 State of the art; slots M12; audit state_of_the_art_<slug> (accuracy frontier kept as a separate field) |
| 10 | applied | DoubleHelix freezes Whisper-medium and AV-HuBERT Large and uses LoRA on LLaMA-3.2-3B (c22, c23), 0.68% (c15). | M03 State of the art; MMS-LLaMA kept as [concurrent]; slots M03; M03 audit |
| 11 | applied | DLLM-VSR Table 1: 21.9% with AV-HuBERT (1,759 h) and 19.4% with USR 2.0 (3,305 h) (c25, c17). | M06 State of the art |
| 12 | applied | 30 h: 28.4 vs 29.8 (t64, c6); VSP-LLM(FT) also trains translation and uses beam 20 (c4, c30). | Claims bullet 1; Verdict uses "closest configuration" |
| 13 | applied | Sec. III-B states the 0.79 to 0.77 reduction (t119). | M12 verdict line credits the authors |
| 14 | applied | ViT3D-CM 1.6% at 90K h (t90), LP Conformer 0.9% at 100K h (t91). | Claims bullet 3 |
| 15 | applied | WF v3 Table 3 tabulates Llama-AVSR (target v1) ASR 0.81% at 1,759 h (c28). | M12 verdict line |
| 16 | applied | Rank-64 LoRA on the video encoder for VSR (t36). | M03 Usual approach; slots M03 choice |
| 17 | applied | M12 audit: 51 prior LRS3 AVSR studies, 9 with a variability hit. | M12 Usual approach; audit |
| 18 | applied | Duplicate chronology tags came from refs.json notes; WF values come from v3; DoubleHelix is a preprint v1. | refs.json notes; References |
