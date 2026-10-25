# From Silent Signals to Natural Language: A Dual-Stage Transformer-LLM Approach

Nithyashree Sivasubramaniam  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2509.04507)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text+summary

Corrects transcripts of speech synthesized from silent EMG (Digital Voicing data) with a Transformer recognizer and GPT-2, reducing WER from 36% to 30% on about 100 utterances.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 8-channel surface EMG (existing Digital Voicing data) |
| Task | Text from EMG-synthesized speech with LM correction |
| Vocabulary | Not stated |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Not stated |
| Key result | WER 36% to 30% (DeepSpeech vs Transformer+GPT-2), ~100 utterances |

**Limitations.** Small test set, missing training and split details, no significance tests, and no check that corrections preserve intended meaning.

## 日本語レビュー

### 要点

筋電から合成した音声の文字起こしをTransformerとGPT-2で修正し、約100発話で単語誤り率36%→30%を報告する。音声そのものの聞き取りやすさや日常利用の実証ではなく、学習・分割・意味保持の検証は不足している。

### レビュー

この論文は、声を出さずに動かした筋肉の信号から音声を作り、その音声を文字に直した後で文章を修正する研究である。主な変更点は筋電計測ではなく、後段のTransformer認識器とGPT-2による修正にある。表1では約100発話の単語誤り率がDeepSpeechの36%からTransformer単独の32.5%、修正追加後の30%へ下がる。全体の差は6ポイントで、言語修正だけの追加分は2.5ポイントである。報告値は後段処理の有用性を示唆する一方、転記文を自然に直すことと、元の発話意図を忠実に保つことは同じではない。信頼度0.7などの修正制約は説明されるが、意味改変の頻度や具体的な失敗例、人による聞き取り評価は示されない。使用話者数、分割ID、認識器とGPT-2の学習・調整方法、反復結果も不足しており、同じ条件で独立再現できるかは未確認である。また筋電の1000Hzという説明に対し実験節では16kHzと記載され、図2は16kHzを合成音声として示すため、これらを同じ計測条件として確定できない。RTX 6000A上の平均0.78秒/発話も、待ち時間や処理範囲が不明なため携帯装置の実時間性を証明しない。SSIの音声生成後に残る認識誤りを扱う初期的な比較として価値はあるが、音声自体の品質改善、未知利用者への汎化、日常会話や臨床での有効性まで主張を広げるべきではない。

### この論文の価値

無声筋電システムの誤りを、音声生成だけでなく後段の認識と文章修正に分けて検討する点。ただし数値の再現性と意味の保持は追加検証が必要。

### それまでの到達点

本論文が基盤とするのは、無声と通常発話の筋電を対応付けて音声を生成するDigital Voicing系の構成。著者は合成波形をDeepSpeechで転記する方式を比較対象とする。

### 何が変わったか

筋電センサーや無声音声の教師信号転送を新しくするのではなく、音声生成後の認識器とテキスト修正段階を変更する。

### 分野での位置づけ

表面筋電を使う無声発話システムの後段処理の研究。筋電からの直接テキスト復号や、新しい生体信号の測定法とは区別する。

### 実用上の意味

合成音声の文字起こしで残る誤りを減らす設計候補になる。ただし本人の意図を変えないことの確認や、手順を再現できる記載がないまま支援機器へ導入できるとはいえない。

### 前進した軸

system_design; problem_reframing; 合成音声の文字起こし誤り率と平均評価時間の改善を報告。

### 未解決の軸

再現可能な学習・分割手順、言語修正による意味改変、未知話者・未知語、逐次処理、携帯端末・臨床評価。

### 後退・限定した軸

言語修正を加えると平均処理時間は0.73秒から0.78秒へ増える。意味改変の増減は定量的に不明。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | 無声の表面筋電から合成した音声を文字起こしし、言語モデルで転記文を修正する。評価対象は最終的な文字列の単語誤り率。 |
| 入力 | 無声調音の表面筋電。認識器への直接入力は、その筋電から生成した音声波形。学習には通常発話の筋電と音声も用いる。 |
| センサ | 著者はDigital Voicingデータを8チャネル・1000Hzの表面筋電と記載。新しいセンサーを開発した研究ではない。電極型番・配置・対象データ版は本論文では不明。 |
| 装着部位 | 皮膚表面の筋電。具体的な電極装着位置は本論文だけでは確定できない。 |
| 出力 | 修正済み転記テキスト。中間段階に合成音声を生成するが、言語モデルが最終音声を再合成する構成ではない。 |
| 語彙の種類 | 文章の認識と修正。閉語彙・開語彙の評価条件や未知語の分離方法は不明。 |
| 語彙数 | 報告なし。約100発話という試験件数を語彙数に読み替えない。 |
| 指標と結果 | 表1の著者報告：DeepSpeechは単語誤り率36%、平均1.42秒/発話。Transformerは32.5%、0.73秒。Transformer+GPT-2は30%、0.78秒。全体で6ポイント低下、相対改善16.6%と記載。言語修正の追加分は2.5ポイント、平均時間は0.05秒増える。約100発話の評価で、信頼区間・有意差・独立再現は示されない。 |
| 評価方法 | Digital Voicingの約100発話の試験集合で、DeepSpeech、Transformer単独、TransformerとGPT-2修正の3条件を比較する。単語誤り率と平均発話当たり処理時間を報告する。 |

