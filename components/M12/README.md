# M12 Evaluation

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## human-lipreader-baseline

- Table: [`human-lipreader-baseline.csv`](human-lipreader-baseline.csv) (7 confirmed, 116 candidates read, 0 unread)
- Inclusion rule: Include studies that place, on the same metric, the results of machine lipreading or silent speech recognition alongside the results of human lipreaders (experts, people with hearing impairment, or general participants) reading the same data (the same test set or a subset of it). Boundary: exclude intelligibility assessments in which people listen to reconstructed speech. Exclude those that only cite human performance as literature values. Exclude studies of lipreading ability among humans with no machine results. Count different versions of the same study as one item.
- Used in: [Lip Reading Sentences in the Wild](../../reviews/lip-reading-sentences-in-the-wild/)

| Paper | Year | Evidence |
| --- | --- | --- |
| LipNet: End-to-End Sentence-level Lipreading (2016) |  | §1, §4.4 Table |
| Lip Reading Sentences in the Wild | 2017 | §5.2, Table 5 |
| Towards Estimating the Upper Bound of Visual-Speech Recognition: The Visual Lip-Reading Feasibility Database (FG 2017) |  | Abstract |
| Large-Scale Visual Speech Recognition |  | Abstract |
| The Lipreading Gap: Do VSR Models Perceive Visual Speech Like Human Lipreaders? |  | §1 |
| isca-hilder09_avsp |  | Abstract, §3.3 Table 1 |
| Human Audio-Visual Consonant Recognition Analyzed with Three Bimodal Integration Models | 2009 | §4, Fig. 3 |

## listener-intelligibility-test

- Table: [`listener-intelligibility-test.csv`](listener-intelligibility-test.csv) (6960 slot-filled, 37 pattern match, usual design in 15, 4 read in full)
- Inclusion rule: Include studies that evaluate speech synthesized from non-acoustic signals (neural activity, EMG, articulatory measurements such as EMA or PMA, ultrasound, mouth video) with an intelligibility test in which human listeners transcribe it or identify words or sentences from a set of choices, and report accuracy, WER or similar. Boundary: exclude those with only naturalness, preference or MOS ratings. Exclude conversion from acoustic input (whisper, NAM microphone, esophageal speech, etc.). Exclude synthesis from text and stimulus sounds for perception experiments. Exclude those that evaluate synthesized speech only with automatic speech recognition. Exclude matches in reviews or citations only. Count different versions of the same study as one item.
- Used in: [A high-performance neuroprosthesis for speech decoding and avatar control](../../reviews/a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control/), [EMA2S: An End-to-End Multimodal Articulatory-to-Speech System](../../reviews/ema2s-an-end-to-end-multimodal-articulatory-to-speech-system/), [Speech synthesis from neural decoding of spoken sentences](../../reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences/)

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
- Used in: [Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction](../../reviews/learning-audio-visual-speech-representation-by-masked-multimodal-cluster-prediction/), [Visual Speech Recognition for Multiple Languages in the Wild](../../reviews/visual-speech-recognition-for-multiple-languages-in-the-wild/)

## silent-emg-voicing-benchmark

- Table: [`silent-emg-voicing-benchmark.csv`](silent-emg-voicing-benchmark.csv) (6960 slot-filled, 16 pattern match, usual design in 9, 4 read in full)
- Inclusion rule: Include studies that synthesize audible speech from silently articulated surface EMG on the Gaddy open-vocabulary corpus and score it by ASR or listener transcription. Boundary: exclude recognition-only (text output) studies, other corpora, and voiced-EMG-only results; count versions once.
- Used in: [Speaking Without Sound: Multi-speaker Silent Speech Voicing with Facial Inputs Only](../../reviews/speaking-without-sound-multi-speaker-silent-speech-voicing-with-facial-inputs-only/)

## whisper-conversion-evaluation

- Table: [`whisper-conversion-evaluation.csv`](whisper-conversion-evaluation.csv) (6960 slot-filled, 60 pattern match, usual design in 26, 4 read in full)
- Inclusion rule: Same population as M02/whisper-to-normal-training-pairing (whispered, murmured or alaryngeal speech converted to voiced speech audio); classify how the converted speech is evaluated: listener quality ratings (MOS, CMOS, MUSHRA), spectral distance to a paired reference (MCD), ASR word or character error rate, or listener transcription. Boundary: a study counts under every measure it reports; measures named only in related work do not count; versions counted once.
- Used in: [WESPER: Zero-shot and Realtime Whisper to Normal Voice Conversion for Whisper-based Speech Interactions](../../reviews/wesper-zero-shot-and-realtime-whisper-to-normal-voice-conversion-for-whisper-based-speech-interactions/)
