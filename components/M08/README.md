# M08 Output

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## biosignal-to-speech-voice-control

- Table: [`biosignal-to-speech-voice-control.csv`](biosignal-to-speech-voice-control.csv) (3268 slot-filled, 93 pattern match, usual design in 48, 4 read in full)
- Inclusion rule: Include studies that synthesize speech audio from a non-acoustic speech signal (surface EMG, mouth or face video, ultrasound, articulography, neural recordings) and set the output voice through a speaker representation, whether taken from reference audio, a speaker label or a face image. Boundary: exclude single-voice systems that only reproduce the recorded speaker, text-to-speech after text decoding, and conversion from acoustic input (whisper, NAM); count versions of one study once.
- Used in: [Speaking Without Sound: Multi-speaker Silent Speech Voicing with Facial Inputs Only](../../reviews/speaking-without-sound-multi-speaker-silent-speech-voicing-with-facial-inputs-only/)

## intracranial-synthesis-waveform-generation

- Table: [`intracranial-synthesis-waveform-generation.csv`](intracranial-synthesis-waveform-generation.csv) (3268 slot-filled, 180 pattern match, usual design in 51, 2 read in full)
- Inclusion rule: Include studies that reconstruct speech acoustics (spectrograms, vocoder features or waveforms) from intracranial recordings (ECoG, sEEG or depth electrodes, intracortical arrays) made during overt, mouthed, attempted or imagined speech production. Boundary: exclude reconstruction of heard speech, text-only decoding read out by a TTS engine, and reviews or citation-only mentions; count versions of one study once. The ledger pattern also admits some reviews and text-decoding papers, so its count is an upper bound. Design of interest: how predicted acoustic features become a waveform (neural vocoder such as WaveNet, WaveGlow or HiFi-GAN; Griffin-Lim or other iterative phase reconstruction; parametric vocoder; unit selection).
- Used in: [Brain-to-Speech: Prosody Feature Engineering and Transformer-Based Reconstruction](../../reviews/brain-to-speech-prosody-feature-engineering-and-transformer-based-reconstruction/)

## neural-speech-synthesis

- Table: [`neural-speech-synthesis.csv`](neural-speech-synthesis.csv) (3268 slot-filled, 35 pattern match, usual design in 11, 2 read in full)
- Inclusion rule: Include studies that decode continuous acoustic representations (spectrograms, MFCC or vocoder features, formants) from non-acoustic neural signals (ECoG, sEEG, intracortical electrodes, EEG, MEG, etc.) associated with speech production (overt, mouthed, attempted, imagined) and either output them as speech or evaluate them in a form convertible to speech. Boundary: exclude studies that reconstruct heard speech from activity during listening (perception). Exclude those that only decode text and then read it aloud with a standard speech synthesizer. Exclude BCIs that operate a synthesizer through limb motor imagery or the like, since this is not activity associated with speech production. Exclude matches in reviews, ethics papers or citations only. Count different versions of the same study as one item.
- Used in: [A high-performance neuroprosthesis for speech decoding and avatar control](../../reviews/a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control/), [Speech synthesis from neural decoding of spoken sentences](../../reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Synthesizing Speech from Intracranial Depth Electrodes using an Encoder-Decoder Framework | 2022 | Ledger |
| EEG-to-Voice Decoding of Spoken and Imagined speech Using Non-Invasive EEG | 2025 | Introduction (matched passage) |
| arxiv-2512.04618 |  | Ledger (study aim) |
| Brain-to-Speech: Prosody Feature Engineering and Transformer-Based Reconstruction | 2026 | Ledger (study aim) |
| Brain2Speech-Net: Fast and Intelligible Brain-to-Speech Synthesis Without Text Decoding | 2026 | Title |
| Brain2Speech-Net: Fast and Intelligible Brain-to-Speech Synthesis Without Text Decoding | 2026 | Title |
| Brain2Speech-Net: Fast and Intelligible Brain-to-Speech Synthesis Without Text Decoding | 2026 | Title |
| doi-10.1038-s41586-019-1119-1 |  | Methods「Neural decoder」「Speech synthesis from acoustic features」 |
| doi-10.1038-s41586-025-09127-3 |  | Ledger (study aim) |
| Speech Synthesis from ECoG using Densely Connected 3D Convolutional Neural Networks |  | Title, Abstract |
| Speech Synthesis from Stereotactic EEG using an Electrode Shaft Dependent Multi-Input Convolutional Neural Network Approach | 2021 | Ledger (study aim) |
| A Wireless Brain-Machine Interface for Real-Time Speech Synthesis | 2009 | Introduction、Methods |
| Decoding spectrotemporal features of overt and covert speech from the human cortex | 2014 | Introduction、Methods |
| Generating Natural, Intelligible Speech From Brain Activity in Motor, Premotor, and Inferior Frontal Cortices | 2019 | Methods |
| MiSTR: Multi-Modal iEEG-to-Speech Synthesis with Transformer-Based Prosody Prediction and Neural Phase Reconstruction | 2025 | Ledger (study aim) |
| Online speech synthesis using a chronically implanted brain-computer interface | 2024 | Ledger (study aim) |
| A neural speech decoding framework leveraging deep learning and speech | 2025 | Main text (matched passage) |
| A wireless brain-machine interface for real-time speech synthesis | 2009 | Introduction、Methods |
| A Wireless Brain-Machine Interface for Real-Time Speech Synthesis | 2009 | Introduction、Methods |
| Decoding spectrotemporal features of overt and covert speech from the human cortex | 2014 | Introduction、Methods |
| Speech Synthesis from ECoG using Densely Connected 3D Convolutional Neural Networks | 2019 | Title, Abstract |
| Generating Natural, Intelligible Speech From Brain Activity in Motor, Premotor, and Inferior Frontal Cortices | 2019 | Methods |
| Generating Natural, Intelligible Speech From Brain Activity in Motor, Premotor, and Inferior Frontal Cortices | 2019 | Methods |

## vsr-output-token-unit

- Table: [`vsr-output-token-unit.csv`](vsr-output-token-unit.csv) (3268 slot-filled, 633 pattern match, usual design in 120, 5 read in full)
- Inclusion rule: Same population as M06. The design compared is the output unit of open-vocabulary sentence-level lip reading: characters, sub-word tokens (WordPiece, SentencePiece/unigram, BPE), phonemes or visemes, or closed-set word classes. Boundary: word classification on LRW-type isolated words is counted as word classes, not as an open-vocabulary unit; a paper counts under every unit its text names as an output; reviews count as pattern matches only.
- Used in: [Sub-word Level Lip Reading With Visual Attention](../../reviews/sub-word-level-lip-reading-with-visual-attention/)
