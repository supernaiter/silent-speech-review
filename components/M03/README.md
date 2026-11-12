# M03 Train / calibrate

この部品について調べた話題と、確認済みの論文。各話題の表は分野全体（wiki の台帳と全文）を検索し、候補を原典で読んで採否を決めたもの。

## length-curriculum

- 採否表：[`length-curriculum.csv`](length-curriculum.csv)（確認済み 18、読んだ候補 71、未読 5、wiki 730b0b4）
- 採る条件：系列を出力する復号器の学習で、短い単位（単語・短い区間）の例から始め、学習の進行に合わせて入力系列の長さを伸ばす（文・長い区間へ移す）手順を使った研究を含める。境界：雑音の強さ・難易度・データ量だけを段階的に変えるカリキュラムは除く。単語単位の事前学習のあと文単位で学習し直す二段階は、短い単位から長い単位へ移す明示的な手順として書かれていれば含める。前作の手順を引き継いだと書くだけでなく実際に使っていれば含める。同一研究の別版は1件。
- 使ったレビュー：[Lip Reading Sentences in the Wild](../../reviews/lip-reading-sentences-in-the-wild/)

| 論文 | 年 | 根拠の位置 |
| --- | --- | --- |
| Lip Reading Sentences in the Wild | 2017 | §3.1 |
| Deep Lip Reading: a comparison of models and an online application |  | §3 |
| Deep Audio-Visual Speech Recognition |  | §5.2 |
| Learning from Videos with Deep Convolutional LSTM Networks |  | §4 |
| LipReading with 3D-2D-CNN BLSTM-HMM and word-CTC models |  | §3 |
| Distinguishing Homophenes Using Multi-Head Visual-Audio Memory for Lip Reading |  | §4 |
| Predict-and-Update Network: Audio-Visual Speech Recognition Inspired by Human Speech Perception |  | §4 |
| Watch or Listen: Robust Audio-Visual Speech Recognition with Visual Corruption Modeling and Reliability Scoring |  | 台帳 M03 |
| AlignVSR: Audio-Visual Cross-Modal Alignment for Visual Speech Recognition |  | 台帳 M03 |
| Cascade-Free Mandarin Visual Speech Recognition via Semantic-Guided Cross-Representation Alignment |  | §4 |
| Spatio-Temporal Fusion based Convolutional Sequence Learning for Lip Reading | 2019 | §4 |
| MultiAVSR: Robust Speech Recognition via Supervised Multi-Task Audio-Visual Learning | 2025 | §4 |
| An Effective Conversion of Visemes to Words for High-Performance Automatic Lipreading | 2021 | §4 |
| Korean Lip-Reading: Data Construction and Sentence-Level Lip-Reading | 2024 | §3 |
| LiRA: Learning Visual Speech Representations from Audio through Self-supervision | 2021 | §4 |
| An Improved End-to-End Audio-Visual Speech Recognition Model |  | §3.1 |
| Research on Robust Audio-Visual Speech Recognition Algorithms | 2023 | 台帳 M03 |
| E-commerce Video & Content Understanding via Vision: A Comprehensive Study on Lip Reading and Visual Speech Recognition for Enhanced Shopping Experience | 2026 | 台帳 M06 |
