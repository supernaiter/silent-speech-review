# M07 Runtime aids

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## large-vocabulary-lm-for-neural-speech

- Table: [`large-vocabulary-lm-for-neural-speech.csv`](large-vocabulary-lm-for-neural-speech.csv) (119 slot-filled, 1162 pattern match, usual design in 152, 4 read in full)
- Inclusion rule: Neural speech decoders that constrain output with a vocabulary of at least 1,000 words via an n-gram or neural language model at use time. Boundary: 50-word or command sets are counted as small vocabulary; LLM rescoring counts.
- Used in: [A cross-species neural foundation model for end-to-end speech decoding](../../reviews/a-cross-species-neural-foundation-model-for-end-to-end-speech-decoding/), [A high-performance neuroprosthesis for speech decoding and avatar control](../../reviews/a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control/), [A high-performance speech neuroprosthesis](../../reviews/a-high-performance-speech-neuroprosthesis/), [Neuroprosthesis for decoding speech in a paralyzed person with anarthria](../../reviews/neuroprosthesis-for-decoding-speech-in-a-paralyzed-person-with-anarthria/)

## llm-transcript-correction

- Table: [`llm-transcript-correction.csv`](llm-transcript-correction.csv) (119 slot-filled, 382 pattern match, usual design in 78, 4 read in full)
- Inclusion rule: Text-producing speech decoders from non-acoustic or neural signals (surface EMG, EEG, MEG, ECoG, intracortical, ultrasound, articulography, lip video, fMRI) whose ledger mentions a use-time language model, lexicon, beam search or rescoring. The design compared is the use-time language prior: an n-gram or lexicon-constrained beam search, neural language-model rescoring, or a large language model that rescores or rewrites the decoded transcript. Boundary: language models used only to build training targets or stimuli do not count; acoustic-only ASR is excluded; versions of one study count once.
- Used in: [From Silent Signals to Natural Language: A Dual-Stage Transformer-LLM Approach](../../reviews/from-silent-signals-to-natural-language-a-dual-stage-transformer-llm-approach/)

## noninvasive-text-decoding-language-model

- Table: [`noninvasive-text-decoding-language-model.csv`](noninvasive-text-decoding-language-model.csv) (119 slot-filled, 1458 pattern match, usual design in 169, 1 read in full)
- Inclusion rule: Language or text decoding studies whose ledger names scalp EEG or MEG. The design compared is the use-time language prior: n-gram or character language model with beam search, neural or large language model rescoring or generation, or none. Boundary: a language model used only to build stimuli or embeddings for training targets does not count; closed candidate-set ranking counts as none.
- Used in: [Brain-to-Text Decoding: A Non-invasive Approach via Typing](../../reviews/brain-to-text-decoding-a-non-invasive-approach-via-typing/), [Continuous Silent Speech Recognition using EEG](../../reviews/continuous-silent-speech-recognition-using-eeg/)
