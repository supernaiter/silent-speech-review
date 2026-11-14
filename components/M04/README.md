# M04 Use-time act

この部品について調べた話題と、確認済みの論文。各話題の表は分野全体（wiki の台帳と全文）を検索し、候補を原典で読んで採否を決めたもの。

## overt-to-silent-transfer

- 採否表：[`overt-to-silent-transfer.csv`](overt-to-silent-transfer.csv)（確認済み 23、読んだ候補 104、未読 0、wiki 730b0b4）
- 採る条件：声に出した（または声に出そうと試みた）発話だけで学習した復号器を、無声の発話（口だけ動かす、無声で調音する、内言・想像）に再学習なしで当て、その結果を報告した研究を含める。信号は問わない（神経、筋電、超音波、映像など）。境界：無声のデータでも学習するもの（可聴側の目標を移す方法など）は、可聴学習のみの基準条件を別に報告していれば含める。可聴モデルを無声データの時刻合わせや初期化にだけ使うものは除く。音響音声のささやき声と通常声の間の転移は除く。聴取（知覚）から内言への転移は除く。神経活動の類似性の解析だけで復号器を当てないものは除く。総説・引用だけの一致は除く。同一研究の別版は1件。
- 使ったレビュー：[Speech synthesis from neural decoding of spoken sentences](../../reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences/)

| 論文 | 年 | 根拠の位置 |
| --- | --- | --- |
| Visual-Only Recognition of Normal, Whispered and Silent Speech |  | Introduction、実験の格子 |
| Digital Voicing of Silent Speech |  | 台帳（基準条件）、§Abstract |
| Towards Neural Decoding of Imagined Speech based on Spoken Speech |  | Abstract |
| Transfer learning for covert speech classification using EEG Hilbert envelope and temporal fine structure | 2025 | 台帳（研究目的） |
| Transfer Learning for Covert Speech Classification Using EEG Hilbert Envelope and Temporal Fine Structure |  | 台帳（研究目的） |
| Relating the Neural Representations of Vocalized, Mimed, and Imagined Speech | 2026 | Results（一致箇所） |
| Affect Decoding in Phonated and Silent Speech Production from Surface EMG |  | 表の説明（一致箇所） |
| Shared and distinct temporal representations of Chinese words across imagined, silent, and overt speech | 2026 | 台帳 |
| doi-10.1038-s41586-019-1119-1 |  | Results「Synthesizing mimed speech」 |
| doi-10.1038-s41586-025-09127-3 |  | Results（一致箇所） |
| Feasibility of decoding covert speech in ECoG with a Transformer trained on overt speech | 2024 | Abstract（一致箇所） |
| Imagined speech event detection from electrocorticography and its transfer between speech modes and subjects | 2024 | 台帳 |
| Word classification across speech modes from low-density electrocorticography signals | 2026 | 台帳 |
| The Nested Hierarchy of Overt, Mouthed, and Imagined Speech Activity Evident in Intracranial Recordings | 2022 | 台帳 |
| Feasibility of decoding covert speech in ECoG with a Transformer trained on overt speech | 2024 | Abstract（一致箇所） |
| Evidence for common spike-based temporal coding of overt and covert speech in pars triangularis of human Broca's area | 2024 | 台帳 |
| Representation of verbal thought in motor cortex and implications for speech neuroprostheses | 2024 | 図の説明（一致箇所） |
| Visual-Only Recognition of Normal, Whispered and Silent Speech | 2018 | Introduction、実験の格子 |
| EMG-to-Speech: Direct Generation of Speech from Facial Electromyographic Signals | 2017 | §6.3 Mapping on EMG Data |
| Digital Voicing of Silent Speech |  | 台帳（基準条件）、§Abstract |
| Feasibility of decoding covert speech in ECoG with a Transformer trained on overt speech | 2024 | Abstract（一致箇所） |
| Semantic-Aware Decoding of Covert Inner Speech: A Multimodal EEG–EMG–Audio Framework | 2026 | 台帳 |
| Silent Speech Recognition with Articulator Positions Estimated from Tongue Ultrasound and Lip Video |  | 本文（一致箇所） |
| Decoding spectrotemporal features of overt and covert speech from the human cortex | 2014 | Introduction、Methods（Dynamic time warping） |
| A Spectral Mapping Method for EMG-based Recognition of Silent Speech | 2010 | Abstract |
| Session-Independent EMG-Based Speech Recognition | 2011 | §（Cross-Modal Testing の節） |
| Silent Speech Recognition with Articulator Positions Estimated from Tongue Ultrasound and Lip Video | 2023 | 本文（一致箇所） |
| Silent Speech Recognition with Articulator Positions Estimated from Tongue Ultrasound and Lip Video |  | 本文（一致箇所） |
| Silent vs Vocalized Articulation for a Portable Ultrasound-Based Silent Speech Interface | 2010 | Abstract |
| Silent vs Vocalized Articulation for a Portable Ultrasound-Based Silent Speech Interface | 2010 | Abstract |
| Relating the Neural Representations of Vocalized, Mimed, and Imagined Speech | 2026 | Results（一致箇所） |
| Feasibility of decoding covert speech in ECoG with a Transformer trained on overt speech | 2024 | Abstract（一致箇所） |
| Imagined speech event detection from electrocorticography and its transfer between speech modes and subjects | 2024 | 台帳 |
| Imagined speech event detection from electrocorticography and its transfer between speech modes and subjects | 2024 | 台帳 |
| From pronounced to imagined: improving speech decoding with multi-condition EEG data | 2025 | Methods |
| Decoding spectrotemporal features of overt and covert speech from the human cortex | 2014 | Introduction、Methods（Dynamic time warping） |
