# M05 Sensing

Topics searched for this component across the whole field, and the confirmed papers. Each table lists every candidate found in the ledgers and full texts, read and marked include or exclude.

## active-acoustic-sensor-placement-and-audio-stream

- Table: [`active-acoustic-sensor-placement-and-audio-stream.csv`](active-acoustic-sensor-placement-and-audio-stream.csv) (7329 slot-filled, 22 pattern match, usual design in 12, 3 read in full)
- Inclusion rule: Same population as active-acoustic-speech-sensing (emitted near-ultrasonic or ultrasonic signal, reflection decoded for speech or mouth state); the design compared is where the transducers sit (in-ear, earphone or headphone; glasses or headset; smartphone or loudspeaker) and whether a voiced or whispered audio stream is fused with the echo. Boundary: a study counts under every design its full text names (upper bound); surveys and datasets count as pattern matches only.
- Used in: [Poster: Recognizing Hidden-in-the-Ear Private Key for Reliable Silent Speech Interface Using Multi-Task Learning](../../reviews/poster-recognizing-hidden-in-the-ear-private-key-for-reliable-silent-speech-interface-using-mult/)

## active-acoustic-speech-sensing

- Table: [`active-acoustic-speech-sensing.csv`](active-acoustic-speech-sensing.csv) (7329 slot-filled, 22 pattern match, usual design in 16, 3 read in full)
- Inclusion rule: Studies that emit an acoustic signal (near-ultrasonic or ultrasonic, from a loudspeaker, earphone or transducer) and decode speech, silent speech or mouth state from its reflection or Doppler shift off the lips, face, jaw or vocal tract, captured by a microphone. Boundary: B-mode ultrasound tongue imaging, RF radar, Wi-Fi and laser sensing are excluded when read; reviews and datasets without a decoding result count as pattern matches only; versions of one study count once.
- Used in: [End-to-End Silent Speech Recognition with Acoustic Sensing](../../reviews/end-to-end-silent-speech-recognition-with-acoustic-sensing/), [Poster: Recognizing Hidden-in-the-Ear Private Key for Reliable Silent Speech Interface Using Multi-Task Learning](../../reviews/poster-recognizing-hidden-in-the-ear-private-key-for-reliable-silent-speech-interface-using-mult/), [SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces](../../reviews/sonispeech-a-large-scale-open-vocabulary-tri-modal-dataset-for-wearable-silent-speech-interfaces/)

| Paper | Year | Evidence |
| --- | --- | --- |
| End-to-end Silent Speech Recognition with Acoustic Sensing |  | Sec. 4.2 |
| M2SILENT: Enabling Multi-user Silent Speech Interactions via Multi-directional Speakers in Shared Spaces |  | Sec. 5 |
| SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces | 2026 | Abstract, Table 3 |
| Multimodal Speech Recognition with Ultrasonic Sensors |  | Sec. 5.1, Table 1 |

## attention-weight-eeg-channel-subset

- Table: [`attention-weight-eeg-channel-subset.csv`](attention-weight-eeg-channel-subset.csv) (7329 slot-filled, 34 pattern match, usual design in 6, 2 read in full)
- Inclusion rule: Neural signal speech or tone decoding studies that shrink the recording set for the main experiment by ranking channels with trained-model attention weights (or similar attribution) and keeping a top subset, and that report a full-versus-reduced accuracy comparison. Boundary: hardware-only channel counts, exhaustive or greedy selection without attention, EMG-only electrode subsets and papers with no full-versus-reduced comparison are excluded; selecting channels with data spanning test folds or subjects is included but flagged; versions of one study count once.
- Used in: [CAT-Net: A Cross-Attention Tone Network for Cross-Subject EEG-EMG Fusion Tone Decoding](../../reviews/cat-net-a-cross-attention-tone-network-for-cross-subject-eeg-emg-fusion-tone-decoding/)

## body-conducted-sensor-with-air-microphone

- Table: [`body-conducted-sensor-with-air-microphone.csv`](body-conducted-sensor-with-air-microphone.csv) (7329 slot-filled, 123 pattern match, usual design in 71, 2 read in full)
- Inclusion rule: Speech studies that record a skin-, bone- or tissue-conducted sensor (throat or contact microphone, accelerometer, vibration sensor, NAM microphone) from the talker together with an air microphone; design compared is the body site of the conducted sensor and whether whispered or murmured input is used. Boundary: sensors only listed in related work still match the full-text pattern (upper bound); hearing devices that do not pick up the talker are excluded by reading; versions count once.
- Used in: [NasoVoce: A Nose-Mounted Low-Audibility Speech Interface for Always-Available Speech Interaction](../../reviews/nasovoce/)

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
- Used in: [Articulatory Feature Prediction from Surface EMG during Speech Production](../../reviews/articulatory-feature-prediction-from-surface-emg-during-speech-production/), [Development of sEMG sensors and algorithms for silent speech recognition](../../reviews/development-of-semg-sensors-and-algorithms-for-silent-speech-recognition/)

