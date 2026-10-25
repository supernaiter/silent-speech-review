# Transfer Learning for Covert Speech Classification Using EEG Hilbert Envelope and Temporal Fine Structure

Saravanakumar Duraisamy, Mateusz Dubiel, Maurice Rekrut, Luis A. Leiva  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2502.04132)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

Pretrains on overt-speech EEG and fine-tunes with the same person's covert (imagined) speech EEG to classify 5 commands. Reports 79.82% mean accuracy, though the simple mean of the per-participant table is about 79.07%.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 64-channel wireless scalp EEG (Brain Products LiveAmp) |
| Task | Covert speech command classification |
| Vocabulary | 5 commands (LEFT, RIGHT, UP, PICK, PUSH) |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 79.82% mean accuracy (reported), 5 commands, transfer learning vs 66.94% without transfer; 15 participants |

**Limitations.** Inconsistencies in reported averages; split independence and leakage controls are unclear; no control ruling out residual muscle artifacts; no online, unseen-user or daily-environment testing.

## 日本語レビュー

### 要点

発声時の脳波で学び、本人の想像発話データを追加して5命令を分類する研究。報告精度79.82%は有望だが、参加者別の表の単純平均は約79.07%で一致しない。自由会話や想像発話データ不要の技術としては読めない。

### レビュー

この研究の価値は、声を出さない入力の学習をすべて想像発話だけで行う代わりに、本人の発声時の脳波を足場にする点にある。健康な15人が画面の合図に合わせて5命令を発声、または口や筋肉を動かさず頭の中で繰り返した既存データを使う。64チャネル脳波の振幅変化と細かな時間構造を組み合わせ、発声で学んだ双方向の系列モデルの一部を固定し、本人の想像発話記録15～30%で出力層を追加学習する。したがって、想像発話の収録が不要になる方法ではない。表IIは平均正解率を発声86.44%、想像79.82%とし、想像の個人値は58.33～90.81%で差が大きい。さらに、表IIの15人分を単純平均すると約79.07%となり、掲載平均79.82%とは一致しない。集計方法は不明であり、ここでは報告値を勝手に置き換えない。転移なしのBiLSTMは表IIIで66.94±4.65%で、掲載平均同士の差は12.88ポイントなのに、本文は20ポイントと記す。25%と30%の条件についても有意差なしという文とp<.05が併記され、同等性や有意な改善を確定できない。声を出さない入力の学習設計として参考になるが、合図付きの本人別5命令分類の結果である。未知人物、未知語、自然な文章、声を出せない患者、別日・再装着、実時間の操作、負担軽減の実測は未確認である。

### この論文の価値

声を出す本人の記録を初期学習に使い、少量の本人の想像発話記録で適応させる実験設計を示した点。高い報告精度の一般化ではなく、収録・分割と集計を明確にした追試へつながる仮説として有用。

### それまでの到達点

本文は、少数の想像単語を脳波で分類する研究、発声と想像の波形の類似を調べる研究、発声で学習した頭蓋内信号モデルを無声へ転用する研究を挙げる。今回の位置付けは、頭皮脳波による本人別の5命令分類と追加学習である。

### 何が変わったか

各2秒・64チャネルの脳波から1000×64のENVと同寸のTFSを作り、1000×128に結合する。本人の発声記録で学んだBiLSTMの再帰層を固定し、想像発話記録で出力層を追加学習する。

### 分野での位置づけ

声を出さない入力を目指す、非侵襲の本人別想像発話・閉集合命令分類。既存脳波記録の特徴表現と転移学習の方法研究で、完成した対話機器の評価ではない。

### 実用上の意味

発声できる本人が想像発話モデルを校正する場合の設計の参考になる。想像側データの必要量を比較しているが、負担削減と患者・日常環境への有効性は今後の確認が必要。

### 前進した軸

本人の発声時データを利用して想像発話の学習を始め、想像発話側の追加学習割合を15・20・25・30%で比較した。音のない入力に向けた本人別の学習設計を検討している。

### 未解決の軸

平均値の集計方法、追加学習割合と表IIの対応、独立した分割・モデル選択、本人以外への汎化、未知語・自然文、患者、別日・再装着、合図なしの発話開始、実時間の操作性、負担削減の実測。

### 後退・限定した軸

