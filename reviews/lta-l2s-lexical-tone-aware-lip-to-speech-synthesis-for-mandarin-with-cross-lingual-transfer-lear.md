# LTA-L2S: Lexical Tone-Aware Lip-to-Speech Synthesis for Mandarin with Cross-Lingual Transfer Learning

Kang Yang, Yifan Liang, Fangkun Liu, Zhenping Xie, Chengshi Zheng  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2509.25670)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text+summary

LTA-L2S synthesizes Mandarin speech from lip video using English pretraining and tone-aware generation, reducing character and tone errors versus baselines, but CER remains 61.2%.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Existing video (CN-CVS), 96x96 mouth crops |
| Task | Lip-to-speech synthesis |
| Vocabulary | Mandarin continuous speech; size not stated |
| Speaker | Speaker-independent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | CER 61.2%, TER 40.9% on CN-CVS unseen-speaker split |

**Limitations.** High character error rate, ASR-based evaluation, unclear speaker-embedding source, and no truly silent or real-time evaluation.

## 日本語レビュー

### 要点

中国語の口元映像からの音声合成で、英語の事前学習と声調を意識した生成を組み合わせ、比較対象より文字・声調の誤りを減らした。ただし文字誤り率61.2%が残り、実際の無声発話や実時間会話の成功を示したわけではない。

### レビュー

LTA-L2Sの価値は、口元映像からの音声合成で、音が自然に聞こえることと、言葉・声調が正しく伝わることを分けて扱う点にある。英語で事前学習した視覚表現を中国語へ調整し、音声認識で調整済みの音声単位から声の高さの変化を生成する。CN-CVSの未知話者用分割では、比較対象Intelligibleの文字誤り率74.9%・声調誤り率50.3%に対し、61.2%・40.9%を報告する。中国語母語話者15人の5段階評定でも、自然さ3.95、内容の伝わりやすさ3.88、話者類似度3.89と、掲載された比較方式を上回る。ただし文字誤り率はなお高く、声調指標も認識文字列を変換して求めており、音響的な声調を直接正しく復元した割合ではない。後処理を外すとDNSMOSは3.200から2.942へ下がる一方、文字誤り率は61.2%から61.0%、声調誤り率は40.9%から40.7%へわずかに改善するため、全構成要素が全指標を改善するとはいえない。音声映像データでの合成評価を、声を出さずに口を動かした利用者の意思伝達へそのまま拡張することもできない。参照音声の条件、分割の詳細、統計的な確かさ、実時間性は未確認であり、声調を持つ言語向けの設計を比較する研究として読むのが適切である。

### この論文の価値

音質の高さだけでは中国語の内容や声調の正確さを保証できないことを、比較表と構成要素の検証から区別できる点。SSIでは、声調を持つ言語への転移と生成表現を検討する材料になる。

### それまでの到達点

口元映像から音声を合成する研究には、事前学習した視覚表現、音声単位の教師情報、生成モデルを使う方式が既にある。本論文は、中国語では見た目が似た音の区別と意味を変える声調が特に難しいと位置付ける。

### 何が変わったか

英語1759時間で事前学習したAV-HuBERT Baseの重みを中国語へ転用し、音声認識で調整済みのwav2vec 2.0第9層から得る2000種類の音声単位を用いる。音声単位と視覚・話者表現からF0を生成し、粗い音響特徴を二段階目の生成モデルで精細化する。

### 分野での位置づけ

映像を用いたSSIに関連する中国語の音声再構成研究。脳波や筋電からの解読ではなく、収録済みの発話映像から音声を合成する評価である。

### 実用上の意味

声調を持つ言語で、事前学習の転用・音声単位・声の高さの生成を選ぶ際の比較材料になる。高い文字誤りが残るため、正確な日常会話や臨床の意思伝達を保証する結果ではない。

### 前進した軸

中国語の文字・声調の誤り率、英語の事前学習重みの再利用、音声単位と声の高さの分離、音質と内容誤りを分けた評価。

### 未解決の軸

高く残る内容誤り、声調を直接聴取した場合の正確さ、参照音声の条件、無声調音への移行、分割・語彙重複の詳細、推論時間、臨床での意思伝達。

### 後退・限定した軸

