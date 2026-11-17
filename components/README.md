# The 13 components

Any speech-intention decoder, whatever its sensor, can be described by the same 13 components (M01–M13). For each component, these are the topics searched across the whole field for the reviews, with every candidate paper and its decision. Tables grow with each review.

| Component | Name | Topics |
| --- | --- | --- |
| M01 | Training-time act | — |
| M02 | Teacher signal | [auxiliary-representation-prediction](M02/), [speech-latent-target](M02/), [ssl-speech-unit-target](M02/), [whisper-to-normal-training-pairing](M02/) |
| M03 | Train / calibrate | [cross-subject-pooled-training](M03/), [length-curriculum](M03/), [self-supervised-pretraining](M03/), [speech-bci-calibration-data](M03/) |
| M04 | Use-time act | [noninvasive-text-production-action](M04/), [overt-to-silent-transfer](M04/) |
| M05 | Sensing | [ecog-speech-decoding](M05/), [intracortical-speech-decoding](M05/) |
| M06 | Decoding | [articulatory-intermediate](M06/), [articulography-to-speech-synthesis](M06/), [attention-seq2seq-decoding](M06/), [closed-vocabulary-word-classification](M06/), [ctc-vs-attention](M06/), [noninvasive-decoding-segmentation](M06/), [noninvasive-speech-decoding-objective](M06/), [phoneme-rnn-ctc-lm-decoding](M06/), [visual-frontend-spatial-pooling](M06/), [whisper-conversion-intermediate-representation](M06/) |
| M07 | Runtime aids | [large-vocabulary-lm-for-neural-speech](M07/), [noninvasive-text-decoding-language-model](M07/) |
| M08 | Output | [biosignal-to-speech-voice-control](M08/), [neural-speech-synthesis](M08/), [vsr-output-token-unit](M08/) |
| M09 | Confirmation | — |
| M10 | Correction | — |
| M11 | Eval reference | [in-the-wild-sentence-benchmark](M11/) |
| M12 | Evaluation | [human-lipreader-baseline](M12/), [listener-intelligibility-test](M12/), [lrs3-visual-only-wer](M12/), [silent-emg-voicing-benchmark](M12/), [whisper-conversion-evaluation](M12/) |
| M13 | Hardware & limits | [long-term-home-use](M13/) |
