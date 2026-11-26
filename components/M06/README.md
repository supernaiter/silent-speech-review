# M06 Decoding

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## air-and-body-conducted-channel-fusion

- Table: [`air-and-body-conducted-channel-fusion.csv`](air-and-body-conducted-channel-fusion.csv) (7345 slot-filled, 68 pattern match, usual design in 42, 2 read in full)
- Inclusion rule: Speech studies that feed an air-microphone channel and a skin-, bone- or tissue-conducted channel from the same talker into one model or feature mapping (enhancement, conversion or recognition). Boundary: systems that use the conducted channel only for voice activity detection are counted by pattern only; reviews count as pattern matches; versions count once.
- Used in: [NasoVoce: A Nose-Mounted Low-Audibility Speech Interface for Always-Available Speech Interaction](../../reviews/nasovoce/)

## articulator-video-spatiotemporal-front-end

- Table: [`articulator-video-spatiotemporal-front-end.csv`](articulator-video-spatiotemporal-front-end.csv) (7345 slot-filled, 1342 pattern match, usual design in 380, 5 read in full)
- Inclusion rule: Include studies that decode text, speech or acoustic features from video of the articulators (lip or face camera, ultrasound tongue imaging) with a trained network, and classify how temporal context enters the image front end: 3D (spatiotemporal) convolution over a frame stack, factorized (2+1)D convolution, a frame-wise 2D CNN followed by a recurrent layer, a temporal convolution network, or ConvLSTM. Boundary: hand-crafted features without a learned front end, audio-only models, contour tracking without speech output and reviews still count as pattern matches (an upper bound); a study can match several designs; versions count once by key.
- Used in: [3D Convolutional Neural Networks for Ultrasound-Based Silent Speech Interfaces](../../reviews/3d-convolutional-neural-networks-for-ultrasound-based-silent-speech-interfaces/), [FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis](../../reviews/fastlts-non-autoregressive-end-to-end-unconstrained-lip-to-speech-synthesis/), [Silent Speech and Emotion Recognition from Vocal Tract Shape Dynamics in Real-Time MRI](../../reviews/silent-speech-and-emotion-recognition-from-vocal-tract-shape-dynamics-in-real-time-mri/)

## articulatory-intermediate

- Table: [`articulatory-intermediate.csv`](articulatory-intermediate.csv) (7345 slot-filled, 12 pattern match, usual design in 2, 44 read in full)
- Inclusion rule: Include studies with a decoding pathway that first decodes an explicit articulatory representation (measured or estimated movement trajectories of the articulators, articulatory features or phonological categories) from non-acoustic signals (neural activity, EMG, video, ultrasound, etc.) and then converts it in a next stage to acoustic features, speech waveforms or symbol sequences. Boundary: exclude those whose input itself is an articulatory measurement (EMA, PMA, ultrasound) and that do not decode an articulatory representation as an intermediate. Exclude those that estimate articulation from acoustics and then return to speech (acoustic input). Exclude those that use articulation only as an auxiliary loss or regularization without placing it in the middle of the pathway. Exclude those that only decode an articulatory representation with no next stage. Exclude mentions in reviews or citations only. Count different versions of the same study as one item.
- Used in: [Articulatory Feature Prediction from Surface EMG during Speech Production](../../reviews/articulatory-feature-prediction-from-surface-emg-during-speech-production/), [Speech synthesis from neural decoding of spoken sentences](../../reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences/)

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

## avsr-audio-stream-input-representation

- Table: [`avsr-audio-stream-input-representation.csv`](avsr-audio-stream-input-representation.csv) (7345 slot-filled, 349 pattern match, usual design in 182, 4 read in full)
- Inclusion rule: Studies whose ledger names audio-visual speech recognition (AVSR), classified by the audio-stream input their full text names: raw waveform fed to a learned front-end, or hand-designed spectral features (log-Mel filterbank, MFCC, spectrogram). Boundary: a study counts under every representation its text names (upper bound); visual-only lip reading without an audio stream is out; audio-visual speech enhancement without recognition is out unless the ledger names AVSR; versions count once by key.
- Used in: [End-to-End Audio-Visual Speech Recognition with Conformers](../../reviews/end-to-end-audio-visual-speech-recognition-with-conformers/), [End-to-End Audiovisual Speech Recognition](../../reviews/end-to-end-audiovisual-speech-recognition/), [Recurrent Neural Network Transducer for Audio-Visual Speech Recognition](../../reviews/recurrent-neural-network-transducer-for-audio-visual-speech-recognition/)

## causal-closed-loop-speech-synthesis

- Table: [`causal-closed-loop-speech-synthesis.csv`](causal-closed-loop-speech-synthesis.csv) (7345 slot-filled, 87 pattern match, usual design in 24, 3 read in full)
- Inclusion rule: Studies that synthesize speech acoustics from a non-acoustic signal (neural, EMG, articulography, ultrasound, video) online, in real time, with the audio played back to the user while or right after they speak. Boundary: include formant or vocoder synthesis of vowels, words or sentences, and offline studies only when they simulate causal frame-level inference; exclude offline acausal reconstruction, text decoding read out by TTS, and conversion from acoustic input; count versions once.
- Used in: [A Wireless Brain-Machine Interface for Real-Time Speech Synthesis](../../reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis/), [An instantaneous voice-synthesis neuroprosthesis](../../reviews/an-instantaneous-voice-synthesis-neuroprosthesis/), [Brain2Speech-Net: Fast and Intelligible Brain-to-Speech Synthesis Without Text Decoding](../../reviews/brain2speech-net-intelligible-real-time-brain-to-speech-synthesis-without-text-decoding/)

## closed-vocabulary-word-classification

- Table: [`closed-vocabulary-word-classification.csv`](closed-vocabulary-word-classification.csv) (7345 slot-filled, 360 pattern match, usual design in 82, 2 read in full)
- Inclusion rule: Studies that decode words or utterances from non-acoustic signals (neural, EMG, articulatory, video) by classifying each detected segment into a closed set of at most a few hundred words or utterances, with or without a language-model or context prior over the sequence. Boundary: open-vocabulary phoneme or character decoders are excluded unless they also report a closed-set word test; acoustic-only ASR is excluded.
- Used in: [Knowledge Distilled Ensemble Model for sEMG-based Silent Speech Interface](../../reviews/knowledge-distilled-ensemble-model-for-semg-based-silent-speech-interface/), [Neuroprosthesis for decoding speech in a paralyzed person with anarthria](../../reviews/neuroprosthesis-for-decoding-speech-in-a-paralyzed-person-with-anarthria/), [Real-time decoding of question-and-answer speech dialogue using human cortical activity](../../reviews/real-time-decoding-of-question-and-answer-speech-dialogue-using-human-cortical-activity/), [Ultrasensitive Textile Strain Sensors Redefine Wearable Silent Speech Interfaces with High Machine Learning Efficiency](../../reviews/ultrasensitive-textile-strain-sensors-redefine-wearable-silent-speech-interfaces-with-high-machine-learning-efficiency/), [Wireless Silent Speech Interface Using Multi-Channel Textile EMG Sensors Integrated into Headphones](../../reviews/wireless-silent-speech-interface-using-multi-channel-textile-emg-sensors-integrated-into-headpho/)

## ctc-vs-attention

