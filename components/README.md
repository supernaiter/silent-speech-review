# The 13 components

Any speech-intention decoder, whatever its sensor, can be described by the same 13 components (M01–M13). For each component, these are the topics searched across the whole field for the reviews, with every candidate paper and its decision. Tables grow with each review.

| Component | Name | Topics |
| --- | --- | --- |
| M01 | Training-time act | — |
| M02 | Teacher signal | — |
| M03 | Train / calibrate | [length-curriculum](M03/) |
| M04 | Use-time act | [overt-to-silent-transfer](M04/) |
| M05 | Sensing | — |
| M06 | Decoding | [articulatory-intermediate](M06/), [attention-seq2seq-decoding](M06/), [ctc-vs-attention](M06/) |
| M07 | Runtime aids | — |
| M08 | Output | [neural-speech-synthesis](M08/) |
| M09 | Confirmation | — |
| M10 | Correction | — |
| M11 | Eval reference | [in-the-wild-sentence-benchmark](M11/) |
| M12 | Evaluation | [human-lipreader-baseline](M12/), [listener-intelligibility-test](M12/) |
| M13 | Hardware & limits | — |
