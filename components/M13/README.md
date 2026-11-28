# M13 Hardware & limits

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## imagined-speech-eeg-online-operation

- Table: [`imagined-speech-eeg-online-operation.csv`](imagined-speech-eeg-online-operation.csv) (6075 slot-filled, 445 pattern match, usual design in 110, 1 read in full)
- Inclusion rule: EEG imagined, inner or covert speech studies (ledger text), classified by full-text pattern into online or closed-loop operation, reported latency, reported calibration time and asynchronous (idle-state) detection. Boundary: reviews counted by the ledger pattern; a pattern hit in related work counts (upper bound); versions once.
- Used in: [Subject-Independent Imagined Speech Detection via Cross-Subject Generalization and Calibration](../../reviews/subject-independent-imagined-speech-detection-via-cross-subject-generalization-and-calibration/)

## implanted-communication-bci-home-use

- Table: [`implanted-communication-bci-home-use.csv`](implanted-communication-bci-home-use.csv) (6075 slot-filled, 382 pattern match, usual design in 181, 6 read in full)
- Inclusion rule: Same population as M13/wireless-implanted-speech-bci (implanted neural sensors, speech or communication); the design compared is where and by whom the system is operated: hospital or laboratory sessions (epilepsy monitoring, bedside, laboratory), sessions at the participant's home, and use without investigators present (independent use). Boundary: full-text pattern counts with the reference list removed, so related-work mentions count (upper bounds); a study counts under every setting it names; versions counted once.
- Used in: [Fully Implanted Brain-Computer Interface in a Locked-In Patient with ALS](../../reviews/fully-implanted-brain-computer-interface-in-a-locked-in-patient-with-als/)

## intracranial-synthesis-participant-and-implant

- Table: [`intracranial-synthesis-participant-and-implant.csv`](intracranial-synthesis-participant-and-implant.csv) (6075 slot-filled, 180 pattern match, usual design in 8, 3 read in full)
- Inclusion rule: Studies that reconstruct speech acoustics from intracranial recordings made during produced, attempted or imagined speech (the published intracranial-synthesis population pattern of M08/intracranial-synthesis-waveform-generation), classified by who was recorded and with what implant: acute clinical monitoring (epilepsy) or intraoperative recordings in people with intact speech, versus a chronic research implant in a person with impaired speech (ALS, brainstem stroke, locked-in, anarthria, dysarthria). Boundary: full-text pattern counts with the reference list removed, so related-work mentions count (upper bounds); a study counts under every design it names; heard-speech reconstruction and text-only decoders are outside; versions once.
- Used in: [Online speech synthesis using a chronically implanted brain–computer interface in an individual with ALS](../../reviews/online-speech-synthesis-using-a-chronically-implanted-brain-computer-interface-in-an-individual-with/)

## long-term-home-use

- Table: [`long-term-home-use.csv`](long-term-home-use.csv) (6075 slot-filled, 39 pattern match, usual design in 21, 3 read in full)
- Inclusion rule: Neural speech or communication BCIs evaluated in sustained use outside a single lab session: home use, independent or personal use, or follow-up of three months or more. Included: speech, command and handwriting BCIs used for communication. Excluded: offline re-analysis of archived data without new use; acoustic or optical silent-speech devices.
- Used in: [An Accurate and Rapidly Calibrating Speech Neuroprosthesis](../../reviews/an-accurate-and-rapidly-calibrating-speech-neuroprosthesis/)

## online-imagined-speech-eeg

- Table: [`online-imagined-speech-eeg.csv`](online-imagined-speech-eeg.csv) (6075 slot-filled, 167 pattern match, usual design in 112, 3 read in full)
- Inclusion rule: Studies that classify imagined, covert or inner speech from scalp EEG (same population as the M06 imagined-speech EEG table); the design compared is whether decoding is run online with feedback (real-time, closed-loop) and its accuracy reported, or offline on recorded trials. Boundary: a mention of real-time use as future work or in related work is a pattern match only, not an online study; reviews excluded as deciding priors; versions count once.
- Used in: [EEG-Based Imagined Speech Decoding Using a Hybrid CNN-SNN Architecture](../../reviews/eeg-based-imagined-speech-decoding-using-a-hybrid-cnn-snn-architecture/), [Lightweight Diffusion-based Framework for Online Imagined Speech Decoding in Aphasia](../../reviews/lightweight-diffusion-based-framework-for-online-imagined-speech-decoding-in-aphasia/), [Toward Practical BCI: A Real-time Wireless Imagined Speech EEG Decoding System](../../reviews/toward-practical-bci-a-real-time-wireless-imagined-speech-eeg-decoding-system/)

