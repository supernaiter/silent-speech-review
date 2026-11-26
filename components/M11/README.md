# M11 Eval reference

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## asr-retranscribed-evaluation-reference

- Table: [`asr-retranscribed-evaluation-reference.csv`](asr-retranscribed-evaluation-reference.csv) (234 slot-filled, 165 pattern match, usual design in 20, 5 read in full)
- Inclusion rule: Include the video-to-speech population of components/M06 (speech waveform synthesized from talking-face or lip video, audio muted at test) and classify from the full text (reference list removed) how the text reference for ASR-scored intelligibility is built: ASR transcripts of the real audio used as the reference (re-transcription), and whether the ASR error on the real test audio is reported beside the systems. Boundary: a study counts under every design its text names (upper bound); audio-visual enhancement, talking-head generation and text-only lip reading excluded; versions counted once.
- Used in: [LTA-L2S: Lexical Tone-Aware Lip-to-Speech Synthesis for Mandarin with Cross-Lingual Transfer Learning](../../reviews/lta-l2s-lexical-tone-aware-lip-to-speech-synthesis-for-mandarin-with-cross-lingual-transfer-lear/), [RobustL2S: Speaker-Specific Lip-to-Speech Synthesis exploiting Self-Supervised Representations](../../reviews/robustl2s-speaker-specific-lip-to-speech-synthesis-exploiting-self-supervised-representations/), [SVTS: Scalable Video-to-Speech Synthesis](../../reviews/svts-scalable-video-to-speech-synthesis/)

## conversational-av-speech-test-corpus

- Table: [`conversational-av-speech-test-corpus.csv`](conversational-av-speech-test-corpus.csv) (234 slot-filled, 59 pattern match, usual design in 16, 2 read in full)
- Inclusion rule: Studies that build or release an audio-visual (face video plus audio) speech test set drawn from spontaneous conversation, meetings or video calls, with transcripts used as ground truth for AVSR or VSR scoring. Boundary: audio-only meeting corpora, read-prompt corpora and broadcast monologue sets selected without a conversation criterion are excluded; corpora derived from conversational recordings of TV or web video count; versions count once.
- Used in: [AVSRBench: A Multi-Condition AVSR Benchmark](../../reviews/avsrbench-a-multi-condition-avsr-benchmark/)

## covert-neural-reconstruction-reference

- Table: [`covert-neural-reconstruction-reference.csv`](covert-neural-reconstruction-reference.csv) (234 slot-filled, 167 pattern match, usual design in 54, 4 read in full)
- Inclusion rule: Neural (ECoG, sEEG, intracortical, EEG, MEG) studies of covert, imagined, mimed, inner or silent speech that decode or reconstruct speech and state how the covert ground truth is constructed. Design of interest: a continuous acoustic reconstruction scored against the same participant's overt recording of the same text, time-aligned (e.g. DTW). Boundary: class-label references, heard-stimulus references in perception studies and text-only references are other designs; acoustic whisper or NAM conversion is not neural; versions of one study count once.
- Used in: [Decoding spectrotemporal features of overt and covert speech from the human cortex](../../reviews/decoding-spectrotemporal-features-of-overt-and-covert-speech-from-the-human-cortex/)

## in-the-wild-sentence-benchmark

