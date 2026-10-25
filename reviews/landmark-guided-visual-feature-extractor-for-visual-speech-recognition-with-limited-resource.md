# Landmark Guided Visual Feature Extractor for Visual Speech Recognition with Limited Resource

Lei Yang, Junshan Jin, Mingyuan Zhang, Yi He, Bofan Chen, Shilin Wang  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2508.07233)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text+summary

Combines 20 lip landmarks with image features for visual word recognition; with one-third training data on LRW-ID, accuracy improves from 85.75% to 86.65%, at larger model size.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Existing broadcast video (lip images and landmarks) |
| Task | Isolated word lip reading |
| Vocabulary | 500 English words |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 86.65% accuracy LRW-ID low-resource (1/3 data) vs DC-TCN 85.75% |

**Limitations.** Small gain with more parameters and FLOPs, no seeds or significance tests, and no silent articulation, free sentences or real-time evaluation.

## 日本語レビュー

### 要点

唇の20点の動きを画像と組み合わせ、学習データ3分の1の500語読唇で正解率を85.75%から86.65%へ改善。ただしモデルは大型化し、実際の無声調音・自由文・実時間動作は未検証。

### レビュー

本稿の価値は、音声を入力しない読唇で、画像だけでなく唇の20個の特徴点の動きも再利用する具体的な設計にある。座標、点間距離、画像特徴の類似度から3種類のグラフを作り、画像特徴と段階的に融合する。LRW-IDでは学習データを3分の1にしても、既存DC-TCNの全標本正解率85.75%に対して86.65%、話者平均83.41%に対して84.25%を報告する。全学習データでは91.15%対91.48%で、改善は小さく、反復・誤差範囲がないため有意差とは言えない。20人の未学習話者を含む評価は重要だが、検証とテストに使うadaptation setの詳細な分け方は不明である。さらに、距離グラフだけでは低資源条件の改善がなく、モデルは52.55Mから62.48Mパラメータへ増える。人工雑音で正解率を保つ結果も、あらゆる乱れに最も強いという意味ではない。音声を使わず放送映像の単語を識別することと、実際に声を出さず動かした口から自由文を読むことは別であり、後者は検証されていない。低資源という名称を少数例学習や低消費電力と読み替えず、500語の範囲内での改善と実装負担の交換条件を示す研究として評価する。

### この論文の価値

既存の顔処理で得る特徴点を、位置だけでなく画像動態と結び付けて使う設計と、その小幅な認識改善・計算負担を比較できること。

### それまでの到達点

本文が比較する既存系は3D畳み込み・ResNet18による画像特徴、DC-TCNによる時間方向の集約、顔の特徴点を併用するLipFormerやGusLipなど。特徴点利用自体を新発明とは扱わない。

### 何が変わったか

既存の画像読唇系に20個の唇特徴点から作る3種のグラフと融合を追加し、同じ500語課題で比較。新しいセンサーや自由文デコーダではない。

### 分野での位置づけ

映像型SSIに関連する単語読唇の構成改良。真の無声調音や臨床インターフェースの直接実証ではない。

### 実用上の意味

大規模な追加の発話データに依存せず、既存の顔特徴点を利用して固定語彙読唇を改善する候補。端末に使える軽量性や省電力は別途検証が必要。

### 前進した軸

LRW-IDの低資源条件で全標本正解率85.75%から86.65%、話者ごとの平均正解率83.41%から84.25%。全学習データでは91.15%から91.48%、89.44%から89.61%。画像雑音・座標ずれを加えた条件も評価。

### 未解決の軸

無声調音そのものへの転用、未知語・自由文、他言語、実環境の照明・姿勢変化、特徴点検出失敗、端末上の遅延・電力、統計的な再現性。

### 後退・限定した軸

表2のモデル規模は52.55Mから62.48Mパラメータ、演算量表記は10.69Gから11.09G FLOPSへ増加。DAGだけの追加では低資源正解率85.75%から85.74%で改善しない。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | speech-recognition：固定英単語の映像分類。 |
| 入力 | video：唇画像と、同じ画像から事前学習済み顔モデルが抽出した特徴点。独立センサーの追加ではない。 |
| センサ | 既存の放送映像。撮影カメラ機種は不明。計算実験はRTX2080Ti（11GB）で実施。 |
| 装着部位 | lip; face |
| 出力 | labels：英語500語のうち1語の分類結果。音声合成や自由文出力ではない。 |
| 語彙の種類 | closed-set isolated-word classification |
| 語彙数 | 500 English word classes |
| 指標と結果 | 表3 LRW-ID低資源 Acc/mAcc：提案0.8665/0.8425、DC-TCN0.8575/0.8341。高資源：提案0.9148/0.8961、DC-TCN0.9115/0.8944。表4 LRW Acc：提案0.9169、DC-TCN（MixUpなし）0.9100。表2：62.48Mパラメータ、11.09G FLOPS（基準52.55M、10.69G）。表5の画像雑音＋座標ずれ下は提案の低資源0.8580/0.8333、高資源0.9075/0.8875。 |
| 評価方法 | オフラインの固定500語分類。LRW-IDの全学習データ／3分の1学習データ、融合比較、順次グラフ追加、ガウス画像雑音・小さな座標ずれ、LRW全体の比較。Accは標本全体、mAccは話者ごとの正解率の平均。 |

### 限界

