# M06 Decoding

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## articulatory-intermediate

- Table: [`articulatory-intermediate.csv`](articulatory-intermediate.csv) (4 confirmed, 44 candidates read, 0 unread)
- Inclusion rule: Include studies with a decoding pathway that first decodes an explicit articulatory representation (measured or estimated movement trajectories of the articulators, articulatory features or phonological categories) from non-acoustic signals (neural activity, EMG, video, ultrasound, etc.) and then converts it in a next stage to acoustic features, speech waveforms or symbol sequences. Boundary: exclude those whose input itself is an articulatory measurement (EMA, PMA, ultrasound) and that do not decode an articulatory representation as an intermediate. Exclude those that estimate articulation from acoustics and then return to speech (acoustic input). Exclude those that use articulation only as an auxiliary loss or regularization without placing it in the middle of the pathway. Exclude those that only decode an articulatory representation with no next stage. Exclude mentions in reviews or citations only. Count different versions of the same study as one item.
- Used in: [Speech synthesis from neural decoding of spoken sentences](../../reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Articulatory Feature Prediction from Surface EMG during Speech Production | 2025 | Abstract |
| doi-10.1038-s41586-019-1119-1 |  | Abstract, Methods "Neural decoder" |
| Overt speech decoding from cortical activity: a comparison of different linear methods | 2023 | Abstract（Methods）、§2.6.3 |
| SPEAK YOUR MIND! Towards Imagined Speech Recognition With Hierarchical Deep Learning |  | Abstract |

## articulography-to-speech-synthesis

- Table: [`articulography-to-speech-synthesis.csv`](articulography-to-speech-synthesis.csv) (7345 slot-filled, 69 pattern match, usual design in 40, 3 read in full)
- Inclusion rule: Include studies that synthesize speech audio from measured articulatory kinematics (EMA, PMA or other magnetic tracking) and report how acoustic features are turned into a waveform. Boundary: exclude acoustic-to-articulatory inversion, talking-head animation and articulatory synthesizers driven by model parameters rather than measurements; count versions once.
- Used in: [EMA2S: An End-to-End Multimodal Articulatory-to-Speech System](../../reviews/ema2s-an-end-to-end-multimodal-articulatory-to-speech-system/)

## attention-seq2seq-decoding

- Table: [`attention-seq2seq-decoding.csv`](attention-seq2seq-decoding.csv) (36 confirmed, 115 candidates read, 441 unread)
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

## causal-closed-loop-speech-synthesis

- Table: [`causal-closed-loop-speech-synthesis.csv`](causal-closed-loop-speech-synthesis.csv) (7345 slot-filled, 87 pattern match, usual design in 24, 3 read in full)
- Inclusion rule: Studies that synthesize speech acoustics from a non-acoustic signal (neural, EMG, articulography, ultrasound, video) online, in real time, with the audio played back to the user while or right after they speak. Boundary: include formant or vocoder synthesis of vowels, words or sentences, and offline studies only when they simulate causal frame-level inference; exclude offline acausal reconstruction, text decoding read out by TTS, and conversion from acoustic input; count versions once.
- Used in: [An instantaneous voice-synthesis neuroprosthesis](../../reviews/an-instantaneous-voice-synthesis-neuroprosthesis/)

## closed-vocabulary-word-classification

- Table: [`closed-vocabulary-word-classification.csv`](closed-vocabulary-word-classification.csv) (7345 slot-filled, 360 pattern match, usual design in 82, 2 read in full)
- Inclusion rule: Studies that decode words or utterances from non-acoustic signals (neural, EMG, articulatory, video) by classifying each detected segment into a closed set of at most a few hundred words or utterances, with or without a language-model or context prior over the sequence. Boundary: open-vocabulary phoneme or character decoders are excluded unless they also report a closed-set word test; acoustic-only ASR is excluded.
- Used in: [Neuroprosthesis for decoding speech in a paralyzed person with anarthria](../../reviews/neuroprosthesis-for-decoding-speech-in-a-paralyzed-person-with-anarthria/)

## ctc-vs-attention

- Table: [`ctc-vs-attention.csv`](ctc-vs-attention.csv) (3 confirmed, 42 candidates read, 128 unread)
- Inclusion rule: Include studies that train, on the same input front end (visual, biosignal, or audio-visual), both a decoder trained with CTC and an attention/sequence-to-sequence decoder (seq2seq or Transformer decoder) and compare the results side by side. Boundary: exclude those that use only the CTC-attention combination (hybrid) with no result for either alone. Exclude comparisons that only list numbers from other papers. Audio-only ASR is outside the wiki and out of scope. Count different versions of the same study as one item.
- Used in: [Deep Audio-Visual Speech Recognition](../../reviews/deep-audio-visual-speech-recognition/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Deep Lip Reading: a comparison of models and an online application |  | §3.3, Table 1 |
| State-of-the-art Speech Recognition using EEG and Towards Decoding of Speech Spectrum From EEG | 2020 | §2 |
| End-to-end Silent Speech Recognition with Acoustic Sensing |  | §4.4, Fig. 4(c) |

## intracranial-synthesis-neural-features

- Table: [`intracranial-synthesis-neural-features.csv`](intracranial-synthesis-neural-features.csv) (7345 slot-filled, 180 pattern match, usual design in 62, 3 read in full)
- Inclusion rule: Include studies that reconstruct speech acoustics (spectrograms, vocoder features or waveforms) from intracranial recordings (ECoG, sEEG or depth electrodes, intracortical arrays) made during overt, mouthed, attempted or imagined speech production. Boundary: exclude reconstruction of heard speech, text-only decoding read out by a TTS engine, and reviews or citation-only mentions; count versions of one study once. The ledger pattern also admits some reviews and text-decoding papers, so its count is an upper bound. Design of interest: the neural feature fed to the acoustic decoder (high-gamma envelope, wavelet multiband decomposition, low-frequency band power, phase-amplitude coupling).
- Used in: [Brain-to-Speech: Prosody Feature Engineering and Transformer-Based Reconstruction](../../reviews/brain-to-speech-prosody-feature-engineering-and-transformer-based-reconstruction/)

## noninvasive-decoding-segmentation

- Table: [`noninvasive-decoding-segmentation.csv`](noninvasive-decoding-segmentation.csv) (7345 slot-filled, 1458 pattern match, usual design in 310, 2 read in full)
- Inclusion rule: Language or text decoding studies whose ledger names scalp EEG or MEG. The design compared is how the decoder is segmented at test time: windows locked to known events supplied to the decoder (word, stimulus or keystroke onsets) versus continuous decoding that infers segmentation itself (CTC, asynchronous or sliding-window decoding). Boundary: event-locked training with continuous test-time decoding counts as continuous; reviews count as pattern matches only.
- Used in: [Brain-to-Text Decoding: A Non-invasive Approach via Typing](../../reviews/brain-to-text-decoding-a-non-invasive-approach-via-typing/)

## noninvasive-speech-decoding-objective

- Table: [`noninvasive-speech-decoding-objective.csv`](noninvasive-speech-decoding-objective.csv) (7345 slot-filled, 538 pattern match, usual design in 98, 6 read in full)
- Inclusion rule: Speech or language decoding studies from scalp EEG or MEG (perceived, imagined, attempted or overt). The design compared is the training objective of the decoder: contrastive alignment to a speech or text embedding with ranking of candidates, regression of an acoustic or feature target, or classification into fixed classes. Boundary: EEG/MEG used only as an auxiliary channel to another sensor still counts; reviews are excluded; versions count once.
- Used in: [Decoding speech perception from non-invasive brain recordings](../../reviews/decoding-speech-perception-from-non-invasive-brain-recordings/)

## phoneme-rnn-ctc-lm-decoding

- Table: [`phoneme-rnn-ctc-lm-decoding.csv`](phoneme-rnn-ctc-lm-decoding.csv) (7345 slot-filled, 97 pattern match, usual design in 61, 5 read in full)
- Inclusion rule: Neural or articulatory speech decoders that emit phoneme (or character) probabilities with a recurrent or CTC-trained network and convert them to words with an n-gram or neural language model. Included: sEMG, EEG, ECoG and intracortical; online or offline. Excluded: closed-set word classifiers and direct audio synthesis.
- Used in: [A high-performance neuroprosthesis for speech decoding and avatar control](../../reviews/a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control/), [A high-performance speech neuroprosthesis](../../reviews/a-high-performance-speech-neuroprosthesis/), [Brain2Char: a deep architecture for decoding text from brain recordings](../../reviews/brain2char-a-deep-architecture-for-decoding-text-from-brain-recordings/)

## video-to-speech-synthesis

- Table: [`video-to-speech-synthesis.csv`](video-to-speech-synthesis.csv) (7345 slot-filled, 165 pattern match, usual design in 49, 3 read in full)
- Inclusion rule: Include studies that synthesize a speech waveform from video of the talking face or lips (silent or with audio muted at test) and report the acoustic representation and how it is turned into a waveform. Boundary: exclude audio-visual speech enhancement or separation that takes noisy audio at test, talking-head generation (speech to video), text-only lip reading and video-to-text-to-TTS pipelines; count versions of one study once.
- Used in: [Lip2AudSpec: Speech Reconstruction from Silent Lip Movements Video](../../reviews/lip2audspec-speech-reconstruction-from-silent-lip-movements-video/)

## visual-frontend-spatial-pooling

- Table: [`visual-frontend-spatial-pooling.csv`](visual-frontend-spatial-pooling.csv) (7345 slot-filled, 1116 pattern match, usual design in 254, 5 read in full)
- Inclusion rule: Visual or audio-visual speech recognition studies (lip reading, VSR, AVSR; word or sentence level) whose ledger names lip reading, VSR, AVSR or an LRS/LRW benchmark. The design compared is how the per-frame spatial feature map of the visual front-end is reduced to a vector: global average pooling (or flatten) after a CNN/ResNet trunk, versus learned spatial attention or transformer pooling over the map. Boundary: temporal attention alone, attention used for audio-visual fusion, and ROI cropping are not spatial pooling; reviews count as pattern matches only; versions of one study count once.
- Used in: [Sub-word Level Lip Reading With Visual Attention](../../reviews/sub-word-level-lip-reading-with-visual-attention/)

## whisper-conversion-intermediate-representation

- Table: [`whisper-conversion-intermediate-representation.csv`](whisper-conversion-intermediate-representation.csv) (7345 slot-filled, 60 pattern match, usual design in 50, 5 read in full)
- Inclusion rule: Same population as M02/whisper-to-normal-training-pairing (unvoiced or whispered acoustic or body-conducted speech converted to voiced speech audio); classify the intermediate representation the converter maps through: frame-level spectral features (MCEP, mel spectrogram, GMM/DNN mapping), self-supervised speech units or features (HuBERT, wav2vec, ContentVec), or an ASR-to-TTS text cascade. Boundary: an SSL model used only for evaluation does not count; recognition-only and normal-to-whisper studies are excluded; count versions once.
- Used in: [WESPER: Zero-shot and Realtime Whisper to Normal Voice Conversion for Whisper-based Speech Interactions](../../reviews/wesper-zero-shot-and-realtime-whisper-to-normal-voice-conversion-for-whisper-based-speech-interactions/)