Table 1のSTOI-NetとDNSMOSはLTBSより低い。Table 3では後処理を付けるとDNSMOSは改善するが、文字誤り率は61.0%から61.2%、声調誤り率は40.7%から40.9%へわずかに悪化する。推論計算量の比較は不明。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | 中国語の口元映像から音声を合成するlip-to-speech。語の識別と声調を含む内容の伝わりやすさ、自然さ、話者の声の類似度を評価する。 |
| 入力 | 口元映像。学習には音声映像の対データを使い、音声合成には話者表現も条件として与える。 |
| センサ | CN-CVSの音声映像を利用。dlibで68顔特徴点を検出し、位置合わせ後に口元中心の96×96画素を白黒化する。収録カメラ機種や撮影距離は本論文では不明。 |
| 装着部位 | lip; face |
| 出力 | 合成音声。文字列の入力装置や命令分類器ではない。 |
| 語彙の種類 | CN-CVSの中国語の連続発話。固定少数命令の分類ではないが、未知語を含む自由会話への性能は未確認。 |
| 語彙数 | 語彙数は不明。2000は離散音声単位のクラスタ数であり、単語数ではない。 |
| 指標と結果 | Table 1：LTA-L2SはSTOI-Net 0.907、DNSMOS 3.200、CER 61.2%、TER 40.9%、SECS 0.828。IntelligibleはCER 74.9%、TER 50.3%。LTBSはSTOI-Net 0.909、DNSMOS 3.291でLTA-L2Sを上回るが、CER 87.3%、TER 56.4%。Table 2：自然さ3.95±0.34、内容の伝わりやすさ3.88±0.30、話者類似度3.89±0.42。真の音声は自然さ4.48±0.16、内容の伝わりやすさ4.54±0.15。±の定義は不明。 |
| 評価方法 | CN-CVSの未知話者用分割を使うオフライン音声合成比較。客観指標はSTOI-Net、DNSMOS、文字誤り率CER、声調誤り率TER、話者埋め込みのコサイン類似度SECS。中国語母語話者15人がモデル当たり30標本を5段階で自然さ・内容の伝わりやすさ・話者類似度について評定する。部品除去と初期重み・音声単位の置換比較も行う。 |

### 限界

- **技術：** 視覚的に似た音や見えにくい声調を、学習済み表現と生成モデルで補うため、自然に聞こえても内容の誤りは残る。事前学習モデル、音声単位の教師情報、話者表現、音声合成器に依存する。話者表現を何の音声から得るかが明確でないため、完全に映像だけで声を再現できるとは断定しない。
- **評価：** CERとTERはFunASRによる転記とg2pM処理に依存し、テストの正解文字ラベルもFunASRで再作成している。機械認識による評価の影響を切り分けた検証はない。MOSは中国語母語話者15人・モデル当たり30標本だが、±の定義、標本選択・提示順、反復学習数、検定は不明。
- **実運用：** 実験は既存の音声映像データを使う。声を出さずに口を動かした専用収録、発声障害のある利用者、移動・遮蔽・撮影角度変化、端末内処理、実時間対話の評価は報告されない。話者表現に用いる参照音声の取得条件も不明。
- **このレビューの範囲：** 固定対象arXiv v1全5ページの本文・図1・表1–4・参考文献に基づく。図1と表1–4はPDF描画でも照合。書誌情報は保存済みコンテキストを維持する。論文の報告値と設計の評価であり、デモ試聴・実装実行・原データによる独立再現ではない。

### 根拠

