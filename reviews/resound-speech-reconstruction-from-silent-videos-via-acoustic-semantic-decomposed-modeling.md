# RESOUND: Speech Reconstruction from Silent Videos via Acoustic-Semantic Decomposed Modeling

Long-Khanh Pham, Thanh V. T. Tran, Minh-Tan Pham, Van Nguyen  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2505.22024)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text+summary

RESOUND synthesizes speech from silent video plus a 0.5 s reference audio by separating content and prosody paths; naturalness improves, but LRS2 WER (28.55%) is worse than LipVoicer (17.04%).

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Existing video (LRS2/LRS3) plus reference audio |
| Task | Speech reconstruction from silent video |
| Vocabulary | English continuous speech; LRS3 over 50,000 words |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | WER 20.06% (LRS3), 28.55% (LRS2); UTMOS 3.002 (LRS3) |

**Limitations.** Needs reference audio from ground truth, higher WER than baseline on LRS2, no variance or significance tests, and no truly silent speech evaluated.

## 日本語レビュー

### 要点

映像と0.5秒の参照音声から、発話内容と抑揚を分けて音声を合成する。自然さは改善するが、LRS2では比較手法より単語誤りが多く、映像だけ・真の無声発話での有効性は未確認。

### レビュー

RESOUNDの価値は、口の映像から内容を推定する処理と、参照音声から声質や抑揚を補う処理を分け、最後に音声へまとめる設計を具体化した点にある。映像特徴と読唇で得た文字を音素へ変換した特徴を組み合わせ、音響特徴と離散音声単位を共同予測する。音声の自然さだけでなく、内容の誤り、声の類似度、抑揚、計算時間を併記した評価も有用である。ただし『無音映像から』という表現を『映像しか使わない』と読んではいけない。方法は参照音声を入力とし、実装説明では正解音声から0.5秒を無作為に切り出す。試験時に独立した別発話へ置き換えても同じ成績になるかは確認できない。LRS3の単語誤り率は20.06%でLipVoicerの21.04%より低く、自然さの自動予測値は3.002、話者類似度は0.777である。一方、LRS2では単語誤り率28.55%でLipVoicerの17.04%より悪く、すべての条件で内容精度が最良とはいえない。LRS3の30人による聴取評価では自然さ3.86±0.13、理解しやすさ3.86±0.15、話者類似度3.57±0.14を報告する。これは5段階の評点と95%信頼区間であって認識正解率ではない。各手法20音声の評価であり、自然音声の評点にはなお差がある。読唇と特徴融合を一緒に外すと単語誤り率が27.49%へ、音響経路を外すと自然さの自動予測値が2.176へ悪化する。構成の有用性は支持されるが、同時に外した要素の個別効果や内容・抑揚の完全な独立性までは証明しない。計算時間比0.063はLipVoicerより小さいものの、比較表の最速手法ではなく、測定機器や前後処理の範囲も不明である。声を出さずに伝える入力手段への関連性は高いが、評価は通常発声の映像音声データであり、本当に声を出さない口の動き、本人の参照音声がない場合、発話障害者の会話支援、実時間の対話性能は未確認である。

### この論文の価値

内容を当てることと自然な声を作ることを別に扱い、二つの経路と共同出力を組み合わせた実装、および内容・音質・速度が必ずしも同時に最良にならない比較結果。

### それまでの到達点

既存の読唇音声合成は、映像特徴、音声由来の学習表現、文字予測、拡散モデルなどを使う。読唇による内容補助や離散音声単位は既存であり、音源・フィルタに着想した分解も音声合成分野に先例がある。

### 何が変わったか

参照音声から得る声質と抑揚情報、映像から得る内容特徴、読唇文字から変換した音素を、注意機構と二つの生成経路で組み合わせる。最終音声合成にスペクトログラムだけでなく予測音声単位も与える。

### 分野での位置づけ

参照音声で声質・抑揚を補う読唇音声合成。通常発声の映像から音声を再構成する研究であり、音声を一切用意できない利用者での無声入力実証とは区別する。

### 実用上の意味

音のない映像に、参照する声の特徴を保った音声を付ける研究の設計例。現状の誤り率と参照条件から、そのまま日常会話や失声者の音声復元へ使えるとはいえない。

### 前進した軸

LRS3で比較した映像音声合成手法より自然さ、話者類似度、単語誤り率、抑揚誤差、音響指標が良い。LRS2でも単語誤り率以外の掲載品質指標が改善する。LRS3の聴取評価でも自然さ・理解しやすさ・類似度の平均が比較手法を上回る。

### 未解決の軸

独立した別発話の参照音声を使った場合の成績、参照音声を用意できない人への対応、真の無声構音、未知話者での分割条件、別言語、計算環境と処理範囲を揃えた遅延、特徴分離そのものの検証。

### 後退・限定した軸