| Paper | Year | Evidence |
| --- | --- | --- |
| Articulatory Feature Prediction from Surface EMG during Speech Production | 2025 | Sec. 4.4; Table 3 |
| EMG-to-Speech with Fewer Channels |  | Sec. 5.2; Table 1 |
| Towards optimizing electrode configurations for silent speech recognition based on high-density surface electromyography | 2021 | Abstract |
| Mutual Information Analysis for Feature and Sensor Subset Selection in Surface Electromyography Based Speech Recognition | 2010 | Abstract |

## emotion-related-vocal-tract-shape-deviation

- Table: [`emotion-related-vocal-tract-shape-deviation.csv`](emotion-related-vocal-tract-shape-deviation.csv) (7329 slot-filled, 88 pattern match, usual design in 14, 1 read in full)
- Inclusion rule: Same vocal-tract MRI population (88 unique ledger studies whose ledger text names rtMRI, real-time or dynamic MRI, MRI-TIMIT, USC-TIMIT or the Vocal Tract Morphology MRI database), counting studies whose full text names emotional speech and studies that compare vocal-tract boundary distances, apertures or constrictions against a neutral reference. Boundary: emotion classifiers without vocal-tract geometry and geometry analyses without an emotion condition fall outside the design; related-work mentions match the pattern (upper bound).
- Used in: [Silent Speech and Emotion Recognition from Vocal Tract Shape Dynamics in Real-Time MRI](../../reviews/silent-speech-and-emotion-recognition-from-vocal-tract-shape-dynamics-in-real-time-mri/)

## event-camera-lip-reading

- Table: [`event-camera-lip-reading.csv`](event-camera-lip-reading.csv) (7329 slot-filled, 11 pattern match, usual design in 7, 4 read in full)
- Inclusion rule: Lip reading or visual/audio-visual speech recognition whose visual input is an event stream, recorded by an event camera (DVS/DAVIS/Prophesee) or converted from RGB video. Boundary: event cameras used for non-speech face tasks (action units, gait) are excluded; event datasets without a recognition result count only if they report one; versions of one study count once.
- Used in: [A First Exploration of Neuromorphic OT-CFM for Multi-Speaker VSR](../../reviews/lipsflow-a-first-exploration-of-neuromorphic-ot-cfm-for-multi-speaker-vsr/)

## facial-emg-channel-layout

- Table: [`facial-emg-channel-layout.csv`](facial-emg-channel-layout.csv) (7329 slot-filled, 17 pattern match, usual design in 2, 2 read in full)
- Inclusion rule: Include silent-speech recognition studies using facial surface EMG that specify or compare electrode, channel, or muscle placement and relate the configuration to word-recognition performance. Boundary: exclude EMG studies without placement or muscle details and studies that change only the decoder or signal-processing method.
- Used in: [Knowledge Distilled Ensemble Model for sEMG-based Silent Speech Interface](../../reviews/knowledge-distilled-ensemble-model-for-semg-based-silent-speech-interface/)

## imagined-speech-eeg-consumer-headset

- Table: [`imagined-speech-eeg-consumer-headset.csv`](imagined-speech-eeg-consumer-headset.csv) (7329 slot-filled, 167 pattern match, usual design in 61, 2 read in full)
- Inclusion rule: Studies that classify imagined, covert or inner speech from scalp EEG (same population as the M06 imagined-speech EEG table); the design compared is the acquisition hardware: a consumer-grade, low-channel or wireless headset (Emotiv, OpenBCI, Muse, Unicorn, NeuroSky) against a research-grade wired amplifier named in the text. Boundary: reviews are counted as pattern matches but are not deciding priors; intracranial recordings are excluded; versions count once.
- Used in: [Toward Practical BCI: A Real-time Wireless Imagined Speech EEG Decoding System](../../reviews/toward-practical-bci-a-real-time-wireless-imagined-speech-eeg-decoding-system/)

## intracortical-speech-decoding

