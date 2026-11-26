# M12 Evaluation

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## acoustic-sensing-test-split

- Table: [`acoustic-sensing-test-split.csv`](acoustic-sensing-test-split.csv) (6960 slot-filled, 22 pattern match, usual design in 7, 3 read in full)
- Inclusion rule: Same population as active-acoustic-speech-sensing; the design compared is how the reported test set is separated from training: user-held-out (leave-one-user-out or cross-user), session- or day-held-out, or a random sample split. Boundary: a paper counts under every protocol its text names; reviews count as pattern matches only.
- Used in: [End-to-End Silent Speech Recognition with Acoustic Sensing](../../reviews/end-to-end-silent-speech-recognition-with-acoustic-sensing/), [Poster: Recognizing Hidden-in-the-Ear Private Key for Reliable Silent Speech Interface Using Multi-Task Learning](../../reviews/poster-recognizing-hidden-in-the-ear-private-key-for-reliable-silent-speech-interface-using-mult/), [SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces](../../reviews/sonispeech-a-large-scale-open-vocabulary-tri-modal-dataset-for-wearable-silent-speech-interfaces/)

| Paper | Year | Evidence |
| --- | --- | --- |
| End-to-end Silent Speech Recognition with Acoustic Sensing |  | Sec. 4.3 |
| M2SILENT: Enabling Multi-user Silent Speech Interactions via Multi-directional Speakers in Shared Spaces |  | Sec. 5 |
| Multimodal Speech Recognition with Ultrasonic Sensors |  | Sec. 5.1 |

## avsr-noise-and-run-variability-protocol

- Table: [`avsr-noise-and-run-variability-protocol.csv`](avsr-noise-and-run-variability-protocol.csv) (6960 slot-filled, 349 pattern match, usual design in 183, 3 read in full)
- Inclusion rule: The same 349-study AVSR population as M06/avsr-audio-stream-input-representation, classified by evaluation protocol its full text names: additive-noise test at stated SNRs, babble noise in particular, and run-to-run variability (seeds, repeated runs, standard deviation, confidence intervals). Boundary: a study counts under every protocol its text names (upper bound, related-work mentions included); versions count once by key.
- Used in: [End-to-End Audio-Visual Speech Recognition with Conformers](../../reviews/end-to-end-audio-visual-speech-recognition-with-conformers/), [End-to-End Audiovisual Speech Recognition](../../reviews/end-to-end-audiovisual-speech-recognition/), [Recurrent Neural Network Transducer for Audio-Visual Speech Recognition](../../reviews/recurrent-neural-network-transducer-for-audio-visual-speech-recognition/), [Robust Self-Supervised Audio-Visual Speech Recognition](../../reviews/robust-self-supervised-audio-visual-speech-recognition/)

## bci2020-imagined-speech-benchmark

- Table: [`bci2020-imagined-speech-benchmark.csv`](bci2020-imagined-speech-benchmark.csv) (6960 slot-filled, 16 pattern match, usual design in 10, 2 read in full)
- Inclusion rule: Studies that report classification results on the 2020 International BCI Competition Track 3 imagined-speech data (15 subjects, five words or phrases, 64-channel EEG), including the organisers' review, classified by the test data scored: the competition's released test trials, the public validation subset used as test, cross-validation, or held-out subjects. Boundary: papers that only cite the dataset, and multi-dataset benchmarks where Track 3 results are not reported separately, are pattern matches only; versions count once.
- Used in: [EEG-Based Imagined Speech Decoding Using a Hybrid CNN-SNN Architecture](../../reviews/eeg-based-imagined-speech-decoding-using-a-hybrid-cnn-snn-architecture/), [NeuroTTT: Bridging Pretrain–Downstream Task Misalignment in EEG Foundation Models via Test-Time Training](../../reviews/neurottt-bridging-pretraining-downstream-task-misalignment-in-eeg-foundation-models-via-test-tim/)

## body-conducted-sensor-noise-test-protocol

- Table: [`body-conducted-sensor-noise-test-protocol.csv`](body-conducted-sensor-noise-test-protocol.csv) (6960 slot-filled, 123 pattern match, usual design in 44, 3 read in full)
- Inclusion rule: Same population as M05 body-conducted-sensor-with-air-microphone; design compared is whether quantitative noise tests expose the conducted sensor to the noise (noise physically present while recording, or noise recorded through both channels) or add noise digitally to the air channel only. Boundary: a paper naming both protocols is counted under each; qualitative field recordings do not count as a quantitative test.
- Used in: [NasoVoce: A Nose-Mounted Low-Audibility Speech Interface for Always-Available Speech Interaction](../../reviews/nasovoce/)

## cross-corpus-avsr-generalization

- Table: [`cross-corpus-avsr-generalization.csv`](cross-corpus-avsr-generalization.csv) (6960 slot-filled, 75 pattern match, usual design in 33, 4 read in full)
- Inclusion rule: Studies that test already trained visual-only or audio-visual sentence recognizers on at least one corpus or recording condition outside the training domain (another corpus, in-the-wild or conversational video, video calls, Lombard speech, non-frontal views) and report WER per condition. Boundary: in-domain tests with only synthetic noise added are excluded; word-level classification (LRW-type) is excluded; benchmark papers built for such testing are included; versions count once.
- Used in: [AVSRBench: A Multi-Condition AVSR Benchmark](../../reviews/avsrbench-a-multi-condition-avsr-benchmark/)

## dvs-lip-benchmark

- Table: [`dvs-lip-benchmark.csv`](dvs-lip-benchmark.csv) (6960 slot-filled, 6 pattern match, usual design in 6, 4 read in full)
- Inclusion rule: Studies that report a recognition result on the DVS-Lip event-camera lip-reading dataset (100 isolated words, 40 speakers, speaker-disjoint 30/10 train/test split). Boundary: other event datasets (EventLRW, LIPSFUS, private recordings) are excluded unless DVS-Lip is also reported; versions of one study count once.
- Used in: [A First Exploration of Neuromorphic OT-CFM for Multi-Speaker VSR](../../reviews/lipsflow-a-first-exploration-of-neuromorphic-ot-cfm-for-multi-speaker-vsr/)

## eeg-held-out-subject-test

