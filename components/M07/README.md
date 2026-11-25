# M07 Runtime aids

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## emg-recognition-grammar-and-language-model

- Table: [`emg-recognition-grammar-and-language-model.csv`](emg-recognition-grammar-and-language-model.csv) (119 slot-filled, 64 pattern match, usual design in 21, 2 read in full)
- Inclusion rule: Surface-EMG decoders scored with WER or CER (the 64-study population of the M12 unseen-sentence table), classified by the use-time linguistic constraint their full text names: hand-written or rule grammar, n-gram language model, neural or large language model, or no language model. Boundary: a study counts under every design its text names, related-work mentions included (upper bound); versions once; acoustic-only ASR excluded.
- Used in: [Development of sEMG sensors and algorithms for silent speech recognition](../../reviews/development-of-semg-sensors-and-algorithms-for-silent-speech-recognition/)

## large-vocabulary-lm-for-neural-speech

- Table: [`large-vocabulary-lm-for-neural-speech.csv`](large-vocabulary-lm-for-neural-speech.csv) (119 slot-filled, 1162 pattern match, usual design in 152, 4 read in full)
- Inclusion rule: Neural speech decoders that constrain output with a vocabulary of at least 1,000 words via an n-gram or neural language model at use time. Boundary: 50-word or command sets are counted as small vocabulary; LLM rescoring counts.
- Used in: [A cross-species neural foundation model for end-to-end speech decoding](../../reviews/a-cross-species-neural-foundation-model-for-end-to-end-speech-decoding/), [A high-performance neuroprosthesis for speech decoding and avatar control](../../reviews/a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control/), [A high-performance speech neuroprosthesis](../../reviews/a-high-performance-speech-neuroprosthesis/), [Brain-to-text: decoding spoken phrases from phone representations in the brain](../../reviews/brain-to-text-decoding-spoken-phrases-from-phone-representations-in-the-brain/), [High-performance brain-to-text communication via handwriting](../../reviews/high-performance-brain-to-text-communication-via-handwriting/), [iPhoneme: Brain-to-Text Communication for ALS Using ConformerXL Decoding](../../reviews/iphoneme-brain-to-text-communication-for-als-using-conformerxl-decoding/), [Neuroprosthesis for decoding speech in a paralyzed person with anarthria](../../reviews/neuroprosthesis-for-decoding-speech-in-a-paralyzed-person-with-anarthria/)

## lip-reader-text-guidance-for-video-to-speech

- Table: [`lip-reader-text-guidance-for-video-to-speech.csv`](lip-reader-text-guidance-for-video-to-speech.csv) (119 slot-filled, 165 pattern match, usual design in 150, 7 read in full)
- Inclusion rule: The 165-study video-to-speech population (pattern of components/M06/video-to-speech-one-to-many-decoder), classified from the full text (reference list removed) by whether text predicted from the video by a lip reader is used at inference to condition or guide speech synthesis, whether a classifier or ASR guides a diffusion sampler, and whether a lip-reader-to-TTS cascade is named. Boundary: a study counts under every design its text names (upper bound, related-work mentions included); text used only as a training loss or as an evaluation reference does not count as use-time text; versions once.
- Used in: [LipVoicer: Generating Speech from Silent Videos Guided by Lip Reading](../../reviews/lipvoicer-generating-speech-from-silent-videos-guided-by-lip-reading/)

## llm-transcript-correction

- Table: [`llm-transcript-correction.csv`](llm-transcript-correction.csv) (119 slot-filled, 382 pattern match, usual design in 78, 4 read in full)
- Inclusion rule: Text-producing speech decoders from non-acoustic or neural signals (surface EMG, EEG, MEG, ECoG, intracortical, ultrasound, articulography, lip video, fMRI) whose ledger mentions a use-time language model, lexicon, beam search or rescoring. The design compared is the use-time language prior: an n-gram or lexicon-constrained beam search, neural language-model rescoring, or a large language model that rescores or rewrites the decoded transcript. Boundary: language models used only to build training targets or stimuli do not count; acoustic-only ASR is excluded; versions of one study count once.
- Used in: [EEG-to-Voice Decoding of Spoken and Imagined speech Using Non-Invasive EEG](../../reviews/eeg-to-voice-decoding-of-spoken-and-imagined-speech-using-non-invasive-eeg/), [From Silent Signals to Natural Language: A Dual-Stage Transformer-LLM Approach](../../reviews/from-silent-signals-to-natural-language-a-dual-stage-transformer-llm-approach/)