- Table: [`in-the-wild-sentence-benchmark.csv`](in-the-wild-sentence-benchmark.csv) (5 confirmed, 49 candidates read, 293 unread)
- Inclusion rule: Include studies that build sentence- or phrase-level audio-visual data with automatically generated transcriptions from video with uncontrolled recording conditions, such as broadcast, YouTube or TED, and define a test split for evaluation (record how the split was made). Boundary: exclude word-level data (LRW, LRW-1000). Exclude those that only reuse existing data or only add training data (no test split defined). Count different versions of the same study as one item.
- Used in: [Deep Audio-Visual Speech Recognition](../../reviews/deep-audio-visual-speech-recognition/), [Lip Reading Sentences in the Wild](../../reviews/lip-reading-sentences-in-the-wild/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Lip Reading Sentences in the Wild | 2017 | §4, Table 2 |
| Large-Scale Visual Speech Recognition |  | §5 |
| LRS3-TED: a large-scale dataset for visual speech recognition | 2018 | §2 |
| Personalized Lip Reading: Adapting to Your Unique Lip Movements with Vision and Language |  | §1 |
| ViCocktail: Automated Multi-Modal Data Collection for Vietnamese Audio-Visual Speech Recognition | 2025 | §2 |

## multi-mode-speech-corpus

- Table: [`multi-mode-speech-corpus.csv`](multi-mode-speech-corpus.csv) (234 slot-filled, 24 pattern match, usual design in 14, 3 read in full)
- Inclusion rule: Studies or corpora that record the same speech material in normal (audible), whispered and silent (mouthed) modes with any non-acoustic or visual channel (EMG, EMA, ultrasound, lip or face video, neural recordings), and use or release the recordings. Boundary: acoustic-only whisper corpora, two-mode corpora without whisper and reviews are pattern matches only; versions of one study count once.
- Used in: [Visual-Only Recognition of Normal, Whispered and Silent Speech](../../reviews/visual-only-recognition-of-normal-whispered-and-silent-speech/)

## open-vocabulary-silent-speech-corpus

- Table: [`open-vocabulary-silent-speech-corpus.csv`](open-vocabulary-silent-speech-corpus.csv) (234 slot-filled, 110 pattern match, usual design in 62, 4 read in full)
- Inclusion rule: Studies whose ledger names silent (mouthed, silently articulated or unvoiced) speech, sentence-level or open- or large-vocabulary material, and a word error rate, with any signal (EMG, ultrasound, video, EEG, intracranial, acoustic sensing); the design compared is the recording signal and whether the corpus comes from a single speaker, counted by full-text pattern. Boundary: imagined or inner speech and silent reading match the ledger pattern and stay in the count (upper bound); closed command sets without sentences are excluded by the pattern; reviews count as pattern matches only; versions of one study count once.
- Used in: [SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces](../../reviews/sonispeech-a-large-scale-open-vocabulary-tri-modal-dataset-for-wearable-silent-speech-interfaces/)

## overt-speech-reference-for-imagined-eeg

- Table: [`overt-speech-reference-for-imagined-eeg.csv`](overt-speech-reference-for-imagined-eeg.csv) (234 slot-filled, 49 pattern match, usual design in 10, 2 read in full)
- Inclusion rule: Include EEG imagined-speech detection studies that construct or align imagined-speech ground-truth labels using overt speech or another explicit reference source. Boundary: exclude overt-speech recognition where overt speech itself is the decoder input, and distinguish directly observed labels from timing labels transferred from a paired overt utterance.
- Used in: [Subject-Independent Imagined Speech Detection via Cross-Subject Generalization and Calibration](../../reviews/subject-independent-imagined-speech-detection-via-cross-subject-generalization-and-calibration/)

## paired-imagery-perception-neural-recordings

- Table: [`paired-imagery-perception-neural-recordings.csv`](paired-imagery-perception-neural-recordings.csv) (234 slot-filled, 112 pattern match, usual design in 83, 3 read in full)
- Inclusion rule: Neural recordings (any modality) in which the same participants both perceive and imagine the same speech or music stimuli in matched trials, so that imagined and perceived responses can be paired. Boundary: imagery-only or perception-only recordings are excluded; overt-versus-covert production without a perception condition is excluded; a recording reused across papers counts once per paper (unique studies).
- Used in: [A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses](../../reviews/a-convolutional-framework-for-mapping-imagined-auditory-meg-into-listened-brain-responses/), [Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping](../../reviews/zero-shot-imagined-speech-decoding-via-imagined-to-listened-meg-mapping/)