- Table: [`eeg-held-out-subject-test.csv`](eeg-held-out-subject-test.csv) (6960 slot-filled, 153 pattern match, usual design in 46, 2 read in full)
- Inclusion rule: EEG decoding studies that report accuracy on subjects whose data were not used to train the decoder (leave-one-subject-out, a fixed set of held-out subjects, or subject-independent cross-validation). Boundary: within-subject cross-validation only, fine-tuning on the test subject's labeled trials before scoring (counted, but recorded as calibrated transfer), and reviews are excluded; versions of one study count once.
- Used in: [CAT-Net: A Cross-Attention Tone Network for Cross-Subject EEG-EMG Fusion Tone Decoding](../../reviews/cat-net-a-cross-attention-tone-network-for-cross-subject-eeg-emg-fusion-tone-decoding/), [Do EEG Foundation Models Transfer to Speech? A Benchmark on Overt and Imagined Speech Decoding](../../reviews/do-eeg-foundation-models-transfer-to-speech-a-benchmark-on-overt-and-imagined-speech-decoding/), [MultiDiffNet: A Multi-Objective Diffusion Framework for Generalizable Brain Decoding](../../reviews/multidiffnet-a-multi-objective-diffusion-framework-for-generalizable-brain-decoding/), [Subject-Independent Imagined Speech Detection via Cross-Subject Generalization and Calibration](../../reviews/subject-independent-imagined-speech-detection-via-cross-subject-generalization-and-calibration/)

## emg-text-unseen-sentence-test

- Table: [`emg-text-unseen-sentence-test.csv`](emg-text-unseen-sentence-test.csv) (6960 slot-filled, 64 pattern match, usual design in 13, 3 read in full)
- Inclusion rule: Surface-EMG decoders whose output is scored with WER or CER (recognition, or ASR on synthesized speech); the design compared is whether the headline error is measured on sentences absent from all training data (sentence-disjoint, open vocabulary) or on repeats of training sentences (closed set). Boundary: a paper is counted under each protocol its text names; reviews count as pattern matches only; versions of one study count once.
- Used in: [Development of sEMG sensors and algorithms for silent speech recognition](../../reviews/development-of-semg-sensors-and-algorithms-for-silent-speech-recognition/), [emg2speech: Synthesizing speech from electromyography using self-supervised speech models](../../reviews/emg2speech-synthesizing-speech-from-electromyography-using-self-supervised-speech-models/), [Multi-Subject Pretraining Enables Short-Calibration Personalization for Closed-Corpus Surface EMG Speech Decoding](../../reviews/multi-subject-pretraining-enables-short-calibration-personalization-for-closed-corpus-surface-emg-speech-decoding/)

| Paper | Year | Evidence |
| --- | --- | --- |
| A Cross-Modal Approach to Silent Speech with LLM-Enhanced Recognition |  | Abstract |
| Multi-Subject Pretraining Enables Short-Calibration Personalization for Closed-Corpus Surface EMG Speech Decoding | 2026 | Sec. 3.2 |
| An Improved Model for Voicing Silent Speech |  | Sec. 1 |

## grid-sentence-lipreading-protocol

- Table: [`grid-sentence-lipreading-protocol.csv`](grid-sentence-lipreading-protocol.csv) (6960 slot-filled, 93 pattern match, usual design in 54, 5 read in full)
- Inclusion rule: Lip-reading or VSR studies whose ledger names optical-camera input and the GRID corpus, classified by the evaluation partition their full text names: an unseen-speaker (speaker-independent or held-out speaker) split, an overlapped-speaker (seen-speaker or speaker-dependent) split, or explicit reuse of the held-out speakers 1, 2, 20 and 22. A separate regex counts studies that report a standard deviation, a confidence interval or a significance test. Boundary: audio-only GRID work and GRID studies without a recognition or synthesis decoder are excluded; a study counts under every partition its text names (upper bound); versions count once by key.
- Used in: [LipNet: End-to-End Sentence-level Lipreading](../../reviews/lipnet-end-to-end-sentence-level-lipreading/)

## human-lipreader-baseline

- Table: [`human-lipreader-baseline.csv`](human-lipreader-baseline.csv) (6960 slot-filled, 64 pattern match, usual design in 40, 116 read in full)
- Inclusion rule: Include studies that place, on the same metric, the results of machine lipreading or silent speech recognition alongside the results of human lipreaders (experts, people with hearing impairment, or general participants) reading the same data (the same test set or a subset of it). Boundary: exclude intelligibility assessments in which people listen to reconstructed speech. Exclude those that only cite human performance as literature values. Exclude studies of lipreading ability among humans with no machine results. Count different versions of the same study as one item.
- Used in: [Lip Reading Sentences in the Wild](../../reviews/lip-reading-sentences-in-the-wild/), [LipNet: End-to-End Sentence-level Lipreading](../../reviews/lipnet-end-to-end-sentence-level-lipreading/)

| Paper | Year | Evidence |
| --- | --- | --- |
| LipNet: End-to-End Sentence-level Lipreading (2016) |  | §1, §4.4 Table |
| Lip Reading Sentences in the Wild | 2017 | §5.2, Table 5 |
| Towards Estimating the Upper Bound of Visual-Speech Recognition: The Visual Lip-Reading Feasibility Database (FG 2017) |  | Abstract |
| Large-Scale Visual Speech Recognition |  | Abstract |
| The Lipreading Gap: Do VSR Models Perceive Visual Speech Like Human Lipreaders? |  | §1 |
| isca-hilder09_avsp |  | Abstract, §3.3 Table 1 |
| Human Audio-Visual Consonant Recognition Analyzed with Three Bimodal Integration Models | 2009 | §4, Fig. 3 |

## imagined-speech-eeg-chance-reference

- Table: [`imagined-speech-eeg-chance-reference.csv`](imagined-speech-eeg-chance-reference.csv) (6960 slot-filled, 167 pattern match, usual design in 95, 2 read in full)
- Inclusion rule: Studies that classify imagined, covert or inner speech from scalp EEG (same ledger population as the M13 online-imagined-speech-eeg table); the design compared is whether reported accuracy is referenced against chance: a stated chance level or above-chance test, or an empirical permutation null. Boundary: full-text pattern counts are upper bounds (a chance mention in related work counts); a study whose full text never uses the word 'chance' is counted as giving no chance reference; versions count once.
- Used in: [Lightweight Diffusion-based Framework for Online Imagined Speech Decoding in Aphasia](../../reviews/lightweight-diffusion-based-framework-for-online-imagined-speech-decoding-in-aphasia/), [Towards Neural Decoding of Imagined Speech based on Spoken Speech](../../reviews/towards-neural-decoding-of-imagined-speech-based-on-spoken-speech/)