- Table: [`ctc-vs-attention.csv`](ctc-vs-attention.csv) (7345 slot-filled, 114 pattern match, usual design in 79, 42 read in full)
- Inclusion rule: Include studies that train, on the same input front end (visual, biosignal, or audio-visual), both a decoder trained with CTC and an attention/sequence-to-sequence decoder (seq2seq or Transformer decoder) and compare the results side by side. Boundary: exclude those that use only the CTC-attention combination (hybrid) with no result for either alone. Exclude comparisons that only list numbers from other papers. Audio-only ASR is outside the wiki and out of scope. Count different versions of the same study as one item.
- Used in: [Deep Audio-Visual Speech Recognition](../../reviews/deep-audio-visual-speech-recognition/), [End-to-End Silent Speech Recognition with Acoustic Sensing](../../reviews/end-to-end-silent-speech-recognition-with-acoustic-sensing/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Deep Lip Reading: a comparison of models and an online application |  | §3.3, Table 1 |
| State-of-the-art Speech Recognition using EEG and Towards Decoding of Speech Spectrum From EEG | 2020 | §2 |
| End-to-end Silent Speech Recognition with Acoustic Sensing |  | §4.4, Fig. 4(c) |
| End-to-end Silent Speech Recognition with Acoustic Sensing |  | §4.4, Fig. 4(c) |

## decoder-internal-interpretability

- Table: [`decoder-internal-interpretability.csv`](decoder-internal-interpretability.csv) (7345 slot-filled, 38 pattern match, usual design in 32, 1 read in full)
- Inclusion rule: Studies that analyse what a trained decoder of speech from a non-acoustic or acoustic signal (neural, EMG, articulatory, video, audio) relies on, by input attribution (saliency, gradients, occlusion, channel importance), probing of hidden layers, or interventions on internal activations (activation patching, unit ablation, causal scrubbing). Boundary: architecture ablations that retrain model variants and brain-mapping studies without a trained decoder are excluded; versions of one study count once; ledger pattern matches are an upper bound.
- Used in: [Mechanistic Interpretability of Brain-to-Speech Models Across Speech Modes](../../reviews/mechanistic-interpretability-of-brain-to-speech-models-across-speech-modes/)

## diffusion-model-eeg-decoding

- Table: [`diffusion-model-eeg-decoding.csv`](diffusion-model-eeg-decoding.csv) (7345 slot-filled, 13 pattern match, usual design in 3, 3 read in full)
- Inclusion rule: EEG decoding studies (classification, text or speech decoding) that train a denoising diffusion model as part of the decoder, either jointly with a classifier, as a feature learner, or to generate training samples. Boundary: diffusion used only to synthesize EEG with no decoding result, reviews, and 'diffusion' in a non-generative sense (drift-diffusion, diffusion MRI) are excluded; versions of one study count once.
- Used in: [Lightweight Diffusion-based Framework for Online Imagined Speech Decoding in Aphasia](../../reviews/lightweight-diffusion-based-framework-for-online-imagined-speech-decoding-in-aphasia/), [MultiDiffNet: A Multi-Objective Diffusion Framework for Generalizable Brain Decoding](../../reviews/multidiffnet-a-multi-objective-diffusion-framework-for-generalizable-brain-decoding/)

## eeg-emg-fusion-architecture

- Table: [`eeg-emg-fusion-architecture.csv`](eeg-emg-fusion-architecture.csv) (7345 slot-filled, 30 pattern match, usual design in 8, 2 read in full)
- Inclusion rule: Speech, tone or articulation decoders that record scalp EEG together with surface EMG and combine the two inside one model; the design value is the fusion form named in the full text (cross-modal or bidirectional attention, feature concatenation, late or decision-level fusion), and studies that record EMG only as an EEG artifact are counted separately. Boundary: non-speech EEG-EMG fusion (limb movement), reviews and datasets without decoding are excluded from the usual-approach reading but stay in the pattern-match population; versions of one study count once.
- Used in: [CAT-Net: A Cross-Attention Tone Network for Cross-Subject EEG-EMG Fusion Tone Decoding](../../reviews/cat-net-a-cross-attention-tone-network-for-cross-subject-eeg-emg-fusion-tone-decoding/)

## emg-speech-encoder-input-and-sequence-model

- Table: [`emg-speech-encoder-input-and-sequence-model.csv`](emg-speech-encoder-input-and-sequence-model.csv) (7345 slot-filled, 83 pattern match, usual design in 18, 3 read in full)
- Inclusion rule: Surface-EMG speech decoders (synthesis or recognition) classified by input representation (hand-crafted time-domain features vs learned convolution over minimally filtered EMG) and sequence model (feed-forward, recurrent, Transformer or Conformer). Boundary: EMG used only as an auxiliary channel to audio, gesture or non-speech EMG, and reviews are excluded; versions counted once.
- Used in: [An Improved Model for Voicing Silent Speech](../../reviews/an-improved-model-for-voicing-silent-speech/), [Non-invasive electromyographic speech neuroprosthesis: a geometric perspective](../../reviews/non-invasive-electromyographic-speech-neuroprosthesis-a-geometric-perspective/)

## emg-to-speech-intermediate-target

- Table: [`emg-to-speech-intermediate-target.csv`](emg-to-speech-intermediate-target.csv) (7345 slot-filled, 54 pattern match, usual design in 37, 4 read in full)
- Inclusion rule: Surface-EMG speech synthesis or voicing studies (EMG to audible speech), classified by the intermediate target the EMG model predicts before the waveform: spectral acoustic features (mel, MFCC, vocoder parameters), self-supervised speech units, articulatory features (EMA-type trajectories), or text/phonemes. Boundary: EMG recognition to text only, EMG as an auxiliary channel to audio, non-speech EMG and reviews are excluded when read; a study can use several targets; versions count once.
- Used in: [Articulatory Feature Prediction from Surface EMG during Speech Production](../../reviews/articulatory-feature-prediction-from-surface-emg-during-speech-production/), [emg2speech: Synthesizing speech from electromyography using self-supervised speech models](../../reviews/emg2speech-synthesizing-speech-from-electromyography-using-self-supervised-speech-models/)

## emg-to-speech-timing-alignment

- Table: [`emg-to-speech-timing-alignment.csv`](emg-to-speech-timing-alignment.csv) (7345 slot-filled, 76 pattern match, usual design in 28, 4 read in full)
- Inclusion rule: Surface-EMG-to-speech synthesis studies (audio or acoustic-feature output), classified by how the EMG time axis is mapped to the audio target: frame-synchronous regression on DTW-aligned targets, explicit duration prediction with a length regulator, or attention-based sequence-to-sequence. Boundary: EMG-to-text recognition, EMG used only as an auxiliary channel to audio, and reviews are excluded; versions counted once; pattern-match counts are upper bounds.
- Used in: [Sequence-to-Sequence Voice Reconstruction for Silent Speech in a Tonal Language](../../reviews/sequence-to-sequence-voice-reconstruction-for-silent-speech-in-a-tonal-language/)

## generative-text-decoder-vsr

- Table: [`generative-text-decoder-vsr.csv`](generative-text-decoder-vsr.csv) (7345 slot-filled, 740 pattern match, usual design in 131, 2 read in full)
- Inclusion rule: Visual or audio-visual speech recognition (text output from lip video or lip event streams) and the decoders they use. The design compared is the text decoder: CTC, attention encoder-decoder, hybrid CTC/attention, LLM decoder, or an iterative generative decoder (diffusion, flow matching) that produces the transcript. Boundary: diffusion or flow models that generate speech audio or lip video (video-to-speech, data synthesis such as LipGen or SynthVSR) are not text decoders and count under their recognizer; versions of one study count once.
- Used in: [A First Exploration of Neuromorphic OT-CFM for Multi-Speaker VSR](../../reviews/lipsflow-a-first-exploration-of-neuromorphic-ot-cfm-for-multi-speaker-vsr/)

## heard-speech-reconstruction-target-representation

- Table: [`heard-speech-reconstruction-target-representation.csv`](heard-speech-reconstruction-target-representation.csv) (7345 slot-filled, 64 pattern match, usual design in 24, 4 read in full)
- Inclusion rule: Studies whose ledger text names intracranial or auditory-cortex recordings, a listening or perception condition, an acoustic representation (spectrogram, temporal modulation, envelope or vocoder features) and reconstruction, decoding or synthesis. The design of interest is the acoustic representation that the decoder reconstructs from neural activity during heard speech: auditory/linear spectrogram, temporal-modulation energy, envelope only, or vocoder parameters. Boundary: production-only synthesis studies and encoding-only studies admitted by the pattern are counted but are not heard-speech reconstruction; full-text design regexes overlap and are upper bounds; versions of one study count once.
- Used in: [Reconstructing Speech from Human Auditory Cortex](../../reviews/reconstructing-speech-from-human-auditory-cortex/), [Towards reconstructing intelligible speech from the human auditory cortex](../../reviews/towards-reconstructing-intelligible-speech-from-the-human-auditory-cortex/)

## heterogeneous-electrode-configuration-input

- Table: [`heterogeneous-electrode-configuration-input.csv`](heterogeneous-electrode-configuration-input.csv) (7345 slot-filled, 98 pattern match, usual design in 25, 2 read in full)
- Inclusion rule: Speech or language decoders from neural or muscle signals (EEG, MEG, ECoG, sEEG, EMG) that train one model on recordings whose channel count or electrode layout differs across participants, devices or datasets, by mapping channels into a shared space (sensor-position spatial attention or coordinate embeddings, per-subject or per-layout input layers, graph models over electrodes, channel tokens, or a common channel subset). Boundary: a model trained and tested on one fixed montage is excluded even when pooled over subjects; channel-subset selection within one array is excluded; auditory-attention and non-speech EEG models are excluded when read; versions of one study count once.
- Used in: [A Silent Speech Decoding System from EEG and EMG with Heterogenous Electrode Configurations](../../reviews/a-silent-speech-decoding-system-from-eeg-and-emg-with-heterogenous-electrode-configurations/), [Towards Unified Neural Decoding with Brain Functional Network Modeling](../../reviews/towards-unified-neural-decoding-with-brain-functional-network-modeling/)

## imagined-speech-eeg-word-classification

- Table: [`imagined-speech-eeg-word-classification.csv`](imagined-speech-eeg-word-classification.csv) (7345 slot-filled, 167 pattern match, usual design in 48, 2 read in full)
- Inclusion rule: Studies that classify imagined, covert or inner speech from scalp EEG into a closed set of words, syllables or commands and report accuracy. Boundary: overt-only EEG, EEG-plus-EMG fusion where EEG is not reported alone, perception-only decoding and reviews are excluded; intracranial recordings are excluded; versions count once.
- Used in: [Do EEG Foundation Models Transfer to Speech? A Benchmark on Overt and Imagined Speech Decoding](../../reviews/do-eeg-foundation-models-transfer-to-speech-a-benchmark-on-overt-and-imagined-speech-decoding/), [EEG-Based Imagined Speech Decoding Using a Hybrid CNN-SNN Architecture](../../reviews/eeg-based-imagined-speech-decoding-using-a-hybrid-cnn-snn-architecture/), [Pretraining Large Brain Language Model for Active BCI: Silent Speech](../../reviews/pretraining-large-brain-language-model-for-active-bci-silent-speech/), [Toward Practical BCI: A Real-time Wireless Imagined Speech EEG Decoding System](../../reviews/toward-practical-bci-a-real-time-wireless-imagined-speech-eeg-decoding-system/), [Transfer Learning for Covert Speech Classification Using EEG Hilbert Envelope and Temporal Fine Structure](../../reviews/transfer-learning-for-covert-speech-classification-using-eeg-hilbert-envelope-and-temporal-fine-/)

## imagined-speech-meg-classification

- Table: [`imagined-speech-meg-classification.csv`](imagined-speech-meg-classification.csv) (7345 slot-filled, 43 pattern match, usual design in 8, 4 read in full)
- Inclusion rule: Studies that decode imagined, covert or inner speech (or contrast it with other conditions) from MEG and report a classification score. Boundary: perceived-speech-only and overt-only MEG decoding are excluded; EEG-only studies are excluded; reviews remain as pattern matches (upper bound); versions of one study count once.
- Used in: [Transfer Learning from ImageNet for MEG-Based Decoding of Imagined Speech](../../reviews/transfer-learning-from-imagenet-for-meg-based-decoding-of-imagined-speech/)

## intracortical-cursor-click-communication-decoder

- Table: [`intracortical-cursor-click-communication-decoder.csv`](intracortical-cursor-click-communication-decoder.csv) (7345 slot-filled, 33 pattern match, usual design in 10, 4 read in full)
- Inclusion rule: Intracortical BCI studies (ledger population: 33 unique studies (46 folders) whose ledger text names an intracortical recording (intracortical, Utah array, microelectrode array) together with cursor, point-and-click, keyboard, typing, text entry, characters per minute, ccpm or grid task); the design compared is the decoder that turns neural activity into text-entry selections: continuous Kalman-family cursor decoder (ReFIT-KF or Kalman filter), discrete click decoder (HMM or LDA state classifier), dwell selection, recurrent-network decoders of characters or words. Boundary: full-text pattern counts with the reference list removed, so related-work mentions and reviews count (upper bound); a study counts under every design it names; the target is included; versions counted once.
- Used in: [High performance communication by people with paralysis using an intracortical brain-computer interface](../../reviews/high-performance-communication-by-people-with-paralysis-using-an-intracortical-brain-computer-interf/)

## intracranial-phoneme-inventory-classification

- Table: [`intracranial-phoneme-inventory-classification.csv`](intracranial-phoneme-inventory-classification.csv) (7345 slot-filled, 101 pattern match, usual design in 4, 5 read in full)
- Inclusion rule: Studies whose ledger text names an intracranial signal (ECoG, sEEG, intracortical, Utah array) together with phonemes, vowels, consonants or syllables (the population of the published topic intracranial-speech-unit-classification); the design of interest is the size of the speech-unit class set: the full phoneme inventory of a language (all phonemes, 38-44 classes) versus a small subset of two to six phonemes, vowels or syllables. Boundary: listening-only, mapping-only and review papers matched by the pattern stay in the count (upper bound); a study counts under every design its full text names; versions of one study count once; usual approach judged on studies first public before 2013-11 (more than six months before the target).
- Used in: [Direct classification of all American English phonemes using signals from functional speech motor cortex](../../reviews/direct-classification-of-all-american-english-phonemes-using-signals-from-functional-speech-motor-co/)

## intracranial-speech-unit-classification

- Table: [`intracranial-speech-unit-classification.csv`](intracranial-speech-unit-classification.csv) (7345 slot-filled, 101 pattern match, usual design in 2, 3 read in full)
- Inclusion rule: Studies whose ledger text names an intracranial signal (ECoG, sEEG, intracortical, Utah array) together with phonemes, vowels, consonants or syllables; the design of interest is whether speech units are decoded from each electrode separately (with the best location reported) or from several electrodes jointly. Boundary: listening-only and review papers matched by the pattern stay in the count (upper bound); word-level intracranial decoders are outside the pattern and are used only as read priors; versions of one study count once; usual approach judged on studies first public before 2011.
- Used in: [Decoding Vowels and Consonants in Spoken and Imagined Words Using Electrocorticographic Signals in Humans](../../reviews/decoding-vowels-and-consonants-in-spoken-and-imagined-words-using-electrocorticographic-signals-in-h/)

## intracranial-synthesis-decoder-architecture

- Table: [`intracranial-synthesis-decoder-architecture.csv`](intracranial-synthesis-decoder-architecture.csv) (7345 slot-filled, 180 pattern match, usual design in 79, 4 read in full)
- Inclusion rule: Studies that reconstruct speech acoustics from intracranial recordings made during overt, mouthed, attempted or imagined speech (the published intracranial-synthesis population pattern), classified by the neural-to-acoustic regression model their full text names: linear or regularized linear regression, recurrent network (LSTM/GRU), transformer, 3D convolution, DenseNet, unit selection. Boundary: a study counts under every design its full text names, including related-work mentions, so counts are upper bounds; heard-speech reconstruction and text-only decoders read out by TTS are outside the topic; versions of one study count once.
- Used in: [Speech Synthesis from ECoG using Densely Connected 3D Convolutional Neural Networks](../../reviews/speech-synthesis-from-ecog-using-densely-connected-3d-convolutional-neural-networks/)

## intracranial-synthesis-neural-features

- Table: [`intracranial-synthesis-neural-features.csv`](intracranial-synthesis-neural-features.csv) (7345 slot-filled, 180 pattern match, usual design in 62, 3 read in full)
- Inclusion rule: Include studies that reconstruct speech acoustics (spectrograms, vocoder features or waveforms) from intracranial recordings (ECoG, sEEG or depth electrodes, intracortical arrays) made during overt, mouthed, attempted or imagined speech production. Boundary: exclude reconstruction of heard speech, text-only decoding read out by a TTS engine, and reviews or citation-only mentions; count versions of one study once. The ledger pattern also admits some reviews and text-decoding papers, so its count is an upper bound. Design of interest: the neural feature fed to the acoustic decoder (high-gamma envelope, wavelet multiband decomposition, low-frequency band power, phase-amplitude coupling).
- Used in: [Brain-to-Speech: Prosody Feature Engineering and Transformer-Based Reconstruction](../../reviews/brain-to-speech-prosody-feature-engineering-and-transformer-based-reconstruction/)

## joint-end-to-end-lip-to-speech-training

- Table: [`joint-end-to-end-lip-to-speech-training.csv`](joint-end-to-end-lip-to-speech-training.csv) (7345 slot-filled, 165 pattern match, usual design in 15, 3 read in full)
- Inclusion rule: Video-to-speech studies (the 165-study population of the M06 video-to-speech-synthesis table), classified by whether the waveform generator is trained together with the visual-to-acoustic path (joint end-to-end waveform training) or is a pre-trained or separately trained vocoder, and whether a DDSP or harmonic-plus-noise signal model is used. Boundary: a study counts under every design its full text names (related-work mentions included, upper bound); end-to-end training that stops at mel or units with a separate vocoder is not joint waveform training; versions count once.
- Used in: [NaturalL2S: End-to-End High-quality Multispeaker Lip-to-Speech Synthesis with Differential Digital Signal Processing](../../reviews/naturall2s-end-to-end-high-quality-multispeaker-lip-to-speech-synthesis-with-differential-digita/), [SVTS: Scalable Video-to-Speech Synthesis](../../reviews/svts-scalable-video-to-speech-synthesis/)

## lip-landmark-geometric-stream

- Table: [`lip-landmark-geometric-stream.csv`](lip-landmark-geometric-stream.csv) (7345 slot-filled, 1116 pattern match, usual design in 368, 5 read in full)
- Inclusion rule: Visual or audio-visual speech recognition studies (lip reading, VSR, AVSR; word or sentence level) whose ledger names lip reading, VSR, AVSR or an LRS/LRW benchmark. The design compared is whether facial or lip landmarks (coordinates, distances, contours, shape-model parameters) enter the recognizer as a feature stream next to or instead of pixels, and how that stream is encoded (graph convolution over landmarks versus other encoders). Boundary: landmarks used only to detect, align or crop the mouth do not count; a study counts under every design its full text names (upper bound, related-work mentions included); reviews count as pattern matches only; versions of one study count once.
- Used in: [Landmark Guided Visual Feature Extractor for Visual Speech Recognition with Limited Resource](../../reviews/landmark-guided-visual-feature-extractor-for-visual-speech-recognition-with-limited-resource/)

## lipreading-temporal-model-and-feature-learning

- Table: [`lipreading-temporal-model-and-feature-learning.csv`](lipreading-temporal-model-and-feature-learning.csv) (7345 slot-filled, 975 pattern match, usual design in 113, 6 read in full)
- Inclusion rule: Automatic lip-reading, visual speech recognition or audio-visual speech recognition studies whose ledger names optical-camera input, classified by the visual model their full text names: recurrent network (LSTM, GRU, RNN, Elman/Jordan or stochastic recurrent), time-delay neural network, learned deep features (CNN, DBN, autoencoder, DNN), hand-crafted appearance or shape features (DCT, PCA/eigenlips, AAM, HOG, LBP), HMM or SVM classifier. Boundary: studies whose full text names no automatic recognizer or classifier (human speechreading and perception studies) are excluded; a study counts under every design its text names, related-work mentions included (upper bound); versions count once; dated against the target's first public month 2016-01.
- Used in: [Lipreading with Long Short-Term Memory](../../reviews/lipreading-with-long-short-term-memory/)

## lrw-audiovisual-word-recognition

- Table: [`lrw-audiovisual-word-recognition.csv`](lrw-audiovisual-word-recognition.csv) (7345 slot-filled, 44 pattern match, usual design in 29, 3 read in full)
- Inclusion rule: Studies whose ledger names both the English LRW benchmark (Lip Reading in the Wild, 500 words) and audio-visual recognition, classified by the audio input and the fusion design their full text names: raw waveform into a learned front end, or spectral features (MFCC, log-Mel, filterbank, spectrogram); concatenation followed by a recurrent fusion network, or attention/Transformer fusion; a pre-trained self-supervised or ASR front end. Boundary: LRW-1000 and other-language LRW variants are excluded; a study counts under every design its text names, related-work mentions included (upper bound); versions count once by key.
- Used in: [End-to-End Audiovisual Speech Recognition](../../reviews/end-to-end-audiovisual-speech-recognition/)

## neural-encoder-decoder-text-decoding

- Table: [`neural-encoder-decoder-text-decoding.csv`](neural-encoder-decoder-text-decoding.csv) (7345 slot-filled, 145 pattern match, usual design in 63, 4 read in full)
- Inclusion rule: Same population as neural-text-output-unit: neural decoders (ECoG, intracortical, sEEG, EEG, MEG) that output text and report a word, character or phoneme error rate. The design compared is the sequence decoder: an autoregressive encoder-decoder (sequence-to-sequence, attention or Transformer decoder), a CTC-trained network, or HMM/Viterbi decoding. Boundary: a paper is counted under every decoder its full text names (upper bounds, including mentions of other work); reviews count as pattern matches only; versions count once.
- Used in: [Machine translation of cortical activity to text with an encoder-decoder framework](../../reviews/machine-translation-of-cortical-activity-to-text-with-an-encoder-decoder-framework/)

## non-acoustic-speech-activity-detection

- Table: [`non-acoustic-speech-activity-detection.csv`](non-acoustic-speech-activity-detection.csv) (7345 slot-filled, 119 pattern match, usual design in 74, 4 read in full)
- Inclusion rule: Include studies that detect speech versus non-speech (or voiced/unvoiced, mouth open/closed as a VAD proxy, speech onset/endpoint) from a non-acoustic signal: lip/face video, ultrasound tongue imaging, ultrasonic Doppler, radar, EMG, EMA, EEG/MEG/ECoG. Boundary: audio-visual systems count when a visual-only or non-acoustic branch is evaluated; papers that only apply an acoustic VAD to their audio match the pattern and inflate the upper bound.
- Used in: [Voice Activity Detection for Ultrasound-based Silent Speech Interfaces using Convolutional Neural Networks](../../reviews/voice-activity-detection-for-ultrasound-based-silent-speech-interfaces-using-convolutional-neural-networks/)

## noninvasive-decoding-segmentation

- Table: [`noninvasive-decoding-segmentation.csv`](noninvasive-decoding-segmentation.csv) (7345 slot-filled, 1458 pattern match, usual design in 310, 2 read in full)
- Inclusion rule: Language or text decoding studies whose ledger names scalp EEG or MEG. The design compared is how the decoder is segmented at test time: windows locked to known events supplied to the decoder (word, stimulus or keystroke onsets) versus continuous decoding that infers segmentation itself (CTC, asynchronous or sliding-window decoding). Boundary: event-locked training with continuous test-time decoding counts as continuous; reviews count as pattern matches only.
- Used in: [Brain-to-Text Decoding: A Non-invasive Approach via Typing](../../reviews/brain-to-text-decoding-a-non-invasive-approach-via-typing/), [Continuous Silent Speech Recognition using EEG](../../reviews/continuous-silent-speech-recognition-using-eeg/)

## noninvasive-language-decoder-search

- Table: [`noninvasive-language-decoder-search.csv`](noninvasive-language-decoder-search.csv) (7345 slot-filled, 335 pattern match, usual design in 251, 5 read in full)
- Inclusion rule: Language, text or semantic decoding studies whose ledger names a non-invasive recording (fMRI/BOLD, fNIRS, MEG or scalp EEG): decoding words, sentences, stories or meaning from perceived, read, imagined or produced language. Boundary: encoding-only or activation-mapping studies and reviews are matched by the ledger pattern but are not deciding priors; versions of one study count once. The design compared is the decoding search: forward encoding-model scoring of candidate word sequences, direct classification, contrastive retrieval of candidates, or sequence-to-sequence generation.
- Used in: [Semantic reconstruction of continuous language from non-invasive brain recordings](../../reviews/semantic-reconstruction-of-continuous-language-from-non-invasive-brain-recordings/)

## noninvasive-speech-decoding-objective

- Table: [`noninvasive-speech-decoding-objective.csv`](noninvasive-speech-decoding-objective.csv) (7345 slot-filled, 538 pattern match, usual design in 98, 6 read in full)
- Inclusion rule: Speech or language decoding studies from scalp EEG or MEG (perceived, imagined, attempted or overt). The design compared is the training objective of the decoder: contrastive alignment to a speech or text embedding with ranking of candidates, regression of an acoustic or feature target, or classification into fixed classes. Boundary: EEG/MEG used only as an auxiliary channel to another sensor still counts; reviews are excluded; versions count once.
- Used in: [Decoding speech perception from non-invasive brain recordings](../../reviews/decoding-speech-perception-from-non-invasive-brain-recordings/), [EEG-to-Voice Decoding of Spoken and Imagined speech Using Non-Invasive EEG](../../reviews/eeg-to-voice-decoding-of-spoken-and-imagined-speech-using-non-invasive-eeg/)

## perception-imagery-cross-condition-model

- Table: [`perception-imagery-cross-condition-model.csv`](perception-imagery-cross-condition-model.csv) (7345 slot-filled, 112 pattern match, usual design in 8, 5 read in full)
- Inclusion rule: Neural decoding or encoding studies (EEG, MEG, ECoG, sEEG, intracortical, fMRI, fNIRS) that use responses recorded during perception (listening, or overt production) to model, decode or transform responses recorded during imagery or covert speech of the same material: training on one condition and testing on the other, joint training on both, or mapping imagined responses into perceived-response space. Boundary: studies that only compare imagery and perception descriptively (activation maps, connectivity) with no cross-condition model are excluded; reviews and datasets without a model are excluded; versions of one study count once.
- Used in: [A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses](../../reviews/a-convolutional-framework-for-mapping-imagined-auditory-meg-into-listened-brain-responses/), [Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping](../../reviews/zero-shot-imagined-speech-decoding-via-imagined-to-listened-meg-mapping/)

## phoneme-rnn-ctc-lm-decoding

- Table: [`phoneme-rnn-ctc-lm-decoding.csv`](phoneme-rnn-ctc-lm-decoding.csv) (7345 slot-filled, 97 pattern match, usual design in 61, 5 read in full)
- Inclusion rule: Neural or articulatory speech decoders that emit phoneme (or character) probabilities with a recurrent or CTC-trained network and convert them to words with an n-gram or neural language model. Included: sEMG, EEG, ECoG and intracortical; online or offline. Excluded: closed-set word classifiers and direct audio synthesis.
- Used in: [A cross-species neural foundation model for end-to-end speech decoding](../../reviews/a-cross-species-neural-foundation-model-for-end-to-end-speech-decoding/), [A high-performance neuroprosthesis for speech decoding and avatar control](../../reviews/a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control/), [A high-performance speech neuroprosthesis](../../reviews/a-high-performance-speech-neuroprosthesis/), [Brain2Char: a deep architecture for decoding text from brain recordings](../../reviews/brain2char-a-deep-architecture-for-decoding-text-from-brain-recordings/), [High-performance brain-to-text communication via handwriting](../../reviews/high-performance-brain-to-text-communication-via-handwriting/), [iPhoneme: Brain-to-Text Communication for ALS Using ConformerXL Decoding](../../reviews/iphoneme-brain-to-text-communication-for-als-using-conformerxl-decoding/)

## radar-ssr-input-representation

- Table: [`radar-ssr-input-representation.csv`](radar-ssr-input-representation.csv) (7345 slot-filled, 32 pattern match, usual design in 21, 5 read in full)
- Inclusion rule: Speech or silent-speech recognition studies that classify speech units from radar or RF reflections or transmissions of the articulators (IR-UWB, FMCW, SFCW, CW Doppler, mmWave, Wi-Fi or RFID backscatter); the design compared is the representation fed to the classifier: hand-engineered features (distances, envelopes, velocity or spectral descriptors) versus raw frames or spectrograms fed to a learned network. Boundary: radar used only to recover the acoustic vibration of the throat or vocal folds is excluded; datasets without a recognizer are excluded; versions of one study count once; ledger hits from non-radar papers are inside the pattern-match upper bound.
- Used in: [IR-UWB Radar-Based Contactless Silent Speech Recognition of Vowels, Consonants, Words, and Phrases](../../reviews/ir-uwb-radar-based-contactless-silent-speech-recognition-of-vowels-consonants-words-and-phrases/), [Movement Detection of Tongue and Related Body Parts Using IR-UWB Radar](../../reviews/movement-detection-of-tongue-and-related-body-parts-using-ir-uwb-radar/)

## sentence-lipreading-encoder-architecture

- Table: [`sentence-lipreading-encoder-architecture.csv`](sentence-lipreading-encoder-architecture.csv) (7345 slot-filled, 633 pattern match, usual design in 233, 6 read in full)
- Inclusion rule: Studies that decode sentence-level or open-vocabulary speech from lip or face video, alone or with audio (the 633-study population of M06/sentence-lipreading-sequence-objective), classified by the temporal encoder their full text names: Conformer, Transformer encoder, recurrent (LSTM/GRU), or temporal convolution (TCN/TDNN). Boundary: a study counts under every encoder its text names, including related-work mentions (upper bound); audio-only ASR is out of scope; versions count once by key.
- Used in: [End-to-End Audio-Visual Speech Recognition with Conformers](../../reviews/end-to-end-audio-visual-speech-recognition-with-conformers/)

## sentence-lipreading-sequence-objective

- Table: [`sentence-lipreading-sequence-objective.csv`](sentence-lipreading-sequence-objective.csv) (7345 slot-filled, 633 pattern match, usual design in 291, 6 read in full)
- Inclusion rule: Studies that decode sentence-level or open-vocabulary speech from lip or face video (ledger names lip reading, VSR, AVSR or an LRS2/LRS3 benchmark together with sentence-level, continuous or open-vocabulary recognition), classified by the sequence objective their full text names: CTC, attention sequence-to-sequence, hybrid CTC/attention, HMM, or transducer. Boundary: isolated-word classification without a sentence-level result is excluded; audio-only ASR is out of scope; reviews count as pattern matches only; a study counts under every objective its text names (upper bound); versions of one study count once by key.
- Used in: [Audio-Visual Speech Recognition with a Hybrid CTC/Attention Architecture](../../reviews/audio-visual-speech-recognition-with-a-hybrid-ctc-attention-architecture/), [LipNet: End-to-End Sentence-level Lipreading](../../reviews/lipnet-end-to-end-sentence-level-lipreading/), [Recurrent Neural Network Transducer for Audio-Visual Speech Recognition](../../reviews/recurrent-neural-network-transducer-for-audio-visual-speech-recognition/)

## silent-command-activation

- Table: [`silent-command-activation.csv`](silent-command-activation.csv) (7345 slot-filled, 183 pattern match, usual design in 20, 1 read in full)
- Inclusion rule: Silent-speech, lip-reading and mouthed-speech studies (any signal) whose ledger names commands, interaction or an interface; the design compared is how a command utterance is started or segmented at use time: an explicit manual trigger (push-to-talk, button or screen tap, manual segmentation), a mouth or speech activity detector, a gaze or gesture trigger, or keyword spotting / a wake word. Boundary: a study counts under every design its full text (reference list removed) names (upper bound); offline corpora with pre-segmented clips have none; versions count once.
- Used in: [LipLearner: Customizable Silent Speech Interactions on Mobile Devices](../../reviews/liplearner-customizable-silent-speech-interactions-on-mobile-devices/)

## speaker-recognition-from-articulation

- Table: [`speaker-recognition-from-articulation.csv`](speaker-recognition-from-articulation.csv) (7345 slot-filled, 58 pattern match, usual design in 34, 5 read in full)
- Inclusion rule: Studies that identify or verify the speaker (or subject) from a non-acoustic speech signal: lip or face motion video during speech, ultrasound, EMA, EMG, non-audible murmur or throat contact microphones, or EEG during speech tasks. Boundary: static face recognition without speech, acoustic-only speaker recognition, and identification used only as an auxiliary loss or nuisance factor are excluded; audio-visual fusion counts when the non-acoustic stream is scored on its own; versions count once.
- Used in: [Neural Speaker Embeddings for Ultrasound-based Silent Speech Interfaces](../../reviews/neural-speaker-embeddings-for-ultrasound-based-silent-speech-interfaces/)

## speech-feature-encoding-model

- Table: [`speech-feature-encoding-model.csv`](speech-feature-encoding-model.csv) (7345 slot-filled, 137 pattern match, usual design in 124, 3 read in full)
- Inclusion rule: Studies that fit forward encoding models (TRF, mTRF, linear or nonlinear regression from time-varying speech features to a recorded biosignal: EEG, MEG, ECoG, EMG, fMRI) and evaluate them on held-out data, classified by the predictor feature space (acoustic, phonetic/phoneme, articulatory). Boundary: pure decoding (signal to features) studies, source-localisation forward models and acoustic-only articulatory inversion are excluded when read; a study can use several feature spaces; versions count once.
- Used in: [Comparison of sEMG Encoding Accuracy Across Speech Modes Using Articulatory and Phoneme Features](../../reviews/comparison-of-semg-encoding-accuracy-across-speech-modes-using-articulatory-and-phoneme-features/)

## speech-signal-verification-model

- Table: [`speech-signal-verification-model.csv`](speech-signal-verification-model.csv) (7345 slot-filled, 75 pattern match, usual design in 37, 4 read in full)
- Inclusion rule: Same verification population as the M03 topic; the design compared is the identity model: GMM/HMM classifiers, GMM-UBM or i-/x-vector back-ends, metric-learning embeddings (triplet, contrastive, angular margin, siamese), cross-modal alignment between two streams, and a multi-task or shared encoder that also serves content recognition. Boundary: a study counts under every design its full text names (upper bound); a related-work mention counts as a match.
- Used in: [Poster: Recognizing Hidden-in-the-Ear Private Key for Reliable Silent Speech Interface Using Multi-Task Learning](../../reviews/poster-recognizing-hidden-in-the-ear-private-key-for-reliable-silent-speech-interface-using-mult/)

## spiking-neural-network-decoder

- Table: [`spiking-neural-network-decoder.csv`](spiking-neural-network-decoder.csv) (7345 slot-filled, 29 pattern match, usual design in 3, 3 read in full)
- Inclusion rule: Studies that decode speech, language or other neural or articulatory signals with a spiking neural network (leaky integrate-and-fire, Izhikevich or other spiking units, in software or on neuromorphic hardware) as the classifier or encoder. Boundary: 'SNN' meaning Siamese network and the SNNS simulator are pattern matches only; reviews, editorials and neuromorphic sensing without a spiking decoder are excluded; versions of one study count once.
- Used in: [EEG-Based Imagined Speech Decoding Using a Hybrid CNN-SNN Architecture](../../reviews/eeg-based-imagined-speech-decoding-using-a-hybrid-cnn-snn-architecture/)

## subword-unit-text-decoding-with-lexicon

- Table: [`subword-unit-text-decoding-with-lexicon.csv`](subword-unit-text-decoding-with-lexicon.csv) (7345 slot-filled, 102 pattern match, usual design in 47, 4 read in full)
- Inclusion rule: Studies whose ledger records a recognition-to-text decoder for a speech-related signal (any modality: EMG, ECoG, intracortical, EEG, video, ultrasound, NAM) and names phones, a lexicon/dictionary, an n-gram/language model, an HMM or CTC; the design compared is how sub-word units become words: HMM/GMM phone models with a pronunciation dictionary and n-gram LM, CTC-trained neural networks, or LLM rescoring. Boundary: a study counts under every design its full text names (upper bound); closed-set word classifiers without a recognition-to-text route are outside; versions once.
- Used in: [Brain-to-text: decoding spoken phrases from phone representations in the brain](../../reviews/brain-to-text-decoding-spoken-phrases-from-phone-representations-in-the-brain/)

## text-and-video-to-speech-decoder

- Table: [`text-and-video-to-speech-decoder.csv`](text-and-video-to-speech-decoder.csv) (7345 slot-filled, 9 pattern match, usual design in 5, 4 read in full)
- Inclusion rule: Studies that synthesize a speech waveform from talking-face or lip video together with text: the script given as input (visual TTS, automated video or movie dubbing) or text predicted by a lip reader and used to condition synthesis (text-aware video-to-speech). Boundary: plain video-to-speech without any text conditioning, talking-head generation (speech or text to face video), audio-visual recognition, and cascades that only run an off-the-shelf TTS on lip-read text without using the video in synthesis are excluded; versions of one study count once; design counts are full-text pattern counts (upper bound, related-work mentions included).
- Used in: [VSpeechLM: A Visual Speech Language Model for Visual Text-to-Speech Task](../../reviews/vspeechlm-a-visual-speech-language-model-for-visual-text-to-speech-task/)

| Paper | Year | Evidence |
| --- | --- | --- |
| LipVoicer: Generating Speech from Silent Videos Guided by Lip Reading |  |  |
| Towards Accurate Lip-to-Speech Synthesis in-the-Wild | 2023 |  |
| VSpeechLM: A Visual Speech Language Model for Visual Text-to-Speech Task | 2025 |  |
| FunCineForge: A Unified Dataset Toolkit and Model for Zero-Shot Movie Dubbing in Diverse Cinematic Scenes | 2026 |  |
| DiFlowDubber: Discrete Flow Matching for Automated Video Dubbing via Cross-Modal Alignment and Synchronization | 2026 |  |
| Watch Your Speech: Text-aware Video-to-Speech Synthesis with Textual Conditioning | 2026 |  |
| Watch Your Speech: Text-aware Video-to-Speech Synthesis with Textual Conditioning | 2026 |  |
| LipAdapter: Text-to-Video Alignment is All You Need for Lip-to-Speech | 2026 |  |
| LipAdapter: Text-to-Video Alignment is All You Need for Lip-to-Speech | 2026 |  |

## ultrasound-image-sequence-temporal-layer

- Table: [`ultrasound-image-sequence-temporal-layer.csv`](ultrasound-image-sequence-temporal-layer.csv) (7345 slot-filled, 148 pattern match, usual design in 27, 4 read in full)
- Inclusion rule: Include studies whose ledger lists ultrasound imaging as an input modality and classify, by full-text pattern (reference list removed), how the network integrates a sequence of ultrasound frames over time: 3D (spatiotemporal) convolution, a CNN followed by a recurrent layer, ConvLSTM, or Transformer/Conformer attention. Boundary: mentions in related work, reviews, theses and tasks other than speech output (contour tracking, image prediction, recognition) still count as pattern matches, an upper bound; ConvLSTM hits were classified by snippet; versions count once by key.
- Used in: [Convolutional Neural Network-Based Age Estimation Using B-Mode Ultrasound Tongue Image](../../reviews/convolutional-neural-network-based-age-estimation-using-b-mode-ultrasound-tongue-image/), [Improved Processing of Ultrasound Tongue Videos by Combining ConvLSTM and 3D Convolutional Networks](../../reviews/improved-processing-of-ultrasound-tongue-videos-by-combining-convlstm-and-3d-convolutional-networks/), [Ultra2Speech - A Deep Learning Framework for Formant Frequency Estimation and Tracking from Ultrasound Tongue Images](../../reviews/ultra2speech-a-deep-learning-framework-for-formant-frequency-estimation-and-tracking-from-ultrasound-tongue-images/)

## ultrasound-to-speech-acoustic-target

- Table: [`ultrasound-to-speech-acoustic-target.csv`](ultrasound-to-speech-acoustic-target.csv) (7345 slot-filled, 50 pattern match, usual design in 35, 7 read in full)
- Inclusion rule: Include studies whose ledger lists ultrasound imaging as input and speech synthesis, a vocoder or an acoustic/formant output, and classify by full-text pattern (whole text, related-work mentions included, so counts are upper bounds) the acoustic representation the network is trained to predict: vocoder spectral parameters (MGC-LSP, mel-cepstrum, MFCC), mel-spectrogram, formant frequencies. Boundary: reviews and corpus papers count as pattern matches; a hit on 'formant' in related work or as an analysis feature is not a formant target unless the snippet shows prediction; versions count once by key.
- Used in: [Ultra2Speech - A Deep Learning Framework for Formant Frequency Estimation and Tracking from Ultrasound Tongue Images](../../reviews/ultra2speech-a-deep-learning-framework-for-formant-frequency-estimation-and-tracking-from-ultrasound-tongue-images/)

## ultrasound-to-speech-network-architecture

- Table: [`ultrasound-to-speech-network-architecture.csv`](ultrasound-to-speech-network-architecture.csv) (7345 slot-filled, 51 pattern match, usual design in 37, 4 read in full)
- Inclusion rule: Include studies that map ultrasound tongue images (with or without lip video) to acoustic features or a waveform with a trained network, and name the mapping architecture. Boundary: exclude ultrasound-to-text recognition without synthesis, contour tracking, ultrasound prediction from other signals and reviews (they inflate the pattern match, an upper bound); spatial transformer networks count as CNNs, not as attention models; count versions once by key.
- Used in: [3D Convolutional Neural Networks for Ultrasound-Based Silent Speech Interfaces](../../reviews/3d-convolutional-neural-networks-for-ultrasound-based-silent-speech-interfaces/), [Adaptation of Tongue Ultrasound-Based Silent Speech Interfaces Using Spatial Transformer Networks](../../reviews/adaptation-of-tongue-ultrasound-based-silent-speech-interfaces-using-spatial-transformer-networks/), [Conformer-based Ultrasound-to-Speech Conversion](../../reviews/conformer-based-ultrasound-to-speech-conversion/), [Improved Processing of Ultrasound Tongue Videos by Combining ConvLSTM and 3D Convolutional Networks](../../reviews/improved-processing-of-ultrasound-tongue-videos-by-combining-convlstm-and-3d-convolutional-networks/), [Speech Synthesis from Text and Ultrasound Tongue Image-based Articulatory Input](../../reviews/speech-synthesis-from-text-and-ultrasound-tongue-image-based-articulatory-input/)

## ultrasound-tongue-image-features

- Table: [`ultrasound-tongue-image-features.csv`](ultrasound-tongue-image-features.csv) (7345 slot-filled, 39 pattern match, usual design in 32, 3 read in full)
- Inclusion rule: Include studies that compress ultrasound tongue images (with or without lip images) into feature vectors for recognition, synthesis or articulatory mapping by DCT, PCA/EigenTongues, autoencoders or learned CNN encoders. Boundary: exclude contour-only tracking without a feature vector used downstream, raw-image end-to-end models with no stated feature stage, and reviews; count versions once.
- Used in: [Autoencoder-Based Articulatory-to-Acoustic Mapping for Ultrasound Silent Speech Interfaces](../../reviews/autoencoder-based-articulatory-to-acoustic-mapping-for-ultrasound-silent-speech-interfaces/), [Denoising Convolutional Autoencoder Based B-mode Ultrasound Tongue Image Feature Extraction](../../reviews/denoising-convolutional-autoencoder-based-b-mode-ultrasound-tongue-image-feature-extraction/), [Updating the Silent Speech Challenge benchmark with deep learning](../../reviews/updating-the-silent-speech-challenge-benchmark-with-deep-learning/)

## ultrasound-tongue-speech-recognition

- Table: [`ultrasound-tongue-speech-recognition.csv`](ultrasound-tongue-speech-recognition.csv) (7345 slot-filled, 38 pattern match, usual design in 15, 5 read in full)
- Inclusion rule: Include studies that recognize phones, words or sentences as text from ultrasound tongue images, with or without lip video, in silent or vocalized articulation, and report a recognition error or accuracy. Boundary: exclude ultrasound-to-speech synthesis without a recognition score, tongue contour tracking or clinical phonetics, reviews and surveys (counted in the pattern match but not as designs), and recognition from lips only; count versions once.
- Used in: [Silent versus modal multi-speaker speech recognition from ultrasound and video](../../reviews/silent-versus-modal-multi-speaker-speech-recognition-from-ultrasound-and-video/), [Updating the Silent Speech Challenge benchmark with deep learning](../../reviews/updating-the-silent-speech-challenge-benchmark-with-deep-learning/)

## ultrasound-tongue-to-speech-synthesis

- Table: [`ultrasound-tongue-to-speech-synthesis.csv`](ultrasound-tongue-to-speech-synthesis.csv) (7345 slot-filled, 51 pattern match, usual design in 34, 3 read in full)
- Inclusion rule: Include studies that synthesize a speech waveform or vocoder/spectral features from ultrasound tongue images (with or without lip video), and name the acoustic representation and the waveform generator. Boundary: exclude ultrasound-to-text recognition without synthesis, tongue contour tracking, ultrasound prediction from other signals, and reviews (they inflate the pattern match, an upper bound); count versions once by key.
- Used in: [Ultrasound-based Silent Speech Interface Built on a Continuous Vocoder](../../reviews/ultrasound-based-silent-speech-interface-built-on-a-continuous-vocoder/)

## video-to-speech-one-to-many-decoder

- Table: [`video-to-speech-one-to-many-decoder.csv`](video-to-speech-one-to-many-decoder.csv) (7345 slot-filled, 165 pattern match, usual design in 54, 4 read in full)
- Inclusion rule: Include the video-to-speech population of components/M06/video-to-speech-synthesis (speech waveform synthesized from talking-face or lip video, audio muted at test) and classify, from the full text with the reference list removed, how the acoustic decoder handles the one-to-many mapping: explicit pitch or energy (variance) predictors, flow-based decoders (normalizing flow, flow matching, rectified flow), diffusion decoders, adversarial training with a discriminator, and self-supervised speech-unit conditioning. Boundary: a study counts under every design its text names (upper bound; related-work mentions included); audio-visual enhancement with noisy audio at test, talking-head generation and video-to-text-to-TTS pipelines excluded; versions counted once.
- Used in: [Let There Be Sound: Reconstructing High Quality Speech from Silent Videos](../../reviews/let-there-be-sound-reconstructing-high-quality-speech-from-silent-videos/), [Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild](../../reviews/lip-to-speech-synthesis-for-arbitrary-speakers-in-the-wild/), [LipDiffuser: Lip-to-Speech Generation with Conditional Diffusion Models](../../reviews/lipdiffuser-lip-to-speech-generation-with-conditional-diffusion-models/), [LipSody: Lip-to-Speech Synthesis with Enhanced Prosody Consistency](../../reviews/lipsody-lip-to-speech-synthesis-with-enhanced-prosody-consistency/), [LipVoicer: Generating Speech from Silent Videos Guided by Lip Reading](../../reviews/lipvoicer-generating-speech-from-silent-videos-guided-by-lip-reading/), [LTA-L2S: Lexical Tone-Aware Lip-to-Speech Synthesis for Mandarin with Cross-Lingual Transfer Learning](../../reviews/lta-l2s-lexical-tone-aware-lip-to-speech-synthesis-for-mandarin-with-cross-lingual-transfer-lear/), [RESOUND: Speech Reconstruction from Silent Videos via Acoustic-Semantic Decomposed Modeling](../../reviews/resound-speech-reconstruction-from-silent-videos-via-acoustic-semantic-decomposed-modeling/), [SLD-L2S: Hierarchical Subspace Latent Diffusion for High-Fidelity Lip to Speech Synthesis](../../reviews/sld-l2s-hierarchical-subspace-latent-diffusion-for-high-fidelity-lip-to-speech-synthesis/), [VCVTS: Multi-Speaker Video-to-Speech Synthesis via Cross-Modal Knowledge Transfer from Voice Conversion](../../reviews/vcvts-multi-speaker-video-to-speech-synthesis-via-cross-modal-knowledge-transfer-from-voice-conversion/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild | 2022 | Sec. 3.2.3; Sec. 3.2.6 |

## video-to-speech-synthesis

- Table: [`video-to-speech-synthesis.csv`](video-to-speech-synthesis.csv) (7345 slot-filled, 165 pattern match, usual design in 49, 3 read in full)
- Inclusion rule: Include studies that synthesize a speech waveform from video of the talking face or lips (silent or with audio muted at test) and report the acoustic representation and how it is turned into a waveform. Boundary: exclude audio-visual speech enhancement or separation that takes noisy audio at test, talking-head generation (speech to video), text-only lip reading and video-to-text-to-TTS pipelines; count versions of one study once.
- Used in: [Audio-visual video-to-speech synthesis with synthesized input audio](../../reviews/audio-visual-video-to-speech-synthesis-with-synthesized-input-audio/), [FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis](../../reviews/fastlts-non-autoregressive-end-to-end-unconstrained-lip-to-speech-synthesis/), [Improved Speech Reconstruction from Silent Video](../../reviews/improved-speech-reconstruction-from-silent-video/), [Intelligible Lip-to-Speech Synthesis with Speech Units](../../reviews/intelligible-lip-to-speech-synthesis-with-speech-units/), [Large-scale unsupervised audio pre-training for video-to-speech synthesis](../../reviews/large-scale-unsupervised-audio-pre-training-for-video-to-speech-synthesis/), [Lip2AudSpec: Speech Reconstruction from Silent Lip Movements Video](../../reviews/lip2audspec-speech-reconstruction-from-silent-lip-movements-video/), [Lipper: Synthesizing Thy Speech using Multi-View Lipreading](../../reviews/lipper-synthesizing-thy-speech-using-multi-view-lipreading/), [Multi-modality Associative Bridging through Memory: Speech Sound Recollected from Face Video](../../reviews/multi-modality-associative-bridging-through-memory-speech-sound-recollected-from-face-video/), [NaturalL2S: End-to-End High-quality Multispeaker Lip-to-Speech Synthesis with Differential Digital Signal Processing](../../reviews/naturall2s-end-to-end-high-quality-multispeaker-lip-to-speech-synthesis-with-differential-digita/), [RobustL2S: Speaker-Specific Lip-to-Speech Synthesis exploiting Self-Supervised Representations](../../reviews/robustl2s-speaker-specific-lip-to-speech-synthesis-exploiting-self-supervised-representations/), [SVTS: Scalable Video-to-Speech Synthesis](../../reviews/svts-scalable-video-to-speech-synthesis/), [Vid2speech: Speech Reconstruction from Silent Video](../../reviews/vid2speech-speech-reconstruction-from-silent-video/), [Video-Driven Speech Reconstruction using Generative Adversarial Networks](../../reviews/video-driven-speech-reconstruction-using-generative-adversarial-networks/), [Vocoder-Based Speech Synthesis from Silent Videos](../../reviews/vocoder-based-speech-synthesis-from-silent-videos/), [Zero-Shot Personalized Lip-to-Speech Synthesis with Face Image Based Voice Control](../../reviews/zero-shot-personalized-lip-to-speech-synthesis-with-face-image-based-voice-control/)

## visual-frontend-spatial-pooling

- Table: [`visual-frontend-spatial-pooling.csv`](visual-frontend-spatial-pooling.csv) (7345 slot-filled, 1116 pattern match, usual design in 254, 5 read in full)
- Inclusion rule: Visual or audio-visual speech recognition studies (lip reading, VSR, AVSR; word or sentence level) whose ledger names lip reading, VSR, AVSR or an LRS/LRW benchmark. The design compared is how the per-frame spatial feature map of the visual front-end is reduced to a vector: global average pooling (or flatten) after a CNN/ResNet trunk, versus learned spatial attention or transformer pooling over the map. Boundary: temporal attention alone, attention used for audio-visual fusion, and ROI cropping are not spatial pooling; reviews count as pattern matches only; versions of one study count once.
- Used in: [Sub-word Level Lip Reading With Visual Attention](../../reviews/sub-word-level-lip-reading-with-visual-attention/)

## visual-keyword-spotting

- Table: [`visual-keyword-spotting.csv`](visual-keyword-spotting.csv) (7345 slot-filled, 18 pattern match, usual design in 12, 4 read in full)
- Inclusion rule: Studies whose ledger names a camera modality and keyword spotting, wake words or hotwords; the design compared is how the keyword is specified and which signal is used: a fixed wake word or keyword set, a text or phoneme query (zero-shot), an enrolled example query (few-shot), audio-visual fusion or visual-only input. Boundary: a study counts under every design its full text (reference list removed) names (upper bound); audio-only KWS and visual forced alignment without spotting are pattern hits only; versions count once.
- Used in: [LipLearner: Customizable Silent Speech Interactions on Mobile Devices](../../reviews/liplearner-customizable-silent-speech-interactions-on-mobile-devices/)

## wearable-silent-sentence-decoding

- Table: [`wearable-silent-sentence-decoding.csv`](wearable-silent-sentence-decoding.csv) (7345 slot-filled, 54 pattern match, usual design in 30, 6 read in full)
- Inclusion rule: Sentence or phrase recognition from silently articulated speech measured by body-worn or contact non-video sensors (EMG, inertial, strain, triboelectric, magnetic, EMA, ultrasound, active acoustic); the design compared is how a sentence is decoded: whole-sentence classification, HMM decoding, CTC, or attention sequence-to-sequence. Boundary: lip video, imagined speech, overt-only and synthesis-only studies are outside; a study counts under every decoder its full text names (upper bound, related-work mentions included); versions count once.
- Used in: [Development of sEMG sensors and algorithms for silent speech recognition](../../reviews/development-of-semg-sensors-and-algorithms-for-silent-speech-recognition/), [Silent Speech Sentence Recognition with Six-Axis Accelerometers using Conformer and CTC Algorithm](../../reviews/silent-speech-sentence-recognition-with-six-axis-accelerometers-using-conformer-and-ctc-algorith/)

## whisper-conversion-intermediate-representation

- Table: [`whisper-conversion-intermediate-representation.csv`](whisper-conversion-intermediate-representation.csv) (7345 slot-filled, 60 pattern match, usual design in 50, 5 read in full)
- Inclusion rule: Same population as M02/whisper-to-normal-training-pairing (unvoiced or whispered acoustic or body-conducted speech converted to voiced speech audio); classify the intermediate representation the converter maps through: frame-level spectral features (MCEP, mel spectrogram, GMM/DNN mapping), self-supervised speech units or features (HuBERT, wav2vec, ContentVec), or an ASR-to-TTS text cascade. Boundary: an SSL model used only for evaluation does not count; recognition-only and normal-to-whisper studies are excluded; count versions once.
- Used in: [WESPER: Zero-shot and Realtime Whisper to Normal Voice Conversion for Whisper-based Speech Interactions](../../reviews/wesper-zero-shot-and-realtime-whisper-to-normal-voice-conversion-for-whisper-based-speech-interactions/)

## within-word-phoneme-onset-classification

- Table: [`within-word-phoneme-onset-classification.csv`](within-word-phoneme-onset-classification.csv) (7345 slot-filled, 51 pattern match, usual design in 27, 5 read in full)
- Inclusion rule: Studies in the wiki first public before 2013-11 (index year, else manifest date; every 2013 item checked by month, one with an unresolved month excluded) whose full text names an intracranial recording (ECoG, intracortical, sEEG, Utah or microelectrode array, single units, depth electrodes) and a speech unit (phoneme, vowel, consonant, syllable); the design of interest is whether analysis windows are aligned to the onset of each phoneme inside a produced word (phoneme events within words) or to the trial cue, stimulus or word or speech onset. Boundary: perception, review and mapping papers stay in the population (upper bound); versions merged by title; target and its duplicate folder excluded;
- Used in: [Direct classification of all American English phonemes using signals from functional speech motor cortex](../../reviews/direct-classification-of-all-american-english-phonemes-using-signals-from-functional-speech-motor-co/)

## word-lipreading-temporal-backend

- Table: [`word-lipreading-temporal-backend.csv`](word-lipreading-temporal-backend.csv) (7345 slot-filled, 156 pattern match, usual design in 115, 6 read in full)
- Inclusion rule: Studies whose ledger names the English LRW benchmark or the Mandarin LRW-1000 / CAS-VSR-W1K benchmark (word-level lip reading), classified by the temporal back end their full text names: recurrent (LSTM or GRU), temporal convolution (TCN, MS-TCN, DC-TCN or a temporal-convolution back end), Transformer, Conformer. Boundary: a study counts under every design its text names, related-work mentions included (upper bound); audio-visual studies stay in; versions count once by key; dated split by first public month (prior before 2019-07, [concurrent] 2019-07 to 2020-07, [later] after).
- Used in: [Combining Residual Networks with LSTMs for Lipreading](../../reviews/combining-residual-networks-with-lstms-for-lipreading/), [Lipreading using Temporal Convolutional Networks](../../reviews/lipreading-using-temporal-convolutional-networks/)

## word-lipreading-visual-frontend

- Table: [`word-lipreading-visual-frontend.csv`](word-lipreading-visual-frontend.csv) (7345 slot-filled, 156 pattern match, usual design in 106, 6 read in full)
- Inclusion rule: Studies whose ledger names the English LRW benchmark or the Mandarin LRW-1000 / CAS-VSR-W1K benchmark (word-level lip reading), classified by the visual front end their full text names: spatiotemporal (3D) convolution, ResNet trunk, VGG trunk, ViT or patch transformer. Boundary: a study counts under every design its text names, related-work mentions included (upper bound); audio-visual studies stay in; versions count once by ledger key (the target has three keys); dated by first public month (prior before 2016-09, [concurrent] 2016-09 to 2017-09, [later] after).
- Used in: [Combining Residual Networks with LSTMs for Lipreading](../../reviews/combining-residual-networks-with-lstms-for-lipreading/)
