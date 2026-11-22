# M05 Sensing

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## active-acoustic-speech-sensing

- Table: [`active-acoustic-speech-sensing.csv`](active-acoustic-speech-sensing.csv) (7329 slot-filled, 22 pattern match, usual design in 16, 3 read in full)
- Inclusion rule: Studies that emit an acoustic signal (near-ultrasonic or ultrasonic, from a loudspeaker, earphone or transducer) and decode speech, silent speech or mouth state from its reflection or Doppler shift off the lips, face, jaw or vocal tract, captured by a microphone. Boundary: B-mode ultrasound tongue imaging, RF radar, Wi-Fi and laser sensing are excluded when read; reviews and datasets without a decoding result count as pattern matches only; versions of one study count once.
- Used in: [End-to-End Silent Speech Recognition with Acoustic Sensing](../../reviews/end-to-end-silent-speech-recognition-with-acoustic-sensing/)

| Paper | Year | Evidence |
| --- | --- | --- |
| End-to-end Silent Speech Recognition with Acoustic Sensing |  | Sec. 4.2 |
| M2SILENT: Enabling Multi-user Silent Speech Interactions via Multi-directional Speakers in Shared Spaces |  | Sec. 5 |
| SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces | 2026 | Abstract, Table 3 |
| Multimodal Speech Recognition with Ultrasonic Sensors |  | Sec. 5.1, Table 1 |

## ecog-speech-decoding

- Table: [`ecog-speech-decoding.csv`](ecog-speech-decoding.csv) (7329 slot-filled, 253 pattern match, usual design in 233, 3 read in full)
- Inclusion rule: Papers that decode speech units, words, sentences or acoustics from electrocorticography in humans, recorded during produced, attempted, mimed or imagined speech. Included: clinical and high-density grids, micro-ECoG, online or offline. Excluded: intracortical microelectrodes and sEEG-only studies; ECoG studies of listening only.
- Used in: [A high-performance neuroprosthesis for speech decoding and avatar control](../../reviews/a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control/), [Neuroprosthesis for decoding speech in a paralyzed person with anarthria](../../reviews/neuroprosthesis-for-decoding-speech-in-a-paralyzed-person-with-anarthria/)

## eeg-emg-fusion-speech-decoding

- Table: [`eeg-emg-fusion-speech-decoding.csv`](eeg-emg-fusion-speech-decoding.csv) (0 confirmed, 0 candidates read, 0 unread)
- Inclusion rule: Include speech-decoding studies (recognition, classification or synthesis of overt, whispered, silent or imagined speech) that record scalp or around-ear EEG together with surface EMG of the speech muscles and report decoding from EEG, EMG or their combination. Boundary: studies that record EMG only to remove or measure artifacts in EEG count as pattern matches but are recorded as artifact-control designs, not fusion; non-speech EEG-EMG fusion (limb movement), reviews and datasets without decoding are excluded; versions of one study count once.
- Used in: [Reconstructing Unseen Sentences from Speech-related Biosignals for Open-vocabulary Neural Communication](../../reviews/reconstructing-unseen-sentences-from-speech-related-biosignals-for-open-vocabulary-neural-commun/)

## emg-lip-video-fusion

- Table: [`emg-lip-video-fusion.csv`](emg-lip-video-fusion.csv) (7329 slot-filled, 20 pattern match, usual design in 2, 3 read in full)
- Inclusion rule: Include studies whose decoder (recognition, classification or speech synthesis) takes surface EMG of the speech muscles together with lip or face video as joint inputs and reports a fused result. Boundary: studies that record both but decode each separately, use a face image only for voice identity, use video only as a prediction target, or only acquire data are excluded; reviews are excluded; full-text-only matches are read as snippets and count only if the snippet shows a fused decoder; versions count once.
- Used in: [Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading](../../reviews/cross-modal-masking-for-robust-silent-speech-synthesis-using-semg-and-lipreading/)

| Paper | Year | Evidence |
| --- | --- | --- |
| AVE Speech: A Comprehensive Multi-Modal Dataset for Speech Recognition Integrating Audio, Visual, and Electromyographic Signals | 2025 |  |
| Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading | 2026 |  |
| Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading |  |  |
| Enhancing Multimodal Silent Speech Interfaces with Feature Selection |  |  |

