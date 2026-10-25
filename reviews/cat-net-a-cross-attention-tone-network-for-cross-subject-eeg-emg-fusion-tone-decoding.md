# CAT-Net: A Cross-Attention Tone Network for Cross-Subject EEG-EMG Fusion Tone Decoding

Yifan Zhuang, Calvin Huang, Zepeng Yu, Yongjie Zou, Jiawei Ju  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2511.10935)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text+summary

CAT-Net fuses EEG and surface EMG with cross-attention to classify Mandarin lexical tones in silent articulation, reporting 85.10% leave-one-subject-out accuracy over 4 tones.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 64-channel NeuSen W EEG plus 5-site face/neck sEMG |
| Task | Mandarin tone classification |
| Vocabulary | 4 tone classes (120 characters as stimuli) |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 85.10% leave-one-subject-out (silent, 4 classes); 88.08% 5-fold |

**Limitations.** Tone classification, not sentence recognition; 10 subjects, metric naming inconsistencies, and unclear split and channel-selection procedures.

## 日本語レビュー

### 要点

脳波と筋電を組み合わせ、声を出さずに発音した中国語の四声を分類する研究。学習に含まない人で平均85.10%を報告するが、文章認識ではなく、指標名や分割・チャネル選択手順には確認が必要。

### レビュー

CAT-Netの価値は、脳波と筋電を互いに参照させる構成を、中国語の四声という限定した課題で比較したことにある。健康な母語話者10人が、各声調30文字を画面の指示に従って有声・無声で発音する。モデルは20脳波チャネルと5筋電チャネルを使い、無声の5分割評価で88.08%、被験者を1人ずつ学習から除外する評価で平均85.10%を報告した。後者の比較対象GATは80.54%である。ただし88.08%は本文では正解率、表では平均適合率と呼ばれ、同じものとして厳密に比較できるかは確認が必要。交差注意を外すとTable 6の適合率は77.63%へ低下する一方、被験者識別器を外した被験者除外の平均は84.69%で、識別器の追加効果は0.41ポイントにとどまる。無声の被験者別成績は53.33–95.00%と幅があり、誰でも同じ性能になるわけではない。無声発話インターフェースとしては、声調情報を非音響信号から補う部品の研究であり、脳波だけによる読心、文字の識別、自由文の認識、音声復元の実証ではない。64チャネルで収録してから20を選んでおり、最初から簡単な装置だけで同じ性能になる保証もない。分割とチャネル選択の独立性、条件別試行数、前処理区間とモデル入力長の対応、患者・別日のデータ、実時間動作は未確認である。

### この論文の価値

四声情報を脳波と筋電で補完できるかを検討する、限定課題の比較材料。注意による融合と被験者差への対策を分けて評価できる点が有用。

### それまでの到達点

脳波の分類器、表面筋電による無声発話認識、両者の結合は既存の研究方向。異なる人で成績が落ちることと、複数信号を単純に連結するだけでは相互関係を捉えにくいことが課題。

### 何が変わったか

四声という限定課題に対して、脳波と筋電を別々に時空間符号化し、互いの特徴を参照する構成を比較評価した。自由な文章の認識や音声合成へ拡張したものではない。

### 分野での位置づけ

非音響信号を用いる無声発話インターフェースに直接関連する、声調分類の研究。内容認識や音声生成の完成した通信システムとは区別する。

### 実用上の意味

声調を持つ言語の無声発話入力を設計する際に、複数信号の融合と被験者別の失敗を検討する材料になる。実際の意思伝達速度や利用者利益は不明。

### 前進した軸

同一データでの比較において四声の平均分類成績を改善し、9人で学習して残る1人を評価する条件でも改善を報告。64チャネルで収録した脳波から20チャネルを選ぶ場合の成績も提示。

### 未解決の軸

未学習の文字・語、別の日や別の施設、発話障害のある利用者、連続した会話、装着のしやすさ、計算遅延、チャネル選択を訓練データだけで行ったかは未確認。

### 後退・限定した軸

