# M12 Evaluation

この部品について調べた話題と、確認済みの論文。各話題の表は分野全体（wiki の台帳と全文）を検索し、候補を原典で読んで採否を決めたもの。

## human-lipreader-baseline

- 採否表：[`human-lipreader-baseline.csv`](human-lipreader-baseline.csv)（確認済み 7、読んだ候補 116、未読 0、wiki 730b0b4）
- 採る条件：機械による読唇・無声発話認識の結果と、人間の読唇者（専門家、聴覚障害のある人、一般の参加者）が同じデータ（同じテスト集合かその部分集合）を読んだ結果を、同じ指標で並べた研究を含める。境界：再構成した音声を人が聞き取る明瞭度評価は除く。人間の成績を文献値として引くだけのものは除く。人間どうしの読唇能力の研究で機械の結果がないものは除く。同一研究の別版は1件。
- 使ったレビュー：[Lip Reading Sentences in the Wild](../../reviews/lip-reading-sentences-in-the-wild/)

| 論文 | 年 | 根拠の位置 |
| --- | --- | --- |
| LipNet: End-to-End Sentence-level Lipreading (2016) |  | §1, §4.4 Table |
| Lip Reading Sentences in the Wild | 2017 | §5.2, Table 5 |
| Towards Estimating the Upper Bound of Visual-Speech Recognition: The Visual Lip-Reading Feasibility Database (FG 2017) |  | Abstract |
| Large-Scale Visual Speech Recognition |  | Abstract |
| The Lipreading Gap: Do VSR Models Perceive Visual Speech Like Human Lipreaders? |  | §1 |
| isca-hilder09_avsp |  | Abstract, §3.3 Table 1 |
| Human Audio-Visual Consonant Recognition Analyzed with Three Bimodal Integration Models | 2009 | §4, Fig. 3 |

## listener-intelligibility-test

- 採否表：[`listener-intelligibility-test.csv`](listener-intelligibility-test.csv)（確認済み 29、読んだ候補 106、未読 0、wiki 730b0b4）
- 採る条件：音響以外の信号（神経活動、筋電、EMA・PMA などの調音計測、超音波、口元映像）から合成した音声を、人間の聴取者が書き取る、または選択肢から語・文を同定する明瞭度試験で評価し、正答率・WER などを報告した研究を含める。境界：自然さ・好み・MOS の評定だけのものは除く。入力が音響（ささやき声、NAM マイク、食道発声など）の変換は除く。テキストからの合成や知覚実験の刺激音は除く。合成音を自動音声認識だけで評価するものは除く。総説・引用だけの一致は除く。同一研究の別版は1件。
- 使ったレビュー：[Speech synthesis from neural decoding of spoken sentences](../../reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences/)

