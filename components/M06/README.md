# M06 Decoding

この部品について調べた話題と、確認済みの論文。各話題の表は分野全体（wiki の台帳と全文）を検索し、候補を原典で読んで採否を決めたもの。

## articulatory-intermediate

- 採否表：[`articulatory-intermediate.csv`](articulatory-intermediate.csv)（確認済み 4、読んだ候補 44、未読 0、wiki 730b0b4）
- 採る条件：音響以外の信号（神経活動、筋電、映像、超音波など）から、明示的な調音表現（計測または推定した調音器官の運動軌跡、調音素性・音韻範疇）をいったん復号し、それを次段で音響特徴・音声波形・記号列に変換する復号経路を持つ研究を含める。境界：入力そのものが調音計測（EMA・PMA・超音波）で、調音表現を中間に復号しないものは除く。音響から調音を推定してから音声に戻すもの（入力が音響）は除く。調音を補助損失・正則化にだけ使い、経路の中間に置かないものは除く。調音表現を復号するだけで次段がないものは除く。総説・引用だけの言及は除く。同一研究の別版は1件。
- 使ったレビュー：[Speech synthesis from neural decoding of spoken sentences](../../reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences/)

| 論文 | 年 | 根拠の位置 |
| --- | --- | --- |
| Articulatory Feature Prediction from Surface EMG during Speech Production | 2025 | 要旨 |
| doi-10.1038-s41586-019-1119-1 |  | 要旨、Methods「Neural decoder」 |
| Overt speech decoding from cortical activity: a comparison of different linear methods | 2023 | Abstract（Methods）、§2.6.3 |
| SPEAK YOUR MIND! Towards Imagined Speech Recognition With Hierarchical Deep Learning |  | Abstract |

## attention-seq2seq-decoding

- 採否表：[`attention-seq2seq-decoding.csv`](attention-seq2seq-decoding.csv)（確認済み 36、読んだ候補 115、未読 441、wiki 730b0b4）
- 採る条件：映像・生体信号・神経信号など音声以外の入力（音声映像の併用を含む）から、注意機構つきの符号器・復号器（系列変換、Transformer 復号器を含む）で文字・単語・音素などの記号系列を自己回帰的に出力し、評価結果を報告した研究を含める。境界：注意を特徴抽出や単語分類だけに使うもの、CTC だけのもの（Transformer 符号器＋CTC を含む）は除く。出力が音声特徴（音声合成）のものは除く。CTC と注意の併用（hybrid）は注意復号器を持つので含める。音声だけの ASR は wiki 外なので対象外。同一研究の別版は1件。
- 使ったレビュー：[Lip Reading Sentences in the Wild](../../reviews/lip-reading-sentences-in-the-wild/)

