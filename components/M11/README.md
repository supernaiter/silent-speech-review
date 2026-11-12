# M11 Eval reference

この部品について調べた話題と、確認済みの論文。各話題の表は分野全体（wiki の台帳と全文）を検索し、候補を原典で読んで採否を決めたもの。

## in-the-wild-sentence-benchmark

- 採否表：[`in-the-wild-sentence-benchmark.csv`](in-the-wild-sentence-benchmark.csv)（確認済み 5、読んだ候補 49、未読 293、wiki 730b0b4）
- 採る条件：放送・YouTube・TED など撮影条件を統制しない映像から、自動で書き起こしを付けた文・句単位の音声映像データを作り、評価用のテスト分割を定めた研究を含める（分割の方法を記録する）。境界：単語単位（LRW、LRW-1000）は除く。既存データの再利用だけ、訓練用の追加データだけ（テスト分割を定めない）は除く。同一研究の別版は1件。
- 使ったレビュー：[Deep Audio-Visual Speech Recognition](../../reviews/deep-audio-visual-speech-recognition/)、[Lip Reading Sentences in the Wild](../../reviews/lip-reading-sentences-in-the-wild/)

| 論文 | 年 | 根拠の位置 |
| --- | --- | --- |
| Lip Reading Sentences in the Wild | 2017 | §4, Table 2 |
| Large-Scale Visual Speech Recognition |  | §5 |
| LRS3-TED: a large-scale dataset for visual speech recognition | 2018 | §2 |
| Personalized Lip Reading: Adapting to Your Unique Lip Movements with Vision and Language |  | §1 |
| ViCocktail: Automated Multi-Modal Data Collection for Vietnamese Audio-Visual Speech Recognition | 2025 | §2 |
