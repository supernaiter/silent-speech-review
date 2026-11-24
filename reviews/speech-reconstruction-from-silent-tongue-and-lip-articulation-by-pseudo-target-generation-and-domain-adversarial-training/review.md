# Speech Reconstruction from Silent Tongue and Lip Articulation By Pseudo Target Generation and Domain Adversarial Training

Rui-Chen Zheng, Yang Ai, Zhen-Hua Ling. arXiv preprint, 2023. [arXiv:2304.05574](https://arxiv.org/abs/2304.05574)

## Verdict

The paper [[1]](#ref-1) changes the silent training target (M02) and adds joint silent-vocalized training with a speaking-mode discriminator (M03); both are standard. DTW transfer of vocalized targets to silent articulation was established for silent EMG [[2]](#ref-2), with realignment by the partially trained model [[3]](#ref-3); neither is cited. The read priors aim domain-adversarial training at speakers or sessions [[4]](#ref-4), [[5]](#ref-5), so the speaking-mode label is new, but its single-run ablation drops the vocalized loss with the discriminator. Silent MCD and STOI are scored against the method's own vocoded pseudo targets, and 18 of 81 speakers were dropped from the silent test by the same DTW cost (Sec. 4.2). The silent WER gain (59.960% to 43.114%, Table 1) is relatively smaller than the vocalized gain (28% against 36%); the absolute silent-vocalized gap narrows by 7.3 points, but the ratio widens from 2.2 to 2.5 (inference).

## Against the field, component by component

### M02 Training-only supervision: silent pseudo targets by DTW

**Usual approach:** Silent decoders take targets from the paired vocalized take by time alignment: 15 of 16 confirmed (52 pattern match, Appendix), as in [[2]](#ref-2) and [[3]](#ref-3). The paper aligns encoder outputs instead of signal features (Sec. 3.1), drops high-cost samples (Sec. 4.2), and is the only ultrasound study in the confirmed set (Appendix).

**State of the art:** The [later] GETS [[6]](#ref-6) (2026) reaches 11.89% WER on the silent EMG test set; the target's 43.114% differs in signal, recognizer and data, so neither ranks the other.

The iterative strategy repeats the prior realignment at a different schedule: Gaddy and Klein recompute alignments every five epochs (76.5% WER without it, 68.0% with, their Table 5); here three rounds give 46.016% to 43.114% (Table 2, Fig. 2a). Verdict: standard.

### M03 Training: joint training with a speaking-mode discriminator

**Usual approach:** The recorded design is paired-audio supervision (31 of 138 slot-filled studies); full-text designs are target transfer 27, domain-adversarial invariance 12, fine-tuning from an overt model 11, a cross-mode divergence 5 (pattern match, Appendix). [[3]](#ref-3) pools both modes but gives vocalized samples their own session embeddings, the opposite of invariance. Domain-adversarial training was earlier aimed at speakers [[4]](#ref-4) and EMG sessions [[5]](#ref-5), and [[7]](#ref-7) adapted TaL recognizers to silent speech with fMLLR; the speaking-mode label is new, but untested alone.

**State of the art:** The [later] [[8]](#ref-8) (2026) aligns silent and voiced representations and lowers silent EMG WER from 26.75% to 25.14% over 10 seeds (p = 0.002), repeated-run evidence this paper lacks.

"w/o DAT" reduces Eq. (3) to the silent loss (Sec. 4.4), removing the discriminator and the vocalized loss together; its deficit (51.199% against 43.114% WER, Table 2) mixes invariance with vocalized co-training, which helped in [[3]](#ref-3) (71.6% WER without its non-parallel vocalized data, 3.6 points worse). Verdict: standard.

### M11 Reference construction: pseudo targets as silent ground truth

**Usual approach:** M11 has no topic tally; the read prior [[3]](#ref-3) scores silent output only by transcription WER, with 9.5% on vocalized test audio as the lower bound.

**State of the art:** Later silent work [[6]](#ref-6), [[8]](#ref-8) (2026) also scores silent output by WER.

Here silent MCD and STOI use PWG waveforms of the test pseudo targets (Sec. 4.3), from an unstated encoder. The proposed model is trained on such targets and TaLNet is not, so both metrics favour it by construction (inference). The reference scores 10.246% WER against 4.110% for natural vocalized recordings (Sec. 4.3). Verdict: standard.

### M12 Evaluation: test population and protocol

**Usual approach:** Ultrasound-to-speech studies use MCD (21 of 51 unique studies) and MUSHRA (14), rarely ASR on output (3) (pattern match, Appendix); this paper's set is broader.

**State of the art:** The [later] Tongue2Speech [[9]](#ref-9) (2026) reports 31.64% WER on TaL80 with another recognizer and split, so it does not rank the target's 17.309% vocalized WER.

The silent test drops 18 speakers by the method's own first-round DTW cost (Sec. 4.2), so results cover speakers whose pseudo targets work. Test speakers are also training speakers (Sec. 4.1). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | TaL silent and aloud takes | Recorded production (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Encoder-space DTW targets, cost filter | Paired-take target transfer (confirmed 15) | [[6]](#ref-6) (2026): EMG WER 11.89% | standard |
| M03 Training and adaptation | Joint training, mode discriminator | Paired-audio supervision (slot-filled 31) | [[8]](#ref-8) (2026): EMG WER 25.14% | standard |
| M04 Use-time action | Silent input, no fine-tuning | Production condition (slot-filled 5,595) | – | standard |
| M05 Sensors | Ultrasound plus lip video | Ultrasound studies (slot-filled 144) | – | standard |
| M06 Processing and decoding | TaLNet encoder-decoder | Encoder-decoder (slot-filled 7,345) | – | standard |
| M07 Lexicon and LM | None | Lexicon or LM (slot-filled 119) | – | not applicable |
| M08 Output | Mel to PWG waveform | Waveform (slot-filled 3,268) | – | standard |
| M09 Confirmation | None | Mostly absent (slot-filled 82) | – | not applicable |
| M10 Correction | None | Mostly absent (slot-filled 82) | – | not applicable |
| M11 Reference construction | Vocoded pseudo targets | Transcript (no topic tally) (slot-filled 234) | – | standard |
| M12 Evaluation | MCD, STOI, WER, MOS; 18 speakers dropped | MCD (pattern match 21) | [[9]](#ref-9) (2026): WER 31.64% | standard |
| M13 Device and cost | Not reported | Device constraints (slot-filled 6,075) | – | not reported |

## Where the claims outrun the evidence

- Invariance is asserted, not measured: no discriminator accuracy or cross-mode distance is reported, and the authors say it "may" explain the vocalized gain (Sec. 4.3).
- The silent-only "w/o DAT" model reaches 25.032% vocalized WER (Table 2): continued training explains about a fifth of the vocalized gain, and Table 2 does not separate the rest (inference).
- In Table 1 the abstract's "over 15%" silent WER drop is 16.8 points or 28% relative, its "approximately 10%" vocalized drop 9.6 points or 36% relative (inference).

## What the field needs next

- M03: remove only the discriminator, keep the vocalized loss, over several seeds, and compare with mode embeddings [[3]](#ref-3).
- M02: encoder-space against feature-space DTW with periodic realignment on TaL, at equal training steps.
- M11/M12: all 81 speakers, speaker-disjoint, scored by a fixed open recognizer.

## Questions for the authors

- Which model and iteration produced the silent test pseudo references?
- How was the checkpoint chosen?
- Which iFLYTEK version and text normalization produced the WERs?
- What are both systems' WERs on the 18 excluded speakers?

## Appendix: literature search

- M02, silent-target-transfer (published table, reused). Inclusion rule: studies that train a decoder or synthesizer on silently articulated non-acoustic signals using acoustic or label targets transferred from a separate vocalized recording of the same utterance by time alignment (DTW, forced alignment or a learned alignment); any signal; training only on vocalized data and testing on silent data, alignment used only for scoring, whisper or NAM conversion and imagined speech excluded; versions count once. Ledger: 31 unique studies slot-filled for M02; 52 unique studies pattern match; 16 confirmed. Usual design: target transfer from the paired vocalized recording, 15 confirmed; prior designs [[2]](#ref-2), [[3]](#ref-3). Signals of the 16 confirmed (published include reasons): ultrasound plus lip video in the target [[1]](#ref-1), EMG-based in all others. Read in full: [[3]](#ref-3), [[2]](#ref-2), [[6]](#ref-6). Known-item recall 0.67.
- M03, overt-silent-joint-training (published table, reused). Inclusion rule: studies with any signal whose ledger mentions both overt and silent speech production, classified by how overt recordings enter the training of a silent-speech decoder (pooled training, fine-tuning from an overt model, time-aligned target transfer, domain-adversarial invariance, an explicit distance or divergence between modes); overt-only training applied to silent test data, whisper-to-normal conversion and perception studies excluded; a study counts under every design its full text names (upper bound); versions count once. Ledger: 1,526 unique studies slot-filled for M03; 354 unique studies pattern match. Usual design: supervision from paired audio, 31 of 138 (slot-filled); target transfer 27, domain-adversarial invariance 12, fine-tuning from an overt model 11, divergence or metric loss 5 (pattern match). Read in full: [[3]](#ref-3), [[4]](#ref-4), [[5]](#ref-5), [[7]](#ref-7), [[8]](#ref-8). Known-item recall 1.0.
- M12, ultrasound-to-speech-output-evaluation (published table, reused). Inclusion rule: studies that synthesize speech or acoustic features from ultrasound tongue images (with or without lip video) and evaluate the output, classified by output measure; recognition-only studies, contour tracking and reviews excluded; versions count once. Ledger: 6,960 unique studies slot-filled for M12; 51 unique studies pattern match. Usual design: MCD 21, often with MUSHRA 14; listener intelligibility 5, MOS 4, ASR on output 3 (pattern match). Read in full: [[9]](#ref-9). Known-item recall 0.57.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Zheng, R., Ai, Y., Ling, Z. “Speech Reconstruction from Silent Tongue and Lip Articulation By Pseudo Target Generation and Domain Adversarial Training.” *arXiv preprint*, 2023. doi:[10.48550/arXiv.2304.05574](https://doi.org/10.48550/arXiv.2304.05574). arXiv:[2304.05574](https://arxiv.org/abs/2304.05574). Target. Read as arXiv v1. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/speech-reconstruction-from-silent-tongue-and-lip-articulation-by-pseudo-target-generation-and-domain-adversarial-training) [wiki: arxiv-2304.05574](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2304.05574/article.md)
2. <a id="ref-2"></a>Janke, M., Diener, L. “EMG-to-Speech: Direct Generation of Speech From Facial Electromyographic Signals.” *IEEE/ACM Transactions on Audio, Speech, and Language Processing*, 2017, 25(12), 2375-2385. doi:[10.1109/TASLP.2017.2738568](https://doi.org/10.1109/TASLP.2017.2738568). Prior; deciding prior for M02 (DTW target transfer to silent EMG). Uncited by the target. [wiki: doi-10.1109-taslp-2017-2738568](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-taslp-2017-2738568/article.md)
3. <a id="ref-3"></a>Gaddy, D., Klein, D. “Digital Voicing of Silent Speech.” *Proc. 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 2020, 5521-5530. doi:[10.18653/v1/2020.emnlp-main.445](https://doi.org/10.18653/v1/2020.emnlp-main.445). arXiv:[2010.02960](https://arxiv.org/abs/2010.02960). Prior; deciding prior for M02, M03 and M11. Uncited by the target. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/digital-voicing-of-silent-speech) [wiki: arxiv-2010.02960](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2010.02960/article.md) [wiki: doi-10.18653-v1-2020.emnlp-main.445](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.18653-v1-2020.emnlp-main.445/article.md)
4. <a id="ref-4"></a>Wand, M., Schmidhuber, J. “Improving Speaker-Independent Lipreading with Domain-Adversarial Training.” *Proc. Interspeech 2017*, 2017, 3662-3666. arXiv:[1708.01565](https://arxiv.org/abs/1708.01565). Prior; domain-adversarial training against speakers. [wiki: arxiv-1708.01565](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1708.01565/article.md)
5. <a id="ref-5"></a>Wand, M., Schultz, T., Schmidhuber, J. “Domain-Adversarial Training for Session Independent EMG-based Speech Recognition.” *Proc. Interspeech 2018*, 2018, 3167-3171. doi:[10.21437/Interspeech.2018-2318](https://doi.org/10.21437/Interspeech.2018-2318). Prior; domain-adversarial training against recording sessions. [wiki: isca-wand18_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-wand18_interspeech/article.md)
6. <a id="ref-6"></a>Lee, J., Lee, J., Lee, K. “GETS: Guiding EMG-to-Speech Synthesis via Silent Speech Recognition.” *Proc. Interspeech 2026*, 2026. doi:[10.21437/Interspeech.2026-1938](https://doi.org/10.21437/Interspeech.2026-1938). Later; state of the art for M02. [later] [wiki: isca-lee26r_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-lee26r_interspeech/article.md)
7. <a id="ref-7"></a>Ribeiro, M. S., Eshky, A., Richmond, K., Renals, S. “Silent versus modal multi-speaker speech recognition from ultrasound and video.” *Proc. Interspeech 2021*, 2021, 641-645. doi:[10.21437/Interspeech.2021-23](https://doi.org/10.21437/Interspeech.2021-23). Prior; cited by the target; silent-modal mismatch on TaL. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/silent-versus-modal-multi-speaker-speech-recognition-from-ultrasound-and-video) [wiki: isca-ribeiro21-silentus](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-ribeiro21-silentus/article.md)
8. <a id="ref-8"></a>Lee, J., Hwang, I., Lee, J., Kim, E., Han, D., Lee, K. “Enhancing EMG-to-Speech via Silent-Voiced Representation Alignment.” *Proc. Interspeech 2026*, 2026. doi:[10.21437/Interspeech.2026-2931](https://doi.org/10.21437/Interspeech.2026-2931). Later; state of the art for M03. [later] [wiki: isca-lee26v_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-lee26v_interspeech/article.md)
9. <a id="ref-9"></a>Sonkar, Y., Kilaru, Y., Yelimeli, S., Shah, N., Gandhi, V. “Tongue2Speech: Real-Time Speech Synthesis from Tongue Ultrasound Videos via Spatiotemporal Transformers.” *Proc. Interspeech 2026*, 2026, 6856-6860. doi:[10.21437/Interspeech.2026-3023](https://doi.org/10.21437/Interspeech.2026-3023). Later; state of the art for M12 (published topic table). [later] [wiki: isca-sonkar26_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-sonkar26_interspeech/article.md)
