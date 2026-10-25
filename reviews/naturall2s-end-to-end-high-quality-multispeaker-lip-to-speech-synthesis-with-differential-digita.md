# NaturalL2S: End-to-End High-quality Multispeaker Lip-to-Speech Synthesis with Differential Digital Signal Processing

Yifan Liang, Fangkun Liu, Andong Li, Xiaodong Li, Chengshi Zheng  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2502.12002)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text+summary

NaturalL2S synthesizes speech from mouth video without a reference audio of the speaker, using differentiable DSP. It improves quality and naturalness, but WER is worse than the comparison (30.4% vs 27.7% on LRS3).

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Existing video (88x88 grayscale mouth crop); no new sensor |
| Task | Speech synthesis from lip video |
| Vocabulary | Open vocabulary English continuous speech (size not stated) |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | WER 30.4% on LRS3 and 36.5% on LRS2 vs 27.7%/33.5% for Lip2Speech Unit |

**Limitations.** Lip motion does not uniquely determine phonemes, so content errors remain; relies on large pretrained video models; true silent speech, real-time conversation and mobile use are untested.

## 日本語レビュー

### 要点

本人の参照音声なしで口元映像から音声を合成し、音質と自然さを改善する。一方、単語誤り率は比較手法より悪く、真の無声発話や実時間会話での有効性は未確認。

### レビュー

NaturalL2Sは、口元映像から内容と声の高さを推定し、学習可能な信号処理で調波と雑音を合成してから神経音声合成器へ渡す研究である。本人の参照音声を推論時に要求せず、粗いメルスペクトログラムを直接音へ変換する際の品質低下に対処する。ただし映像特徴抽出器AV-HuBERTは固定した事前学習モデルであり、学習には対応する音声、音声単位、正解F0を使う。全体が音声なしで学習する方式ではない。通常発声を収録したLRS2とLRS3で、15人の聴取評価は音質4.40±0.26、自然さ4.34±0.30、理解しやすさ4.39±0.32、声の似方3.98±0.33を報告する。いずれも5段階の平均±標準偏差で、正解率ではない。一方、単語誤り率は36.5%と30.4%で、Lip2Speech Unitの33.5%と27.7%より悪い。自然に聞こえることと、言葉が正しいことは別である。自動話者類似度は両データで0.63だが、DiffV2Sとの関係はLRS2で上回りLRS3で同率で、本文の説明はこの順序が逆になっている。構成除去実験は設計全体の有用性を支持するが、一体学習を外す条件では複数の部品と合成器の学習データも変わるため、単独要因の効果を断定できない。声を出さずに伝える技術への意味は、参照音声なしで口元から聞きやすい音を作る具体的な手段を示した点にある。真に声を出さない発話、患者、語彙を分離した未知語、未知話者、日常会話の遅延や携帯端末での利用は、この固定版からは確認できない。

### この論文の価値

音声の調波・雑音の構造を読唇音声合成へ組み込み、参照音声なしの音質改善と内容誤りの残存を同時に示した点。

### それまでの到達点

既存の読唇音声合成では、事前学習済み映像特徴、音声単位やメルスペクトログラム、神経音声合成器を組み合わせる。DiffV2Sは映像由来の話者特徴を用い、Lip2Speech Unitなどは参照音声の話者特徴を補助入力にする。DDSP自体は既存の音声・歌声合成技術である。

### 何が変わったか

予測したメルスペクトログラムを最終合成器へ直接入れる代わりに、内容特徴とF0から調波・雑音の粗い波形を作り、これを条件付きHiFi-GANへ与える。メル予測はF0の補正用に残す。映像特徴抽出器は固定し、その後の生成部と合成器を共同学習する。

### 分野での位置づけ

口元映像から発話音声を再構成する系統で、参照音声なしの音質・韻律生成を重視する。無声入力技術に関連するが、評価は通常発声映像の音声を入力から外した再構成であり、無声発話の臨床実証ではない。

### 実用上の意味

本人の参照音声を用意できない映像から、聞きやすい音声を生成する研究上の選択肢。内容誤りを許容できない用途では別途検証が必要。

### 前進した軸

LRS2/LRS3で掲載した生成手法の中ではSTOI-Net、DNS-MOS、映像音声同期、F0相関が高い。15人の5段階聴取評価でも音質・自然さ・理解しやすさ・声の似方の平均が比較生成手法を上回る。推論時の本人参照音声を要求しない。

### 未解決の軸

真に声を出さない発話、発話障害者、未知話者の分離と事前学習重複、未知語、他言語、照明・向き・遮蔽、逐次出力の遅延、携帯端末の電力・メモリ、音質改善の因果的な寄与。

### 後退・限定した軸

