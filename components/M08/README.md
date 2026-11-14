# M08 Output

この部品について調べた話題と、確認済みの論文。各話題の表は分野全体（wiki の台帳と全文）を検索し、候補を原典で読んで採否を決めたもの。

## neural-speech-synthesis

- 採否表：[`neural-speech-synthesis.csv`](neural-speech-synthesis.csv)（確認済み 15、読んだ候補 140、未読 361、wiki 730b0b4）
- 採る条件：音響以外の神経信号（ECoG、sEEG、皮質内電極、EEG、MEG など）のうち、発話の産出（声に出す、口だけ動かす、試みる、想像する）に伴う活動から、連続的な音響表現（スペクトログラム、MFCC・ボコーダー特徴、フォルマント）を復号し、音声として出すか音声に変換できる形で評価した研究を含める。境界：聴取中の活動から聞いた音声を再構成する研究（知覚）は除く。テキストを復号してから定型の音声合成器で読み上げるだけのものは除く。四肢運動の想像などで合成器を操作する BCI は、発話の産出に伴う活動ではないので除く。総説・倫理論文・引用だけの一致は除く。同一研究の別版は1件。
- 使ったレビュー：[Speech synthesis from neural decoding of spoken sentences](../../reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences/)

| 論文 | 年 | 根拠の位置 |
| --- | --- | --- |
| Synthesizing Speech from Intracranial Depth Electrodes using an Encoder-Decoder Framework | 2022 | 台帳 |
| EEG-to-Voice Decoding of Spoken and Imagined speech Using Non-Invasive EEG | 2025 | Introduction（一致箇所） |
| arxiv-2512.04618 |  | 台帳（研究目的） |
| Brain-to-Speech: Prosody Feature Engineering and Transformer-Based Reconstruction | 2026 | 台帳（研究目的） |
| Brain2Speech-Net: Fast and Intelligible Brain-to-Speech Synthesis Without Text Decoding | 2026 | 題名 |
| Brain2Speech-Net: Fast and Intelligible Brain-to-Speech Synthesis Without Text Decoding | 2026 | 題名 |
| Brain2Speech-Net: Fast and Intelligible Brain-to-Speech Synthesis Without Text Decoding | 2026 | 題名 |
| doi-10.1038-s41586-019-1119-1 |  | Methods「Neural decoder」「Speech synthesis from acoustic features」 |
| doi-10.1038-s41586-025-09127-3 |  | 台帳（研究目的） |
| Speech Synthesis from ECoG using Densely Connected 3D Convolutional Neural Networks |  | 題名、Abstract |
| Speech Synthesis from Stereotactic EEG using an Electrode Shaft Dependent Multi-Input Convolutional Neural Network Approach | 2021 | 台帳（研究目的） |
| A Wireless Brain-Machine Interface for Real-Time Speech Synthesis | 2009 | Introduction、Methods |
| Decoding spectrotemporal features of overt and covert speech from the human cortex | 2014 | Introduction、Methods |
| Generating Natural, Intelligible Speech From Brain Activity in Motor, Premotor, and Inferior Frontal Cortices | 2019 | Methods |
| MiSTR: Multi-Modal iEEG-to-Speech Synthesis with Transformer-Based Prosody Prediction and Neural Phase Reconstruction | 2025 | 台帳（研究目的） |
| Online speech synthesis using a chronically implanted brain-computer interface | 2024 | 台帳（研究目的） |
| A neural speech decoding framework leveraging deep learning and speech | 2025 | 本文（一致箇所） |
| A wireless brain-machine interface for real-time speech synthesis | 2009 | Introduction、Methods |
| A Wireless Brain-Machine Interface for Real-Time Speech Synthesis | 2009 | Introduction、Methods |
| Decoding spectrotemporal features of overt and covert speech from the human cortex | 2014 | Introduction、Methods |
| Speech Synthesis from ECoG using Densely Connected 3D Convolutional Neural Networks | 2019 | 題名、Abstract |
| Generating Natural, Intelligible Speech From Brain Activity in Motor, Premotor, and Inferior Frontal Cortices | 2019 | Methods |
| Generating Natural, Intelligible Speech From Brain Activity in Motor, Premotor, and Inferior Frontal Cortices | 2019 | Methods |