| 論文 | 年 | 根拠の位置 |
| --- | --- | --- |
| Vid2speech: Speech Reconstruction from Silent Video (CVPR 2017) |  | §（Human listening study） |
| Lip2AudSpec: Speech reconstruction from silent lip movements video |  | §4.3.4 |
| Learning Individual Speaking Styles for Accurate Lip to Speech Synthesis |  | Abstract |
| Digital Voicing of Silent Speech |  | §1 |
| An Improved Model for Voicing Silent Speech |  | §（一致箇所） |
| Synthesizing Speech from Intracranial Depth Electrodes using an Encoder-Decoder Framework | 2022 | §（一致箇所） |
| FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis | 2022 | §（一致箇所） |
| Deep Speech Synthesis from Articulatory Representations |  | §（一致箇所） |
| emg2speech: synthesizing speech from electromyography using self-supervised speech models | 2026 | §（一致箇所） |
| Learning Individual Speaking Styles for Accurate Lip to Speech Synthesis | 2020 | Abstract |
| Noninvasive Speech Restoration After Total Laryngectomy Using Surface Electromyography: Pilot Study | 2026 | Methods（一致箇所） |
| Statistical Conversion of Silent Articulation into Audible Speech using Full-Covariance HMM | 2016 | §（Perceptual evaluation） |
| A Real-Time Silent Speech System for Voice Restoration after Total Laryngectomy | 2018 | §（一致箇所） |
| doi-10.1038-s41586-019-1119-1 |  | Results「Synthesis performance」、Methods「Intelligibility Assessment」 |
| doi-10.1038-s41586-025-09127-3 |  | Methods（一致箇所） |
| A neural architecture for imagined and overt speech motor dynamics | 2026 | Methods（一致箇所） |
| Towards reconstructing intelligible speech from the human auditory cortex | 2019 | 主観評価の図の説明 |
| Online speech synthesis using a chronically implanted brain-computer interface in an individual with ALS | 2024 | 台帳 |
| doi-10.1109-taslp-2017-2757263 | 2017 | Abstract |
| Generating Intelligible Audio Speech from Visual Speech | 2017 | §VI |
| End-to-End Mandarin Speech Reconstruction Based on Ultrasound Tongue Images Using Deep Learning | 2025 | 台帳 |
| Real-Time Control of an Articulatory-Based Speech Synthesizer for Brain Computer Interfaces | 2016 | Abstract |
| Digital Voicing of Silent Speech |  | §1 |
| An Improved Model for Voicing Silent Speech |  | §（一致箇所） |
| Robust Articulatory Speech Synthesis using Deep Neural Networks for BCI Applications | 2014 | 台帳 |
| Reconstructing intelligible audio speech from visual speech features | 2015 | §1 |
| Generating Natural, Intelligible Speech From Brain Activity in Motor, Premotor, and Inferior Frontal Cortices | 2019 | Methods「Listening Tests」 |
| Robust articulatory speech synthesis using deep neural networks for BCI applications | 2014 | 台帳 |
| Reconstructing intelligible audio speech from visual speech features | 2015 | §1 |
| Reconstructing intelligible audio speech from visual speech features | 2015 | §1 |
| isca-taguchi18_interspeech |  | 台帳 |
| Hush-Hush Speak: Speech Reconstruction Using Silent Videos | 2019 | §（Human evaluation） |
| Hush-Hush Speak: Speech Reconstruction Using Silent Videos |  | §（Human evaluation） |
| A neural architecture for imagined and overt speech motor dynamics | 2026 | Methods（一致箇所） |
| A neural architecture for imagined and overt speech motor dynamics | 2026 | Methods（一致箇所） |
| Decoding and synthesizing tonal language speech from brain activity | 2023 | 台帳 |
| Online speech synthesis using a chronically implanted brain-computer interface in an individual with ALS | 2024 | 台帳 |
| Noninvasive Speech Restoration After Total Laryngectomy Using Surface Electromyography: Pilot Study | 2026 | Methods（一致箇所） |
| Noninvasive Speech Restoration After Total Laryngectomy Using Surface Electromyography: Pilot Study | 2026 | Methods（一致箇所） |
| Noninvasive Speech Restoration After Total Laryngectomy Using Surface Electromyography: Pilot Study | 2026 | Methods（一致箇所） |
| Noninvasive Speech Restoration After Total Laryngectomy Using Surface Electromyography: Pilot Study | 2025 | Methods（一致箇所） |
| High-Resolution, Non-Invasive Imaging of Upper Vocal Tract Articulators Compatible | 2016 | Abstract（一致箇所） |
| Generating Natural, Intelligible Speech From Brain Activity in Motor, Premotor, and Inferior Frontal Cortices | 2019 | Methods「Listening Tests」 |
| Generating Natural, Intelligible Speech From Brain Activity in Motor, Premotor, and Inferior Frontal Cortices | 2019 | Methods「Listening Tests」 |
| Sequence-to-Sequence Voice Reconstruction for Silent Speech in a Tonal Language | 2022 | 台帳 |
| Sequence-to-Sequence Voice Reconstruction for Silent Speech in a Tonal Language | 2022 | 台帳 |