- **技術：** 事前学習済み顔位置合わせ・特徴点検出に依存。画像雑音と小さな座標ずれ以外の欠損・遮蔽・大きな姿勢変化は未検証。順次追加比較だけでは全てのグラフの独立効果を分離できない。
- **評価：** 低資源は1つの3分の1条件。乱数種、反復回数、分散・信頼区間・有意差検定、LRW-IDの検証とテストの厳密な割当、学習率・epoch数、雑音強度と座標ずれの分布は不明。表4のDC-TCNはMixUpなし。比較表を全読唇研究に対する最高性能とはしない。
- **実運用：** 録画映像の単語分類実験。カメラ機種、端末実装、消費電力、全処理遅延、連続会話の区切り検出は報告されない。著者もグラフ計算の負担が端末展開を妨げる可能性を述べる。
- **このレビューの範囲：** 英語500語のLRW/LRW-ID録画映像。文単位、未知単語、実際の無声調音、他言語、患者、歩行中の専用評価はない。

### 根拠

- 唇の20点を座標LCG、距離DAG、画像特徴の類似度SAGで表し、画像特徴と融合する。顔特徴点自体や画像読唇は既存であり、新センサーではない。（pp.2–5, Sections 1–3.3; Figures 1–3）
- 3D畳み込みとResNet18に、時間・グラフ畳み込みおよび双方向GRUを組み合わせ、DC-TCNと動画単位の分類器で単語を出力する。双方向GRUは過去・未来情報を参照する。（pp.3–5, Sections 3.1–3.4; Figures 2–3）
- LRWはBBC放送からの1000人超、500語。1動画29フレーム・1.16秒、学習488766、検証25000、テスト25000と記載。実際の無声調音を新規収録した実験ではない。（p.6, Section 4.1 Dataset, LRW description）
- LRW-IDは500英単語で、各900動画以上の20話者のadaptation setを検証とテスト、それ以外を学習に使用。低資源は各学習話者から均等に3分の1を選び、全テストデータで評価。本文は話者適応の追加学習なしと述べるが、厳密な検証・テストIDは示さない。（p.6, Sections 4.1–4.2; p.7, Section 4.5）
- 96×96切り出し、水平反転と時間マスク、MixUpなし、512次元特徴、AdamW、ラベル平滑化0.1。RTX2080Ti（11GB）で学習は低資源4日、高資源9日。少ない発話学習データでも顔の事前学習モデルを使用する。（p.6, Section 4.2; pp.2–3, pretrained face detector/align network）
- Accは全動画標本の正解率、mAccは各話者の正解率を平均した指標であり、クラス平均や単語誤り率ではない。（p.6, Section 4.2, Equations (6)–(7)）
- 表3のLRW-ID低資源条件は提案Acc0.8665/mAcc0.8425、DC-TCN0.8575/0.8341。高資源条件は提案0.9148/0.8961、DC-TCN0.9115/0.8944。（p.7, Table 3 Performance comparisons on LRW-ID dataset）
- 表2は低資源でbaseline0.8575、DAG追加0.8574、DAG+LCG0.8628、全3グラフ0.8665。高資源は順に0.9115、0.9138、0.9140、0.9148。DAG単独の低資源改善はない。（p.7, Table 2 Ablation study on LRW-ID Result）
- 表2の全モデルは62.48Mパラメータ、11.09G FLOPS、基準は52.55M、10.69G。著者も行列計算の負担が端末展開を妨げ得ると認める。前処理の特徴点再利用は全モデルの追加計算ゼロを意味しない。（p.7, Table 2; p.8, Section 4.7 Discussion）
- 表1ではDAGとSAGを連結・チャネル削減後にLCGへ加算する融合がAcc0.8665/mAcc0.8425。3枝の重み付き和は0.8545/0.8290。融合方法によって結果が異なる。（p.6, Table 1 and Section 4.3 Lip Dynamics Fusion）
- 表4のLRW全体比較は提案Acc0.9169、DC-TCN0.9100で、後者の脚注はMixUpなし。固定単語分類の成績であり自由文の誤り率ではない。（p.7, Table 4 and footnote a; Section 4.5）
- 表5の画像雑音と座標ずれを共に加えた提案法は低資源Acc/mAcc0.8580/0.8333、高資源0.9075/0.8875。DC-TCNの同条件は0.8479/0.8237、0.8992/0.8796。（p.7, Table 5 The Robustness Test）
- 表5で雑音・ずれを共に加えた高資源Accは提案0.9148→0.9075、GusLip0.8984→0.8943。提案の最終正解率は高いが低下幅はGusLipより大きく、全ての頑健性指標で最良とは言えない。雑音強度・座標ずれの具体的分布は不明。（p.7, Table 5; Section 4.6 Robustness Analysis）
- 全9ページでは反復回数・乱数種・信頼区間・有意差検定やLRW-IDの検証／テストの厳密な割当が報告されない。小幅な正解率差を統計的有意差として扱わない。（pp.6–8, Sections 4.1–4.7; Tables 1–5; full-text reporting audit）
- 対象は放送映像由来の英語500語であり、未知語、自由文、実際に声を出さない調音、患者、歩行、他言語、端末遅延・電力の専用評価はない。音声を入力しないことと無声調音で成功したことは区別が必要。（pp.6–8, Sections 4.1–5; Tables 1–5）
- 本文はコードを公開予定としているが、本レビューでは公開状況やコード・データによる独立再現は確認していない。書誌情報は固定コンテキストのarXiv記録を保持し、未確定のDOIを補完しない。（p.6, Section 4.2 code availability statement; p.1 publication block）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
