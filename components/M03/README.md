# M03 Train / calibrate

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## cross-subject-pooled-training

- Table: [`cross-subject-pooled-training.csv`](cross-subject-pooled-training.csv) (1526 slot-filled, 370 pattern match, usual design in 90, 4 read in full)
- Inclusion rule: Speech or language decoders from neural or other biosignals that train one model on data pooled across participants, with or without participant-specific layers or embeddings. Boundary: a per-participant model that only reports results averaged over participants is excluded; transfer by fine-tuning from another participant counts; versions of one study count once.
- Used in: [Decoding speech perception from non-invasive brain recordings](../../reviews/decoding-speech-perception-from-non-invasive-brain-recordings/)

## eeg-user-identification

- Table: [`eeg-user-identification.csv`](eeg-user-identification.csv) (1526 slot-filled, 6 pattern match, usual design in 6, 3 read in full)
- Inclusion rule: Studies in the wiki that identify the user (subject identification, biometric authentication) from scalp EEG; the design compared is identification from speech-imagery trials and how identification is tested (session-held-out vs trials permuted across sessions). Boundary: identification used only as a nuisance factor is excluded; versions count once; the target is counted in the pattern match.
- Used in: [Toward Practical BCI: A Real-time Wireless Imagined Speech EEG Decoding System](../../reviews/toward-practical-bci-a-real-time-wireless-imagined-speech-eeg-decoding-system/)

## length-curriculum

- Table: [`length-curriculum.csv`](length-curriculum.csv) (18 confirmed, 71 candidates read, 5 unread)
- Inclusion rule: Include studies that train a sequence-output decoder with a procedure that starts from examples of short units (words, short segments) and grows the input sequence length as training proceeds (moving to sentences, long segments). Boundary: exclude curricula that only progressively change noise level, difficulty or data amount. A two-stage procedure that pretrains on words and then retrains on sentences is included if it is described as an explicit procedure moving from short to long units. Include studies that actually use the procedure, not only those that say they inherited a predecessor's procedure. Count different versions of the same study as one item.
- Used in: [Lip Reading Sentences in the Wild](../../reviews/lip-reading-sentences-in-the-wild/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Lip Reading Sentences in the Wild | 2017 | §3.1 |
| Deep Lip Reading: a comparison of models and an online application |  | §3 |
| Deep Audio-Visual Speech Recognition |  | §5.2 |
| Learning from Videos with Deep Convolutional LSTM Networks |  | §4 |
| LipReading with 3D-2D-CNN BLSTM-HMM and word-CTC models |  | §3 |
| Distinguishing Homophenes Using Multi-Head Visual-Audio Memory for Lip Reading |  | §4 |
| Predict-and-Update Network: Audio-Visual Speech Recognition Inspired by Human Speech Perception |  | §4 |
| Watch or Listen: Robust Audio-Visual Speech Recognition with Visual Corruption Modeling and Reliability Scoring |  | Ledger M03 |
| AlignVSR: Audio-Visual Cross-Modal Alignment for Visual Speech Recognition |  | Ledger M03 |
| Cascade-Free Mandarin Visual Speech Recognition via Semantic-Guided Cross-Representation Alignment |  | §4 |
| Spatio-Temporal Fusion based Convolutional Sequence Learning for Lip Reading | 2019 | §4 |
| MultiAVSR: Robust Speech Recognition via Supervised Multi-Task Audio-Visual Learning | 2025 | §4 |
| An Effective Conversion of Visemes to Words for High-Performance Automatic Lipreading | 2021 | §4 |
| Korean Lip-Reading: Data Construction and Sentence-Level Lip-Reading | 2024 | §3 |
| LiRA: Learning Visual Speech Representations from Audio through Self-supervision | 2021 | §4 |
| An Improved End-to-End Audio-Visual Speech Recognition Model |  | §3.1 |
| Research on Robust Audio-Visual Speech Recognition Algorithms | 2023 | Ledger M03 |
| E-commerce Video & Content Understanding via Vision: A Comprehensive Study on Lip Reading and Visual Speech Recognition for Enhanced Shopping Experience | 2026 | Ledger M06 |

## self-supervised-pretraining

- Table: [`self-supervised-pretraining.csv`](self-supervised-pretraining.csv) (1526 slot-filled, 123 pattern match, usual design in 31, 3 read in full)
- Inclusion rule: Include studies that pre-train an encoder on unlabelled non-audio-only input (video, audio-visual, biosignal or neural recordings) with a self-supervised or teacher-generated objective (masked prediction, contrastive, feature regression, cross-modal distillation) before supervised fine-tuning for speech or text decoding. Boundary: exclude audio-only self-supervised ASR; exclude studies that only reuse a released pre-trained checkpoint without training a new objective; count versions of one study once.
- Used in: [Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction](../../reviews/learning-audio-visual-speech-representation-by-masked-multimodal-cluster-prediction/), [Visual Speech Recognition for Multiple Languages in the Wild](../../reviews/visual-speech-recognition-for-multiple-languages-in-the-wild/)

## speech-bci-calibration-data

- Table: [`speech-bci-calibration-data.csv`](speech-bci-calibration-data.csv) (1526 slot-filled, 51 pattern match, usual design in 4, 3 read in full)
- Inclusion rule: Neural speech-decoding studies (intracortical, ECoG, sEEG, EEG) that state how much same-participant calibration or training data the decoder needs, or how it is recalibrated across days. Included: daily supervised recalibration, cumulative multi-day training, unsupervised or no recalibration, cross-participant pretraining. Excluded: non-neural silent-speech sensors; perception-only recalibration studies; cursor or handwriting BCIs unless they decode speech.
- Used in: [An Accurate and Rapidly Calibrating Speech Neuroprosthesis](../../reviews/an-accurate-and-rapidly-calibrating-speech-neuroprosthesis/)