## emg-speech-electrode-subset

- Table: [`emg-speech-electrode-subset.csv`](emg-speech-electrode-subset.csv) (7329 slot-filled, 42 pattern match, usual design in 10, 4 read in full)
- Inclusion rule: Surface-EMG speech studies (recognition or synthesis) that evaluate a reduced subset of their electrodes or rank electrodes, classified by how the subset is chosen: exhaustive or greedy search over trained models, single-channel ranking, random subsets, or model attribution / association analysis. Boundary: studies that only report a fixed array, sensor-hardware papers without a subset comparison, non-speech EMG and EEG-only studies are excluded when read; versions count once.
- Used in: [Articulatory Feature Prediction from Surface EMG during Speech Production](../../reviews/articulatory-feature-prediction-from-surface-emg-during-speech-production/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Articulatory Feature Prediction from Surface EMG during Speech Production | 2025 | Sec. 4.4; Table 3 |
| EMG-to-Speech with Fewer Channels |  | Sec. 5.2; Table 1 |
| Towards optimizing electrode configurations for silent speech recognition based on high-density surface electromyography | 2021 | Abstract |
| Mutual Information Analysis for Feature and Sensor Subset Selection in Surface Electromyography Based Speech Recognition | 2010 | Abstract |

## event-camera-lip-reading

- Table: [`event-camera-lip-reading.csv`](event-camera-lip-reading.csv) (7329 slot-filled, 11 pattern match, usual design in 7, 4 read in full)
- Inclusion rule: Lip reading or visual/audio-visual speech recognition whose visual input is an event stream, recorded by an event camera (DVS/DAVIS/Prophesee) or converted from RGB video. Boundary: event cameras used for non-speech face tasks (action units, gait) are excluded; event datasets without a recognition result count only if they report one; versions of one study count once.
- Used in: [A First Exploration of Neuromorphic OT-CFM for Multi-Speaker VSR](../../reviews/lipsflow-a-first-exploration-of-neuromorphic-ot-cfm-for-multi-speaker-vsr/)

## imagined-speech-eeg-consumer-headset

- Table: [`imagined-speech-eeg-consumer-headset.csv`](imagined-speech-eeg-consumer-headset.csv) (7329 slot-filled, 167 pattern match, usual design in 61, 2 read in full)
- Inclusion rule: Studies that classify imagined, covert or inner speech from scalp EEG (same population as the M06 imagined-speech EEG table); the design compared is the acquisition hardware: a consumer-grade, low-channel or wireless headset (Emotiv, OpenBCI, Muse, Unicorn, NeuroSky) against a research-grade wired amplifier named in the text. Boundary: reviews are counted as pattern matches but are not deciding priors; intracranial recordings are excluded; versions count once.
- Used in: [Toward Practical BCI: A Real-time Wireless Imagined Speech EEG Decoding System](../../reviews/toward-practical-bci-a-real-time-wireless-imagined-speech-eeg-decoding-system/)

## intracortical-speech-decoding

- Table: [`intracortical-speech-decoding.csv`](intracortical-speech-decoding.csv) (7329 slot-filled, 75 pattern match, usual design in 67, 5 read in full)
- Inclusion rule: Papers that decode speech units (phonemes, words, sentences, sound) from intracortical microelectrode recordings in humans. Included: attempted, imagined or overt speech; any array count. Excluded: intracortical decoding of hand/arm movement or handwriting only; ECoG/sEEG.
- Used in: [A high-performance speech neuroprosthesis](../../reviews/a-high-performance-speech-neuroprosthesis/), [An Accurate and Rapidly Calibrating Speech Neuroprosthesis](../../reviews/an-accurate-and-rapidly-calibrating-speech-neuroprosthesis/)

## multi-view-camera-input

- Table: [`multi-view-camera-input.csv`](multi-view-camera-input.csv) (7329 slot-filled, 787 pattern match, usual design in 693, 4 read in full)
- Inclusion rule: Include studies that decode speech (text or a speech waveform) from video of the talking face or lips, with the ledger recording an optical camera and a lip-reading, visual speech recognition or video-to-speech task, and count from the full text (reference list removed) whether the study feeds more than one simultaneous camera view (multi-view input), addresses non-frontal or profile poses, or uses the multi-view OuluVS2 corpus. Boundary: audio-visual speech recognition counts when the visual stream is decoded; talking-head generation, face recognition and biometric-only studies are excluded; a study counts under every design its text names (upper bound, related-work mentions included); versions counted once.
- Used in: [Harnessing AI for Speech Reconstruction using Multi-view Silent Video Feed](../../reviews/harnessing-ai-for-speech-reconstruction-using-multi-view-silent-video-feed/)

## rf-articulator-sensing-placement

- Table: [`rf-articulator-sensing-placement.csv`](rf-articulator-sensing-placement.csv) (7329 slot-filled, 33 pattern match, usual design in 21, 1 read in full)
- Inclusion rule: Speech or silent-speech recognition studies that sense the articulators with radar or other RF signals (IR-UWB, FMCW/SFCW, mmWave, RFID, backscatter, Wi-Fi channel sensing); the design compared is the RF front end and where it sits (active radar at a distance, Wi-Fi channel sensing, or a tag or antenna worn on the face, in a headset or in a mask). Boundary: papers that mention Wi-Fi only as a data link are left out by the pattern; datasets and surveys count; full-text and ledger hits include related-work mentions, so counts are upper bounds.
- Used in: [Lip-Siri: Contactless Open-Sentence Silent Speech with Wi-Fi Backscatter](../../reviews/lip-siri-contactless-open-sentence-silent-speech-with-wi-fi-backscatter/)

## skin-strain-sensor-channel-count

- Table: [`skin-strain-sensor-channel-count.csv`](skin-strain-sensor-channel-count.csv) (7329 slot-filled, 27 pattern match, usual design in 18, 3 read in full)
- Inclusion rule: Speech or silent-speech decoding studies whose ledger names a skin-mounted mechanical sensor (strain sensor or gauge, piezoresistive, piezoelectric or triboelectric film, textile or crack-based sensor, artificial throat); the design compared is the number of sensing channels (one versus several) and the placement (throat or neck versus face). Boundary: contactless radar and palatal pressure plates are excluded when read; reviews counted but not used as state of the art.
- Used in: [Ultrasensitive Textile Strain Sensors Redefine Wearable Silent Speech Interfaces with High Machine Learning Efficiency](../../reviews/ultrasensitive-textile-strain-sensors-redefine-wearable-silent-speech-interfaces-with-high-machine-learning-efficiency/)

## video-to-speech-visual-input-stream

- Table: [`video-to-speech-visual-input-stream.csv`](video-to-speech-visual-input-stream.csv) (7329 slot-filled, 165 pattern match, usual design in 76, 4 read in full)
- Inclusion rule: Include the video-to-speech population of components/M06/video-to-speech-synthesis (speech waveform synthesized from talking-face or lip video, audio muted at test) and count, from the full text with the reference list removed, the visual input named: a mouth or lip crop, the full face, an optical-flow stream. Boundary: a study counts under every input its text names (upper bound; related-work mentions included); audio-visual enhancement with noisy audio at test, talking-head generation and video-to-text-to-speech pipelines excluded; versions counted once.
- Used in: [Improved Speech Reconstruction from Silent Video](../../reviews/improved-speech-reconstruction-from-silent-video/)

## wearable-integrated-dry-emg-speech-sensing

- Table: [`wearable-integrated-dry-emg-speech-sensing.csv`](wearable-integrated-dry-emg-speech-sensing.csv) (7329 slot-filled, 21 pattern match, usual design in 16, 2 read in full)
- Inclusion rule: Surface-EMG speech or silent-speech decoding studies whose electrodes are dry, textile or printed and mounted on a worn object or garment (headphones, earphones, around-ear frame, glasses, mask, collar or choker, headband, patch-free garment) rather than adhesive gel electrodes placed one by one. Boundary: tattoo-like or adhesive dry patches count as dry electrodes but not as integrated into a worn object; wet adhesive arrays, non-speech EMG and non-EMG wearables (strain, acoustic) are excluded when read; versions count once.
- Used in: [Wireless Silent Speech Interface Using Multi-Channel Textile EMG Sensors Integrated into Headphones](../../reviews/wireless-silent-speech-interface-using-multi-channel-textile-emg-sensors-integrated-into-headpho/)
