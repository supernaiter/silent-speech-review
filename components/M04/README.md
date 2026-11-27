# M04 Use-time act

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## covert-speech-decoding-with-paired-overt-condition

- Table: [`covert-speech-decoding-with-paired-overt-condition.csv`](covert-speech-decoding-with-paired-overt-condition.csv) (5595 slot-filled, 777 pattern match, usual design in 10, 6 read in full)
- Inclusion rule: Studies whose ledger text names decoding, classification or recognition together with imagined, covert, inner or unspoken speech (any signal: EEG, MEG, ECoG, sEEG, intracortical, EMG, video). The design of interest is a decoder trained and tested on imagined-speech trials, with an overt condition on the same items in the same participants, from intracranial recordings. Boundary: attempted speech by paralysed users is a different action and is not counted as imagined speech; the ledger pattern also admits lip-reading and perception studies that mention covert speech, so counts are upper bounds; versions of one study count once; usual approach judged on studies first public before 2011.
- Used in: [Decoding Vowels and Consonants in Spoken and Imagined Words Using Electrocorticographic Signals in Humans](../../reviews/decoding-vowels-and-consonants-in-spoken-and-imagined-words-using-electrocorticographic-signals-in-h/)

## imagined-speech-test-trial-averaging

- Table: [`imagined-speech-test-trial-averaging.csv`](imagined-speech-test-trial-averaging.csv) (5595 slot-filled, 68 pattern match, usual design in 9, 1 read in full)
- Inclusion rule: Studies that classify or decode imagined, covert or inner speech from EEG or MEG and state whether each test decision uses one trial or an average over repeated trials of the same item. Boundary: averaging over subjects, folds or seeds is not test-trial averaging; ERP figures averaged for display only are excluded; perceived or overt speech alone is excluded; versions of one study count once.
- Used in: [Physiological Noise Augmentation Improves Non-Invasive Brain-to-Speech](../../reviews/physiological-noise-augmentation-improves-non-invasive-brain-to-speech/)

## lipreading-word-segmentation-at-test

- Table: [`lipreading-word-segmentation-at-test.csv`](lipreading-word-segmentation-at-test.csv) (5595 slot-filled, 975 pattern match, usual design in 65, 2 read in full)
- Inclusion rule: Same lip-reading population as M06, classified by whether the full text names isolated or pre-segmented word input at recognition, or continuous / connected / sentence-level decoding. Boundary: corpus-derived boundaries at test count as pre-segmented; a study counts under both designs if its text names both (upper bound); versions count once; dated against 2016-01.
- Used in: [Lipreading with Long Short-Term Memory](../../reviews/lipreading-with-long-short-term-memory/)

## neural-text-entry-action

- Table: [`neural-text-entry-action.csv`](neural-text-entry-action.csv) (5595 slot-filled, 154 pattern match, usual design in 68, 4 read in full)
- Inclusion rule: Neural BCI studies (intracortical, ECoG, sEEG, EEG, MEG) whose ledger names the recording modality together with a text output, a text error rate or a text-entry rate (characters or words per minute); the design compared is the user action that drives text at use time (attempted handwriting, attempted or overt speech, imagined or inner speech, cursor or keyboard selection, evoked-potential spelling, speech perception). Boundary: a study counts under every action its full text names (upper bound, related-work mentions included); reviews count as pattern matches; versions counted once.
- Used in: [High-performance brain-to-text communication via handwriting](../../reviews/high-performance-brain-to-text-communication-via-handwriting/), [High performance communication by people with paralysis using an intracortical brain-computer interface](../../reviews/high-performance-communication-by-people-with-paralysis-using-an-intracortical-brain-computer-interf/)

## noninvasive-text-production-action

