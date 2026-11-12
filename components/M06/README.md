# M06 Decoding

この部品について調べた話題と、確認済みの論文。各話題の表は分野全体（wiki の台帳と全文）を検索し、候補を原典で読んで採否を決めたもの。

## ctc-vs-attention

- 採否表：[`ctc-vs-attention.csv`](ctc-vs-attention.csv)（確認済み 3、読んだ候補 42、未読 128、wiki 730b0b4）
- 採る条件：同じ入力前段（視覚・生体信号・音声映像のいずれか）の上で、CTC で学習した復号器と注意機構／系列変換（seq2seq・Transformer 復号器）を両方学習し、結果を並べて比べた研究を含める。境界：CTC と注意の併用（hybrid）だけで片方単独の結果が無いものは除く。他論文の数値を並べただけの比較は除く。音声のみの ASR は wiki 外なので対象外。同一研究の別版は1件に数える。
- 使ったレビュー：[Deep Audio-Visual Speech Recognition](../../reviews/deep-audio-visual-speech-recognition/)

| 論文 | 年 | 根拠の位置 |
| --- | --- | --- |
| Deep Lip Reading: a comparison of models and an online application |  | §3.3, Table 1 |
| State-of-the-art Speech Recognition using EEG and Towards Decoding of Speech Spectrum From EEG | 2020 | §2 |
| End-to-end Silent Speech Recognition with Acoustic Sensing |  | §4.4, Fig. 4(c) |