LRS2の単語誤り率は28.55%で、LipVoicerの17.04%より悪い。計算時間比は0.063でLipVoicerの14.117より小さいが、Intelligible L2Sの0.041より大きく、最速ではない。元音声や正解音響特徴を入れた合成器の品質には届かない。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | speech-reconstruction |
| 入力 | 口元映像に加え、声質と抑揚のための音声参照。実装では正解音声の0.5秒区間を参照とする。学習には対応音声、音響特徴、音声単位、音高、エネルギーを使う。映像のみの推論として分類しない。 |
| センサ | 既存LRS2/LRS3映像を利用。MediaPipeで口元96×96画素を切り出し、88×88画素の無作為切り出しを適用する。新規カメラ装置・接触センサは提案せず、音声は16 kHzへ変換する。 |
| 装着部位 | lip;face |
| 出力 | speech-audio |
| 語彙の種類 | 英語の連続発話からの音声合成。固定単語分類ではないが、無制限の語彙への一般化を実証したわけではない。 |
| 語彙数 | LRS3全体の語彙は5万語超との記載。試験語彙数と学習にない語の数は不明であり、5万語分類器ではない。 |
| 指標と結果 | 表1のLRS3: UTMOS 3.002、SECS 0.777、WER 20.06%、MAERMSE 0.025、MAEF0 49.52、ESTOI 0.423、MCD-DTW-SL 8.71。LRS2: 2.382、0.730、28.55%、0.025、51.79、0.420、10.56。LipVoicerのWERはLRS3 21.04%、LRS2 17.04%。計算時間比RTFはRESOUND 0.063、Intelligible L2S 0.041、LipVoicer 14.117。表2のLRS3聴取評価は自然さ3.86±0.13、理解しやすさ3.86±0.15、類似度3.57±0.14（5段階、95%信頼区間）。表3で読唇と融合を除くとWER 27.49%、音響経路を除くとUTMOS 2.176、WER 21.93%、MAEF0 69.219。著者報告値であり独立再現ではない。 |
| 評価方法 | LRS2/LRS3のオフライン音声合成、自然さの自動予測値、話者埋め込み類似度、自動音声認識による単語誤り率、抑揚誤差、音響指標、計算時間比、LRS3の聴取評価と構成要素の除去実験。 |

### 限界

- **技術：** 読唇の誤りが音素経路へ入り得る。音源・フィルタに着想した潜在表現は実際の声帯振動・声道共鳴を直接計測したものではなく、除去実験だけで完全な分離は保証されない。読唇と融合を同時除去するため個別効果は分からず、音声単位追加単独の対照もない。LRS2の差を雑音とする説明は著者の解釈である。
- **評価：** 客観成績の試行間ばらつきや有意差検定は示されない。聴取評価は30人・各手法20音声・95%信頼区間を報告するが、評価者属性、割付、区間計算の単位や対応関係は十分に説明されない。参照音声の抽出元と試験時の扱い、比較手法間の入力条件の統一、速度測定機器と前後処理の範囲、話者重複の監査が不十分。
- **実運用：** 口元の映像、参照音声、複数の事前学習モデルと音声合成器が必要。携帯機器、歩行、マスクや遮蔽、連続会話、発話障害者での操作を評価していない。速度表だけでは計測から音声再生までの応答時間を決められない。
- **このレビューの範囲：** arXiv:2505.22024v1の全5ページ、図1、表1–3に基づく。LRS2/LRS3の英語映像音声再構成とLRS3の聴取・除去実験に限る。著者実験の独立再現や配布物の検証は行っていない。

### 根拠