### 限界

- **技術：** GPT-2の版・学習や調整・入力形式、修正候補の生成方法、信頼度の定義、認識器の損失適用と学習設定が不足。筋電1000Hzと実験節16kHzの関係も説明不足。
- **評価：** 試験は約100発話とされるが、話者別成績、分割ID、反復回数、信頼区間、有意差、正解文と修正文の例を示さない。単語誤り率を人の聞き取りや意味の忠実性の測定値に読み替えない。
- **実運用：** GPUでの処理時間だけでは装着機器の消費電力・実時間性・長時間使用を評価できない。患者や日常会話での検証は報告されない。
- **このレビューの範囲：** arXiv 2509.04507v1全5ページを読み、図2・図3・表1をPDFでも確認した。本論文内の報告を評価し、引用元のデータ条件は流用しない。実装・データの独立再現や著者への照会は行っていない。

### 根拠

- 提案の中心は筋電からの音声生成後に置くTransformer転記器と言語モデル修正であり、言語修正後に音声を再合成する経路は示されない。（p.2 Sec.2.1; p.3 Fig.2 and caption）
- 著者はDigital Voicingを複数話者の無声・通常発話並行データ、8チャネル表面筋電、1000Hzと記載する。一方、本研究が使用した話者数やデータ版は記載しない。（p.2 Sec.2.2 Dataset; p.4 Sec.3）
- 筋電の特徴は31ms窓、11.6ms刻み、5種類の時間特徴と16点STFTからなり、8チャネルで112次元と記載される。（p.2 Sec.2.3 first paragraph）
- 音声生成部は80帯域mel特徴を生成する6層Transformer、8ヘッド、768次元、順伝播3072、dropout0.2と記載。DTW・CCAによるAudio Target TransferとHiFi-GANを利用する。転記用Transformerとは別の段階である。（p.2 Sec.2.3; p.3 Fig.2）
- 転記用Transformerは6層ずつの符号化器・復号器で、実験節は8ヘッド、埋込512、順伝播2048、dropout0.1、探索幅500と記載する。（p.3 Sec.2.4; p.4 Sec.3 first paragraph）
- 修正にはGPT-2を用い、最大128トークンと記載する。一般的な置換の排除、最小長、領域に関連する修正の選別、信頼度閾値0.7を説明する。（p.3 Sec.2.5 continuing p.4; p.4 Sec.3）
- 実験環境はNVIDIA RTX 6000AとPyTorch、試験集合は約100発話。MSE、Adam、32次元セッション埋込、無声・通常発話の混合学習を記載する。（p.4 Sec.3 first two paragraphs）
- 表1の単語誤り率はDeepSpeech 36%、Transformer単独32.5%、Transformer+LLM修正30%。相対改善はそれぞれ基準、9.7%、16.6%と報告される。（p.4 Table1; p.4 Sec.3 right column; Fig.3 WER bars）
- 表1の平均発話当たり処理時間はDeepSpeech 1.42秒、Transformer 0.73秒、Transformer+LLM修正0.78秒。言語修正追加は単語誤り率2.5ポイント低下と処理時間0.05秒増加に対応する。（p.4 Table1; p.4–5 Sec.3 runtime discussion; differences calculated directly from table）
- 筋電データは2.2節で1000Hz、3節ではEMG signal processing at 16kHzと記載されるが、図2は16KHzをHiFi-GANの合成音声として示す。この関係や再サンプリング手順は説明されない。（p.2 Sec.2.2; p.3 Fig.2 HiFi-GAN block; p.4 Sec.3）
- データ版、使用話者数、学習・検証・試験の具体的分割、話者別成績、未知語の分離は示されず、複数話者というデータ説明だけでは未知話者への汎化を評価できない。（p.2 Sec.2.2; p.4 Sec.3 and Table1; entire pp.1–5）
- 認識器とGPT-2の学習・調整手順、GPT-2版・入力形式、修正候補と信頼度の計算は十分に明示されない。実験節のMSEの記載だけでは各処理段階の損失を確定できない。（pp.2–4 Secs.2.3–2.5 and Sec.3）
- 単語誤り率を報告する一方、人による聞き取り試験、音声品質の独立評価、修正による意味改変率、具体的な転記・修正例、信頼区間や有意差は示さない。（pp.3–5 Secs.2.5–4; Table1; entire pp.1–5）
- 著者は平均処理時間からnear real-timeへの可能性を述べるが、時間計測の処理範囲、発話長分布、逐次入力や携帯端末での評価は示さない。省資源装置での実時間復号は今後の方向として記載する。（p.4–5 Sec.3 runtime discussion; p.5 Sec.4 future work）
- 著者自身が、合成音声の非流暢さや不自然な表現が残ること、言語モデルを誤り修正に主として限定していることを限界として挙げる。（p.5 Sec.4 limitations paragraph）
- 本論文の変更点は既存の筋電・音声生成系の後段認識と文章修正の組合せである。SSIへの初適用という著者の優先性主張を独立に確定する調査は本レビューでは行っていない。（p.2 Sec.1 contribution paragraph and Fig.1; p.3 Fig.2 orange/green stages）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