- Table: [`intracortical-speech-decoding.csv`](intracortical-speech-decoding.csv) (7329 slot-filled, 75 pattern match, usual design in 67, 5 read in full)
- Inclusion rule: Papers that decode speech units (phonemes, words, sentences, sound) from intracortical microelectrode recordings in humans. Included: attempted, imagined or overt speech; any array count. Excluded: intracortical decoding of hand/arm movement or handwriting only; ECoG/sEEG.
- Used in: [A high-performance speech neuroprosthesis](../../reviews/a-high-performance-speech-neuroprosthesis/), [An Accurate and Rapidly Calibrating Speech Neuroprosthesis](../../reviews/an-accurate-and-rapidly-calibrating-speech-neuroprosthesis/)

## intracranial-speech-electrode-scale

- Table: [`intracranial-speech-electrode-scale.csv`](intracranial-speech-electrode-scale.csv) (7329 slot-filled, 618 pattern match, usual design in 2, 4 read in full)
- Inclusion rule: Design of interest: electrode type and scale used to record speech-related activity: penetrating intracortical microelectrodes, clinical subdural grids (about 1 cm spacing), high-density ECoG (about 4 mm) or micro-ECoG (under about 3 mm, microwire or thin film). Boundary: design counts are full-text pattern matches (mentions included, upper bounds). Setting: human studies that decode produced, attempted or imagined speech from intracranial recordings (ECoG, micro-ECoG, sEEG, intracortical arrays); ledger pattern = the published intracranial-speech-test-partition pattern (intracranial signal and speech unit named in the ledger text). Off-population at the target's time: reviews, listening/perception studies and studies with no decoder. Target first public 2010-09; prior = first public before 2010-03; [concurrent] = 2010-03 to 2011-03; versions of one study count once; two index-misdated 2012 papers (pmc-3321121-revspeech, pmc-3342676-gammaev) are later; 18 undated hits are all arXiv 2023 or later. Sensor-slot boundary (differs from M06/M12 on purpose): for electrode type the decoder requirement is dropped, so every intracranial recording during speech or word production before 2010-03 counts; listening-only studies and reviews stay excluded.
- Used in: [Decoding spoken phonemes from sensorimotor cortex with High-Density ECoG grids](../../reviews/decoding-spoken-phonemes-from-sensorimotor-cortex-with-high-density-ecog-grids/), [Decoding spoken words using local field potentials recorded from the cortical surface](../../reviews/decoding-spoken-words-using-local-field-potentials-recorded-from-the-cortical-surface/)

## multi-view-camera-input

- Table: [`multi-view-camera-input.csv`](multi-view-camera-input.csv) (7329 slot-filled, 787 pattern match, usual design in 693, 4 read in full)
- Inclusion rule: Include studies that decode speech (text or a speech waveform) from video of the talking face or lips, with the ledger recording an optical camera and a lip-reading, visual speech recognition or video-to-speech task, and count from the full text (reference list removed) whether the study feeds more than one simultaneous camera view (multi-view input), addresses non-frontal or profile poses, or uses the multi-view OuluVS2 corpus. Boundary: audio-visual speech recognition counts when the visual stream is decoded; talking-head generation, face recognition and biometric-only studies are excluded; a study counts under every design its text names (upper bound, related-work mentions included); versions counted once.
- Used in: [Harnessing AI for Speech Reconstruction using Multi-view Silent Video Feed](../../reviews/harnessing-ai-for-speech-reconstruction-using-multi-view-silent-video-feed/), [Lipper: Synthesizing Thy Speech using Multi-View Lipreading](../../reviews/lipper-synthesizing-thy-speech-using-multi-view-lipreading/)

## rf-articulator-sensing-placement

- Table: [`rf-articulator-sensing-placement.csv`](rf-articulator-sensing-placement.csv) (7329 slot-filled, 33 pattern match, usual design in 21, 1 read in full)
- Inclusion rule: Speech or silent-speech recognition studies that sense the articulators with radar or other RF signals (IR-UWB, FMCW/SFCW, mmWave, RFID, backscatter, Wi-Fi channel sensing); the design compared is the RF front end and where it sits (active radar at a distance, Wi-Fi channel sensing, or a tag or antenna worn on the face, in a headset or in a mask). Boundary: papers that mention Wi-Fi only as a data link are left out by the pattern; datasets and surveys count; full-text and ledger hits include related-work mentions, so counts are upper bounds.
- Used in: [Lip-Siri: Contactless Open-Sentence Silent Speech with Wi-Fi Backscatter](../../reviews/lip-siri-contactless-open-sentence-silent-speech-with-wi-fi-backscatter/), [Movement Detection of Tongue and Related Body Parts Using IR-UWB Radar](../../reviews/movement-detection-of-tongue-and-related-body-parts-using-ir-uwb-radar/)

