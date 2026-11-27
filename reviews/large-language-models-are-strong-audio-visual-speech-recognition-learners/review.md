# Large Language Models are Strong Audio-Visual Speech Recognition Learners

Umberto Cappellazzo, Minsu Kim, Honglie Chen, Pingchuan Ma, Stavros Petridis, Daniele Falavigna, Alessio Brutti, Maja Pantic. ICASSP 2025. [doi:10.1109/ICASSP49660.2025.10889251](https://doi.org/10.1109/ICASSP49660.2025.10889251) [arXiv:2409.12319](https://arxiv.org/abs/2409.12319)

## Verdict

The paper [[1]](#ref-1) changes two components, both standard. M06, a frozen Llama3.1-8B decoder fed by projected, pooled encoder tokens, departs from the field's hybrid CTC/attention decoder, but VSP-LLM [[2]](#ref-2) already decoded LRS3 lip video with a LoRA-tuned LLaMA2-7B behind a linear projector and token reduction, seven months earlier (Appendix); M03, training only projectors and LoRA (Table I), is VSP-LLM's regime too. The strongest overreach is the comparison set in Table I: against the matched VSP-LLM configuration the visual-only gain is 0.1 points (25.3% against 25.4%, Table I; [[2]](#ref-2) Table 1), and the "new SOTA" AVSR figure of 0.77% sits 0.01 points from the 0.76% of the [concurrent] Whisper-Flamingo [[3]](#ref-3) (inference), from one run per cell. The paper shows a frozen LLM decoder reaching the LRS3 AVSR frontier with few trainable parameters; that it beats a trained decoder on the same frozen features is untested.

## Against the field, component by component

### M06 Processing: frozen LLM decoder with projectors and token pooling

**Usual approach:** Before 2024-03, 55 of 407 VSR/AVSR studies name a hybrid CTC/attention decoder, trained end to end with its encoder, and an LLM decoder appears in 1 (VSP-LLM [[2]](#ref-2), read; pattern match, Appendix). Llama-AVSR substitutes a frozen LLM and pools tokens (K = 3, Sec. III-A).

**State of the art:** The best LRS3 clean AVSR WER now is 0.68% from DoubleHelix [[4]](#ref-4) [later] (2026), an LLM-based system trained on 1,759 hours, against 0.77% here at 1,756 hours (Table I), 0.09 points or 12% lower (inference). For VSR, DLLM-VSR [[5]](#ref-5) [later] reaches 19.4% at 433 labelled hours against 25.3% (Table I).

VSP-LLM uses "a single linear layer" (Sec. 4.2) and shortens the visual sequence by about 50% (Sec. 1); Llama-AVSR adds audio and audio-visual input and a stronger LLM. In the [concurrent] window 7 of 50 studies name an LLM decoder (Appendix), among them SynesLM [[6]](#ref-6) (OPT, Sec. 3.2), Personalized Lip Reading [[7]](#ref-7) (LLaMA3-8B, Sec. 4) and MMS-LLaMA [[8]](#ref-8), which cuts tokens by 86% (Sec. 1). Verdict: standard; the deciding prior has the design.

### M03 Training: frozen encoders and LLM, projectors and LoRA only

**Usual approach:** Before 2024-03, 193 of 407 VSR/AVSR studies name end-to-end training or full fine-tuning, 17 a frozen encoder and 3 LoRA (pattern match, Appendix); the one LoRA design inside the boundary is VSP-LLM, with a frozen AV-HuBERT and QLoRA on LLaMA2-7B (Sec. 4.2). Llama-AVSR keeps Whisper-medium, AV-HuBERT Large and the LLM frozen and trains about 42M to 57M parameters (Table I).

**State of the art:** MMS-LLaMA [[8]](#ref-8) [concurrent] (2025) applies QLoRA to LLaMA 3.1 8B (Sec. 4.2.3) and reaches 0.72% LRS3 AVSR WER at 1,759 hours, 0.05 points below the 0.77% here (inference).

Table I's "Labeled Hours" counts 433 hours for a model whose audio encoder saw 680k hours of speech [[3]](#ref-3) (Sec. 1) and whose video encoder was pre-trained on LRS3 and VoxCeleb2 (Sec. III-A), and the 42M trainable parameters (Table I) exclude the frozen 8B decoder run at test time. The 2.3% full fine-tuning row is Whisper-Large trained with noise and beam 15 [[3]](#ref-3) (Table 3), matching Llama-AVSR's own setup (Sec. III-A); trained without noise and decoded greedily it gives 1.0% at 433 hours and 0.68% at 1,759 hours, below the 1.1% and 0.79% here. Verdict: standard.

### M12 Evaluation: single-run SOTA claims on LRS3

**Usual approach:** Of 182 AVSR studies before 2024-03, at least 143 report no seeds, repeated runs or intervals (pattern match, Appendix). Llama-AVSR reports one WER per cell and copies other rows from their papers (Table I).

**State of the art:** 0.68% LRS3 AVSR (2026) [[4]](#ref-4) [later]; at the target's time, Whisper-Flamingo (2024) reported 0.76% [[3]](#ref-3) [concurrent] (Sec. 4).

Verdict: standard; it matters here because the gains are small: adding video at 1,756 hours moves 0.79% to 0.77% (Table I), about 2.5% relative (inference).

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Voiced TED speech; VoxCeleb2 at 1,756 h | Voiced speech | – | standard |
| M02 Training-only supervision | Transcripts; Whisper pseudo-labels (VoxCeleb2) | Text labels | – | standard |
| M03 Training and adaptation | Frozen encoders and LLM; projectors and LoRA trained | End-to-end training; of 407 prior (pattern match 193) | [[8]](#ref-8) 0.72% AVSR [concurrent] | standard |
| M04 Use-time action | Voiced speech; babble at test | Voiced speech | – | standard |
| M05 Sensors | Mouth ROI video plus audio | Camera plus microphone | – | standard |
| M06 Processing and decoding | Frozen Llama3.1-8B; projectors; pooled tokens | Hybrid CTC/attention; of 407 prior (pattern match 55) | [[4]](#ref-4) 0.68% AVSR [later] | standard |
| M07 Lexicon and LM | No external LM | Neural LM or LLM rescoring | – | standard |
| M08 Output | Text | Text | – | standard |
| M09 Confirmation | None | Mostly absent | – | not applicable |
| M10 Correction | None | Mostly absent | – | not applicable |
| M11 Reference construction | LRS3 test; size not written | Public split | – | standard |
| M12 Evaluation | One run per cell; copied rows | Single run; of 182 prior AVSR (pattern match 143) | [[4]](#ref-4) 0.68% AVSR [later] | standard |
| M13 Device and cost | Trainable parameters only | Cost often reported | – | not reported |

## Where the claims outrun the evidence

- Table I lists VSP-LLM at 26.7% (frozen encoder), not its 25.4% with the encoder unfrozen [[2]](#ref-2) (Table 1), the closer match to Llama-AVSR's video-encoder LoRA (Sec. III-A); "outstrips VSP-LLM" (Sec. III-B) rests on 0.1 points at 433 hours (28.4% against 29.8% at 30 hours).
- "Two new SOTA" for AVSR (Sec. III-B): Table I cites Whisper-Flamingo only at 433 hours (1.5%), not its 0.76% at 1,759 hours, or 0.86% noise-trained [[3]](#ref-3) (Table 3); the 0.77% leads only the latter.
- "Outperforms methods that exploit tens of thousands of hours" (§III-B): at 433 hours, 0.95% is above LP Conformer's 0.9% (Table I).
- §III-B pairs 433 hours with 1.5% and 30 hours with 1.1% for ASR, the reverse of Table I.
- The authors concede VSR is only comparable to earlier work (§IV); it trails BRAVEn's 20.1% (Table I).

## What the field needs next

- M06: the frozen Whisper and AV-HuBERT features (Sec. III-A) decoded by a trained hybrid CTC/attention decoder of matched trainable size, to isolate what the LLM adds.
- M12: several seeds and a significance test for the 1,756-hour ASR and AVSR runs (Table I).
- M03 and M13: total pre-training hours and inference memory and latency next to the trainable parameters of Table I.

## Questions for the authors

- Which test partition and text normalization give the WERs, and are copied rows scored the same way?
- Why omit VSP-LLM(FT) and Whisper-Flamingo's 1,759-hour rows?
- On which held-out data were K, LoRA rank and checkpoints chosen?
- How were the VoxCeleb2 pseudo-labels filtered?
- What is the AVSR result at 30 hours?

## Appendix: literature search

- Setting, the same for every topic: sentence-level VSR, AVSR and ASR on LRS3. Population: 739 unique VSR/AVSR studies with a WER, CER or accuracy result (pattern match on the ledger, target excluded). Dated against 2024-09: prior before 2024-03 (407 studies), [concurrent] 2024-03 to 2025-03 (50), [later] after 2025-03 (135), date unresolved 147. Counts are full-text pattern matches, related-work mentions included, unless marked read.
- M06, generative-text-decoder-vsr (published table, appended). Inclusion rule: the published rule (VSR or AVSR text decoders: CTC, attention, hybrid CTC/attention, LLM or iterative generative decoder). Ledger counts: 7,345 unique studies slot-filled for M06; 740 unique studies pattern match. Prior: hybrid CTC/attention 55; LLM decoder 2 hits, 1 after reading (VSP-LLM; the other is audio-only error correction). [Concurrent]: LLM decoder 9 hits, 7 after reading. Read: [[2]](#ref-2) (prior); [[6]](#ref-6), [[7]](#ref-7) ([concurrent]); [[8]](#ref-8), [[4]](#ref-4), [[5]](#ref-5) (state of the art). Known-item recall 1.0.
- M03, frozen-encoder-parameter-efficient-training-vsr (new). Inclusion rule: the same 739-study population, classified by the training regime the full text names (LoRA or QLoRA; adapters, prompt tuning or other parameter-efficient tuning; frozen encoder; end-to-end or full fine-tuning); a study counts under every regime it names. Ledger counts: 1,526 unique studies slot-filled for M03; 740 unique studies pattern match. Prior: end-to-end or full fine-tuning 193, frozen encoder 17, adapters or prompt tuning 14, LoRA 3 (1 inside the boundary after reading: VSP-LLM). [Concurrent]: LoRA 8. Read: [[2]](#ref-2) (prior); [[8]](#ref-8) (state of the art). Known-item recall 1.0.
- M12, avsr-noise-and-run-variability-protocol (published table, appended). Inclusion rule: the published rule and regexes (additive noise at stated SNRs, babble, run variability) over the AVSR population. Ledger counts: 6,960 unique studies slot-filled for M12; 349 unique studies pattern match (348 without the target). Prior 182: run-variability pattern 39 (upper bound), babble 63, LRS3 51, LRS3 with a variability pattern 9. Read: [[3]](#ref-3) ([concurrent]); [[4]](#ref-4) (state of the art). Known-item recall 1.0.
- Lineage: VoxCeleb2 pseudo-labels follow [[9]](#ref-9).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Cappellazzo, U., Kim, M., Chen, H., Ma, P., Petridis, S., Falavigna, D., et al. “Large Language Models are Strong Audio-Visual Speech Recognition Learners.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2025. doi:[10.1109/ICASSP49660.2025.10889251](https://doi.org/10.1109/ICASSP49660.2025.10889251). arXiv:[2409.12319](https://arxiv.org/abs/2409.12319). First public as arXiv:2409.12319 (2024-09); text read: v2 (7 Mar 2025). [wiki: arxiv-2409.12319](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2409.12319/article.md) [wiki: doi-10.1109-icassp49660.2025.10889251](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-icassp49660.2025.10889251/article.md)
2. <a id="ref-2"></a>Yeo, J. H., Han, S., Kim, M., Ro, Y. M. “Where Visual Speech Meets Language: VSP-LLM Framework for Efficient and Context-Aware Visual Speech Processing.” *Findings of the Association for Computational Linguistics: EMNLP 2024*, 2024. arXiv:[2402.15151](https://arxiv.org/abs/2402.15151). Prior; deciding prior for M03 and M06. [wiki: arxiv-2402.15151](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2402.15151/article.md) [wiki: acl-emnlp24-vspll](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/acl-emnlp24-vspll/article.md)
3. <a id="ref-3"></a>Rouditchenko, A., Gong, Y., Thomas, S., Karlinsky, L., Kuehne, H., Feris, R., et al. “Whisper-Flamingo: Integrating Visual Features into Whisper for Audio-Visual Speech Recognition and Translation.” *Interspeech*, 2024. arXiv:[2406.10082](https://arxiv.org/abs/2406.10082). [concurrent]; values from arXiv v3 (Nov 2024). [concurrent] [wiki: arxiv-2406.10082](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.10082/article.md) [wiki: isca-rouditchenko24_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-rouditchenko24_interspeech/article.md) [wiki: isca-rouditchenko24-whisperflamingo](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-rouditchenko24-whisperflamingo/article.md) [wiki: in24-whisperflamingo](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/in24-whisperflamingo/article.md)
4. <a id="ref-4"></a>Cheng, Z. “DoubleHelix: Structured Cross-Modal Fusion for Audio-Visual Speech Recognition with LLMs.” *arXiv preprint*, 2026. arXiv:[2607.29112](https://arxiv.org/abs/2607.29112). [later] [later] [wiki: arxiv-2607.29112](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2607.29112/article.md) [wiki: arxiv-2607-29112-doublehelix](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2607-29112-doublehelix/article.md) [wiki: arxiv-2607.29112-doublehelix](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2607.29112-doublehelix/article.md)
5. <a id="ref-5"></a>Yeo, J. H., Kim, C. W., Rha, H., Ro, Y. M. “Diffusion Large Language Models for Visual Speech Recognition.” *arXiv preprint*, 2026. arXiv:[2605.28456](https://arxiv.org/abs/2605.28456). [later] [later] [wiki: arxiv-2605.28456](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2605.28456/article.md) [wiki: arxiv-2605-28456-dllmvsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2605-28456-dllmvsr/article.md) [wiki: arxiv-2605.28456-dllmvsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2605.28456-dllmvsr/article.md)
6. <a id="ref-6"></a>Lu, Y., Song, J., Chang, X., Bian, H., Maiti, S., Watanabe, S. “SynesLM: A Unified Approach for Audio-visual Speech Recognition and Translation via Language Model and Synthetic Data.” *arXiv preprint*, 2024. arXiv:[2408.00624](https://arxiv.org/abs/2408.00624). [concurrent] [concurrent] [wiki: arxiv-2408.00624](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2408.00624/article.md)
7. <a id="ref-7"></a>Yeo, J. H., Kim, C. W., Kim, H., Rha, H., Han, S., Cheng, W., et al. “Personalized Lip Reading: Adapting to Your Unique Lip Movements with Vision and Language.” *arXiv preprint*, 2024. arXiv:[2409.00986](https://arxiv.org/abs/2409.00986). [concurrent] [concurrent] [wiki: arxiv-2409.00986](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2409.00986/article.md)
8. <a id="ref-8"></a>Yeo, J. H., Rha, H., Park, S. J., Ro, Y. M. “MMS-LLaMA: Efficient LLM-based Audio-Visual Speech Recognition with Minimal Multimodal Speech Tokens.” *arXiv preprint*, 2025. arXiv:[2503.11315](https://arxiv.org/abs/2503.11315). [concurrent] (2025-03, six months after the target). [concurrent] [wiki: arxiv-2503.11315](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2503.11315/article.md) [wiki: acl-2025-mms-llama](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/acl-2025-mms-llama/article.md)
9. <a id="ref-9"></a>Ma, P., Haliassos, A., Fernandez-Lopez, A., Chen, H., Petridis, S., Pantic, M. “Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2023. arXiv:[2303.14307](https://arxiv.org/abs/2303.14307). Prior; source of the VoxCeleb2 pseudo-labelling recipe. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/auto-avsr-audio-visual-speech-recognition-with-automatic-labels) [wiki: arxiv-2303.14307](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2303.14307/article.md)