## noninvasive-text-decoding-language-model

- Table: [`noninvasive-text-decoding-language-model.csv`](noninvasive-text-decoding-language-model.csv) (119 slot-filled, 1458 pattern match, usual design in 169, 1 read in full)
- Inclusion rule: Language or text decoding studies whose ledger names scalp EEG or MEG. The design compared is the use-time language prior: n-gram or character language model with beam search, neural or large language model rescoring or generation, or none. Boundary: a language model used only to build stimuli or embeddings for training targets does not count; closed candidate-set ranking counts as none.
- Used in: [Brain-to-Text Decoding: A Non-invasive Approach via Typing](../../reviews/brain-to-text-decoding-a-non-invasive-approach-via-typing/), [Continuous Silent Speech Recognition using EEG](../../reviews/continuous-silent-speech-recognition-using-eeg/)

## reference-speaker-conditioning-at-inference

- Table: [`reference-speaker-conditioning-at-inference.csv`](reference-speaker-conditioning-at-inference.csv) (119 slot-filled, 165 pattern match, usual design in 21, 3 read in full)
- Inclusion rule: Video-to-speech studies (the 165-study population of the M06 video-to-speech-synthesis table), classified by the speaker information supplied at use time: a speaker embedding from reference audio, a speaker embedding derived from the face or lip video, or none. Boundary: embeddings used only in training or only to score speaker similarity are not use-time conditioning; a study counts under every design its full text names (upper bound); versions count once.
- Used in: [NaturalL2S: End-to-End High-quality Multispeaker Lip-to-Speech Synthesis with Differential Digital Signal Processing](../../reviews/naturall2s-end-to-end-high-quality-multispeaker-lip-to-speech-synthesis-with-differential-digita/), [RESOUND: Speech Reconstruction from Silent Videos via Acoustic-Semantic Decomposed Modeling](../../reviews/resound-speech-reconstruction-from-silent-videos-via-acoustic-semantic-decomposed-modeling/), [SVTS: Scalable Video-to-Speech Synthesis](../../reviews/svts-scalable-video-to-speech-synthesis/), [VCVTS: Multi-Speaker Video-to-Speech Synthesis via Cross-Modal Knowledge Transfer from Voice Conversion](../../reviews/vcvts-multi-speaker-video-to-speech-synthesis-via-cross-modal-knowledge-transfer-from-voice-conversion/), [Zero-Shot Personalized Lip-to-Speech Synthesis with Face Image Based Voice Control](../../reviews/zero-shot-personalized-lip-to-speech-synthesis-with-face-image-based-voice-control/)

## task-context-prior-from-decoded-utterance

- Table: [`task-context-prior-from-decoded-utterance.csv`](task-context-prior-from-decoded-utterance.csv) (119 slot-filled, 1274 pattern match, usual design in 341, 5 read in full)
- Inclusion rule: Brain-signal (ECoG, sEEG, intracortical, EEG, MEG) speech or language decoders whose ledger text names a speech unit and decoding or classification; the design of interest is the use-time prior over outputs: language model, grammar or finite-state network, pronunciation lexicon, or a context prior derived from another decoded utterance (for example a decoded question constraining the answer). A study counts under every design its full text names (upper bound); priors used only in training do not count; versions once.
- Used in: [Real-time decoding of question-and-answer speech dialogue using human cortical activity](../../reviews/real-time-decoding-of-question-and-answer-speech-dialogue-using-human-cortical-activity/)

## use-time-language-model-visual-speech

- Table: [`use-time-language-model-visual-speech.csv`](use-time-language-model-visual-speech.csv) (119 slot-filled, 633 pattern match, usual design in 143, 4 read in full)
- Inclusion rule: The same sentence-level lip-reading / VSR population as M06/sentence-lipreading-sequence-objective, classified by the use-time language information its full text names: an n-gram language model (character or word level), a neural language model or LLM rescoring, or an explicit statement that no external language model is used; a grammar, lexicon or dictionary constraint is counted separately for the period before the target. M07 is slot-filled for about 1% of the wiki, so every count here is pattern match (an upper bound); a study counts under every design its text names; versions count once by key.
- Used in: [End-to-End Audio-Visual Speech Recognition with Conformers](../../reviews/end-to-end-audio-visual-speech-recognition-with-conformers/), [LipNet: End-to-End Sentence-level Lipreading](../../reviews/lipnet-end-to-end-sentence-level-lipreading/)
