# M03 Train / calibrate

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## adversarial-speaker-removal-from-signal-encoder

- Table: [`adversarial-speaker-removal-from-signal-encoder.csv`](adversarial-speaker-removal-from-signal-encoder.csv) (1526 slot-filled, 18 pattern match, usual design in 6, 3 read in full)
- Inclusion rule: Studies that decode speech or text from a non-acoustic speech signal (lip or face video, articulatory imaging, EMG, EEG/ECoG/intracortical) and train the signal encoder against a speaker, subject or session classifier (gradient reversal, entropy-maximising or confusion loss, mutual-information penalty, or a VAE split of identity and content) to remove identity from the content representation. Boundary: GAN discriminators on the generated audio, plain multi-speaker training, and speaker classifiers used only for evaluation are excluded; versions count once; the pattern match is an upper bound.
- Used in: [CAT-Net: A Cross-Attention Tone Network for Cross-Subject EEG-EMG Fusion Tone Decoding](../../reviews/cat-net-a-cross-attention-tone-network-for-cross-subject-eeg-emg-fusion-tone-decoding/), [Speaker disentanglement in video-to-speech conversion](../../reviews/speaker-disentanglement-in-video-to-speech-conversion/)

## articulatory-recognizer-speaker-adaptation

- Table: [`articulatory-recognizer-speaker-adaptation.csv`](articulatory-recognizer-speaker-adaptation.csv) (1526 slot-filled, 48 pattern match, usual design in 27, 4 read in full)
- Inclusion rule: Recognizers that decode text from non-acoustic speech signals (articulatory imaging, EMA, EMG, lip video, neural recordings) and apply speaker, session or speaking-mode adaptation of features or model (fMLLR/SAT, Procrustes normalization, unsupervised or test-time adaptation) and report an unadapted comparison. Boundary: acoustic-only ASR, synthesis without recognition, articulatory phonetics without a recognizer, reviews, and supervised retraining on the full target data are excluded; versions counted once.
- Used in: [Silent versus modal multi-speaker speech recognition from ultrasound and video](../../reviews/silent-versus-modal-multi-speaker-speech-recognition-from-ultrasound-and-video/)

## articulatory-speech-model-speaker-session-adaptation

- Table: [`articulatory-speech-model-speaker-session-adaptation.csv`](articulatory-speech-model-speaker-session-adaptation.csv) (1526 slot-filled, 93 pattern match, usual design in 17, 5 read in full)
- Inclusion rule: Models that map a non-acoustic speech signal (ultrasound, EMA or PMA, EMG, lip video, other wearable sensors) to speech, text or articulatory output and adapt a trained model to a new speaker or recording session with target data, reporting an unadapted or full-retraining comparison; classified by what is adapted (whole network, a layer subset, an input-space transform, or an input prompt/padding/embedding). Boundary: acoustic-only systems, speaker-independent training without an adaptation step, neural-recording calibration, tongue-contour tracking and reviews are excluded; versions counted once.
- Used in: [Adaptation of Tongue Ultrasound-Based Silent Speech Interfaces Using Spatial Transformer Networks](../../reviews/adaptation-of-tongue-ultrasound-based-silent-speech-interfaces-using-spatial-transformer-networks/)

## audio-only-decoder-pretraining

- Table: [`audio-only-decoder-pretraining.csv`](audio-only-decoder-pretraining.csv) (1526 slot-filled, 30 pattern match, usual design in 9, 3 read in full)
- Inclusion rule: Studies that synthesize speech from a non-acoustic signal (video, ultrasound, EMG, articulography, neural recordings) and pre-train the speech-generating part of the model (decoder, generator or speech autoencoder) on speech data without the non-acoustic signal, then transfer it into the signal-to-speech model. Boundary: an off-the-shelf pretrained vocoder used alone is counted separately (pretrained_vocoder_only), encoder-side self-supervised pre-training on the non-acoustic signal belongs to M03 self-supervised-pretraining, audio-visual paired pre-training (VoxCeleb2) is counted separately, knowledge distillation into a visual encoder belongs to M02 audio-knowledge-transfer-to-video; full-text design counts are pattern matches (upper bounds, mentions included); versions counted once.
- Used in: [Large-scale unsupervised audio pre-training for video-to-speech synthesis](../../reviews/large-scale-unsupervised-audio-pre-training-for-video-to-speech-synthesis/)

## cross-subject-pooled-training