出力は合図に合わせた2秒の脳波から選ぶ5命令に限られる。実験では発声もできる本人の学習データを要し、声を出せない人へそのまま適用できる設計とは示されていない。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | command-recognition |
| 入力 | 非侵襲の頭皮脳波（EEG）。発声時の脳波で初期学習し、口や筋肉を動かさず頭の中で単語を繰り返す想像発話の脳波へ追加学習する。 |
| センサ | Brain Products Live Amp 64の無線64チャネル脳波計、500Hz、10–20配置。課題と脳波を同じWindows PCで記録し、キー入力・注視合図と同期する。 |
| 装着部位 | brain |
| 出力 | LEFT・RIGHT・UP・PICK・PUSHの5命令の分類ラベル。文章の書き起こしや音声の生成ではない。 |
| 語彙の種類 | 閉じた命令集合。任意の語や連続文を生成しない。 |
| 語彙数 | 5命令：LEFT、RIGHT、UP、PICK、PUSH。 |
| 指標と結果 | 表IIの著者報告平均正解率：発声LSTM83.99%、GRU81.46%、BiLSTM86.44%、BiGRU81.51%；転移後の想像BiLSTM79.82%。想像の個人値は58.33～90.81%。表IIの想像15値の単純平均はレビューでの計算で約79.07%となり、掲載平均と不一致。表IIIの転移なし想像BiLSTMは66.94±4.65%（標準偏差）。掲載平均同士の差79.82−66.94は12.88ポイントで、本文の20ポイントと不一致。図3は追加学習割合15・20・25・30%の比較で誤差棒は標準偏差だが、各点の厳密な値は記されない。 |
| 評価方法 | 本人別・保存済み脳波の5命令正解率。発声側はLSTM・GRU・BiLSTM・BiGRUを比較し、想像側は追加学習割合と転移なし学習を比較する。未知人物の試験やオンライン対話評価ではない。 |

### 限界

- **技術：** 1試行は1000×128の特徴で、双方向系列処理を用いる。眼球・筋活動の除去にICAを使うが、残留筋活動や視覚合図ではなく神経由来の語情報だけを分類したと確定する対照は示されない。ENV単独・TFS単独・生波形との除去比較も示されず、両特徴や波形同期の因果的な寄与は未分離。
- **評価：** 発声分類は5分割交差検証、追加学習した想像発話モデルは未使用の想像発話データ20%で試験したと説明する。収録単位で分離したか、特徴抽出・ICAと分割の関係、調整と試験の独立性、表IIの採用割合は十分に記載されない。不正な漏洩があったと断定せず、再現に必要な条件が不明と扱う。
- **実運用：** 64チャネル頭皮脳波、着座・動きを抑えた環境、画面の合図とキー操作、Windows PCを使う。保存後の解析であり、実際の脳波判定でロボットを連続操作する試験、携帯利用、日常環境の頑健性は示されない。
- **このレビューの範囲：** 健康な英語話者15人の本人別5命令、着座、画面合図付き2秒の発声・想像発話。患者、未知人物・未知語、自然会話、歩行、口の動きや筋活動の独立した監視による確認は示されない。

### 根拠