単語誤り率はLRS2で36.5%、LRS3で30.4%であり、Lip2Speech Unitの33.5%、27.7%より悪い。自動話者類似度0.63/0.63も参照音声を使う同手法の0.72/0.76より低い。構成要素を減らした方が良い指標もあり、全指標で最良ではない。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | speech-reconstruction |
| 入力 | 推論入力は口元の白黒映像。本人の参照音声や話者特徴を補助入力として要求しない。学習は対応する音声とその音響特徴・音声単位を利用し、映像モデルも音声映像事前学習と読唇の調整を経ている。 |
| センサ | 新規センサーなし。映像25フレーム/秒、音声16kHz、dlibで顔位置を合わせ口元88×88画素を白黒化する。映像処理はResNet-18と24層Transformerを含むLarge AV-HuBERT。学習はNVIDIA A100を1台使用する。 |
| 装着部位 | lip;face |
| 出力 | speech-audio |
| 語彙の種類 | 英語の連続発話を音声へ再構成する。固定単語分類ではないが、任意の語彙を正しく出力できることを保証しない。 |
| 語彙数 | 固有語数はこの固定版では不明。200クラスタは教師音声単位数であり語彙数ではない。 |
| 指標と結果 | 表1 LRS2: STOI-Net 0.92、DNS-MOS 2.95、WER 36.5%、LSE-C 8.74、LSE-D 5.84、F0相関0.61、話者類似度0.63。表2 LRS3: 同順に0.94、3.23、30.4%、8.08、6.46、0.65、0.63。Lip2Speech UnitのWERは33.5%/27.7%、参照音声ありの話者類似度は0.72/0.76。表3の5段階聴取評点は音質4.40±0.26、自然さ4.34±0.30、理解しやすさ4.39±0.32、声の似方3.98±0.33（平均±標準偏差）。15人、LRS2とLRS3の試験区分から各50サンプルを選択。表4 LRS2ではDDSP除去でDNS-MOS 2.89・WER 37.0%、音声単位教師除去でWER 38.8%。WERとLSE-Dは低いほどよい。著者報告値で独立再現ではない。 |
| 評価方法 | LRS2/LRS3の既存分割によるオフライン比較。自動音質推定、認識器による単語誤り率、映像音声同期、正規化F0相関、話者特徴類似度、15人の5段階聴取評点を用いる。LRS2で4種類の構成除去実験と図による定性比較を行う。 |

### 限界

- **技術：** 口元から音素や韻律は一意に決まらず、自然な波形でも言葉が誤る。学習時はDDSPへ正解F0、推論時は予測F0を与える差がある。事前学習モデルを固定した共同学習であり、すべての構成要素を新規に一括学習するわけではない。F0の時間間隔には本文内の記述差がある。
- **評価：** 比較手法のうちDiffV2SとLRS2のLip2Speech Unitは著者提供の合成サンプルに依存し、全手法を同一コード・全試験集合で再実行した比較ではない。客観評価の対象数・対応付け、聴取試験の割付や統計的有意差は明確でない。表3の±は標準偏差であり信頼区間ではない。
- **実運用：** 口元88×88画素の抽出と顔の位置合わせ、大規模な学習済み映像モデルを前提とする。実機での会話、録画開始終了を含む操作、患者、携帯機器、歩行中の評価はない。
- **このレビューの範囲：** arXiv:2502.12002v1の全13ページ、図1–4、表1–4を確認。固定コンテキストの書誌情報を保持し、PDFの学会誌用テンプレートの2021年表記を実際の掲載誌や受理日とは扱わない。外部配布物と実験の独立再現は未確認。

### 根拠

