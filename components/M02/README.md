# M02 Teacher signal

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## adversarial-loss-non-acoustic-to-speech

- Table: [`adversarial-loss-non-acoustic-to-speech.csv`](adversarial-loss-non-acoustic-to-speech.csv) (31 slot-filled, 400 pattern match, usual design in 129, 3 read in full)
- Inclusion rule: Include studies that generate speech (waveform, spectrogram or vocoder features) from a non-acoustic speech signal (ultrasound, EMA, PMA, EMG, lip or face video, radar, intracranial recordings) and train the mapping network itself with an adversarial (discriminator or critic) loss, alone or added to a regression loss. Boundary: exclude a GAN vocoder (HiFi-GAN, MelGAN, Parallel WaveGAN) trained only on audio and used off the shelf, domain-adversarial or gradient-reversal training against speaker or session, acoustic-input conversion (whisper, NAM) and reviews; the pattern match is an upper bound; versions count once by key.
- Used in: [Improving Neural Silent Speech Interface Models by Adversarial Training](../../reviews/improving-neural-silent-speech-interface-models-by-adversarial-training/)

## audio-knowledge-transfer-to-video

- Table: [`audio-knowledge-transfer-to-video.csv`](audio-knowledge-transfer-to-video.csv) (31 slot-filled, 54 pattern match, usual design in 40, 8 read in full)
- Inclusion rule: Include lip-reading and video-to-speech studies that take only lip or face video at test and use paired audio or a speech model during training to enrich the visual model, by knowledge distillation, regression of audio features, or a learned memory of audio representations recalled from video. Boundary: exclude audio-visual models that need audio at test and talking-head generation; full-text design counts are pattern matches (upper bounds, mentions included); count versions of one study once.
- Used in: [AKVSR: Audio Knowledge Empowered Visual Speech Recognition by Compressing Audio Knowledge of a Pretrained Model](../../reviews/akvsr-audio-knowledge-empowered-visual-speech-recognition-by-compressing-audio-knowledge-of-a-pretrained-model/), [Multi-modality Associative Bridging through Memory: Speech Sound Recollected from Face Video](../../reviews/multi-modality-associative-bridging-through-memory-speech-sound-recollected-from-face-video/)

## audio-only-pretraining-for-visual-speech-generation

- Table: [`audio-only-pretraining-for-visual-speech-generation.csv`](audio-only-pretraining-for-visual-speech-generation.csv) (31 slot-filled, 165 pattern match, usual design in 9, 2 read in full)
- Inclusion rule: Include the video-to-speech population of components/M06/video-to-speech-one-to-many-decoder (speech synthesized from lip or face video, audio muted at test) and count, from full text with the reference list removed, studies that pretrain the speech generator on audio without video before training with paired video, and studies that denoise or enhance the training target audio. Boundary: a study counts under every design its text names (upper bound, mentions and vocoder-only pretraining included); audio-visual enhancement with noisy audio at test is counted only if it is in that population; versions counted once.
- Used in: [LipDiffuser: Lip-to-Speech Generation with Conditional Diffusion Models](../../reviews/lipdiffuser-lip-to-speech-generation-with-conditional-diffusion-models/)

## auxiliary-phoneme-loss-in-speech-synthesis