## implanted-communication-bci-chance-and-false-positives

- Table: [`implanted-communication-bci-chance-and-false-positives.csv`](implanted-communication-bci-chance-and-false-positives.csv) (6960 slot-filled, 382 pattern match, usual design in 169, 1 read in full)
- Inclusion rule: Same population as M13/wireless-implanted-speech-bci; the design compared is the floor reported for decoding or selection accuracy: a chance level or shuffled or permutation null, and a false-positive (unintended selection) rate. Boundary: full-text pattern counts with the reference list removed (upper bounds; offline classification studies count); a study counts under every design it names.
- Used in: [Fully Implanted Brain-Computer Interface in a Locked-In Patient with ALS](../../reviews/fully-implanted-brain-computer-interface-in-a-locked-in-patient-with-als/)

## intracortical-communication-rate-benchmark

- Table: [`intracortical-communication-rate-benchmark.csv`](intracortical-communication-rate-benchmark.csv) (6960 slot-filled, 33 pattern match, usual design in 5, 2 read in full)
- Inclusion rule: Same 33-study intracortical text-entry population as the M06 topic; the design compared is the rate metric reported for communication: achieved bitrate on a cued grid, information transfer rate (ITR), correct characters per minute (ccpm), words per minute, word error rate alongside the rate. Boundary: full-text pattern counts with the reference list removed (upper bound; definitions and related-work mentions count); a study counts under every metric it names; the target is included.
- Used in: [High performance communication by people with paralysis using an intracortical brain-computer interface](../../reviews/high-performance-communication-by-people-with-paralysis-using-an-intracortical-brain-computer-interf/)

## intracranial-speech-test-partition

- Table: [`intracranial-speech-test-partition.csv`](intracranial-speech-test-partition.csv) (6960 slot-filled, 618 pattern match, usual design in 132, 2 read in full)
- Inclusion rule: Speech or language decoding studies from intracranial recordings (sEEG, ECoG, intracortical arrays) whose ledger text names the signal and a speech unit; the design of interest is how test data are separated from training data: random trial split, k-fold cross-validation, held-out session or day, or held-out subject. Boundary: the ledger pattern also admits reviews, listening studies and non-intracranial papers that mention intracranial work, so counts are upper bounds; versions of one study count once.
- Used in: [Decoding Vowels and Consonants in Spoken and Imagined Words Using Electrocorticographic Signals in Humans](../../reviews/decoding-vowels-and-consonants-in-spoken-and-imagined-words-using-electrocorticographic-signals-in-h/), [Towards Unified Neural Decoding with Brain Functional Network Modeling](../../reviews/towards-unified-neural-decoding-with-brain-functional-network-modeling/)

## lip-command-recognition-test-split

- Table: [`lip-command-recognition-test-split.csv`](lip-command-recognition-test-split.csv) (6960 slot-filled, 402 pattern match, usual design in 163, 2 read in full)
- Inclusion rule: Camera-based lip-reading or silent-speech studies whose ledger names word, phrase or command classification (closed lexicon); the design compared is how test data are separated from enrollment or training data (speaker-disjoint, within-speaker, session- or condition-disjoint) and whether chance level is reported. Boundary: a study counts under every split its full text (reference list removed) names (upper bound); human lipreading perception studies are pattern hits only; versions count once.
- Used in: [LipLearner: Customizable Silent Speech Interactions on Mobile Devices](../../reviews/liplearner-customizable-silent-speech-interactions-on-mobile-devices/)

## listener-intelligibility-test