| 論文 | 年 | 根拠の位置 |
| --- | --- | --- |
| Lip Reading Sentences in the Wild | 2017 | §2.3, §6 |
| Can DNNs Learn to Lipread Full Sentences? |  | Abstract |
| Deep Lip Reading: a comparison of models and an online application |  | Abstract, §1 |
| Large-Scale Visual Speech Recognition |  | Table 3 (台帳の比較行) |
| Deep Audio-Visual Speech Recognition |  | §3, Table 2 |
| Modality Attention for End-to-End Audio-visual Speech Recognition |  | 台帳 M12 |
| A Cascade Sequence-to-Sequence Model for Chinese Mandarin Lip Reading |  | 台帳 |
| State-of-the-art Speech Recognition using EEG and Towards Decoding of Speech Spectrum From EEG | 2020 | §3 |
| Hearing Lips: Improving Lip Reading by Distilling Speech Recognizers |  | 台帳 |
| EEG based Continuous Speech Recognition using Transformers | 2020 | Abstract |
| Pseudo-Convolutional Policy Gradient for Sequence-to-Sequence Lip-Reading |  | 題名・台帳 |
| How to Teach DNNs to Pay Attention to the Visual Modality in Speech Recognition |  | 台帳 |
| Should we hard-code the recurrence concept or learn it instead? Exploring the Transformer architecture for Audio-Visual Speech Recognition |  | 台帳 |
| "Notic My Speech" -- Blending Speech Patterns With Multimedia |  | 台帳 M06 |
| End-to-end Silent Speech Recognition with Acoustic Sensing |  | Abstract |
| End-to-End Audio-Visual Speech Recognition with Conformers | 2021 | 台帳 |
| Lip reading using external viseme decoding |  | 台帳 |
| Fusing information streams in end-to-end audio-visual speech recognition |  | §5 |
| Sub-word Level Lip Reading With Visual Attention |  | 台帳 |
| Open Vocabulary Electroencephalography-To-Text Decoding and Zero-shot Sentiment Classification |  | 台帳 |
| VisG AV-HuBERT: Viseme-Guided AV-HuBERT | 2026 | §3 |
| SENSE: Semantic Neural Speech Synthesis from Brain Dynamics via Spatial Graph Encoding | 2026 | §3 |
| Learning from the Master: Distilling Cross-modal Advanced Knowledge for Lip Reading | 2021 | 台帳 |
| Discriminative Multi-modality Speech Recognition | 2020 | 台帳 M06 |
| Spatio-Temporal Fusion based Convolutional Sequence Learning for Lip Reading | 2019 | 台帳 M06 |
| Audio-Visual Speech Recognition with a Hybrid CTC/Attention Architecture | 2018 | 台帳 M06 |
| Visual Speech Recognition for Multiple Languages in the Wild | 2022 | 台帳 |
| doi-10.3390-app13116521 | 2023 | §3 |
| Speaker-Adapted End-to-End Visual Speech Recognition for Continuous Spanish | 2022 | 台帳 |
| AVATAR: Unconstrained Audiovisual Speech Recognition | 2022 | 台帳 |
| Visual Context-driven Audio Feature Enhancement for Robust End-to-End Audio-Visual Speech Recognition | 2022 | 台帳 |
| LiRA: Learning Visual Speech Representations from Audio through Self-supervision | 2021 | 台帳 |
| Robust Self-Supervised Audio-Visual Speech Recognition | 2022 | 台帳 |
| CI-AVSR: A Cantonese Audio-Visual Speech Dataset for In-car Command Recognition | 2022 | 台帳 |
| SSR7000: A Synchronized Corpus of Ultrasound Tongue Imaging for End-to-End Silent Speech Recognition | 2022 | 台帳 M06 |
| Reliability-Based Large-Vocabulary Audio-Visual Speech Recognition | 2022 | §3 |

## ctc-vs-attention

- 採否表：[`ctc-vs-attention.csv`](ctc-vs-attention.csv)（確認済み 3、読んだ候補 42、未読 128、wiki 730b0b4）
- 採る条件：同じ入力前段（視覚・生体信号・音声映像のいずれか）の上で、CTC で学習した復号器と注意機構／系列変換（seq2seq・Transformer 復号器）を両方学習し、結果を並べて比べた研究を含める。境界：CTC と注意の併用（hybrid）だけで片方単独の結果が無いものは除く。他論文の数値を並べただけの比較は除く。音声のみの ASR は wiki 外なので対象外。同一研究の別版は1件に数える。
- 使ったレビュー：[Deep Audio-Visual Speech Recognition](../../reviews/deep-audio-visual-speech-recognition/)

| 論文 | 年 | 根拠の位置 |
| --- | --- | --- |
| Deep Lip Reading: a comparison of models and an online application |  | §3.3, Table 1 |
| State-of-the-art Speech Recognition using EEG and Towards Decoding of Speech Spectrum From EEG | 2020 | §2 |
| End-to-end Silent Speech Recognition with Acoustic Sensing |  | §4.4, Fig. 4(c) |