- Table: [`auxiliary-phoneme-loss-in-speech-synthesis.csv`](auxiliary-phoneme-loss-in-speech-synthesis.csv) (31 slot-filled, 34 pattern match, usual design in 10, 3 read in full)
- Inclusion rule: Speech synthesis from a non-acoustic signal (EMG, ultrasound, articulography, video, neural) whose training adds a phoneme, phone-state, CTC or text classification loss on a shared encoder that is discarded or used only as guidance at synthesis time. Boundary: recognition-only models, cascaded recognize-then-TTS systems, and regression-only auxiliary targets are excluded; versions counted once.
- Used in: [An Improved Model for Voicing Silent Speech](../../reviews/an-improved-model-for-voicing-silent-speech/), [emg2speech: Synthesizing speech from electromyography using self-supervised speech models](../../reviews/emg2speech-synthesizing-speech-from-electromyography-using-self-supervised-speech-models/), [Sequence-to-Sequence Voice Reconstruction for Silent Speech in a Tonal Language](../../reviews/sequence-to-sequence-voice-reconstruction-for-silent-speech-in-a-tonal-language/), [Vocoder-Based Speech Synthesis from Silent Videos](../../reviews/vocoder-based-speech-synthesis-from-silent-videos/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Sequence-to-Sequence Voice Reconstruction for Silent Speech in a Tonal Language | 2021 | Sec. III-D |

## auxiliary-representation-prediction

- Table: [`auxiliary-representation-prediction.csv`](auxiliary-representation-prediction.csv) (31 slot-filled, 104 pattern match, usual design in 8, 6 read in full)
- Inclusion rule: Include visual or biosignal speech-recognition studies whose training adds a loss that predicts or regresses representations produced by a pretrained audio or visual encoder (cross-modal distillation, feature regression), whether as pretraining or as a joint auxiliary task. Boundary: exclude targets generated by the model itself (masked cluster prediction, EMA self-distillation); exclude output-posterior distillation with no representation target; count versions of one study once.
- Used in: [Decoding speech perception from non-invasive brain recordings](../../reviews/decoding-speech-perception-from-non-invasive-brain-recordings/), [Visual Speech Recognition for Multiple Languages in the Wild](../../reviews/visual-speech-recognition-for-multiple-languages-in-the-wild/)

## auxiliary-speech-feature-regression

- Table: [`auxiliary-speech-feature-regression.csv`](auxiliary-speech-feature-regression.csv) (31 slot-filled, 16 pattern match, usual design in 5, 3 read in full)
- Inclusion rule: Text or speech-unit decoders from a non-acoustic signal (neural, EMG, articulography, ultrasound, video) whose training adds a loss that regresses acoustic or articulatory features of the paired produced speech (MFCC, mel spectrogram, kinematic trajectories) from an intermediate layer, discarded at use time. Boundary: exclude decoders whose output is the acoustic feature (synthesis); exclude targets taken from a pretrained speech encoder (counted under auxiliary-representation-prediction); count versions once.
- Used in: [Brain2Char: a deep architecture for decoding text from brain recordings](../../reviews/brain2char-a-deep-architecture-for-decoding-text-from-brain-recordings/)

## auxiliary-ssl-loss-in-neural-fine-tuning

- Table: [`auxiliary-ssl-loss-in-neural-fine-tuning.csv`](auxiliary-ssl-loss-in-neural-fine-tuning.csv) (31 slot-filled, 40 pattern match, usual design in 37, 0 read in full)
- Inclusion rule: Neural-signal decoders (EEG, MEG, intracranial) that start from a checkpoint pretrained on large neural corpora (the 40-study neural foundation-model population) and, during supervised fine-tuning, add a training-only self-supervised loss (signal-transformation prediction, reconstruction, contrastive or pretext targets) to the task loss. Boundary: pretraining objectives used only before fine-tuning are excluded; use-time updates are M03; versions of one study count once; full-text pattern hits are an upper bound.
- Used in: [NeuroTTT: Bridging Pretrain–Downstream Task Misalignment in EEG Foundation Models via Test-Time Training](../../reviews/neurottt-bridging-pretraining-downstream-task-misalignment-in-eeg-foundation-models-via-test-tim/)

## silent-articulation-text-label-supervision

- Table: [`silent-articulation-text-label-supervision.csv`](silent-articulation-text-label-supervision.csv) (31 slot-filled, 195 pattern match, usual design in 46, 3 read in full)
- Inclusion rule: Decoders that map silently articulated (mouthed, subvocal) non-acoustic signals to phoneme, word or sentence sequences, classified by the training-only target: text or phoneme labels of the silent utterance alone (HMM or CTC), or targets transferred from a parallel vocalized recording by time alignment (DTW). Any signal qualifies. Boundary: isolated-word closed-set classifiers, train-on-vocalized/test-on-silent studies without silent training data, imagined speech, and synthesis-only studies are outside the design comparison; pattern-match counts are upper bounds; versions count once.
- Used in: [Non-invasive electromyographic speech neuroprosthesis: a geometric perspective](../../reviews/non-invasive-electromyographic-speech-neuroprosthesis-a-geometric-perspective/)

## silent-target-transfer

- Table: [`silent-target-transfer.csv`](silent-target-transfer.csv) (31 slot-filled, 52 pattern match, usual design in 15, 4 read in full)
- Inclusion rule: Include studies that train a decoder or synthesizer on silently articulated (mimed, mouthed) non-acoustic signals using acoustic or label targets transferred from a separate vocalized recording of the same utterance by time alignment (DTW, forced alignment or a learned alignment). Any signal qualifies. Boundary: exclude studies that train only on vocalized data and test on silent data (M04 overt-to-silent transfer), alignment used only to score outputs, whisper or NAM acoustic conversion, and imagined speech; count versions once.
- Used in: [Comparison of sEMG Encoding Accuracy Across Speech Modes Using Articulatory and Phoneme Features](../../reviews/comparison-of-semg-encoding-accuracy-across-speech-modes-using-articulatory-and-phoneme-features/), [Digital Voicing of Silent Speech](../../reviews/digital-voicing-of-silent-speech/), [Reconstructing Unseen Sentences from Speech-related Biosignals for Open-vocabulary Neural Communication](../../reviews/reconstructing-unseen-sentences-from-speech-related-biosignals-for-open-vocabulary-neural-commun/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Digital Voicing of Silent Speech |  |  |
| Speech Reconstruction from Silent Tongue and Lip Articulation By Pseudo Target Generation and Domain Adversarial Training |  |  |
| A Cross-Modal Approach to Silent Speech with LLM-Enhanced Recognition |  |  |
| Diff-ETS: Learning a Diffusion Probabilistic Model for Electromyography-to-Speech Conversion |  |  |
| From Silent Signals to Natural Language: A Dual-Stage Transformer-LLM Approach |  |  |
| From Silent Signals to Natural Language: A Dual-Stage Transformer-LLM Approach | 2025 |  |
| Speaking Without Sound: Multi-speaker Silent Speech Voicing with Facial Inputs Only | 2025 |  |
| EMG-to-Speech: Direct Generation of Speech from Facial Electromyographic Signals | 2017 |  |
| Digital Voicing of Silent Speech |  |  |
| Adaptive Phone-Wise Weighted Loss for Silent Speech Restoration in Continuous Spanish | 2026 |  |
| TAP-ETS: Time Aligned Phoneme Guiding for EMG-to-Speech Synthesis | 2026 |  |
| GETS: Guiding EMG-to-Speech Synthesis via Silent Speech Recognition | 2026 |  |
| Enhancing EMG-to-Speech via Silent-Voiced Representation Alignment | 2026 |  |
| Emergence of Phonetic Representations in EMG-based Silent Speech Interfaces | 2026 |  |
| isca-wand09_interspeech | 2009 |  |
| Sequence-to-Sequence Voice Reconstruction for Silent Speech in a Tonal Language | 2022 |  |
| An Improved Model for Voicing Silent Speech | 2021 |  |
| isca-wand09_interspeech |  |  |
| Reconstructing Unseen Sentences from Speech-related Biosignals for Open-vocabulary Neural Communication | 2025 | Sec. III-A; Sec. III-B |

## speech-latent-target

- Table: [`speech-latent-target.csv`](speech-latent-target.csv) (31 slot-filled, 40 pattern match, usual design in 10, 4 read in full)
- Inclusion rule: Include studies that synthesize speech from a non-acoustic signal (articulography, ultrasound, video, EMG, neural recordings) and supervise the signal encoder during training with paired speech, either by direct spectral regression or by matching the latent of a speech encoder or autoencoder that is not used at test time. Boundary: exclude acoustic-input conversion, recognition-only studies and self-generated targets; count versions of one study once; the design of interest is the speech-latent (autoencoder bottleneck or deep feature) target.
- Used in: [EMA2S: An End-to-End Multimodal Articulatory-to-Speech System](../../reviews/ema2s-an-end-to-end-multimodal-articulatory-to-speech-system/), [Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild](../../reviews/lip-to-speech-synthesis-for-arbitrary-speakers-in-the-wild/), [Lip2AudSpec: Speech Reconstruction from Silent Lip Movements Video](../../reviews/lip2audspec-speech-reconstruction-from-silent-lip-movements-video/), [Video-Driven Speech Reconstruction using Generative Adversarial Networks](../../reviews/video-driven-speech-reconstruction-using-generative-adversarial-networks/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild | 2022 | Sec. 3.2.2-3.2.5 |

## ssl-speech-unit-target

- Table: [`ssl-speech-unit-target.csv`](ssl-speech-unit-target.csv) (31 slot-filled, 54 pattern match, usual design in 11, 2 read in full)
- Inclusion rule: Include studies that synthesize speech from a non-acoustic speech signal and train the signal encoder to predict self-supervised speech representations (HuBERT units, soft units, ContentVec, wav2vec features) derived from paired or aligned audio, instead of or besides spectral targets. Boundary: exclude recognition-only studies, targets the model generates itself, and acoustic-input conversion; count versions once.
- Used in: [Intelligible Lip-to-Speech Synthesis with Speech Units](../../reviews/intelligible-lip-to-speech-synthesis-with-speech-units/), [Let There Be Sound: Reconstructing High Quality Speech from Silent Videos](../../reviews/let-there-be-sound-reconstructing-high-quality-speech-from-silent-videos/), [LTA-L2S: Lexical Tone-Aware Lip-to-Speech Synthesis for Mandarin with Cross-Lingual Transfer Learning](../../reviews/lta-l2s-lexical-tone-aware-lip-to-speech-synthesis-for-mandarin-with-cross-lingual-transfer-lear/), [Speaking Without Sound: Multi-speaker Silent Speech Voicing with Facial Inputs Only](../../reviews/speaking-without-sound-multi-speaker-silent-speech-voicing-with-facial-inputs-only/)

## synthetic-speech-target

- Table: [`synthetic-speech-target.csv`](synthetic-speech-target.csv) (31 slot-filled, 56 pattern match, usual design in 8, 2 read in full)
- Inclusion rule: Studies that train a decoder of speech acoustics (or speech units) from a non-acoustic signal using target speech that the user did not produce: text-to-speech output, a reference speaker's recording, or a voice-converted or pre-injury voice, because the user cannot produce intelligible audio. Boundary: exclude targets recorded from the same user during the same or a paired vocalized trial (paired audio, DTW target transfer); exclude text-only targets; count versions of one study once.
- Used in: [An instantaneous voice-synthesis neuroprosthesis](../../reviews/an-instantaneous-voice-synthesis-neuroprosthesis/), [Brain2Speech-Net: Fast and Intelligible Brain-to-Speech Synthesis Without Text Decoding](../../reviews/brain2speech-net-intelligible-real-time-brain-to-speech-synthesis-without-text-decoding/), [emg2speech: Synthesizing speech from electromyography using self-supervised speech models](../../reviews/emg2speech-synthesizing-speech-from-electromyography-using-self-supervised-speech-models/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Brain2Speech-Net: Fast and Intelligible Brain-to-Speech Synthesis Without Text Decoding | 2026 | Sec. 3 |

## whisper-to-normal-training-pairing

- Table: [`whisper-to-normal-training-pairing.csv`](whisper-to-normal-training-pairing.csv) (31 slot-filled, 60 pattern match, usual design in 39, 5 read in full)
- Inclusion rule: Include studies that convert whispered, non-audible-murmur or other unvoiced or alaryngeal speech captured acoustically or by body conduction into voiced, normal-sounding speech audio, and classify how the converter is supervised: time-aligned whisper-normal pairs (parallel, DTW), unpaired or non-parallel data, or synthetic whisper made from normal speech. Boundary: exclude whispered-speech recognition without audio output, normal-to-whisper synthesis, speaker verification, and conversion from non-acoustic signals (EMG, video, neural); count versions of one study once.
- Used in: [WESPER: Zero-shot and Realtime Whisper to Normal Voice Conversion for Whisper-based Speech Interactions](../../reviews/wesper-zero-shot-and-realtime-whisper-to-normal-voice-conversion-for-whisper-based-speech-interactions/)