- 著者は発声で学んだ分類器を想像発話へ移し、発声86.44%・想像79.82%の精度と学習負担軽減を主張する。実際の方法には想像発話側の追加学習が含まれる。（p.1 Abstract / Introduction; p.3 Section III-C）
- 既存データは健康な右利き15人、男性11人・女性4人、平均26.8歳、全員英語に堪能。患者を含む試験ではない。（p.2 Section III-A.1 Participants）
- 5命令はLEFT・RIGHT・UP・PICK・PUSH。発声と想像が各2収録、各収録200試行、本人ごとに各条件400試行・計800試行と記載される。（p.2 Section III-A.2 Design / III-A.3 Procedure）
- スペースキーの後に準備2秒、白い十字の合図と発話2秒、休息2秒が続く。想像条件では口や筋肉を動かさず頭の中で単語を繰り返す指示。筋活動の独立した監視結果は示されない。（p.2 Section III-A.3 Procedure; Figure 1）
- 無線Live Amp 64で64チャネルを500Hz、10–20配置で収録し、課題と脳波を同じWindows PCで同期して保存後に解析する。（p.3 Section III-A.4 Data collection）
- 収録ごとに50Hz除去、0.5～80Hz帯域処理、ICAによる眼球・筋・動作雑音の除去を行い、発話の2秒区間を切り出し、直前100msの平均を引く。原稿は帯域処理にButterworthとFIRを併記しており実装詳細は不明。（p.3 Section III-B Data preprocessing and feature extraction）
- 脳波の解析信号の大きさをENV、元信号をENVで割ったものをTFSとし、1000×64の特徴2組を1000×128へ結合する。音声波形を入力特徴にする記述ではない。（p.3 Section III-B; Equations 1–3）
- 本人別モデルを発声脳波で学習し、BiLSTMの再帰層を固定して想像脳波の15・20・25・30%で全結合層を追加学習する。想像脳波なしの転用ではない。（p.3 Section III-C; p.5 Section IV-B）
- 入力1000×128、2層のBiLSTMの隠れユニット512・256、dropout0.3・0.2、5分類出力。batch32、Adam学習率0.0001、β1=0.9、β2=0.999を記載。（p.3 Section III-C; p.4 Table I）
- 発声と想像の包絡の最大相関係数としてUP0.5234・LEFT0.6412・RIGHT0.6607・PICK0.4791・PUSH0.5624を挙げる。図2は参加者10のRIGHTの例で、全員・全命令の神経機構の同一性を示すものではない。（p.4 Section IV-A; Figure 2）
- 発声分類は本人別の5分割交差検証と説明し、想像への転移評価では未使用の想像データ20%を試験に使う。収録単位の分離やモデル選択、表IIで採用した追加学習割合は十分に特定されない。（pp.4–5 Section IV-B）
- 表IIの掲載平均は発声LSTM83.99%、GRU81.46%、BiLSTM86.44%、BiGRU81.51%、転移後の想像BiLSTM79.82%。想像の個人値は最小P2の58.33%、最大P10の90.81%。（p.5 Table II）
- 表IIの想像15人分58.92,58.33,86.21,85.90,85.72,86.20,89.74,79.17,73.36,90.81,86.55,83.68,67.34,85.60,68.59をレビュー側で単純平均すると79.074666…%となり、掲載平均79.82%と一致しない。集計方法は不明で、報告値を修正して扱わない。（p.5 Table II, P1–P15 Covert BiLSTM and Avg. Accuracy; reviewer arithmetic）
- 転移なしの想像分類は表IIIでLSTM65.70±3.39%、GRU65.0±3.68%、BiLSTM66.94±4.65%、BiGRU65.83±4.72%。±は標準偏差と表記されるが、ばらつきの集計単位は十分に説明されない。（p.5 Table III and Section IV-B）
- 本文は転移なしBiLSTMが転移ありより20ポイント低いとするが、表II・IIIの掲載平均79.82%と66.94%の差は12.88ポイントである。差の計算はレビュー側によるもので、原稿の20ポイントとは一致しない。（p.5 Section IV-B; Tables II–III; reviewer arithmetic）
- 図3に関して25%と30%の追加学習条件の差を有意でないと説明しながら、p<.05とBonferroni補正付き対応t検定を併記している。正確なp値・比較の対応は不明で、有意差なしや同等性を確定できない。（p.5 Section IV-B, paragraph before Table III）
- 図3は想像側の追加学習割合15・20・25・30%を比較し、誤差棒は標準偏差。各点の厳密な値は図中に記載されず、プロットから精密な精度を補わない。（p.5 Figure 3 and caption）
- 表IVは命令数12・8・5の研究とEEG/ECoGの異なる計測をまとめる。報告精度の大小だけで同条件の最高性能とはいえない。（p.6 Table IV）
- 著者は個人間の脳波差を限界に挙げ、話者独立性を今後の課題とする。15人の本人別モデルは未知人物の試験ではなく、未知語・自然文・患者も実験対象でない。（p.6 Section IV-C; pp.2–3 Sections III-A and III-C）
- 波形の類似を転移性能の理由に挙げるが、ENV単独・TFS単独などの除去比較や独立した筋活動対照は示されない。特徴の因果的な寄与や純粋な神経由来の語情報とまでは確定できない。（p.3 Section III-B; pp.4–6 Section IV, Figures 2–3 and Tables II–IV）
- 学習負担の軽減を動機としているが、疲労・所要時間の削減を測る対照実験は示されない。保存済みの合図付き分類であり、2秒入力を総応答遅延とみなさず、実時間・携帯・手放し利用の実証としない。（p.1 Introduction; pp.2–3 Section III-A; pp.4–6 Section IV）
- p.1の脚注はデータ配布先DOI 10.5281/zenodo.14645653を示す。原稿にはICASSP 2025掲載予定の注記もあるが、本レビューの書誌情報は固定コンテキストのarXiv値を保持する。外部配布物の完全性は今回未確認。（p.1 footnote 1 and publication note）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
