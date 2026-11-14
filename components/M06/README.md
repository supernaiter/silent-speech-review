# M06 Decoding

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## articulatory-intermediate

- Table: [`articulatory-intermediate.csv`](articulatory-intermediate.csv) (7345 slot-filled, 12 pattern match, 44 read in full)
- Inclusion rule: Include studies with a decoding pathway that first decodes an explicit articulatory representation (measured or estimated movement trajectories of the articulators, articulatory features or phonological categories) from non-acoustic signals (neural activity, EMG, video, ultrasound, etc.) and then converts it in a next stage to acoustic features, speech waveforms or symbol sequences. Boundary: exclude those whose input itself is an articulatory measurement (EMA, PMA, ultrasound) and that do not decode an articulatory representation as an intermediate. Exclude those that estimate articulation from acoustics and then return to speech (acoustic input). Exclude those that use articulation only as an auxiliary loss or regularization without placing it in the middle of the pathway. Exclude those that only decode an articulatory representation with no next stage. Exclude mentions in reviews or citations only. Count different versions of the same study as one item.
- Used in: [Speech synthesis from neural decoding of spoken sentences](../../reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Articulatory Feature Prediction from Surface EMG during Speech Production | 2025 | Abstract |
| doi-10.1038-s41586-019-1119-1 |  | Abstract, Methods "Neural decoder" |
| Overt speech decoding from cortical activity: a comparison of different linear methods | 2023 | Abstract（Methods）、§2.6.3 |
| SPEAK YOUR MIND! Towards Imagined Speech Recognition With Hierarchical Deep Learning |  | Abstract |

## attention-seq2seq-decoding

- Table: [`attention-seq2seq-decoding.csv`](attention-seq2seq-decoding.csv) (7345 slot-filled, 210 pattern match, 115 read in full)
- Inclusion rule: Include studies that autoregressively output symbol sequences such as characters, words or phonemes from non-audio input such as video, biosignals or neural signals (including combined audio-visual input) with an attention-based encoder-decoder (including sequence-to-sequence and Transformer decoders), and report evaluation results. Boundary: exclude those that use attention only for feature extraction or word classification, and those that use only CTC (including Transformer encoder + CTC). Exclude those whose output is speech features (speech synthesis). The CTC-attention combination (hybrid) has an attention decoder and is included. Audio-only ASR is outside the wiki and out of scope. Count different versions of the same study as one item.
- Used in: [Lip Reading Sentences in the Wild](../../reviews/lip-reading-sentences-in-the-wild/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Lip Reading Sentences in the Wild | 2017 | §2.3, §6 |
| Can DNNs Learn to Lipread Full Sentences? |  | Abstract |
| Deep Lip Reading: a comparison of models and an online application |  | Abstract, §1 |
| Large-Scale Visual Speech Recognition |  | Table 3 (ledger comparison row) |
| Deep Audio-Visual Speech Recognition |  | §3, Table 2 |
| Modality Attention for End-to-End Audio-visual Speech Recognition |  | Ledger M12 |
| A Cascade Sequence-to-Sequence Model for Chinese Mandarin Lip Reading |  | Ledger |
| State-of-the-art Speech Recognition using EEG and Towards Decoding of Speech Spectrum From EEG | 2020 | §3 |
| Hearing Lips: Improving Lip Reading by Distilling Speech Recognizers |  | Ledger |
| EEG based Continuous Speech Recognition using Transformers | 2020 | Abstract |
| Pseudo-Convolutional Policy Gradient for Sequence-to-Sequence Lip-Reading |  | Title and ledger |
| How to Teach DNNs to Pay Attention to the Visual Modality in Speech Recognition |  | Ledger |
| Should we hard-code the recurrence concept or learn it instead? Exploring the Transformer architecture for Audio-Visual Speech Recognition |  | Ledger |
| "Notic My Speech" -- Blending Speech Patterns With Multimedia |  | Ledger M06 |
| End-to-end Silent Speech Recognition with Acoustic Sensing |  | Abstract |
| End-to-End Audio-Visual Speech Recognition with Conformers | 2021 | Ledger |
| Lip reading using external viseme decoding |  | Ledger |
| Fusing information streams in end-to-end audio-visual speech recognition |  | §5 |
| Sub-word Level Lip Reading With Visual Attention |  | Ledger |
| Open Vocabulary Electroencephalography-To-Text Decoding and Zero-shot Sentiment Classification |  | Ledger |
| VisG AV-HuBERT: Viseme-Guided AV-HuBERT | 2026 | §3 |
| SENSE: Semantic Neural Speech Synthesis from Brain Dynamics via Spatial Graph Encoding | 2026 | §3 |
| Learning from the Master: Distilling Cross-modal Advanced Knowledge for Lip Reading | 2021 | Ledger |
| Discriminative Multi-modality Speech Recognition | 2020 | Ledger M06 |
| Spatio-Temporal Fusion based Convolutional Sequence Learning for Lip Reading | 2019 | Ledger M06 |
| Audio-Visual Speech Recognition with a Hybrid CTC/Attention Architecture | 2018 | Ledger M06 |
| Visual Speech Recognition for Multiple Languages in the Wild | 2022 | Ledger |
| doi-10.3390-app13116521 | 2023 | §3 |
| Speaker-Adapted End-to-End Visual Speech Recognition for Continuous Spanish | 2022 | Ledger |
| AVATAR: Unconstrained Audiovisual Speech Recognition | 2022 | Ledger |
| Visual Context-driven Audio Feature Enhancement for Robust End-to-End Audio-Visual Speech Recognition | 2022 | Ledger |
| LiRA: Learning Visual Speech Representations from Audio through Self-supervision | 2021 | Ledger |
| Robust Self-Supervised Audio-Visual Speech Recognition | 2022 | Ledger |
| CI-AVSR: A Cantonese Audio-Visual Speech Dataset for In-car Command Recognition | 2022 | Ledger |
| SSR7000: A Synchronized Corpus of Ultrasound Tongue Imaging for End-to-End Silent Speech Recognition | 2022 | Ledger M06 |
| Reliability-Based Large-Vocabulary Audio-Visual Speech Recognition | 2022 | §3 |

## ctc-vs-attention

- Table: [`ctc-vs-attention.csv`](ctc-vs-attention.csv) (7345 slot-filled, 114 pattern match, 42 read in full)
- Inclusion rule: Include studies that train, on the same input front end (visual, biosignal, or audio-visual), both a decoder trained with CTC and an attention/sequence-to-sequence decoder (seq2seq or Transformer decoder) and compare the results side by side. Boundary: exclude those that use only the CTC-attention combination (hybrid) with no result for either alone. Exclude comparisons that only list numbers from other papers. Audio-only ASR is outside the wiki and out of scope. Count different versions of the same study as one item.
- Used in: [Deep Audio-Visual Speech Recognition](../../reviews/deep-audio-visual-speech-recognition/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Deep Lip Reading: a comparison of models and an online application |  | §3.3, Table 1 |
| State-of-the-art Speech Recognition using EEG and Towards Decoding of Speech Spectrum From EEG | 2020 | §2 |
| End-to-end Silent Speech Recognition with Acoustic Sensing |  | §4.4, Fig. 4(c) |
