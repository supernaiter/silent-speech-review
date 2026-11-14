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

- Table: [`listener-intelligibility-test.csv`](listener-intelligibility-test.csv) (6960 slot-filled, 37 pattern match, usual design in 15, 2 read in full)
- Inclusion rule: Include studies that evaluate speech synthesized from non-acoustic signals (neural activity, EMG, articulatory measurements such as EMA or PMA, ultrasound, mouth video) with an intelligibility test in which human listeners transcribe it or identify words or sentences from a set of choices, and report accuracy, WER or similar. Boundary: exclude those with only naturalness, preference or MOS ratings. Exclude conversion from acoustic input (whisper, NAM microphone, esophageal speech, etc.). Exclude synthesis from text and stimulus sounds for perception experiments. Exclude those that evaluate synthesized speech only with automatic speech recognition. Exclude matches in reviews or citations only. Count different versions of the same study as one item.
- Used in: [A high-performance neuroprosthesis for speech decoding and avatar control](../../reviews/a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control/), [Speech synthesis from neural decoding of spoken sentences](../../reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences/)

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