- Table: [`noninvasive-text-production-action.csv`](noninvasive-text-production-action.csv) (5595 slot-filled, 1458 pattern match, usual design in 784, 3 read in full)
- Inclusion rule: Language or text decoding studies whose ledger names scalp EEG or MEG. The design compared is the use-time action that produces the decoded signal: perception (listening or reading), imagined or covert speech, evoked-potential spelling (P300/SSVEP speller), or executed motor text production (typing, handwriting). Boundary: keypresses used only as behavioural responses are not typing decoding; reviews are counted as pattern matches but cannot be deciding priors; versions of one study count once.
- Used in: [Brain-to-Text Decoding: A Non-invasive Approach via Typing](../../reviews/brain-to-text-decoding-a-non-invasive-approach-via-typing/), [Continuous Silent Speech Recognition using EEG](../../reviews/continuous-silent-speech-recognition-using-eeg/)

## overt-to-silent-transfer

- Table: [`overt-to-silent-transfer.csv`](overt-to-silent-transfer.csv) (5595 slot-filled, 33 pattern match, usual design in 23, 104 read in full)
- Inclusion rule: Include studies that apply a decoder trained only on overt (or attempted overt) speech to silent speech (mouthed, silently articulated, inner or imagined speech) without retraining and report the results. Any signal qualifies (neural, EMG, ultrasound, video, etc.). Boundary: those that also train on silent data (such as methods that transfer audible-side targets) are included if they separately report an audible-training-only baseline condition. Exclude those that use an audible model only for time alignment or initialization of silent data. Exclude transfer between whispered and normal voice in acoustic speech. Exclude transfer from listening (perception) to inner speech. Exclude those that only analyse similarity of neural activity without applying a decoder. Exclude matches in reviews or citations only. Count different versions of the same study as one item.
- Used in: [Affect Decoding in Phonated and Silent Speech Production from Surface EMG](../../reviews/affect-decoding-in-phonated-and-silent-speech-production-from-surface-emg/), [Decoding spectrotemporal features of overt and covert speech from the human cortex](../../reviews/decoding-spectrotemporal-features-of-overt-and-covert-speech-from-the-human-cortex/), [Digital Voicing of Silent Speech](../../reviews/digital-voicing-of-silent-speech/), [EMG-to-Speech: Direct Generation of Speech from Facial Electromyographic Signals](../../reviews/emg-to-speech-direct-generation-of-speech-from-facial-electromyographic-signals/), [Improving the Gap in Visual Speech Recognition Between Normal and Silent Speech Based on Metric Learning](../../reviews/improving-the-gap-in-visual-speech-recognition-between-normal-and-silent-speech-based-on-metric-learning/), [LipNet: End-to-End Sentence-level Lipreading](../../reviews/lipnet-end-to-end-sentence-level-lipreading/), [Mechanistic Interpretability of Brain-to-Speech Models Across Speech Modes](../../reviews/mechanistic-interpretability-of-brain-to-speech-models-across-speech-modes/), [Real-time synthesis of imagined speech processes from minimally invasive recordings of neural activity](../../reviews/real-time-synthesis-of-imagined-speech-processes-from-minimally-invasive-recordings-of-neural-activi/), [Relating the Neural Representations of Vocalized, Mimed, and Imagined Speech](../../reviews/relating-the-neural-representations-of-vocalized-mimed-and-imagined-speech/), [Silent versus modal multi-speaker speech recognition from ultrasound and video](../../reviews/silent-versus-modal-multi-speaker-speech-recognition-from-ultrasound-and-video/), [Speech synthesis from neural decoding of spoken sentences](../../reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences/), [Towards Neural Decoding of Imagined Speech based on Spoken Speech](../../reviews/towards-neural-decoding-of-imagined-speech-based-on-spoken-speech/), [Transfer Learning for Covert Speech Classification Using EEG Hilbert Envelope and Temporal Fine Structure](../../reviews/transfer-learning-for-covert-speech-classification-using-eeg-hilbert-envelope-and-temporal-fine-/), [Visual-Only Recognition of Normal, Whispered and Silent Speech](../../reviews/visual-only-recognition-of-normal-whispered-and-silent-speech/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Visual-Only Recognition of Normal, Whispered and Silent Speech |  | Introduction, experimental grid |
| Digital Voicing of Silent Speech |  | Ledger (baseline condition), §Abstract |
| Towards Neural Decoding of Imagined Speech based on Spoken Speech |  | Abstract |
| Transfer learning for covert speech classification using EEG Hilbert envelope and temporal fine structure | 2025 | Ledger (study aim) |
| Transfer Learning for Covert Speech Classification Using EEG Hilbert Envelope and Temporal Fine Structure |  | Ledger (study aim) |
| Relating the Neural Representations of Vocalized, Mimed, and Imagined Speech | 2026 | Results (matched passage) |
| Affect Decoding in Phonated and Silent Speech Production from Surface EMG |  | Table caption (matched passage) |
| Shared and distinct temporal representations of Chinese words across imagined, silent, and overt speech | 2026 | Ledger |
| doi-10.1038-s41586-019-1119-1 |  | Results「Synthesizing mimed speech」 |
| doi-10.1038-s41586-025-09127-3 |  | Results (matched passage) |
| Feasibility of decoding covert speech in ECoG with a Transformer trained on overt speech | 2024 | Abstract (matched passage) |
| Imagined speech event detection from electrocorticography and its transfer between speech modes and subjects | 2024 | Ledger |
| Word classification across speech modes from low-density electrocorticography signals | 2026 | Ledger |
| The Nested Hierarchy of Overt, Mouthed, and Imagined Speech Activity Evident in Intracranial Recordings | 2022 | Ledger |
| Feasibility of decoding covert speech in ECoG with a Transformer trained on overt speech | 2024 | Abstract (matched passage) |
| Evidence for common spike-based temporal coding of overt and covert speech in pars triangularis of human Broca's area | 2024 | Ledger |
| Representation of verbal thought in motor cortex and implications for speech neuroprostheses | 2024 | Figure caption (matched passage) |
| Visual-Only Recognition of Normal, Whispered and Silent Speech | 2018 | Introduction, experimental grid |
| EMG-to-Speech: Direct Generation of Speech from Facial Electromyographic Signals | 2017 | §6.3 Mapping on EMG Data |
| Digital Voicing of Silent Speech |  | Ledger (baseline condition), §Abstract |
| Feasibility of decoding covert speech in ECoG with a Transformer trained on overt speech | 2024 | Abstract (matched passage) |
| Semantic-Aware Decoding of Covert Inner Speech: A Multimodal EEG–EMG–Audio Framework | 2026 | Ledger |
| Silent Speech Recognition with Articulator Positions Estimated from Tongue Ultrasound and Lip Video |  | Main text (matched passage) |
| Decoding spectrotemporal features of overt and covert speech from the human cortex | 2014 | Introduction、Methods（Dynamic time warping） |
| A Spectral Mapping Method for EMG-based Recognition of Silent Speech | 2010 | Abstract |
| Session-Independent EMG-Based Speech Recognition | 2011 | § (Cross-Modal Testing section) |
| Silent Speech Recognition with Articulator Positions Estimated from Tongue Ultrasound and Lip Video | 2023 | Main text (matched passage) |
| Silent Speech Recognition with Articulator Positions Estimated from Tongue Ultrasound and Lip Video |  | Main text (matched passage) |
| Silent vs Vocalized Articulation for a Portable Ultrasound-Based Silent Speech Interface | 2010 | Abstract |
| Silent vs Vocalized Articulation for a Portable Ultrasound-Based Silent Speech Interface | 2010 | Abstract |
| Relating the Neural Representations of Vocalized, Mimed, and Imagined Speech | 2026 | Results (matched passage) |
| Feasibility of decoding covert speech in ECoG with a Transformer trained on overt speech | 2024 | Abstract (matched passage) |
| Imagined speech event detection from electrocorticography and its transfer between speech modes and subjects | 2024 | Ledger |
| Imagined speech event detection from electrocorticography and its transfer between speech modes and subjects | 2024 | Ledger |
| From pronounced to imagined: improving speech decoding with multi-condition EEG data | 2025 | Methods |
| Decoding spectrotemporal features of overt and covert speech from the human cortex | 2014 | Introduction、Methods（Dynamic time warping） |
| Silent versus modal multi-speaker speech recognition from ultrasound and video | 2021 | Sec. 3.3 |
| Improving the Gap in Visual Speech Recognition Between Normal and Silent Speech Based on Metric Learning | 2023 | Sec. 4.4 |
| Improving the Gap in Visual Speech Recognition Between Normal and Silent Speech Based on Metric Learning | 2023 | Sec. 4.4 |
| Improving the Gap in Visual Speech Recognition Between Normal and Silent Speech Based on Metric Learning | 2023 | Sec. 4.4 |
| Decoding spectrotemporal features of overt and covert speech from the human cortex | 2014 | Introduction, Methods (Dynamic time warping) |
| Decoding spectrotemporal features of overt and covert speech from the human cortex | 2014 | Introduction, Methods (Dynamic time warping) |
| doi-10.1038-s41586-019-1119-1 |  | Results"Synthesizing mimed speech" |
| Decoding spectrotemporal features of overt and covert speech from the human cortex | 2014 | Introduction; Methods (Dynamic time warping) |
| Decoding spectrotemporal features of overt and covert speech from the human cortex | 2014 | Introduction; Methods (Dynamic time warping) |
| doi-10.1038-s41586-019-1119-1 |  | Results, "Synthesizing mimed speech" |
| doi-10.1038-s41586-019-1119-1 |  | Results, "Synthesizing mimed speech" |

## speech-or-motor-spelling-action

- Table: [`speech-or-motor-spelling-action.csv`](speech-or-motor-spelling-action.csv) (5595 slot-filled, 0 pattern match, usual design in 8, 7 read in full)
- Inclusion rule: Setting (one definition for all four topics): text entry by spelling, in any signal type in the wiki (neural, EMG, EOG, EPG, video, ultrasound and others): studies whose full text, reference list removed, names a speller, letter-by-letter entry, or spelling out words, letters or sentences. Boundary: acoustic-only systems are outside the wiki; mentions in related work, reviews and unrelated uses of 'spelling' enter, so every count is an upper bound (pattern match); versions are counted once; the target's three versions are excluded; the usual approach is counted at the target's time (index year 2022 or earlier, target first public 2022-11). Design compared: the user action that selects each letter: evoked-potential speller (P300, SSVEP, RSVP), motor or cursor selection (point-and-click, virtual keyboard, motor imagery), attempted handwriting, NATO or radio-alphabet code words, other speech production of letters. A study counts under every action its text names.
- Used in: [Generalizable spelling using a speech neuroprosthesis in an individual with severe limb and vocal paralysis](../../reviews/generalizable-spelling-using-a-speech-neuroprosthesis-in-an-individual-with-severe-limb-and-vocal-pa/)

## speech-task-closed-loop-bci-control

- Table: [`speech-task-closed-loop-bci-control.csv`](speech-task-closed-loop-bci-control.csv) (5595 slot-filled, 171 pattern match, usual design in 1, 4 read in full)
- Inclusion rule: Setting (one definition for all three topics): human studies, any signal type in the wiki, that close a loop from recorded activity to a device or display with feedback (online, real-time or closed-loop BCI/BMI/neuroprosthesis) in a speech-related context. Design of interest: the user's control action is a speech task (overt, attempted, mimed or imagined phonemes, vowels, words) rather than limb movement or imagery, a non-speech cognitive task or an evoked-potential selection. Boundary: reviews, offline-only decoders and perception studies are excluded from the prior population; reports of the same experiment are counted once; ledger and full-text pattern counts are upper bounds; earlier BCIs missing from the wiki are taken from the target's own citations and labelled so.
- Used in: [Using the electrocorticographic speech network to control a brain-computer interface in humans](../../reviews/using-the-electrocorticographic-speech-network-to-control-a-brain-computer-interface-in-humans/)