- 著者は複数話者の読唇音声合成で合成器の共同学習、DDSPによる音響の事前知識、参照話者特徴を要求しない生成を主要貢献とする。初の主張は著者の位置付けであり、網羅的な先行研究の独立検証ではない。（pp.1–2, Abstract; I Introduction, contribution list 1–3）
- 図1の推論入力は映像であり、内容特徴とF0からDDSP信号を生成し条件付きHiFi-GANで波形を作る。参照音声入力はないが、学習には対応音声の音響特徴と音声単位を使う。（pp.3–7, III Model Architecture; Fig.1; IV.B–D）
- AV-HuBERTは固定映像特徴抽出器であり、生成部と合成器を共同学習する。メル予測はF0補正に使用し、最終合成器への直接入力にはせず、内容特徴とDDSP波形を使う。（pp.4–6, III.A–E; Fig.1; equations (4)–(9), (15), (20)–(23)）
- DDSPは調波と非周期雑音の信号を合計し、F0と内容特徴に基づく振幅を用いる。実験設定では調波32本、FFTサイズ1024。（pp.5–7, III.C, Fig.2, equations (10)–(14); IV.C.3）
- LRS2はBBC由来144,300クリップ・約200時間、LRS3はTED/TEDx由来約150,000クリップ・5,000人超・約439時間と記載され、元の学習・検証・試験分割を使う。通常発声の既存映像音声であり、新たな無声発話患者の試験ではない。（p.7, IV.A Datasets; p.10, V.B Subjective Evaluation Results）
- 映像25Hz・音声16kHz、dlibで顔位置を合わせた88×88の白黒口元入力を用いる。音声教師は80帯域メル、200クラスタHuBERT単位、RAPTのF0を使う。（p.7, IV.A–C）
- DDSPの学習時は正解F0、推論時は予測F0を使う。口元だけで学習する方法ではなく、訓練と推論のF0条件にも差が残る。（p.7, IV.D Training, ground-truth versus predicted F0）
- 学習は各データセット500kステップ、A100単体、バッチ48、混合精度で、波形5920サンプルと特徴37フレームの断片を使う。これらは学習条件であり推論遅延を示す値ではない。（p.7, IV.D Training）
- STOI-NetとDNS-MOSは自動推定指標、単語誤り率は認識モデル、F0相関は正規化軌跡、話者類似度はResemblyzerで評価する。これらは人の聞き取り正解率と同じ指標ではない。（pp.7–8, IV.E Evaluation Metrics; equation (24)）
- DiffV2Sのコードが非公開、Lip2Speech UnitのLRS2推論コードが不足するため、比較には著者提供の合成映像サンプルを使う。評価対象の完全な対応数は示されない。（p.8, V Results, baseline implementation paragraph）
- 表1のNaturalL2SはLRS2でSTOI-Net 0.92、DNS-MOS 2.95、WER 36.5%、LSE-C 8.74、LSE-D 5.84、F0相関0.61、話者類似度0.63。Lip2Speech UnitはWER 33.5%、参照話者特徴ありの類似度0.72。（p.8, Table I, Proposed and Lip2Speech Unit rows, reference-embedding footnote）
- 表2のNaturalL2SはLRS3でSTOI-Net 0.94、DNS-MOS 3.23、WER 30.4%、LSE-C 8.08、LSE-D 6.46、F0相関0.65、話者類似度0.63。Lip2Speech UnitはWER 27.7%、参照話者特徴ありの類似度0.76。（p.8, Table II, Proposed and Lip2Speech Unit rows, reference-embedding footnote）
- NaturalL2SとDiffV2Sの話者類似度はLRS2で0.63対0.58、LRS3で0.63対0.63。p.9本文はLRS3で優位・LRS2で同率と説明しており、表と逆なので表の数値を優先する。（p.8, Tables I–II, Voice Similarity; p.9, V.A, voice similarity comparison）
- 聴取評価は15人、LRS2とLRS3試験区分から各50サンプルを選択し、音質・自然さ・理解しやすさ・声の似方を1–5で評点する。表3は平均と標準偏差で、認識正解率や信頼区間ではない。（p.10, V.B; Table III title and caption）
- 表3はNaturalL2Sの音質4.40±0.26、自然さ4.34±0.30、理解しやすさ4.39±0.32、声の似方3.98±0.33を報告。比較生成手法の平均を上回るが、元音声の音質4.88、自然さ4.94、理解しやすさ4.93には届かない。（p.10, Table III, Proposed and Ground Truth rows）
- 表4のLRS2ではDDSP除去でDNS-MOSが2.95から2.89、WERが36.5%から37.0%へ変化し、話者類似度は0.63で同じ。音声単位教師の除去ではWER 38.8%。（p.11, Table IV, Full NaturalL2S, wo-DDSP and wo-unit rows）
- 一体学習除去条件はF0予測器・DDSPを外し、内容特徴をメル予測へ変更し、LRS3で学習した通常HiFi-GANを段階的に接続する。したがって一体学習だけの独立した因果効果を測る比較ではない。（p.10, V.C.1 NaturalL2S-wo-e2e; p.11, Table IV）
- 表4は一体学習除去のWER 36.3%が完全モデル36.5%より低いこと、メル予測・F0補正除去のLSE-C 8.76とLSE-D 5.79が完全モデル8.74と5.84より良いことを示す。全構成要素が全指標を改善するわけではない。（pp.10–11, V.C.1 and V.C.4; Table IV）
- F0は前処理で50Hzと書かれる一方、式(5)–(7)は映像の4倍の長さMでF0を予測しメルは100Hzとされる。AdamW係数もβ1を二度記しており、実装を推測で補わない。（p.3, III, M=4T; p.5, III.B equations (5)–(7); p.7, IV.B and IV.D）
- 図3と図4はスペクトログラム、正規化F0、調波・雑音成分の定性的な例であり、全発話での完全再構成を保証するものではない。図4(e)のキャプションはnoiseをharmonic synthesizer由来と記すが、方式は図2とIII.Cで別の雑音合成器を示す。（p.9, Fig.3; p.11, Fig.4; pp.5–6, III.C and Fig.2）
- 結論は大規模な事前学習モデルへの依存と軽量実装を今後の課題として挙げる。本文の実験には携帯端末の推論速度・電力、逐次会話、歩行、発話障害者の無声入力試験はない。（p.11, VI Conclusion; pp.7–11, IV–V）
- 元の分割の利用は述べるが、話者非重複や事前学習との重複、語彙を分けた未知語評価は明確でない。通常発声映像の音声再構成を、未知利用者や真の無声発話の実証へ拡張しない。（p.7, IV.A Datasets and IV.C.1 Video Encoder; pp.8–11, V Results）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
