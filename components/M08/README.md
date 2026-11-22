# M08 Output

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## articulatory-f0-prediction

- Table: [`articulatory-f0-prediction.csv`](articulatory-f0-prediction.csv) (3268 slot-filled, 138 pattern match, usual design in 31, 5 read in full)
- Inclusion rule: Include studies that generate speech (waveform or vocoder features) from a non-acoustic speech signal (ultrasound, EMA, PMA, EMG, lip or face video, rtMRI, intracranial or scalp neural recordings) and in which F0 or voicing of the output is predicted or evaluated. Boundary: exclude acoustic-input conversion (whisper, electrolarynx or NAM as the only input), talking-head or head-motion synthesis driven by speech, text-to-speech after text decoding, and reviews; the pattern match is an upper bound; versions count once by key.
- Used in: [Autoencoder-Based Articulatory-to-Acoustic Mapping for Ultrasound Silent Speech Interfaces](../../reviews/autoencoder-based-articulatory-to-acoustic-mapping-for-ultrasound-silent-speech-interfaces/), [Ultrasound-based Silent Speech Interface Built on a Continuous Vocoder](../../reviews/ultrasound-based-silent-speech-interface-built-on-a-continuous-vocoder/)

## biosignal-to-speech-voice-control

- Table: [`biosignal-to-speech-voice-control.csv`](biosignal-to-speech-voice-control.csv) (3268 slot-filled, 93 pattern match, usual design in 48, 4 read in full)
- Inclusion rule: Include studies that synthesize speech audio from a non-acoustic speech signal (surface EMG, mouth or face video, ultrasound, articulography, neural recordings) and set the output voice through a speaker representation, whether taken from reference audio, a speaker label or a face image. Boundary: exclude single-voice systems that only reproduce the recorded speaker, text-to-speech after text decoding, and conversion from acoustic input (whisper, NAM); count versions of one study once.
- Used in: [Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild](../../reviews/lip-to-speech-synthesis-for-arbitrary-speakers-in-the-wild/), [Speaker disentanglement in video-to-speech conversion](../../reviews/speaker-disentanglement-in-video-to-speech-conversion/), [Speaking Without Sound: Multi-speaker Silent Speech Voicing with Facial Inputs Only](../../reviews/speaking-without-sound-multi-speaker-silent-speech-voicing-with-facial-inputs-only/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild | 2022 | Sec. 3.2.4 |

## intracranial-synthesis-waveform-generation

- Table: [`intracranial-synthesis-waveform-generation.csv`](intracranial-synthesis-waveform-generation.csv) (3268 slot-filled, 180 pattern match, usual design in 51, 2 read in full)
- Inclusion rule: Include studies that reconstruct speech acoustics (spectrograms, vocoder features or waveforms) from intracranial recordings (ECoG, sEEG or depth electrodes, intracortical arrays) made during overt, mouthed, attempted or imagined speech production. Boundary: exclude reconstruction of heard speech, text-only decoding read out by a TTS engine, and reviews or citation-only mentions; count versions of one study once. The ledger pattern also admits some reviews and text-decoding papers, so its count is an upper bound. Design of interest: how predicted acoustic features become a waveform (neural vocoder such as WaveNet, WaveGlow or HiFi-GAN; Griffin-Lim or other iterative phase reconstruction; parametric vocoder; unit selection).
- Used in: [Brain-to-Speech: Prosody Feature Engineering and Transformer-Based Reconstruction](../../reviews/brain-to-speech-prosody-feature-engineering-and-transformer-based-reconstruction/), [Brain2Speech-Net: Fast and Intelligible Brain-to-Speech Synthesis Without Text Decoding](../../reviews/brain2speech-net-intelligible-real-time-brain-to-speech-synthesis-without-text-decoding/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Brain2Speech-Net: Fast and Intelligible Brain-to-Speech Synthesis Without Text Decoding | 2026 | Sec. 4 |

## neural-speech-synthesis

- Table: [`neural-speech-synthesis.csv`](neural-speech-synthesis.csv) (3268 slot-filled, 35 pattern match, usual design in 11, 2 read in full)
- Inclusion rule: Include studies that decode continuous acoustic representations (spectrograms, MFCC or vocoder features, formants) from non-acoustic neural signals (ECoG, sEEG, intracortical electrodes, EEG, MEG, etc.) associated with speech production (overt, mouthed, attempted, imagined) and either output them as speech or evaluate them in a form convertible to speech. Boundary: exclude studies that reconstruct heard speech from activity during listening (perception). Exclude those that only decode text and then read it aloud with a standard speech synthesizer. Exclude BCIs that operate a synthesizer through limb motor imagery or the like, since this is not activity associated with speech production. Exclude matches in reviews, ethics papers or citations only. Count different versions of the same study as one item.
- Used in: [A high-performance neuroprosthesis for speech decoding and avatar control](../../reviews/a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control/), [An instantaneous voice-synthesis neuroprosthesis](../../reviews/an-instantaneous-voice-synthesis-neuroprosthesis/), [Speech synthesis from neural decoding of spoken sentences](../../reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences/)

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

## neural-text-output-unit

- Table: [`neural-text-output-unit.csv`](neural-text-output-unit.csv) (3268 slot-filled, 145 pattern match, usual design in 63, 5 read in full)
- Inclusion rule: Neural decoders (ECoG, intracortical, sEEG, EEG, MEG) that output text and report a word, character or phoneme error rate. The design compared is the unit the decoder emits before any lexicon or language model: characters, phonemes, or whole words / sentence classes. Boundary: a paper is counted under every unit its text names; handwriting and spelling BCIs count as characters; count versions once.
- Used in: [Brain2Char: a deep architecture for decoding text from brain recordings](../../reviews/brain2char-a-deep-architecture-for-decoding-text-from-brain-recordings/)

## paralinguistic-output-from-production-signals

- Table: [`paralinguistic-output-from-production-signals.csv`](paralinguistic-output-from-production-signals.csv) (3268 slot-filled, 99 pattern match, usual design in 12, 4 read in full)
- Inclusion rule: Include studies that infer a paralinguistic property of the speaker or utterance (affect or emotion, speaker identity, speaking mode, prosody, intonation or pitch) from a non-acoustic speech-production signal recorded while speaking (EMG, EMA, ultrasound, real-time MRI, electropalatography, strain sensors, ECoG or intracortical recordings). Boundary: acoustic-only and face-video audiovisual emotion recognition are excluded; facial EMG or EEG emotion recognition without speech production is excluded; F0 or prosody counts only when reported as an output; surveys are pattern matches only; versions of one study count once.
- Used in: [Affect Decoding in Phonated and Silent Speech Production from Surface EMG](../../reviews/affect-decoding-in-phonated-and-silent-speech-production-from-surface-emg/)

## rf-ssr-output-granularity

- Table: [`rf-ssr-output-granularity.csv`](rf-ssr-output-granularity.csv) (3268 slot-filled, 33 pattern match, usual design in 5, 3 read in full)
- Inclusion rule: Radar or RF silent-speech and speech recognition studies (same population as M05 rf-articulator-sensing-placement, plus papers whose text mentions RF or FMCW sensing); the design compared is the output: a class label from a closed list of vowels, words, commands or sentences, versus a variable-length token sequence decoded into words and scored by WER. Boundary: a paper counts under every output it reports; classification over a fixed list of sentences counts as closed set; pattern counts include related-work mentions, so they are upper bounds.
- Used in: [Lip-Siri: Contactless Open-Sentence Silent Speech with Wi-Fi Backscatter](../../reviews/lip-siri-contactless-open-sentence-silent-speech-with-wi-fi-backscatter/)

## vsr-output-token-unit

- Table: [`vsr-output-token-unit.csv`](vsr-output-token-unit.csv) (3268 slot-filled, 633 pattern match, usual design in 120, 5 read in full)
- Inclusion rule: Same population as M06. The design compared is the output unit of open-vocabulary sentence-level lip reading: characters, sub-word tokens (WordPiece, SentencePiece/unigram, BPE), phonemes or visemes, or closed-set word classes. Boundary: word classification on LRW-type isolated words is counted as word classes, not as an open-vocabulary unit; a paper counts under every unit its text names as an output; reviews count as pattern matches only.
- Used in: [Sub-word Level Lip Reading With Visual Attention](../../reviews/sub-word-level-lip-reading-with-visual-attention/)
