# NeuroTTT: Bridging Pretraining-Downstream Task Misalignment in EEG Foundation Models via Test-Time Training

Suli Wang, Yangshen Deng, Zhenghua Bao, Xinyu Zhan, Yiqun Duan  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2509.26301)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

NeuroTTT adds task-specific self-supervision and test-time training to EEG foundation models, raising within-subject 5-class imagined speech balanced accuracy for CBraMod to 58.98%.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 64-channel scalp EEG (existing dataset) |
| Task | Closed-set imagined speech classification |
| Vocabulary | 5 phrases (hello, help me, stop, thank you, yes) |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Balanced accuracy 58.98% (CBraMod, TTT with Tent), within-subject, 5 classes |

**Limitations.** Within-subject only for imagined speech, needs labeled user data, and participant counts, splits and statistical tests are unclear.

## 日本語レビュー

### 要点

課題別の補助学習とテスト時適応により、本人内の5種類の想像発話分類を改善する研究。CBraModのBalanced Accuracyは58.98%だが、未知被験者への想像発話適用は偶然水準で、自由文や較正不要のSSIではない。

### レビュー

NeuroTTTの価値は、音を出さずに話そうとする際の脳波を扱う既存モデルへ、目的の課題に合う学習を追加する設計にある。まず、正解ラベル付きの分類と同時に、脳波から除いた周波数帯域や与えた振幅倍率を当てる補助課題を学ばせる。次に、テスト入力だけで補助課題を解くTTTか、予測の不確かさを下げるTentを用いてモデルを調整する。これは追加の補助ラベルを人が付けなくてよい仕組みであり、主課題の教師あり学習が不要という意味ではない。想像発話はhello、help me、stop、thank you、yesの5種類を、同じ人の学習・評価データで分類する条件である。Table 1のCBraModでは、クラス別の正答率を平均するBalanced Accuracyが浅い多層分類器の47.33%からTent構成の58.98%へ上がる。Cohenのκは0.4872、重み付きF1は0.5895。一方、SSLによるテスト時適応でも58.87%であり、Tentとの差は小さい。Figure 3と本文は、想像発話でのテスト時適応の上積みは小さく、補助課題による微調整の寄与と分けて読む必要があることを示す。さらに付録は、別の人に移す想像発話評価ではCBraModとLaBraMがともに偶然水準だったため被験者内結果を掲載したと明記する。ストレス・運動想像の被験者間改善を、想像発話の未知利用者への成功へ読み替えてはいけない。参加者数や±の定義、反復・分割の詳細、Tentの更新回数などは不明で、100対150 epochの学習量差も比較上の注意点である。固定表現の脳波分類を改善する研究として有用だが、自由な文章の読取り、音声合成、較正不要の会話機器、臨床的有用性、実時間性を実証した研究ではない。

### この論文の価値

脳波基盤モデルの大きさだけでなく、下流課題に合った補助学習とテスト時適応を分けて評価する設計を示す点。SSIでは改善した本人内分類と失敗した被験者間移行を併記できることが重要である。

### それまでの到達点

CBraModとLaBraMの事前学習済み脳波表現に対する教師あり微調整、線形／浅い多層分類器、LoRA、SHOTが比較対象。TTTとTentは既存のテスト時適応法である。

### 何が変わったか

事前学習済み表現をそのまま分類に使うだけでなく、目的の課題に合わせた変換予測を教師あり学習へ加え、さらに正解ラベルのないテスト入力で更新する。新しい語彙や計測装置の実現ではない。

### 分野での位置づけ

非侵襲の脳波を使うSSIに関連するモデル適応研究。想像発話の固定表現分類が対象であり、発声筋の動きから文章を復元する装着型SSIと同じ条件の比較ではない。

### 実用上の意味

既存基盤モデルを固定表現の脳波分類へ転用する際に、課題別補助学習と適応の選択を検討する材料になる。未知利用者や日常会話の性能を保証するものではない。

### 前進した軸

既存脳波基盤モデルの課題への適合。想像発話の被験者内5クラス分類で、課題別補助学習とテスト時適応を組み合わせた構成が掲載比較法を上回る。

### 未解決の軸

想像発話の未知被験者への汎化、未知語・自由文、別日・別装置、患者での意思伝達、実時間処理、安定した継続適応、統計的な有意差。

