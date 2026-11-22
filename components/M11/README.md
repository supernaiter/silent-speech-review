# M11 Eval reference

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## conversational-av-speech-test-corpus

- Table: [`conversational-av-speech-test-corpus.csv`](conversational-av-speech-test-corpus.csv) (234 slot-filled, 59 pattern match, usual design in 16, 2 read in full)
- Inclusion rule: Studies that build or release an audio-visual (face video plus audio) speech test set drawn from spontaneous conversation, meetings or video calls, with transcripts used as ground truth for AVSR or VSR scoring. Boundary: audio-only meeting corpora, read-prompt corpora and broadcast monologue sets selected without a conversation criterion are excluded; corpora derived from conversational recordings of TV or web video count; versions count once.
- Used in: [AVSRBench: A Multi-Condition AVSR Benchmark](../../reviews/avsrbench-a-multi-condition-avsr-benchmark/)

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

## paired-imagery-perception-neural-recordings

- Table: [`paired-imagery-perception-neural-recordings.csv`](paired-imagery-perception-neural-recordings.csv) (234 slot-filled, 112 pattern match, usual design in 83, 3 read in full)
- Inclusion rule: Neural recordings (any modality) in which the same participants both perceive and imagine the same speech or music stimuli in matched trials, so that imagined and perceived responses can be paired. Boundary: imagery-only or perception-only recordings are excluded; overt-versus-covert production without a perception condition is excluded; a recording reused across papers counts once per paper (unique studies).
- Used in: [A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses](../../reviews/a-convolutional-framework-for-mapping-imagined-auditory-meg-into-listened-brain-responses/), [Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping](../../reviews/zero-shot-imagined-speech-decoding-via-imagined-to-listened-meg-mapping/)