- 著者は抑揚と発話内容を別経路で扱い、メルスペクトログラムと離散音声単位を共同利用する音声合成を提案する。音源・フィルタ理論に着想したL2Sでの初例という主張は著者の位置付けであり、このレビューによる網羅的先行研究確認ではない。（p.1 Abstract and Introduction; pp.2–3 Sections 2.1–2.3; Figure 1）
- 推論構成は口元映像だけでなく音声参照を受け取り、声質符号器と話者参照符号器へ渡す。実装説明では正解音声から0.5秒を無作為抽出する。試験時に独立した別発話参照を用いた成績は示されない。（p.2 Figure 1 and Section 2.1; p.3 Section 3.3, audio prompt paragraph）
- AVHuBERTで映像特徴を、読唇モデルと文字から音素への変換で音素特徴を得る。映像を問い合わせ、音素をキーと値にする注意処理とConformerで融合する。（pp.2–3 Sections 2.2.1–2.2.3; Figure 1）
- 二経路の励振表現と共鳴表現を加算して音響特徴を作り、別に音声単位を予測して多入力音声合成器へ渡す。これは学習された表現であって声帯や声道を直接計測した値ではない。（p.3 Section 2.3; p.2 Figure 1）
- LRS2は英語のBBC映像220時間超で、事前学習・学習区分と試験区分を利用する。LRS3は英語のTED/TEDx映像438時間、5万語超で、学習131,000発話、試験約1,300発話を用いる。新たに収録した真の無声構音群ではない。（p.3 Section 3.1 Datasets）
- 口元96×96画素から88×88画素の無作為切り出しを行い、反転・消去・時間マスクを適用する。音声は16 kHzへ変換し、HuBERT-BASEの200群を音声単位とする。LRS3で事前学習済みのAVHuBERTをLRS3では固定しLRS2では追加学習する。（p.3 Section 3.3 Implementation Details）
- 80 epoch、各データセット40,000 step、初期学習率0.001で学習する。メル・音高・エネルギーのL1損失と音声単位の交差エントロピーの重みは100・0.1・0.1・0.01、ラベル平滑化は0.1。Conformerは8層、各生成経路は3 FFTブロック、隠れ次元512・注意8ヘッド。（p.3 Sections 2.4 and 3.3; Equation 3）
- 自然さはUTMOSという自動予測値、話者類似度はResemblyzer、単語誤り率はAuto-AVSRで評価する。ほかに音高・エネルギー誤差、ESTOI、MCD-DTW-SL、生成音声長に対する計算時間比を測る。これらの自動指標と聴取評点は別の評価である。（p.3 Section 3.2 Evaluation Metrics; p.4 Table 2）
- 表1のLRS3のRESOUNDはUTMOS 3.002、SECS 0.777、WER 20.06%、MAERMSE 0.025、MAEF0 49.52、ESTOI 0.423、MCD-DTW-SL 8.71。LipVoicerのWERは21.04%。元音声はUTMOS 3.519、WER 0.99%であり、モデル成績は元音声の上限に達していない。（p.4 Table 1, LRS3-TED block）
- 表1のLRS2のRESOUNDはUTMOS 2.382、SECS 0.730、WER 28.55%、MAERMSE 0.025、MAEF0 51.79、ESTOI 0.420、MCD-DTW-SL 10.56。LipVoicerのWERは17.04%であり、RESOUNDが全データ・全指標で最良という解釈は誤り。（p.4 Table 1, LRS2-BBC block; Section 4.1）
- 計算時間比RTFはRESOUND 0.063、LipVoicer 14.117、Intelligible L2S 0.041。RESOUNDはLipVoicerより速いが表中最速ではない。測定機器や前後処理の包含範囲が記載されず、対話全体の応答時間は確定できない。（p.4 Table 1, Efficiency column; Section 4.1 speed paragraph; p.3 Sections 3.2–3.3）
- LRS3の聴取評価は30人が各手法20音声を0.5刻みの5段階で評定し、95%信頼区間を示す。これは正誤を採点した認識率ではない。割付や区間算出単位の詳しい説明はない。（p.4 Section 4.1 MOS paragraph and Table 2）
- LRS3聴取評価のRESOUNDは自然さ3.86±0.13、理解しやすさ3.86±0.15、類似度3.57±0.14。元音声は順に4.80±0.05、4.76±0.07、4.92±0.04である。掲載した比較手法の平均を上回るが、元音声との差は残る。（p.4 Table 2; Section 4.1 specifies 95% confidence intervals）
- 読唇モデルと意味参照注意を同時に除くと、LRS3のWERは20.06%から27.49%、UTMOSは3.002から2.840になる。同時除去なので、読唇と融合それぞれの独立の効果を分離できない。（p.4 Table 3, w/o L2T & SRA row; Section 4.2）
- 音響経路の除去ではUTMOS 2.176、WER 21.93%、SECS 0.713、MAEF0 69.219、ESTOI 0.385。エネルギー予測器の除去ではUTMOS 2.698、WER 20.22%、SECS 0.744、MAEF0 51.22、ESTOI 0.400。構成要素の有用性を支持するが、内容と抑揚の完全な独立性を直接証明する試験ではない。（p.4 Table 3 and Section 4.2, acoustic branch and energy predictor paragraphs）
- LRS2でLipVoicerより単語誤り率が悪い理由を著者は雑音と拡散モデルの関係で説明するが、雑音量を操作・統一した対照実験は掲載されない。原因が実証されたとは扱わない。（p.4 Section 4.1, LRS2 discrepancy paragraph; Tables 1 and 3）
- 二つの英語データとオフライン合成評価に限り、無声構音、発話障害者の対話、歩行・携帯機器、語彙を分離した試験はない。話者分割の詳細と独立参照音声の条件も不明。多言語・多様な訛りへの適用は今後の課題とされる。（pp.3–4 Sections 3.1–3.3 and 4.1–4.2; p.4 Section 5 Conclusion）
- 表1のVocoder行は正解メルスペクトログラムと正解音声単位を両方与えた条件である。この行を映像入力だけの手法として比較しない。LRS3の同条件はSECS 0.890で、RESOUNDの0.777より高い。（p.4 Table 1, Vocoder dagger rows and footnote）
- 既存の読唇、音声単位、音源・フィルタに着想した合成を組み合わせ、内容・抑揚の経路と共同出力を構成した点が主な貢献。本文の先行研究整理からは各部品自体を新規とは扱えない。（p.1 Introduction and cited prior approaches; pp.2–3 Sections 2.1–2.4）
- 本文はサンプルとコードのデモページを案内するが、その記載だけでは重み・前処理・評価実装の完全性や独立再現を確認できない。客観指標の試行間ばらつきも掲載されない。（p.1 Introduction final paragraph and footnote 1; p.3 Section 3.3; p.4 Tables 1–3）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