- Table: [`listener-intelligibility-test.csv`](listener-intelligibility-test.csv) (6960 slot-filled, 37 pattern match, usual design in 15, 5 read in full)
- Inclusion rule: Include studies that evaluate speech synthesized from non-acoustic signals (neural activity, EMG, articulatory measurements such as EMA or PMA, ultrasound, mouth video) with an intelligibility test in which human listeners transcribe it or identify words or sentences from a set of choices, and report accuracy, WER or similar. Boundary: exclude those with only naturalness, preference or MOS ratings. Exclude conversion from acoustic input (whisper, NAM microphone, esophageal speech, etc.). Exclude synthesis from text and stimulus sounds for perception experiments. Exclude those that evaluate synthesized speech only with automatic speech recognition. Exclude matches in reviews or citations only. Count different versions of the same study as one item.
- Used in: [A high-performance neuroprosthesis for speech decoding and avatar control](../../reviews/a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control/), [An instantaneous voice-synthesis neuroprosthesis](../../reviews/an-instantaneous-voice-synthesis-neuroprosthesis/), [Brain-to-Speech: Prosody Feature Engineering and Transformer-Based Reconstruction](../../reviews/brain-to-speech-prosody-feature-engineering-and-transformer-based-reconstruction/), [Brain2Speech-Net: Fast and Intelligible Brain-to-Speech Synthesis Without Text Decoding](../../reviews/brain2speech-net-intelligible-real-time-brain-to-speech-synthesis-without-text-decoding/), [EMA2S: An End-to-End Multimodal Articulatory-to-Speech System](../../reviews/ema2s-an-end-to-end-multimodal-articulatory-to-speech-system/), [Sequence-to-Sequence Voice Reconstruction for Silent Speech in a Tonal Language](../../reviews/sequence-to-sequence-voice-reconstruction-for-silent-speech-in-a-tonal-language/), [Speech synthesis from neural decoding of spoken sentences](../../reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences/), [Ultrasound-based Silent Speech Interface Built on a Continuous Vocoder](../../reviews/ultrasound-based-silent-speech-interface-built-on-a-continuous-vocoder/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Vid2speech: Speech Reconstruction from Silent Video (CVPR 2017) |  | §（Human listening study） |
| Lip2AudSpec: Speech reconstruction from silent lip movements video |  | §4.3.4 |
| Learning Individual Speaking Styles for Accurate Lip to Speech Synthesis |  | Abstract |
| Digital Voicing of Silent Speech |  | §1 |
| An Improved Model for Voicing Silent Speech |  | § (matched passage) |
| Synthesizing Speech from Intracranial Depth Electrodes using an Encoder-Decoder Framework | 2022 | § (matched passage) |
| FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis | 2022 | § (matched passage) |
| Deep Speech Synthesis from Articulatory Representations |  | § (matched passage) |
| emg2speech: synthesizing speech from electromyography using self-supervised speech models | 2026 | § (matched passage) |
| Learning Individual Speaking Styles for Accurate Lip to Speech Synthesis | 2020 | Abstract |
| Noninvasive Speech Restoration After Total Laryngectomy Using Surface Electromyography: Pilot Study | 2026 | Methods (matched passage) |
| Statistical Conversion of Silent Articulation into Audible Speech using Full-Covariance HMM | 2016 | §（Perceptual evaluation） |
| A Real-Time Silent Speech System for Voice Restoration after Total Laryngectomy | 2018 | § (matched passage) |
| doi-10.1038-s41586-019-1119-1 |  | Results「Synthesis performance」、Methods「Intelligibility Assessment」 |
| doi-10.1038-s41586-025-09127-3 |  | Methods (matched passage) |
| A neural architecture for imagined and overt speech motor dynamics | 2026 | Methods (matched passage) |
| Towards reconstructing intelligible speech from the human auditory cortex | 2019 | Caption of the subjective-evaluation figure |
| Online speech synthesis using a chronically implanted brain-computer interface in an individual with ALS | 2024 | Ledger |
| doi-10.1109-taslp-2017-2757263 | 2017 | Abstract |
| Generating Intelligible Audio Speech from Visual Speech | 2017 | §VI |
| End-to-End Mandarin Speech Reconstruction Based on Ultrasound Tongue Images Using Deep Learning | 2025 | Ledger |
| Real-Time Control of an Articulatory-Based Speech Synthesizer for Brain Computer Interfaces | 2016 | Abstract |
| Digital Voicing of Silent Speech |  | §1 |
| An Improved Model for Voicing Silent Speech |  | § (matched passage) |
| Robust Articulatory Speech Synthesis using Deep Neural Networks for BCI Applications | 2014 | Ledger |
| Reconstructing intelligible audio speech from visual speech features | 2015 | §1 |
| Generating Natural, Intelligible Speech From Brain Activity in Motor, Premotor, and Inferior Frontal Cortices | 2019 | Methods「Listening Tests」 |
| Robust articulatory speech synthesis using deep neural networks for BCI applications | 2014 | Ledger |
| Reconstructing intelligible audio speech from visual speech features | 2015 | §1 |
| Reconstructing intelligible audio speech from visual speech features | 2015 | §1 |
| isca-taguchi18_interspeech |  | Ledger |
| Hush-Hush Speak: Speech Reconstruction Using Silent Videos | 2019 | §（Human evaluation） |
| Hush-Hush Speak: Speech Reconstruction Using Silent Videos |  | §（Human evaluation） |
| A neural architecture for imagined and overt speech motor dynamics | 2026 | Methods (matched passage) |
| A neural architecture for imagined and overt speech motor dynamics | 2026 | Methods (matched passage) |
| Decoding and synthesizing tonal language speech from brain activity | 2023 | Ledger |
| Online speech synthesis using a chronically implanted brain-computer interface in an individual with ALS | 2024 | Ledger |
| Noninvasive Speech Restoration After Total Laryngectomy Using Surface Electromyography: Pilot Study | 2026 | Methods (matched passage) |
| Noninvasive Speech Restoration After Total Laryngectomy Using Surface Electromyography: Pilot Study | 2026 | Methods (matched passage) |
| Noninvasive Speech Restoration After Total Laryngectomy Using Surface Electromyography: Pilot Study | 2026 | Methods (matched passage) |
| Noninvasive Speech Restoration After Total Laryngectomy Using Surface Electromyography: Pilot Study | 2025 | Methods (matched passage) |
| High-Resolution, Non-Invasive Imaging of Upper Vocal Tract Articulators Compatible | 2016 | Abstract (matched passage) |
| Generating Natural, Intelligible Speech From Brain Activity in Motor, Premotor, and Inferior Frontal Cortices | 2019 | Methods「Listening Tests」 |
| Generating Natural, Intelligible Speech From Brain Activity in Motor, Premotor, and Inferior Frontal Cortices | 2019 | Methods「Listening Tests」 |
| Sequence-to-Sequence Voice Reconstruction for Silent Speech in a Tonal Language | 2022 | Ledger |
| Sequence-to-Sequence Voice Reconstruction for Silent Speech in a Tonal Language | 2022 | Ledger |

## lrs3-visual-only-wer

- Table: [`lrs3-visual-only-wer.csv`](lrs3-visual-only-wer.csv) (6960 slot-filled, 258 pattern match, usual design in 18, 1 read in full)
- Inclusion rule: Include studies that report word error rate of visual-only (lip-reading) recognition on the LRS3 test set, any training regime. Boundary: exclude audio-only and audio-visual WER rows, LRS2/LRW/GRID-only results, and numbers quoted from other papers without new training; count versions of one study once.
- Used in: [AKVSR: Audio Knowledge Empowered Visual Speech Recognition by Compressing Audio Knowledge of a Pretrained Model](../../reviews/akvsr-audio-knowledge-empowered-visual-speech-recognition-by-compressing-audio-knowledge-of-a-pretrained-model/), [Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels](../../reviews/auto-avsr-audio-visual-speech-recognition-with-automatic-labels/), [Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction](../../reviews/learning-audio-visual-speech-representation-by-masked-multimodal-cluster-prediction/), [Visual Speech Recognition for Multiple Languages in the Wild](../../reviews/visual-speech-recognition-for-multiple-languages-in-the-wild/)

## lrw-word-accuracy

- Table: [`lrw-word-accuracy.csv`](lrw-word-accuracy.csv) (6960 slot-filled, 155 pattern match, usual design in 90, 2 read in full)
- Inclusion rule: Visual-only word-level lip reading evaluated on the English LRW benchmark (500 words, BBC clips) with top-1 accuracy on its test set. Boundary: LRW-1000 / CAS-VSR-W1k and other-language LRW variants are excluded; audio-visual results count only when a visual-only figure is also reported; results that feed word-boundary indicators to the model are kept but labelled; versions of one study count once.
- Used in: [Combining Residual Networks with LSTMs for Lipreading](../../reviews/combining-residual-networks-with-lstms-for-lipreading/), [Landmark Guided Visual Feature Extractor for Visual Speech Recognition with Limited Resource](../../reviews/landmark-guided-visual-feature-extractor-for-visual-speech-recognition-with-limited-resource/), [Lipreading using Temporal Convolutional Networks](../../reviews/lipreading-using-temporal-convolutional-networks/)

## neural-speech-reconstruction-identification-test

- Table: [`neural-speech-reconstruction-identification-test.csv`](neural-speech-reconstruction-identification-test.csv) (6960 slot-filled, 173 pattern match, usual design in 122, 4 read in full)
- Inclusion rule: Studies that reconstruct a continuous acoustic speech representation (spectrogram, mel features, envelope or waveform) from neural recordings (EEG, MEG, ECoG, sEEG or intracortical) during perceived, produced, mimed or imagined speech and evaluate the reconstruction. Boundary: classification-only and text-only decoders are excluded; auditory attention decoding that only tracks an envelope to select a talker is counted by the ledger pattern but is not a reconstruction study; versions of one study count once. Design categories are full-text pattern matches and overlap: correlation, identification among candidates, mel-cepstral distortion, human listening test, STOI.
- Used in: [Relating the Neural Representations of Vocalized, Mimed, and Imagined Speech](../../reviews/relating-the-neural-representations-of-vocalized-mimed-and-imagined-speech/), [Speech Synthesis from ECoG using Densely Connected 3D Convolutional Neural Networks](../../reviews/speech-synthesis-from-ecog-using-densely-connected-3d-convolutional-neural-networks/)

## neural-text-unseen-sentence-test

- Table: [`neural-text-unseen-sentence-test.csv`](neural-text-unseen-sentence-test.csv) (6960 slot-filled, 145 pattern match, usual design in 21, 4 read in full)
- Inclusion rule: Same population as neural-text-output-unit. The design compared is whether the reported WER is measured on sentences absent from training (sentence-disjoint) or on repeats of training sentences. Boundary: a paper is counted under each protocol its text names; reviews count as pattern matches only.
- Used in: [A cross-species neural foundation model for end-to-end speech decoding](../../reviews/a-cross-species-neural-foundation-model-for-end-to-end-speech-decoding/), [Brain-to-text: decoding spoken phrases from phone representations in the brain](../../reviews/brain-to-text-decoding-spoken-phrases-from-phone-representations-in-the-brain/), [Brain2Char: a deep architecture for decoding text from brain recordings](../../reviews/brain2char-a-deep-architecture-for-decoding-text-from-brain-recordings/), [Continuous Silent Speech Recognition using EEG](../../reviews/continuous-silent-speech-recognition-using-eeg/), [EEG-to-Voice Decoding of Spoken and Imagined speech Using Non-Invasive EEG](../../reviews/eeg-to-voice-decoding-of-spoken-and-imagined-speech-using-non-invasive-eeg/), [High-performance brain-to-text communication via handwriting](../../reviews/high-performance-brain-to-text-communication-via-handwriting/), [iPhoneme: Brain-to-Text Communication for ALS Using ConformerXL Decoding](../../reviews/iphoneme-brain-to-text-communication-for-als-using-conformerxl-decoding/), [Machine translation of cortical activity to text with an encoder-decoder framework](../../reviews/machine-translation-of-cortical-activity-to-text-with-an-encoder-decoder-framework/), [Reconstructing Unseen Sentences from Speech-related Biosignals for Open-vocabulary Neural Communication](../../reviews/reconstructing-unseen-sentences-from-speech-related-biosignals-for-open-vocabulary-neural-commun/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Reconstructing Unseen Sentences from Speech-related Biosignals for Open-vocabulary Neural Communication | 2025 | Sec. II-A; Table II |

## non-acoustic-speech-activity-evaluation-protocol

- Table: [`non-acoustic-speech-activity-evaluation-protocol.csv`](non-acoustic-speech-activity-evaluation-protocol.csv) (6960 slot-filled, 119 pattern match, usual design in 46, 5 read in full)
- Inclusion rule: Same population as M06/non-acoustic-speech-activity-detection; classify the evaluation protocol of the detector: held-out speakers (speaker-independent, leave-one-subject-out), held-out sessions, or a single speaker. Boundary: a pattern hit in a paper that uses VAD only as preprocessing counts toward the upper bound.
- Used in: [Voice Activity Detection for Ultrasound-based Silent Speech Interfaces using Convolutional Neural Networks](../../reviews/voice-activity-detection-for-ultrasound-based-silent-speech-interfaces-using-convolutional-neural-networks/)

## null-model-construction-neural-decoding

- Table: [`null-model-construction-neural-decoding.csv`](null-model-construction-neural-decoding.csv) (6960 slot-filled, 132 pattern match, usual design in 45, 2 read in full)
- Inclusion rule: Neural decoding or neural-response prediction studies that test significance against an empirical null built by shuffling or permuting the data (labels, trials, time, channels) rather than only against a theoretical chance level. Boundary: studies that report only theoretical chance are excluded; a null that is mentioned but not described still counts; versions of one study count once.
- Used in: [A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses](../../reviews/a-convolutional-framework-for-mapping-imagined-auditory-meg-into-listened-brain-responses/), [Brain-to-text: decoding spoken phrases from phone representations in the brain](../../reviews/brain-to-text-decoding-spoken-phrases-from-phone-representations-in-the-brain/), [Mechanistic Interpretability of Brain-to-Speech Models Across Speech Modes](../../reviews/mechanistic-interpretability-of-brain-to-speech-models-across-speech-modes/), [Relating the Neural Representations of Vocalized, Mimed, and Imagined Speech](../../reviews/relating-the-neural-representations-of-vocalized-mimed-and-imagined-speech/), [Semantic reconstruction of continuous language from non-invasive brain recordings](../../reviews/semantic-reconstruction-of-continuous-language-from-non-invasive-brain-recordings/), [Transfer Learning from ImageNet for MEG-Based Decoding of Imagined Speech](../../reviews/transfer-learning-from-imagenet-for-meg-based-decoding-of-imagined-speech/), [Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping](../../reviews/zero-shot-imagined-speech-decoding-via-imagined-to-listened-meg-mapping/)

## radar-ssr-speaker-split

- Table: [`radar-ssr-speaker-split.csv`](radar-ssr-speaker-split.csv) (6960 slot-filled, 32 pattern match, usual design in 22, 3 read in full)
- Inclusion rule: Speech or silent-speech recognition studies on radar or RF sensing of the articulators (same population as radar-ssr-input-representation); the design compared is whether test speakers are held out from training (speaker-independent, cross-user or new-user test) or every model is trained and tested within one speaker (speaker-dependent, per-participant cross-validation). Boundary: a paper counts under every split it reports; pooling several speakers' data without holding any speaker out counts as speaker-dependent; full-text pattern hits include mentions in related-work sections, so counts are upper bounds.
- Used in: [IR-UWB Radar-Based Contactless Silent Speech Recognition of Vowels, Consonants, Words, and Phrases](../../reviews/ir-uwb-radar-based-contactless-silent-speech-recognition-of-vowels-consonants-words-and-phrases/), [Lip-Siri: Contactless Open-Sentence Silent Speech with Wi-Fi Backscatter](../../reviews/lip-siri-contactless-open-sentence-silent-speech-with-wi-fi-backscatter/), [Movement Detection of Tongue and Related Body Parts Using IR-UWB Radar](../../reviews/movement-detection-of-tongue-and-related-body-parts-using-ir-uwb-radar/)

## real-time-intracranial-speech-online-evaluation

- Table: [`real-time-intracranial-speech-online-evaluation.csv`](real-time-intracranial-speech-online-evaluation.csv) (6960 slot-filled, 134 pattern match, usual design in 18, 3 read in full)
- Inclusion rule: Intracranial (ECoG, sEEG, intracortical) speech decoding studies whose ledger text mentions real-time, online or closed-loop operation; the design of interest is what the evaluation reports for that operation: an online accuracy or error-rate figure, an offline simulation or replay of the real-time pipeline, and a numeric latency. Boundary: listening-only and review papers enter through the pattern, so counts are upper bounds; versions once.
- Used in: [Real-time decoding of question-and-answer speech dialogue using human cortical activity](../../reviews/real-time-decoding-of-question-and-answer-speech-dialogue-using-human-cortical-activity/)

## rtmri-decoding-test-split

- Table: [`rtmri-decoding-test-split.csv`](rtmri-decoding-test-split.csv) (6960 slot-filled, 88 pattern match, usual design in 11, 5 read in full)
- Inclusion rule: Same population as M08 rtmri-decoder-output (88 unique ledger studies whose ledger text names rtMRI, real-time or dynamic MRI, MRI-TIMIT, USC-TIMIT or the Vocal Tract Morphology MRI database). The design compared is the test protocol of studies that train a decoder or classifier on vocal-tract MRI: held-out (unseen) test speakers, sentence-disjoint test material, and repeated splits, folds or seeds. Boundary: a study counts under every protocol its full text names (upper bound, related-work mentions included); analysis-only studies without a trained model fall outside the comparison even when matched.
- Used in: [Silent Speech and Emotion Recognition from Vocal Tract Shape Dynamics in Real-Time MRI](../../reviews/silent-speech-and-emotion-recognition-from-vocal-tract-shape-dynamics-in-real-time-mri/)

## silent-emg-voicing-benchmark

- Table: [`silent-emg-voicing-benchmark.csv`](silent-emg-voicing-benchmark.csv) (6960 slot-filled, 16 pattern match, usual design in 9, 4 read in full)
- Inclusion rule: Include studies that synthesize audible speech from silently articulated surface EMG on the Gaddy open-vocabulary corpus and score it by ASR or listener transcription. Boundary: exclude recognition-only (text output) studies, other corpora, and voiced-EMG-only results; count versions once.
- Used in: [An Improved Model for Voicing Silent Speech](../../reviews/an-improved-model-for-voicing-silent-speech/), [Digital Voicing of Silent Speech](../../reviews/digital-voicing-of-silent-speech/), [From Silent Signals to Natural Language: A Dual-Stage Transformer-LLM Approach](../../reviews/from-silent-signals-to-natural-language-a-dual-stage-transformer-llm-approach/), [Speaking Without Sound: Multi-speaker Silent Speech Voicing with Facial Inputs Only](../../reviews/speaking-without-sound-multi-speaker-silent-speech-voicing-with-facial-inputs-only/)

## silent-speech-challenge-benchmark

- Table: [`silent-speech-challenge-benchmark.csv`](silent-speech-challenge-benchmark.csv) (6960 slot-filled, 8 pattern match, usual design in 3, 4 read in full)
- Inclusion rule: Include studies that report recognition or reconstruction results on the Silent Speech Challenge archive (single speaker, silent TIMIT training, 100 WSJ0 5k test sentences) or that test on the same 100 SSC sentences with a new recording. Boundary: exclude studies that only cite the SSC, surveys that restate its numbers (kept in the pattern match), and studies on other ultrasound corpora; count versions once.
- Used in: [Denoising Convolutional Autoencoder Based B-mode Ultrasound Tongue Image Feature Extraction](../../reviews/denoising-convolutional-autoencoder-based-b-mode-ultrasound-tongue-image-feature-extraction/), [Updating the Silent Speech Challenge benchmark with deep learning](../../reviews/updating-the-silent-speech-challenge-benchmark-with-deep-learning/)

## text-and-video-to-speech-evaluation

- Table: [`text-and-video-to-speech-evaluation.csv`](text-and-video-to-speech-evaluation.csv) (6960 slot-filled, 9 pattern match, usual design in 6, 4 read in full)
- Inclusion rule: Same population as M06 text-and-video-to-speech-decoder; classify from the full text how synthesized speech is evaluated: SyncNet lip-sync scores (LSE-C/LSE-D), length-weighted mel-cepstral distortion (MCD-DTW-SL), listener or opinion tests, ASR WER and speaker similarity. Boundary: a study counts under every protocol its text names (upper bound); versions once.
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

## ultrasound-to-speech-output-evaluation

- Table: [`ultrasound-to-speech-output-evaluation.csv`](ultrasound-to-speech-output-evaluation.csv) (6960 slot-filled, 51 pattern match, usual design in 21, 3 read in full)
- Inclusion rule: Include studies that synthesize speech or acoustic features from ultrasound tongue images (with or without lip video) and evaluate the output; classify the output measures used (MCD or other spectral distance, MUSHRA or MOS ratings, listener transcription or identification, ASR on the synthesized speech). Boundary: exclude recognition-only studies, contour tracking and reviews (they inflate the pattern match, an upper bound); count versions once by key.
- Used in: [3D Convolutional Neural Networks for Ultrasound-Based Silent Speech Interfaces](../../reviews/3d-convolutional-neural-networks-for-ultrasound-based-silent-speech-interfaces/), [Adaptation of Tongue Ultrasound-Based Silent Speech Interfaces Using Spatial Transformer Networks](../../reviews/adaptation-of-tongue-ultrasound-based-silent-speech-interfaces-using-spatial-transformer-networks/), [Conformer-based Ultrasound-to-Speech Conversion](../../reviews/conformer-based-ultrasound-to-speech-conversion/), [Improved Processing of Ultrasound Tongue Videos by Combining ConvLSTM and 3D Convolutional Networks](../../reviews/improved-processing-of-ultrasound-tongue-videos-by-combining-convlstm-and-3d-convolutional-networks/), [Improving Neural Silent Speech Interface Models by Adversarial Training](../../reviews/improving-neural-silent-speech-interface-models-by-adversarial-training/), [Speech Reconstruction from Silent Tongue and Lip Articulation By Pseudo Target Generation and Domain Adversarial Training](../../reviews/speech-reconstruction-from-silent-tongue-and-lip-articulation-by-pseudo-target-generation-and-domain-adversarial-training/), [Speech Synthesis from Text and Ultrasound Tongue Image-based Articulatory Input](../../reviews/speech-synthesis-from-text-and-ultrasound-tongue-image-based-articulatory-input/), [Ultra2Speech - A Deep Learning Framework for Formant Frequency Estimation and Tracking from Ultrasound Tongue Images](../../reviews/ultra2speech-a-deep-learning-framework-for-formant-frequency-estimation-and-tracking-from-ultrasound-tongue-images/), [Voice Activity Detection for Ultrasound-based Silent Speech Interfaces using Convolutional Neural Networks](../../reviews/voice-activity-detection-for-ultrasound-based-silent-speech-interfaces-using-convolutional-neural-networks/)

## ultrasound-tongue-speaker-split

- Table: [`ultrasound-tongue-speaker-split.csv`](ultrasound-tongue-speaker-split.csv) (6960 slot-filled, 148 pattern match, usual design in 48, 4 read in full)
- Inclusion rule: Include studies whose ledger lists ultrasound imaging as an input modality and classify by full-text pattern (reference list removed where the script detects it) whether evaluation holds out speakers (speaker-independent, unseen or held-out speakers, leave-one-speaker-out, cross-speaker) or trains and tests within the same speakers (speaker-dependent, single-speaker). Boundary: mentions in related work and reviews count as pattern matches (upper bound); a study counts under every split it reports; versions count once by key.
- Used in: [Convolutional Neural Network-Based Age Estimation Using B-Mode Ultrasound Tongue Image](../../reviews/convolutional-neural-network-based-age-estimation-using-b-mode-ultrasound-tongue-image/)

## video-to-speech-output-evaluation

- Table: [`video-to-speech-output-evaluation.csv`](video-to-speech-output-evaluation.csv) (6960 slot-filled, 165 pattern match, usual design in 83, 5 read in full)
- Inclusion rule: Include studies that synthesize a speech waveform from talking-face or lip video (the population of the M06 video-to-speech-synthesis table) and compare how the synthesized speech is evaluated: human listener or opinion tests, ASR word error on the synthesized speech, and tests on speakers unseen in training. Boundary: audio-visual enhancement with noisy audio at test, talking-head generation, text-only lip reading and video-to-text-to-TTS pipelines excluded; a study counts under every protocol its full text names (upper bound, related-work mentions included); versions counted once.
- Used in: [Audio-visual video-to-speech synthesis with synthesized input audio](../../reviews/audio-visual-video-to-speech-synthesis-with-synthesized-input-audio/), [FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis](../../reviews/fastlts-non-autoregressive-end-to-end-unconstrained-lip-to-speech-synthesis/), [Harnessing AI for Speech Reconstruction using Multi-view Silent Video Feed](../../reviews/harnessing-ai-for-speech-reconstruction-using-multi-view-silent-video-feed/), [Improved Speech Reconstruction from Silent Video](../../reviews/improved-speech-reconstruction-from-silent-video/), [Large-scale unsupervised audio pre-training for video-to-speech synthesis](../../reviews/large-scale-unsupervised-audio-pre-training-for-video-to-speech-synthesis/), [LipDiffuser: Lip-to-Speech Generation with Conditional Diffusion Models](../../reviews/lipdiffuser-lip-to-speech-generation-with-conditional-diffusion-models/), [Lipper: Synthesizing Thy Speech using Multi-View Lipreading](../../reviews/lipper-synthesizing-thy-speech-using-multi-view-lipreading/), [LipVoicer: Generating Speech from Silent Videos Guided by Lip Reading](../../reviews/lipvoicer-generating-speech-from-silent-videos-guided-by-lip-reading/), [LTA-L2S: Lexical Tone-Aware Lip-to-Speech Synthesis for Mandarin with Cross-Lingual Transfer Learning](../../reviews/lta-l2s-lexical-tone-aware-lip-to-speech-synthesis-for-mandarin-with-cross-lingual-transfer-lear/), [NaturalL2S: End-to-End High-quality Multispeaker Lip-to-Speech Synthesis with Differential Digital Signal Processing](../../reviews/naturall2s-end-to-end-high-quality-multispeaker-lip-to-speech-synthesis-with-differential-digita/), [RESOUND: Speech Reconstruction from Silent Videos via Acoustic-Semantic Decomposed Modeling](../../reviews/resound-speech-reconstruction-from-silent-videos-via-acoustic-semantic-decomposed-modeling/), [RobustL2S: Speaker-Specific Lip-to-Speech Synthesis exploiting Self-Supervised Representations](../../reviews/robustl2s-speaker-specific-lip-to-speech-synthesis-exploiting-self-supervised-representations/), [SLD-L2S: Hierarchical Subspace Latent Diffusion for High-Fidelity Lip to Speech Synthesis](../../reviews/sld-l2s-hierarchical-subspace-latent-diffusion-for-high-fidelity-lip-to-speech-synthesis/), [SVTS: Scalable Video-to-Speech Synthesis](../../reviews/svts-scalable-video-to-speech-synthesis/), [VCVTS: Multi-Speaker Video-to-Speech Synthesis via Cross-Modal Knowledge Transfer from Voice Conversion](../../reviews/vcvts-multi-speaker-video-to-speech-synthesis-via-cross-modal-knowledge-transfer-from-voice-conversion/), [Vid2speech: Speech Reconstruction from Silent Video](../../reviews/vid2speech-speech-reconstruction-from-silent-video/), [Video-Driven Speech Reconstruction using Generative Adversarial Networks](../../reviews/video-driven-speech-reconstruction-using-generative-adversarial-networks/), [Zero-Shot Personalized Lip-to-Speech Synthesis with Face Image Based Voice Control](../../reviews/zero-shot-personalized-lip-to-speech-synthesis-with-face-image-based-voice-control/)

## video-to-speech-speaker-held-out-test

- Table: [`video-to-speech-speaker-held-out-test.csv`](video-to-speech-speaker-held-out-test.csv) (6960 slot-filled, 165 pattern match, usual design in 78, 5 read in full)
- Inclusion rule: Include the video-to-speech population of components/M06/video-to-speech-synthesis (speech waveform synthesized from talking-face or lip video, audio muted at test) and count, from the full text with the reference list removed, the evaluation protocols named: a test on speakers held out of training (unseen, speaker-independent, speaker-disjoint, out-of-domain speakers), listener or opinion-score tests, ASR WER on the output, and repeated runs over seeds. Boundary: a study counts under every protocol its text names (upper bound; related-work mentions included); enhancement with noisy audio at test, talking-head generation and video-to-text-to-speech pipelines excluded; versions counted once.
- Used in: [Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading](../../reviews/cross-modal-masking-for-robust-silent-speech-synthesis-using-semg-and-lipreading/), [Let There Be Sound: Reconstructing High Quality Speech from Silent Videos](../../reviews/let-there-be-sound-reconstructing-high-quality-speech-from-silent-videos/), [Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild](../../reviews/lip-to-speech-synthesis-for-arbitrary-speakers-in-the-wild/), [LipSody: Lip-to-Speech Synthesis with Enhanced Prosody Consistency](../../reviews/lipsody-lip-to-speech-synthesis-with-enhanced-prosody-consistency/), [Speaker disentanglement in video-to-speech conversion](../../reviews/speaker-disentanglement-in-video-to-speech-conversion/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild | 2022 | Table 3 caption; Supplement A.1.1 |

## voiced-emg-to-speech-benchmark

- Table: [`voiced-emg-to-speech-benchmark.csv`](voiced-emg-to-speech-benchmark.csv) (6960 slot-filled, 23 pattern match, usual design in 11, 3 read in full)
- Inclusion rule: Include studies that synthesize speech from vocalized (audible) surface EMG and report a word error rate of the synthesized speech, by ASR or listener transcription. Boundary: silent-EMG-only results belong to silent-emg-voicing-benchmark; recognition-only (EMG-to-text) studies are excluded; tests on synthetic EMG are recorded as a design value, not as a benchmark result; versions once.
- Used in: [Confidence-Based Self-Training for EMG-to-Speech: Leveraging Synthetic EMG for Robust Modeling](../../reviews/confidence-based-self-training-for-emg-to-speech-leveraging-synthetic-emg-for-robust-modeling/)

## wearable-sensor-word-test-split

- Table: [`wearable-sensor-word-test-split.csv`](wearable-sensor-word-test-split.csv) (6960 slot-filled, 143 pattern match, usual design in 65, 3 read in full)
- Inclusion rule: Word or command classification studies whose ledger names a wearable non-acoustic sensor on the face or neck (strain, piezo or triboelectric sensor, surface EMG, accelerometer); the design compared is how test samples are separated from training samples: speaker-disjoint, session- or day-disjoint, or a random or per-class sample split. Boundary: a paper counts under every split it reports; reviews and acoustic-only studies are excluded when read.
- Used in: [Knowledge Distilled Ensemble Model for sEMG-based Silent Speech Interface](../../reviews/knowledge-distilled-ensemble-model-for-semg-based-silent-speech-interface/), [Silent Speech Sentence Recognition with Six-Axis Accelerometers using Conformer and CTC Algorithm](../../reviews/silent-speech-sentence-recognition-with-six-axis-accelerometers-using-conformer-and-ctc-algorith/), [SilentWear: an Ultra-Low Power Wearable System for EMG-based Silent Speech Recognition](../../reviews/silentwear-an-ultra-low-power-wearable-system-for-emg-based-silent-speech-recognition/), [Soft Active EMG Interface for Machine Learning-Enabled Silent Speech Recognition](../../reviews/soft-active-electromyography-interface-for-machine-learning-enabled-silent-speech-recognition/), [Ultrasensitive Textile Strain Sensors Redefine Wearable Silent Speech Interfaces with High Machine Learning Efficiency](../../reviews/ultrasensitive-textile-strain-sensors-redefine-wearable-silent-speech-interfaces-with-high-machine-learning-efficiency/), [Wireless Silent Speech Interface Using Multi-Channel Textile EMG Sensors Integrated into Headphones](../../reviews/wireless-silent-speech-interface-using-multi-channel-textile-emg-sensors-integrated-into-headpho/)

## whisper-conversion-evaluation

- Table: [`whisper-conversion-evaluation.csv`](whisper-conversion-evaluation.csv) (6960 slot-filled, 60 pattern match, usual design in 26, 4 read in full)
- Inclusion rule: Same population as M02/whisper-to-normal-training-pairing (whispered, murmured or alaryngeal speech converted to voiced speech audio); classify how the converted speech is evaluated: listener quality ratings (MOS, CMOS, MUSHRA), spectral distance to a paired reference (MCD), ASR word or character error rate, or listener transcription. Boundary: a study counts under every measure it reports; measures named only in related work do not count; versions counted once.
- Used in: [WESPER: Zero-shot and Realtime Whisper to Normal Voice Conversion for Whisper-based Speech Interactions](../../reviews/wesper-zero-shot-and-realtime-whisper-to-normal-voice-conversion-for-whisper-based-speech-interactions/)