### 後退・限定した軸

想像発話の自己教師あり微調整は教師ありのみの100 epochに対し150 epoch。テスト時の勾配計算も追加される。実測処理時間・電力がないため、精度と負担の交換関係は定量化できない。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | 脳波基盤モデルの下流課題適応。SSI対象は5種類の想像発話の分類で、ストレス検出と運動想像分類も補助的に評価する。 |
| 入力 | EEG（頭皮脳波） |
| センサ | Appendix B.1の想像発話は64チャンネル、256 Hzで取得。B.2は再参照・帯域通過処理後に200 Hzへ変換し1秒区間へ分割すると記す。取得機種、具体的なフィルタ設定や窓の集約詳細は本論文では不明。 |
| 装着部位 | 頭皮・脳 |
| 出力 | 想像した固定表現のクラスラベル。文章や音声波形を生成しない。 |
| 語彙の種類 | 固定された単語・短い表現。自由語彙や自由文ではない。 |
| 語彙数 | 5クラス：hello、help me、stop、thank you、yes。 |
| 指標と結果 | Table 1：CBraModのBalanced AccuracyはLinear 0.3976±0.0113、Shallow MLP 0.4733±0.0098、LoRA 0.3531±0.0158、SHOT 0.5008±0.0010、TTT with SSL 0.5887±0.0170、TTT with Tent 0.5898±0.0148。Tentのκ 0.4872±0.0185、Weighted F1 0.5895±0.0142。LaBraMのTentはBalanced Accuracy 0.2742±0.0047、κ 0.0928±0.0159、Weighted F1 0.2713±0.0126。±の定義と反復数は不明。単語誤り率や文章の認識率ではない。 |
| 評価方法 | 想像発話は同じ被験者の学習・テストを分離する被験者内評価。ストレスは被験者1–28／29–32／33–36、運動想像は1–5／6–7／8–9を学習／検証／テストに分ける被験者間評価。 |

### 限界

- **技術：** 補助課題は手設計で、その適合性に依存する。SSL適応は全パラメータを更新し、雑音を含む試行で不安定になる可能性を著者も認める。Tentは正規化層に更新を限定し、強い分布変化への適応力は限定される。実装の詳細や継続適応の安定性は未確認。
- **評価：** 被験者内の既定分割と被験者平均は記載されるが、想像発話の参加者数、試行数、分割ID、反復数、±の定義、有意差検定は本文・付録だけでは不明。学習epoch数が100対150で異なる。Figure 3の棒を精密な数値へ変換せず、Table 1の報告値を採用した。
- **実運用：** 既存データ上のオフライン分類。想像発話は本人のラベル付き学習データを必要とする。テスト時にラベルを使わないことと、新規利用者の準備が不要であることは異なる。連続会話、装着負担、消費電力、端末上の遅延は未評価。
- **このレビューの範囲：** arXiv v2全17ページの本文・図表・参考文献・付録A–Cに基づく。Table 1–3とFigure 3はPDF描画でも確認。本文の報告値と設計を評価したもので、著者コード・元データの実行、統計量の再計算、臨床効果の独立確認は行っていない。

### 根拠