被験者を分けると無声の報告平均は88.08%から85.10%へ低下。有声も87.83%から83.27%へ低下する。無声のS9ではDeepConvNet 95.63%に対し94.79%であり、全員で最高ではない。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | 有声・無声の発音動作から中国語の四声を分類し、未学習の被験者での成績を調べる。 |
| 入力 | 脳波（EEG）と表面筋電（sEMG）の同期信号。無声条件も実際に発音動作をする課題であり、運動を伴わない想像発話と同一視しない。 |
| センサ | 64チャネルNeuSen W無線脳波装置で収録し、主な解析では20チャネルを選択。表面筋電は右頬筋、右頸部僧帽筋、左頬筋、左頸部僧帽筋、オトガイ筋と記載された5部位。1000 Hzで取得し500 Hzへ間引く。 |
| 装着部位 | 頭皮の脳波と、左右の頬・頸部、顎先の表面筋電。筋の名称は本文およびFigure B2の表記に従う。 |
| 出力 | 中国語の4声調のクラスラベル。文字列や音声波形の出力ではない。 |
| 語彙の種類 | 固定された四声ラベル。文字提示は入力課題の手掛かりで、自由語彙の認識ではない。 |
| 語彙数 | 出力は4クラス。刺激は各声調30文字、計120文字であり、120文字を識別した成績ではない。 |
| 指標と結果 | 無声5分割のTable 3はAverage 88.08%、Kappa 0.8415、DeepConvNet 86.56%。本文はaccuracy、表はAverage Precisionと表記。無声の被験者除外はTable 4で85.10%、GAT 80.54%、DeepConvNet 80.48%。有声はTable C3で87.83%、Kappa 0.8377、Table C2の被験者除外は83.27%。Table 5で被験者識別器なし84.69%、あり85.10%。Table 6で交差注意なしの適合率77.63%、全構成88.08%。全て著者報告値で独立再現ではない。 |
| 評価方法 | 有声・無声それぞれのオフライン4クラス分類。5分割交差検証、9人で訓練し1人をテストする被験者除外評価、チャネル数比較、構成要素の除去比較、特徴寄与の解析。 |

### 限界

- **技術：** 脳波の筋電由来成分を除去する前処理を記載するが、脳由来と筋由来の寄与を因果的に分離した証明ではない。特徴寄与のSHAP解析は分類器の説明であり、神経機構の証明ではない。前処理は刺激前後2秒、モデル入力は500点と記されるが対応手順は不明。
- **評価：** 10人の単一収録集による5分割評価と被験者を1人ずつ除外する評価。5分割の分割単位、同じ文字の反復を分離したか、チャネル選択や前処理が各訓練分割内で完結したかは不明。主要結果の信頼区間や有意差検定の手順は示されない。表と本文の指標・一部記述に不整合がある。
- **実運用：** 画面に提示された文字を所定の時間に発音する実験。頭皮・顔・頸部への電極装着と前処理が必要であり、日常の自発発話、移動中、患者での運用は示されない。
- **このレビューの範囲：** 12ページのarXiv v1本文・付録、主要な図表を確認。書誌情報は固定コンテキストを保持した。公開コードの実行、元データの取得と再解析、著者への照会は行っていない。

### 根拠

