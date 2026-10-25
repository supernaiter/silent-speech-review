# Toward Practical BCI: A Real-time Wireless Imagined Speech EEG Decoding System

Ji-Ha Park, Heon-Gyu Kwak, Gi-Hwan Shin, Yoo-In Jeon, Sun-Min Park, Ji-Yeon Hwang, Seong-Whan Lee  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2511.07936)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

Implements a wired and wireless EEG prototype classifying four imagined commands with per-user calibration; accuracy is 62.00% wired and 46.67% wireless (chance 25%) in three healthy subjects.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | BrainAmp 32-ch wired EEG; Emotiv EPOC X wireless |
| Task | Imagined command classification |
| Vocabulary | 4 commands (help me, tell me, bored, tired) |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Not stated |
| Key result | 62.00% wired, 46.67% wireless accuracy, 4 classes, chance 25% |

**Limitations.** Only three subjects, unclear train/test splits, no rest-state false-trigger or identification results, and no mobile or patient testing.

## 日本語レビュー

### 要点

想像した4命令を脳波で分類する試作系を有線・無線で実装し、正解率は62.00%と46.67%。本人の較正が必要で、3人・分割不明の評価から日常利用や自由な文章の解読まで実証したとはいえない。

### レビュー

本研究は、頭の中で発話した4種類の命令を脳波から分類し、利用者登録から本人向けの追加学習、連続取得、推論結果の画面表示までをつなぐ試作システムである。自由な文章や音声を復元する研究ではない。健康な韓国人3人を対象とし、Table Iの4クラス正解率は有線62.00±3.47%、無線46.67±0.72%、マクロ平均F1はそれぞれ0.62±0.04と0.46±0.01だった。4択の理論上の偶然水準25%は上回るものの、±の定義、データ分割、表の測定が連続利用にどう対応するかは明確でなく、統計的な優位性まで確認できない。声を出さない入力を扱うSSIとしての価値は、有線の実験系だけでなく無線ヘッドセットを含む操作手順を具体化した点にある。ただし本人の安静脳波30秒と各クラス10試行の較正を使うため、装着するだけで誰でも使える仕組みではない。0.1秒ごとのデータ取得と2秒窓による推論は記載されるが、0.1秒で命令を認識できるという遅延実測ではない。利用者識別の精度、休止状態の判定方法、学習とテストの独立性、眼球や筋肉の信号の影響も十分に検証されていない。無線機器で動くことは日常環境で頑健に使えることとは別であり、患者、歩行、長時間利用での意思伝達の実用性は今後の課題である。

### この論文の価値

非侵襲の想像発話SSIを、個人の登録・較正・連続取得・結果表示という実際の利用手順までつなげた実装例。無線化した際の性能と、分類値だけでは足りない運用上の検証課題を示す。

### それまでの到達点

論文が述べる従来の問題は、高密度有線機器と個人別較正への依存により、想像発話の分類を日常利用へ移しにくいことである。既存手法との同条件の定量比較は本論文にない。

### 何が変わったか

分類精度だけでなく、有線・無線入力を選べる操作画面、30秒の安静登録、クラスごと10試行の本人較正、連続表示をまとめた点が差分。未知利用者に較正なしで使える手法ではない。

### 分野での位置づけ

神経信号を使う非侵襲SSIの固定命令分類とシステム統合の研究。語彙制限のない発話認識や音声合成とは分けて評価すべき試作例。

### 実用上の意味

無線入力を含む本人登録・較正・連続推論の手順を設計する参考になる。利用者識別や休止時の誤作動を含む実運用の性能は未提示で、完成した会話支援機器とは位置付けない。

### 前進した軸

有線だけでなく無線機器を入力に使う一体の操作画面、本人の登録と追加学習、連続計測から命令表示までの接続を具体化。

### 未解決の軸

学習・検証・テストの分割、本人識別の精度、無線側の取得条件、較正前後の差、実際の処理遅延、休止状態の誤検出、患者・歩行・日をまたぐ利用、コードとデータの再現性。

### 後退・限定した軸

Table Iの報告正解率は有線62.00%から無線46.67%へ低下し、平均値の差は15.33ポイント。機器以外の条件を統制した因果比較とは確認できない。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | 内的に発話したhelp me、tell me、bored、tiredの4命令を脳波から分類。本人の識別と個人別モデルの選択を含む試作アプリケーション。 |
| 入力 | 非侵襲の頭皮EEG。有線取得は30 EEGと2 EOGの計32チャンネルと記載され、モデル説明もEEGとEOGの入力に言及する。無線側は12電極を列挙する。 |
| センサ | 有線はBrain ProductsのBrainAmp、BrainVision、250 Hz、30頭皮EEGとTP9・TP10をEOGとする計32チャンネル、Fpz接地・鼻梁参照と記載。60 Hzノッチのみ、振幅を10^4倍。無線はEmotiv EPOC Xを用い、F7/F3/FC5/T7/P7/O1/O2/P8/T8/FC6/F4/F8の12電極を記載。無線の標本化周波数と同一前処理の適用範囲は不明。 |
| 装着部位 | 頭皮の脳波。主取得条件では眼電図として扱う2チャンネルも記述される。 |
| 出力 | 4種類の命令ラベルと画面表示。文章や音声波形は生成しない。利用者識別も構成要素として持つが精度報告はない。 |
| 語彙の種類 | 固定された閉じた命令集合。実装のrest状態をTable Iの追加の5番目の分類対象とは扱えない。 |
| 語彙数 | 4命令：C1 help me、C2 tell me、C3 bored、C4 tired。文章中の単語認識ではない。 |
| 指標と結果 | Table Iの著者報告値：有線の4クラス正解率62.00±3.47%、マクロ平均F1 0.62±0.04、平均適合率0.63±0.05、平均再現率0.62±0.03。無線は46.67±0.72%、0.46±0.01、0.51±0.04、0.47±0.00。クラス別F1は有線C1–C4が0.68、0.64、0.47、0.67、無線が0.44、0.43、0.44、0.51。4クラスの理論上の偶然水準は25%。±の定義・集約単位は不明で、独立再現値ではない。 |
| 評価方法 | 健康な3人を対象に、有線・無線機器で想像発話4クラスの適合率、再現率、F1、正解率を報告。連続取得と推論表示の実装も提示するが、表の評価と連続利用の関係、独立したテストの手順は不明。 |