## streaming-lip-reading-decoding

- Table: [`streaming-lip-reading-decoding.csv`](streaming-lip-reading-decoding.csv) (6075 slot-filled, 25 pattern match, usual design in 5, 5 read in full)
- Inclusion rule: Decoders that transcribe or recognise speech from lip, face or articulator video (alone or with audio) and claim online, streaming, simultaneous or real-time operation, classified by whether the full text reports a measured latency, algorithmic delay or real-time factor and an online-scored error rate. Boundary: human-perception studies, speech enhancement or separation, talking-head synthesis and phonetic analyses are excluded on reading of the ledger text; reference-list mentions do not count; versions count once; Cai et al. 2011 (isca-cai11-lightssi) and a 2017 real-time lip vowel recogniser (doi-10.1109-access.2017.2649838) are added from the whole-wiki recall check.
- Used in: [Deep Lip Reading: a comparison of models and an online application](../../reviews/deep-lip-reading-a-comparison-of-models-and-an-online-application/)

## use-time-adaptation-cost

- Table: [`use-time-adaptation-cost.csv`](use-time-adaptation-cost.csv) (6075 slot-filled, 64 pattern match, usual design in 22, 2 read in full)
- Inclusion rule: Speech-related or neural-signal decoders (any modality) whose text ties test-time or online adaptation, or inference, to latency, runtime, memory, compute, power or wearability. Boundary: training-only cost is excluded; privacy or edge-suitability claims without a measurement count as pattern matches only; versions count once.
- Used in: [NeuroTTT: Bridging Pretrain–Downstream Task Misalignment in EEG Foundation Models via Test-Time Training](../../reviews/neurottt-bridging-pretraining-downstream-task-misalignment-in-eeg-foundation-models-via-test-tim/)

## wearable-speech-sensor-on-device-inference

- Table: [`wearable-speech-sensor-on-device-inference.csv`](wearable-speech-sensor-on-device-inference.csv) (6075 slot-filled, 30 pattern match, usual design in 24, 5 read in full)
- Inclusion rule: Non-acoustic silent-speech or speech-recognition wearables (EMG, strain, accelerometer, ultrasound, EEG) whose decoder runs on an embedded processor or microcontroller on or near the body, rather than on a PC, phone or cloud; design compared: whether inference latency, energy per inference and total system power are measured. Boundary: neural implants with external rack processing, acoustic-only keyword spotting and PC-tethered real-time demos are excluded when read; versions once.
- Used in: [Knowledge Distilled Ensemble Model for sEMG-based Silent Speech Interface](../../reviews/knowledge-distilled-ensemble-model-for-semg-based-silent-speech-interface/), [SilentWear: an Ultra-Low Power Wearable System for EMG-based Silent Speech Recognition](../../reviews/silentwear-an-ultra-low-power-wearable-system-for-emg-based-silent-speech-recognition/), [Soft Active EMG Interface for Machine Learning-Enabled Silent Speech Recognition](../../reviews/soft-active-electromyography-interface-for-machine-learning-enabled-silent-speech-recognition/)

## wireless-implanted-speech-bci

- Table: [`wireless-implanted-speech-bci.csv`](wireless-implanted-speech-bci.csv) (6075 slot-filled, 382 pattern match, usual design in 216, 3 read in full)
- Inclusion rule: Speech or communication studies that record from implanted neural sensors (intracortical, ECoG, sEEG, depth) in humans or animals, classified by how the signal leaves the body: percutaneous connector or pedestal, wireless telemetry (including a transmitter mounted on a percutaneous pedestal), or a fully implanted system with no skin-penetrating hardware. Boundary: reviews and related-work mentions inflate the full-text counts (upper bounds); wearable EMG/EEG wireless devices are outside the population (ledger modality filter).
- Used in: [A Wireless Brain-Machine Interface for Real-Time Speech Synthesis](../../reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis/), [Fully Implanted Brain-Computer Interface in a Locked-In Patient with ALS](../../reviews/fully-implanted-brain-computer-interface-in-a-locked-in-patient-with-als/)