- 健康な中国語母語話者10人（24–35歳）が有声・無声の両条件を実施。各声調30文字を4回ずつ提示し、出力は4声調である。120文字の識別や自由文認識の評価ではない。（PDF pp.3–5, Signal Inputs; Experiment Setup / Data Collection; Figure 2）
- 要旨は脳波・筋電それぞれ4800試行と記し、Data Collectionは480試行を両条件で完了と記す。条件別および除外後の総試行数は明確に対応付けられていない。（PDF pp.1,4–5, Abstract; Data Collection; Figure 2）
- 64チャネルNeuSen W脳波装置と5部位の表面筋電を1000 Hzで同期収録し、500 Hzへ間引く。主な解析は選択した20脳波チャネルと5筋電チャネルを用いる。（PDF pp.4–5, Data Collection; Preprocessing; Channel Selection; p.9 Table A1 / Figures B1–B2）
- CAT-Netは信号別の空間・時間特徴抽出、双方向交差注意、四声分類、勾配反転を用いた被験者識別を組み合わせる。新しい計測原理ではなく既存手法の統合である。（PDF pp.3–4, Figure 1; Methods; Algorithm 1; Cross-Modal Attention Fusion）
- Table 1の平均は脳波5チャネル86.92%、10チャネル87.02%、20チャネル88.08%、全チャネル88.45%。20チャネルが絶対的な最小数と示されたわけではない。（PDF p.5, Table 1; Channel Selection）
- 無声5分割のTable 3でCAT-NetのAverageは88.08%、Kappaは0.8415、DeepConvNetのAverageは86.56%。表はAverage Precision、本文はaccuracyと呼ぶため指標の定義に注意が必要。（PDF p.6, Table 3 caption and K-Fold Cross Validation）
- 被験者除外評価は1人をテストに取り置き9人で学習する。筋電を用いない比較アルゴリズムにも脳波と筋電を連結して入力すると記載されており、比較を脳波単独対融合と読み替えない。（PDF p.6, Baseline Comparisons / K-Fold Cross Validation; Cross-Subject Calibration）
- 無声の被験者除外評価はCAT-Net平均85.10%、GAT 80.54%、DeepConvNet 80.48%。CAT-NetはS1で53.33%、S7で95.00%、S9では94.79%でDeepConvNet 95.63%を下回る。（PDF p.7, Table 4）
- 被験者識別器なしの無声被験者除外平均は84.69%、ありは85.10%で差は0.41ポイント。S1は48.96%から53.33%へ上がるが、一部の被験者は下がる。（PDF p.7, Table 5; Generalization Across Subjects）
- 5分割のTable 6では全構成の適合率88.08%に対し、交差注意なし77.63%、BiLSTMなし78.42%。方向別の融合除去条件は76.60%と76.46%で、純粋な脳波単独・筋電単独比較とは明示されていない。（PDF p.7, Table 6; Cross-Attention Mechanism）
- 有声のTable C3はAverage 87.83%、Kappa 0.8377。Table C2の被験者除外平均は83.27%。S10はCAT-Net 89.17%よりGAT 90.00%が高く、付録の全10人で最高という記述は表に一致しない。（PDF pp.11–12, Tables C2–C3; Cross Subject Results）
- 5分割の分割単位、同じ文字の反復を分けたか、チャネル選択を各訓練分割だけで実施したかは本文に明記されない。主要結果について信頼区間や有意差検定の具体的手順は示されない。（PDF pp.5–7, Channel Selection; Baseline Comparisons; Tables 1–6; p.9 Table A1）
- 前処理は刺激前後2秒の区間を500 Hzで扱う一方、Signal InputsはT=500と記す。変換方法は不明。式(4)の中心損失はAlgorithm 1とTable A1に同様には記載されず、実装の対応確認が必要。（PDF pp.3–5, Signal Inputs; Algorithm 1; Equation 4; Preprocessing; p.9 Table A1）
- Table 2のCAT-NetのMacro AvgはF1=88.08、Recall=88.06だがTable 6はRecall=88.08、F1=88.06。Table 1と3の20チャネルTone 3も87.29と87.27で異なり、報告値を勝手に補正しない。（PDF pp.5–7, Tables 1–3 and 6）
- SHAP解析は多くの条件で筋電の特徴寄与が大きく、無声Tone 2では脳波の寄与が大きいと報告する。これはモデルの寄与解析であり、脳・筋の因果関係を確定する実験ではない。（PDF p.12, Appendix D; Figure D1）
- 提示文字を有声または無声で発音する健康者のオフライン四声分類を評価する。患者の意思伝達、自由文の復元、実時間遅延、歩行、日常装着の検証は示されず、より多様なデータと実環境への展開は今後の課題とされる。（PDF pp.4–7, Experiment Setup; Figure 2; Baseline Comparisons; Conclusion）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