- NeuroTTTは主課題の教師あり損失と課題別自己教師あり損失を共同学習し、テスト時にSSL適応またはTentを使う。主課題のラベル付き学習を除く方法ではない。（pp.3–6, Section 3, Figure 2, equations (1)–(4)）
- 想像発話の補助課題は除いた周波数帯域の予測と振幅倍率の予測。帯域は0.5–8、8–30、30–70、70–100 Hz、振幅は16倍率の離散分類で説明される。神経機構を因果的に実証する実験ではなく、補助学習の設計である。（pp.13–14, Appendix A.1, Table 4）
- BCIC2020-IIIはhello、help me、stop、thank you、yesの5クラスを同じ被験者内で学習・評価し、被験者間で平均する。本論文では参加者数、試行数、個別分割IDは不明。（p.14, Appendix B.1, Imagined Speech Classification; p.8, Table 1）
- 想像発話の被験者間評価ではCBraModとLaBraMがともに偶然水準だったため、著者は被験者内結果を報告すると明記する。未知利用者への成功とはいえない。（p.14, Appendix B.1, Imagined Speech Classification）
- 想像発話データの取得条件は64チャンネル・256 Hz。前処理は再参照・帯域通過処理後200 Hz化し1秒窓に分割する。フィルタ詳細や窓の集約方法は本論文だけでは不明。（pp.14–15, Appendix B.1–B.2）
- Table 1のCBraMod Balanced AccuracyはLinear 0.3976±0.0113、Shallow MLP 0.4733±0.0098、LoRA 0.3531±0.0158、SHOT 0.5008±0.0010、TTT with SSL 0.5887±0.0170、TTT with Tent 0.5898±0.0148。いずれも被験者内5クラス分類で、単語誤り率ではない。（p.8, Table 1, CBraMod Balanced-Accuracy column）
- CBraModのTent構成はCohenのκ 0.4872±0.0185、Weighted F1 0.5895±0.0142。LaBraMのTentはBalanced Accuracy 0.2742±0.0047、κ 0.0928±0.0159、Weighted F1 0.2713±0.0126で、基盤モデルによって性能水準は大きく異なる。（p.8, Table 1, TTT with Tent row）
- 想像発話の学習は教師ありのみ100 epoch、自己教師あり補助学習を加えると150 epoch。学習量を揃えた効果比較と同一視できない。反復数、表の±の定義、有意差検定の詳細は本文・付録では不明。（p.7, Section 4.1; p.8, Tables 1–3; pp.15–16, Appendix B.4）
- Figure 3の除去比較とSection 4.3は、想像発話の被験者内条件ではテスト時適応の上積みが小さく、被験者間のストレス・運動想像では大きいと述べる。微調整の補助学習とテスト時適応の寄与を分ける必要がある。（p.9, Figure 3 and Section 4.3）
- Table 7のSSL適応はSteps 1、Batch size 1、学習率1e-5、Dropout 0.1、Adam、online False。想像発話の補助損失係数は各0.6。これは継続的なオンライン適応を実測した条件ではない。（p.16, Table 7 and Appendix B.4）
- Tentは予測エントロピーを用いて正規化層のスケール・シフトを更新し、平均・分散の更新は任意と説明する。B.4はテストバッチごとに複数更新と記すが、その回数やバッチサイズは示さない。SSL適応とTentは比較する別構成である。（p.6, Section 3.3 and equation (4); p.16, Appendix B.4）
- ストレス課題は20チャンネル・500 Hz、被験者1–28／29–32／33–36を学習／検証／テストに分ける。運動想像は22チャンネル・250 Hz、左手・右手・両足・舌の4クラスで、被験者1–5／6–7／8–9を分割する。これらの被験者間評価を想像発話の条件へ置き換えない。（pp.14–15, Appendix B.1）
- Table 2のLaBraMストレス検出AUROCはSSL適応0.8180、Tent 0.7916でTentが上回らない。Table 3の運動想像Balanced AccuracyはCBraModでSSL 0.5435、Tent 0.5674。全課題・全指標でTentが最良とはいえない。（p.8, Tables 2–3）
- Table 2のLaBraMはAccuracyという列名でSection 4.1のBalanced Accuracy説明と異なる。Table 3のLaBraM SHOTはBalanced Accuracyとκが同じ0.36310±0.02880。Figure 3の運動想像ラベルは5-classだがB.1は4クラスを列挙する。訂正値を推定せず要確認とする。（p.7, Section 4.1; p.8, Tables 2–3; p.9, Figure 3; p.15, Appendix B.1）
- Section 4.1は全設定で基盤モデル全体を学習可能と述べる一方、Appendix B.4のLoRAは元の重みを凍結すると説明する。実際の比較実装は確認が必要である。（p.7, Section 4.1; p.15, Appendix B.4, Lora Finetuning）
- 著者は手設計の補助課題への依存、雑音試行での全パラメータSSL適応の不安定性、Tentの正規化層だけでは強い変化を補い切れない可能性を限界として挙げる。（pp.16–17, Appendix C, Limitations 1–3）
- 軽量・実時間向きという説明はあるが、実測遅延、電力、日常装着、患者での会話、未知語・自由文は評価されない。本文にコード公開先の記載はあるが、このレビューではコードや原データによる独立再現を行っていない。（p.1, abstract/code link; pp.5–7, Sections 3.2–4.1; pp.14–17, Appendices B–C）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