## skin-strain-sensor-channel-count

- Table: [`skin-strain-sensor-channel-count.csv`](skin-strain-sensor-channel-count.csv) (7329 slot-filled, 27 pattern match, usual design in 18, 3 read in full)
- Inclusion rule: Speech or silent-speech decoding studies whose ledger names a skin-mounted mechanical sensor (strain sensor or gauge, piezoresistive, piezoelectric or triboelectric film, textile or crack-based sensor, artificial throat); the design compared is the number of sensing channels (one versus several) and the placement (throat or neck versus face). Boundary: contactless radar and palatal pressure plates are excluded when read; reviews counted but not used as state of the art.
- Used in: [Ultrasensitive Textile Strain Sensors Redefine Wearable Silent Speech Interfaces with High Machine Learning Efficiency](../../reviews/ultrasensitive-textile-strain-sensors-redefine-wearable-silent-speech-interfaces-with-high-machine-learning-efficiency/)

## video-to-speech-visual-input-stream

- Table: [`video-to-speech-visual-input-stream.csv`](video-to-speech-visual-input-stream.csv) (7329 slot-filled, 165 pattern match, usual design in 76, 4 read in full)
- Inclusion rule: Include the video-to-speech population of components/M06/video-to-speech-synthesis (speech waveform synthesized from talking-face or lip video, audio muted at test) and count, from the full text with the reference list removed, the visual input named: a mouth or lip crop, the full face, an optical-flow stream. Boundary: a study counts under every input its text names (upper bound; related-work mentions included); audio-visual enhancement with noisy audio at test, talking-head generation and video-to-text-to-speech pipelines excluded; versions counted once.
- Used in: [Improved Speech Reconstruction from Silent Video](../../reviews/improved-speech-reconstruction-from-silent-video/), [Vid2speech: Speech Reconstruction from Silent Video](../../reviews/vid2speech-speech-reconstruction-from-silent-video/)

## wearable-inertial-silent-speech-sensing

- Table: [`wearable-inertial-silent-speech-sensing.csv`](wearable-inertial-silent-speech-sensing.csv) (7329 slot-filled, 13 pattern match, usual design in 14, 3 read in full)
- Inclusion rule: Silent-speech studies (any task) whose ledger or full text names wearable accelerometers, gyroscopes or IMUs on the face, jaw or neck; the design compared is the inertial quantity used (acceleration only, gyroscope or attitude angles) and whether sensor count, subsets or axes are compared. Boundary: body-conduction microphones and accelerometers used only as vibration pickups for voiced speech, EMA/magnetic tracking without inertial sensors, and hand or body gesture IMUs are outside when read; versions count once.
- Used in: [Silent Speech Sentence Recognition with Six-Axis Accelerometers using Conformer and CTC Algorithm](../../reviews/silent-speech-sentence-recognition-with-six-axis-accelerometers-using-conformer-and-ctc-algorith/)

## wearable-integrated-dry-emg-speech-sensing

- Table: [`wearable-integrated-dry-emg-speech-sensing.csv`](wearable-integrated-dry-emg-speech-sensing.csv) (7329 slot-filled, 21 pattern match, usual design in 16, 2 read in full)
- Inclusion rule: Surface-EMG speech or silent-speech decoding studies whose electrodes are dry, textile or printed and mounted on a worn object or garment (headphones, earphones, around-ear frame, glasses, mask, collar or choker, headband, patch-free garment) rather than adhesive gel electrodes placed one by one. Boundary: tattoo-like or adhesive dry patches count as dry electrodes but not as integrated into a worn object; wet adhesive arrays, non-speech EMG and non-EMG wearables (strain, acoustic) are excluded when read; versions count once.
- Used in: [SilentWear: an Ultra-Low Power Wearable System for EMG-based Silent Speech Recognition](../../reviews/silentwear-an-ultra-low-power-wearable-system-for-emg-based-silent-speech-recognition/), [Soft Active EMG Interface for Machine Learning-Enabled Silent Speech Recognition](../../reviews/soft-active-electromyography-interface-for-machine-learning-enabled-silent-speech-recognition/), [Wireless Silent Speech Interface Using Multi-Channel Textile EMG Sensors Integrated into Headphones](../../reviews/wireless-silent-speech-interface-using-multi-channel-textile-emg-sensors-integrated-into-headpho/)