- Table: [`cross-subject-pooled-training.csv`](cross-subject-pooled-training.csv) (1526 slot-filled, 370 pattern match, usual design in 90, 4 read in full)
- Inclusion rule: Speech or language decoders from neural or other biosignals that train one model on data pooled across participants, with or without participant-specific layers or embeddings. Boundary: a per-participant model that only reports results averaged over participants is excluded; transfer by fine-tuning from another participant counts; versions of one study count once.
- Used in: [A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses](../../reviews/a-convolutional-framework-for-mapping-imagined-auditory-meg-into-listened-brain-responses/), [A cross-species neural foundation model for end-to-end speech decoding](../../reviews/a-cross-species-neural-foundation-model-for-end-to-end-speech-decoding/), [A Silent Speech Decoding System from EEG and EMG with Heterogenous Electrode Configurations](../../reviews/a-silent-speech-decoding-system-from-eeg-and-emg-with-heterogenous-electrode-configurations/), [Decoding speech perception from non-invasive brain recordings](../../reviews/decoding-speech-perception-from-non-invasive-brain-recordings/), [Multi-Subject Pretraining Enables Short-Calibration Personalization for Closed-Corpus Surface EMG Speech Decoding](../../reviews/multi-subject-pretraining-enables-short-calibration-personalization-for-closed-corpus-surface-emg-speech-decoding/), [MultiDiffNet: A Multi-Objective Diffusion Framework for Generalizable Brain Decoding](../../reviews/multidiffnet-a-multi-objective-diffusion-framework-for-generalizable-brain-decoding/), [Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping](../../reviews/zero-shot-imagined-speech-decoding-via-imagined-to-listened-meg-mapping/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Multi-Subject Pretraining Enables Short-Calibration Personalization for Closed-Corpus Surface EMG Speech Decoding | 2026 | Sec. 3.2 |

## eeg-user-identification

- Table: [`eeg-user-identification.csv`](eeg-user-identification.csv) (1526 slot-filled, 6 pattern match, usual design in 6, 3 read in full)
- Inclusion rule: Studies in the wiki that identify the user (subject identification, biometric authentication) from scalp EEG; the design compared is identification from speech-imagery trials and how identification is tested (session-held-out vs trials permuted across sessions). Boundary: identification used only as a nuisance factor is excluded; versions count once; the target is counted in the pattern match.
- Used in: [Toward Practical BCI: A Real-time Wireless Imagined Speech EEG Decoding System](../../reviews/toward-practical-bci-a-real-time-wireless-imagined-speech-eeg-decoding-system/)

## emg-cross-session-recalibration

- Table: [`emg-cross-session-recalibration.csv`](emg-cross-session-recalibration.csv) (1526 slot-filled, 41 pattern match, usual design in 11, 3 read in full)
- Inclusion rule: Surface-EMG speech or silent-speech decoders tested on a recording session or day not used for training (electrodes re-attached), classified by how the session shift is handled: no recalibration, supervised fine-tuning or retraining on new-session data, or unsupervised/feature-level adaptation. Boundary: same-session random splits only, cross-speaker transfer without a session test, non-EMG sensors, and reviews are excluded when read; versions once.
- Used in: [SilentWear: an Ultra-Low Power Wearable System for EMG-based Silent Speech Recognition](../../reviews/silentwear-an-ultra-low-power-wearable-system-for-emg-based-silent-speech-recognition/)

## emg-cross-speaker-training-and-calibration

- Table: [`emg-cross-speaker-training-and-calibration.csv`](emg-cross-speaker-training-and-calibration.csv) (1526 slot-filled, 64 pattern match, usual design in 40, 3 read in full)
- Inclusion rule: Surface-EMG speech decoders (recognition, classification or synthesis) that train on data from several speakers and test on a speaker held out of that training pool, with or without target-speaker calibration or adaptation. Boundary: per-speaker models averaged over speakers and pooled training with speaker-mixed random splits are excluded; session-only adaptation within one speaker is excluded; EEG-EMG fusion counts when EMG is a decoder input; reviews count as pattern matches only; versions of one study count once.
- Used in: [Multi-Subject Pretraining Enables Short-Calibration Personalization for Closed-Corpus Surface EMG Speech Decoding](../../reviews/multi-subject-pretraining-enables-short-calibration-personalization-for-closed-corpus-surface-emg-speech-decoding/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Multi-Subject Pretraining Enables Short-Calibration Personalization for Closed-Corpus Surface EMG Speech Decoding | 2026 | Sec. 3.2 |
| Personalizing Myoelectric Silent Speech Interfaces via Cross-Speaker Training and Voice Timbre Control | 2026 | Scheck et al. 2024, Sec. IV-B |
| A novel silent speech recognition approach based on parallel inception convolutional neural network and Mel frequency spectral coefficient |  | Sec. 5 |
| Towards Speaker-Adaptive Speech Recognition Based on Surface Electromyography | 2008 | Sec. 3.4 |

## imagenet-pretrained-vision-backbone-neural-speech

- Table: [`imagenet-pretrained-vision-backbone-neural-speech.csv`](imagenet-pretrained-vision-backbone-neural-speech.csv) (1526 slot-filled, 8 pattern match, usual design in 5, 3 read in full)
- Inclusion rule: Speech or language decoders from EEG, MEG or intracranial recordings that initialize a vision backbone pretrained on natural images (ImageNet CNN or ViT) and fine-tune it, or train a head on it, using time-frequency or other image-like neural inputs. Boundary: decoding of images viewed during EEG (ImageNet as stimulus set) is excluded; non-speech imagery (e.g. visual arrows) and reviews remain as pattern matches (upper bound); versions of one study count once.
- Used in: [Transfer Learning from ImageNet for MEG-Based Decoding of Imagined Speech](../../reviews/transfer-learning-from-imagenet-for-meg-based-decoding-of-imagined-speech/)

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

## modality-dropout-training

- Table: [`modality-dropout-training.csv`](modality-dropout-training.csv) (1526 slot-filled, 21 pattern match, usual design in 38, 2 read in full)
- Inclusion rule: Include studies that train a multimodal speech model (audio-visual or other paired modalities) while randomly withholding one input modality for whole training examples or sequences (modality dropout), so the model also works from either modality alone. Boundary: frame-level masking inside one modality, ordinary feature dropout, and papers that only cite modality dropout without using it are excluded; counts are pattern match over ledger text and full text (reference lists removed), grouped into unique studies by title.
- Used in: [Audio-visual video-to-speech synthesis with synthesized input audio](../../reviews/audio-visual-video-to-speech-synthesis-with-synthesized-input-audio/), [Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading](../../reviews/cross-modal-masking-for-robust-silent-speech-synthesis-using-semg-and-lipreading/)

## neural-foundation-model-speech-transfer

- Table: [`neural-foundation-model-speech-transfer.csv`](neural-foundation-model-speech-transfer.csv) (1526 slot-filled, 40 pattern match, usual design in 28, 2 read in full)
- Inclusion rule: Speech or language decoders from EEG, MEG or intracranial recordings that initialize from a checkpoint pretrained on large neural corpora (a neural foundation model) and fine-tune it for word, phrase, sentence or speech-feature decoding. Boundary: speech-audio or video foundation models are excluded; reviews and dataset papers that only mention foundation models still count as pattern matches (upper bound); versions of one study count once.
- Used in: [Do EEG Foundation Models Transfer to Speech? A Benchmark on Overt and Imagined Speech Decoding](../../reviews/do-eeg-foundation-models-transfer-to-speech-a-benchmark-on-overt-and-imagined-speech-decoding/)

## neural-signal-training-augmentation

- Table: [`neural-signal-training-augmentation.csv`](neural-signal-training-augmentation.csv) (1526 slot-filled, 45 pattern match, usual design in 12, 2 read in full)
- Inclusion rule: Speech or language decoders from EEG, MEG, ECoG, sEEG or intracortical recordings that perturb or remix real training recordings to enlarge or regularize the training set (additive noise, shifts and crops, masking or channel dropout, scaling, mixup, injection of artifact or reference-channel signals). Boundary: signals generated by a model from speech or text belong to M03/synthetic-biosignal-training-data and are excluded; augmenting only the audio or text target is excluded; artifact removal without re-injection is excluded; reviews remain as pattern matches (upper bound); versions of one study count once.
- Used in: [Physiological Noise Augmentation Improves Non-Invasive Brain-to-Speech](../../reviews/physiological-noise-augmentation-improves-non-invasive-brain-to-speech/)

## overt-silent-joint-training

- Table: [`overt-silent-joint-training.csv`](overt-silent-joint-training.csv) (1526 slot-filled, 354 pattern match, usual design in 31, 5 read in full)
- Inclusion rule: Studies with any signal (video, ultrasound, EMG, neural, other) whose ledger mentions both overt (normal, vocalized, voiced, audible, modal) and silent (mouthed, silently articulated, unvoiced) speech production. The design compared is how overt recordings enter the training of a silent-speech decoder: pooled training without a cross-mode term, fine-tuning from an overt model, time-aligned target transfer (DTW / CCA from vocalized to silent), domain-adversarial invariance, or an explicit distance or divergence between paired overt and silent representations or outputs (metric learning, KL, contrastive, triplet). Boundary: overt-only training applied to silent test data belongs to M04 overt-to-silent-transfer; whisper-to-normal acoustic conversion and perception-versus-production comparisons are excluded; a study counts under every design its full text names (upper bound, related-work mentions included); reviews count as pattern matches only; versions of one study count once.
- Used in: [Improving the Gap in Visual Speech Recognition Between Normal and Silent Speech Based on Metric Learning](../../reviews/improving-the-gap-in-visual-speech-recognition-between-normal-and-silent-speech-based-on-metric-learning/), [SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces](../../reviews/sonispeech-a-large-scale-open-vocabulary-tri-modal-dataset-for-wearable-silent-speech-interfaces/)

## self-supervised-pretraining

- Table: [`self-supervised-pretraining.csv`](self-supervised-pretraining.csv) (1526 slot-filled, 123 pattern match, usual design in 31, 3 read in full)
- Inclusion rule: Include studies that pre-train an encoder on unlabelled non-audio-only input (video, audio-visual, biosignal or neural recordings) with a self-supervised or teacher-generated objective (masked prediction, contrastive, feature regression, cross-modal distillation) before supervised fine-tuning for speech or text decoding. Boundary: exclude audio-only self-supervised ASR; exclude studies that only reuse a released pre-trained checkpoint without training a new objective; count versions of one study once.
- Used in: [Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction](../../reviews/learning-audio-visual-speech-representation-by-masked-multimodal-cluster-prediction/), [Pretraining Large Brain Language Model for Active BCI: Silent Speech](../../reviews/pretraining-large-brain-language-model-for-active-bci-silent-speech/), [Visual Speech Recognition for Multiple Languages in the Wild](../../reviews/visual-speech-recognition-for-multiple-languages-in-the-wild/)

## speaker-embedding-conditioning

- Table: [`speaker-embedding-conditioning.csv`](speaker-embedding-conditioning.csv) (1526 slot-filled, 42 pattern match, usual design in 20, 4 read in full)
- Inclusion rule: Studies that decode speech or text from a non-acoustic speech signal (articulatory imaging, EMA/PMA, EMG, lip or face video, neural recordings) with one model shared across speakers that is conditioned on a per-speaker or per-utterance embedding (x-vector, i-vector, d-vector/GE2E, speaker-encoder output, learned subject embedding). Boundary: acoustic-only systems, audio-visual enhancement or separation with noisy audio at test, speaker embeddings used only as an output-similarity metric, and reviews are excluded (they inflate the pattern match, an upper bound); versions count once.
- Used in: [Neural Speaker Embeddings for Ultrasound-based Silent Speech Interfaces](../../reviews/neural-speaker-embeddings-for-ultrasound-based-silent-speech-interfaces/), [Speaker disentanglement in video-to-speech conversion](../../reviews/speaker-disentanglement-in-video-to-speech-conversion/)

## speech-bci-calibration-data

- Table: [`speech-bci-calibration-data.csv`](speech-bci-calibration-data.csv) (1526 slot-filled, 51 pattern match, usual design in 4, 3 read in full)
- Inclusion rule: Neural speech-decoding studies (intracortical, ECoG, sEEG, EEG) that state how much same-participant calibration or training data the decoder needs, or how it is recalibrated across days. Included: daily supervised recalibration, cumulative multi-day training, unsupervised or no recalibration, cross-participant pretraining. Excluded: non-neural silent-speech sensors; perception-only recalibration studies; cursor or handwriting BCIs unless they decode speech.
- Used in: [An Accurate and Rapidly Calibrating Speech Neuroprosthesis](../../reviews/an-accurate-and-rapidly-calibrating-speech-neuroprosthesis/)

## synthetic-biosignal-training-data

- Table: [`synthetic-biosignal-training-data.csv`](synthetic-biosignal-training-data.csv) (1526 slot-filled, 13 pattern match, usual design in 8, 3 read in full)
- Inclusion rule: Include speech or language decoders (recognition or synthesis) from a non-acoustic speech signal (EMG, EEG, ECoG, ultrasound, articulography, MRI, lip or face video) that are trained on input signals generated by a model from speech, text or another signal, alone or mixed with real recordings. Boundary: signal-level augmentation of real recordings (noise, warping, channel dropout, SpecAugment) is excluded; synthetic target speech is M02 and excluded; speech-to-articulation or talking-face generators that are not used to train a decoder count as pattern matches only; versions of one study count once.
- Used in: [Confidence-Based Self-Training for EMG-to-Speech: Leveraging Synthetic EMG for Robust Modeling](../../reviews/confidence-based-self-training-for-emg-to-speech-leveraging-synthetic-emg-for-robust-modeling/)