- 著者は中国語の口元映像からの合成に対し、英語からの転移学習、声調情報を含む音声単位に条件付けたF0生成、二段階の音響特徴精細化を提案する。（p.1 Abstract, Introduction, Section 2; p.2 Figure 1）
- 視覚符号化器はAV-HuBERT Baseに基づき、英語1759時間で事前学習した重みで初期化して中国語の第一段階学習で調整する。（p.2 Section 2.1 Visual Encoder）
- 音声単位は音声認識で調整済みのwav2vec 2.0第9層の特徴をk-meansで2000群に分けて得る。4層のConformerで予測し、平滑化係数0.1の交差エントロピーで学習する。2000は単語数ではない。（p.2 Section 2.2 and Eq.1; p.3 Section 3.2）
- F0と有声・無声ラベルをYAAPTで抽出し、視覚特徴・音声単位・話者埋め込みからF0を生成する。話者埋め込みは事前学習した話者照合モデル由来だが、参照音声の出所・長さ・テスト音声との独立性は本文に明記されない。（pp.2–3 Section 2.3, Figure 1, Eqs.2–3 and footnote 2）
- 第一段階の音声単位・有声無声・F0・メル音響特徴の損失重みは0.1/1/1/1。第二段階では第一段階を固定してフローマッチングによる後処理だけを学習する。音声合成器はCN-CVSで事前学習したHiFi-GANを使用する。（p.3 Sections 2.4–2.5, Eq.5 and Section 3.2）
- CN-CVS speech subsetの規模は273.4時間・2529話者。未知話者用の元分割に従い、中国語以外を除き、テストの文字ラベルをFunASRで再転記する。除外後の分割別規模・IDや語彙非重複の確認は本論文では示されない。（p.3 Section 3.1 Datasets）
- 68顔特徴点で位置合わせし口元の96×96画素を白黒化する。音声は16 kHz、80メル帯域、窓40 ms・間隔10 ms。2台のNVIDIA 4090で各段階100 epochを学習し、F0と後処理の推論にはそれぞれNFE 24を用いる。実測の生成遅延は記載されない。（p.3 Section 3.2 Implementation Details）
- CERとTERはFunASRの転記とg2pM処理から計算すると記載される。TERは音響波形の声調を直接聴取・判定した正解率ではなく、機械転記に依存する。テストの正解文字ラベルもFunASRで再作成している。（p.3 Sections 3.1 and 3.4 Evaluation Metrics）
- Table 1でLTA-L2SのCERは61.2%、TERは40.9%。Intelligibleの74.9%・50.3%より低い。LTA-L2SのSTOI-Net 0.907、DNSMOS 3.200はLTBSの0.909・3.291を下回る。SECSは0.828で掲載された合成方式中で最も高い。（p.4 Table 1 and Section 4.1; PDF table visually checked）
- 中国語母語話者15人がモデル当たり30標本を5段階評価。LTA-L2Sは自然さ3.95±0.34、内容の伝わりやすさ3.88±0.30、話者類似度3.89±0.42。真の音声は自然さ4.48±0.16、内容の伝わりやすさ4.54±0.15。±の定義は本文にない。（p.3 Section 3.4; p.4 Table 2 and Section 4.2; PDF table visually checked）
- 後処理を除くとDNSMOSは3.200から2.942へ下がるが、CERは61.2%から61.0%、TERは40.9%から40.7%へわずかに改善する。後処理による音質向上と内容誤りの改善は同一ではない。（p.4 Table 3, w/o postnet row, Section 4.3; PDF table visually checked）
- F0生成のフローマッチングをL1損失へ替えるw/o f0 cfmではCER 63.2%、TER 42.0%。ピッチ予測全体を外すw/o pitchではCER 61.5%、TER 40.9%、STOI-Net 0.877、DNSMOS 2.731。ピッチの導入が全指標を一様に改善するとはいえない。（p.4 Table 3 and Section 4.3; PDF table visually checked）
- 音声単位の教師情報を外すとCER 69.2%、TER 46.2%、SECS 0.660。英語の事前学習で初期化しないRandom Init.ではCER 74.6%、TER 49.1%。これらの比較は音声単位と転移学習の有用性を支持するが、誤りのない合成を意味しない。（p.4 Tables 3–4 and Section 4.3; PDF tables visually checked）
- 音声単位を事前学習HuBERT第9層の2000群へ置換するとCER 64.4%、TER 42.8%となり、提案方式の61.2%・40.9%より悪化する。一方DNSMOS 3.206とSECS 0.831は提案方式の3.200と0.828を上回る。（p.4 Table 4, HuBERT Unit row, Section 4.3; PDF table visually checked）
- 本文は改善をsignificantと表現するが、検定、学習反復数、MOSの±の定義は示さない。4.3節の初期化比較の説明にCER/PERとある一方、Table 4の列はCER/TERであり、独立したPERの測定値は提示されない。（pp.3–4 Sections 3.3–3.4 and 4.1–4.3, Tables 1–4）
- 評価はCN-CVSの音声映像を使う音声合成である。実際に声を出さず調音した専用データ、発声障害のある利用者、移動時や端末内・実時間対話の評価は本文にない。中国語の別方言・アクセントへの拡張は今後の課題とされる。（pp.1–4 Sections 1–5, especially Section 3.1 and Section 5 Conclusion）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