### 限界

- **技術：** モデル規模、最適化条件、事前学習データと分割の詳細がなく再現に不足。有線のEOG入力に言及する一方、眼電・筋電の寄与を切り分ける比較はない。実装にはrest状態が登場するが、4命令との判定方法や休止データは説明されない。
- **評価：** 学習・検証・テストの分割方法と各件数、Table Iが連続利用のどの試行を評価したか、±の定義と集約単位が不明。比較分類器、構成除去、統計検定、識別精度、較正前後の比較はない。
- **実運用：** 無線ヘッドセットを使うが、図2はコンピューターの前で使う構成。携帯機器内だけでの処理、通信断、電池寿命、歩行、屋外、長時間使用の試験は報告されない。患者での評価もない。
- **このレビューの範囲：** arXiv v1全4ページ、図1・2、Table Iと参考文献を確認。図表はPDFでも目視照合した。著者コード・データの実行や独立再現は行っていない。文献から詳細条件や性能を補完していない。

### 根拠

- 著者は、有線・無線の双方で利用者識別、個人別モデル、連続転送と4命令分類をつなぐ実用志向の想像発話BCIを提案する。（p.1 Abstract and Introduction; p.2 Fig.1 and caption）
- 健康な韓国人3人を対象とし、help me、tell me、bored、tiredの内的発話を収録する。1セッション800試行、各クラス200試行、各2秒と記載されるが、参加者別・機器別の全体試行数は明記されない。（p.2 II-A.1 Experimental setup）
- 有線取得はBrainAmpとBrainVisionを用い、250 Hz、30 EEGとTP9・TP10をEOGとする計32チャンネル、Fpz接地、鼻梁参照と記載する。60 Hzノッチ以外の追加フィルタは使わず、振幅を10^4倍する。（p.2 II-A.2 EEG recording and preprocessing）
- 無線取得にはEmotiv EPOC Xを用い、F7、F3、FC5、T7、P7、O1、O2、P8、T8、FC6、F4、F8の12電極を列挙する。無線側の標本化周波数は記載されない。（p.2 II-A.2, wireless device paragraph）
- モデル説明はEEGとEOGを1次元畳み込みで特徴化し、時間方向、空間方向の順に2段のTransformerへ渡し、相対位置情報を用いる。モデル規模、事前学習データ、最適化設定の詳細は記載されない。（p.2 II-B Decoding Model; Fig.1）
- 利用者識別に安静脳波30秒を収録し、各クラス10試行の較正データで事前学習モデルを追加学習する。本人のデータが不要な仕組みではない。（p.3 II-C.3 System implementation; p.2 Fig.1 caption）
- 実装はLSLで連続転送し、0.1秒ごとに取得した脳波を蓄え、2秒の移動窓で推論する。rest以外の命令を画面表示するが、0.1秒は命令認識の実測遅延ではない。（p.2 Fig.1; p.3 II-C.3 System implementation, both columns; Fig.2）
- Table Iの有線4クラス正解率は62.00±3.47%、マクロ平均F1は0.62±0.04、平均適合率0.63±0.05、平均再現率0.62±0.03。無線はそれぞれ46.67±0.72%、0.46±0.01、0.51±0.04、0.47±0.00である。±の定義は明記されない。（p.3 Table I and III-A; p.4 III-B）
- Table Iのクラス別F1の平均値は有線C1–C4が0.68、0.64、0.47、0.67、無線が0.44、0.43、0.44、0.51。本文は4クラスの理論上の偶然水準を25%とする。（p.3 Table I and III-A Performance on Wired EEG Device）
- 学習・検証・テストの分割と件数、表の評価と連続運用との関係、±の集約単位が不明である。比較分類器、構成除去、統計検定、較正前後の性能比較も提示されない。（pp.2–3 II Materials and Methods; pp.3–4 III Results and Discussion; Table I）
- 本人識別は機能として説明されるが識別精度は報告されない。rest状態の判定方法・学習データ、休止時の誤検出率、処理遅延の測定値も示されない。（pp.2–3 II-C Personalized BCI Application; p.3 Table I; pp.3–4 III）
- 眼電図も入力に含むとの説明と60 Hzノッチのみの前処理記述がある一方、眼球や筋肉の信号の寄与を切り分ける比較はなく、脳波のみが成績を支えるとは確定できない。（p.2 II-A.2 and II-B; pp.3–4 III and Table I）
- 著者は無線の低成績を信号対雑音比や不安定性で説明するが、それらを計測して原因を切り分けた結果はない。機器別条件の詳細も不足し、無線化だけが低下原因だとは断定できない。（p.4 III-B Performance on Wireless EEG Device; p.2 II-A.2）
- 研究の具体的な価値は、有線・無線入力、登録、本人較正、連続転送と表示をまとめた試作系にある。対象は固定4命令であり、自由文、患者、歩行、屋外、長時間利用での信頼性を測った報告ではない。（p.2 Fig.1 and II-A; p.3 Fig.2 and II-C; p.4 IV Conclusions）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
