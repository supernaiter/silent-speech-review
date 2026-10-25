# VSpeechLM: A Visual Speech Language Model for Visual Text-to-Speech Task

Yuyue Wang, Xin Cheng, Yihan Wu, Xihua Wang, Jinchuan Tian, Ruihua Song  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2511.22229)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text+summary

VSpeechLM generates lip-synchronized speech from text, a reference voice and lip video by converting lip timing into phoneme sequences; WER is 12.5% on Chem and 18.3% on GRID.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Existing video; AV-HuBERT lip features (25 fps) |
| Task | Visual text-to-speech (video dubbing) |
| Vocabulary | Not stated (text-conditioned English) |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | WER 12.5% (Chem), 18.3% (GRID) on generated speech |

**Limitations.** Requires input text and reference audio, so it does not read content from lips; table inconsistencies and no silent-speech use evaluated.

## 日本語レビュー

### 要点

文章と参考音声を使い、唇に合う音声を作る時間制御の研究。単語誤り率と同期指標は改善するが、唇だけから内容を読む方式ではなく、数値の不整合と無声利用の未検証が残る。

### レビュー

VSpeechLMの価値は、映像から発話内容そのものを解読することではなく、既知の文章を唇の動きに合わせて自然に読み上げるための時間制御にある。音素と唇の対応から音素列を引き延ばし、参考音声とともに既存の音声言語モデルへ渡すので、映像を直接入力するより既存モデルの能力を利用しやすい設計である。Chemの除去実験では、提案方式の単語誤り率12.48%・長さを考慮した音響距離5.28に対し、映像なしは15.02%・6.49、映像を前置する方式は15.16%・6.94だった。ただし音質予測値では映像なしが高く、映像利用が全側面を改善するわけではない。主比較の単語誤り率はChemで12.5%、GRIDで18.3%であり、いずれも文章を入力して作った音声の評価である。口の動きだけで単語を読み取った成績と解釈してはいけない。音質予測値はEmoDubberに及ばず、主観評価もChemでは有利な一方、GRIDの同期では引き分けが多い。LRS2の200映像での16.1%という単語誤り率は、追加学習なしの吹き替えへの移行を支持するが、事前学習データとの重複や参考音声の条件は不明であり、真の無声構音や患者への汎化を示さない。さらにGRIDの分割数、表間のUTMOS、本文の改善率に整合しない記載があるため、表の実測報告値と限定された比較だけを採用する。音を出さずに意思を伝える技術にとっては、内容の復元後に発話のタイミングを整える関連技術として有用だが、単独で実用的な無声発話インターフェースを完成させた研究ではない。

### この論文の価値

唇の時間情報を既存の音声生成器が利用できる音素列に変換する接続方法を、映像なし・単純前置との比較で検証した点。

### それまでの到達点

映像への吹き替えでは、入力文章、唇の動き、参考話者の音声から発話を合成する方式が既にある。音声言語モデルも既存であり、映像なしで文章から音声を作れることと、唇の時間情報を正しく利用できることは別問題である。

### 何が変わったか

映像を音声生成器に直接前置する代わりに、唇のフレームに対応した音素列へ変換し、既存生成器の文章系入力に時間情報を載せる。

### 分野での位置づけ

文章と参考音声を条件とする映像吹き替え。無声発話から内容を認識する中核方式ではなく、映像に合わせた音声出力を作る関連技術。

### 実用上の意味

台本と参考話者の音声が用意できる動画吹き替えに有用な設計候補。内容が未知の無声発話支援へは別の内容認識系と実利用評価が必要。

### 前進した軸

Table 1では比較した生成方式より単語誤り率、話者類似度、音響距離、長さを考慮した音響距離が改善。映像を単に前置する方式より音素の時間対応を使う方式が良く、LRS2の200映像で追加学習なしの評価も行う。

### 未解決の軸

本当に無声で口を動かした映像への移行、文章を与えない内容復元、参考音声の取得条件、学習データとの重複、実時間処理、機器上の計算量、表と本文の数値不整合。

### 後退・限定した軸

音質の自動予測値UTMOSはEmoDubberより低い。Chemの映像なし条件もUTMOSでは提案方式を上回り、同期・内容の改善と音質予測値の間にトレードオフがある。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | speech-reconstruction |
| 入力 | 唇の映像、入力文章、話者の声質を指定する参考音声。学習時には正解音声と、その音素持続時間から得た教師信号も使用する。 |
| センサ | 既存動画から毎秒25フレームの唇特徴をAV-HuBERTで抽出する。新しい撮影機器や装着センサーは提案していない。 |
| 装着部位 | lip;face |
| 出力 | speech-audio |
| 語彙の種類 | 入力文章で内容を指定する英語の動画吹き替え。 |
| 語彙数 | 正確な語彙数は報告されていない。 |
| 指標と結果 | Table 1の提案方式: ChemはWER 12.5%、Spk Sim 78.9、UTMOS 3.73、MCD-DTW 5.16、MCD-DTW-SL 5.28。GRIDは18.3%、69.7、3.94、3.91、3.90。EmoDubberのUTMOSはChem 3.87・GRID 3.98。Table 2のChem: 提案方式WER 12.48%・MCD-DTW-SL 5.28、映像なし15.02%・6.49、映像前置15.16%・6.94。Table 4のLRS2: WER 16.1%、Spk Sim 53.9、UTMOS 2.98、MCD-DTW-SL 7.59。すべて著者報告で独立再現は未実施。WERは生成音声の単語誤り率、Spk Simは話者類似度、UTMOSは音質の自動予測、MCD系は音響距離で、MCD-DTW-SLは音声長を考慮した代理指標である。 |
| 評価方法 | 収録済み英語映像のオフライン吹き替え。生成音声の認識器由来の単語誤り率、話者類似度、音質予測、音響距離、10人の専門評価者による対比較、映像入力方法と事前学習の除去実験、およびLRS2への追加学習なしの転用。 |

### 限界

- **技術：** 学習時は正解の音素持続時間で展開した列を生成器に与えるが、推論時は予測列に変わる。音声符号化による品質上限も著者が指摘する。音響距離は唇と音声の直接的な時刻ずれ測定ではなく、部分的な唇の隠れや低品質映像は将来課題。
- **評価：** GRID分割の数が整合しない。Table 3の提案方式UTMOSはTable 1・2と異なり、本文の同期改善率もTable 1の値から再現できない。比較方式の単語誤り率と音響距離は既報値、UTMOSと話者類似度は公開モデルで生成した音声の再評価で、完全に統一した再実験ではない。主観評価の信頼区間、検定、盲検化の詳細は不明。
- **実運用：** 入力文章と参考音声が必要であり、発話内容が未知の利用者をカメラだけで支援する実証ではない。装着機器、携帯端末、処理遅延、患者の会話利用は評価されていない。
- **このレビューの範囲：** 確認した8ページの本文・図表・参考文献に基づく。補足資料と実装の独立確認は未実施。英語の既存映像を使う文章条件付き音声合成の範囲に限定する。

### 根拠

- 入力は映像だけでなく文章と参考音声を含む。参考音声は話者情報を与え、正解音声は学習対象となる。この課題は文章条件付きの吹き替えであり、口の動きだけによる内容認識ではない。（pp. 2–3, Sections 3.1–3.2 and Figure 2(a)）
- 音素列と唇特徴の類似度から各映像フレームに音素を割り当てて列を展開し、大域・局所Transformerによる音声生成器へ時間情報を渡す。映像を単純に前置する方式とは異なる接続方法である。（pp. 3–4, Sections 3.3–3.4, Figure 2(b), Equations 3–6）
- 唇特徴は25fpsの映像からAV-HuBERTで抽出し、音声は16kHz、EnCodecの8コードブックで符号化する。学習用の音素持続時間はMontreal Forced Alignerから得る。学習時の生成器は正解展開列、推論時は予測展開列を使う。（pp. 3–4, Sections 3.2 and 3.5.1–3.5.3）
- Chemの分割は学習6,240・検証200・テスト200と報告される。GRIDは33話者各1,000映像、各話者100映像をテストと説明する一方、学習32,670・テスト900とも記し、数が整合しないため正しい分割数は不明である。（p. 4, Section 4.1, Datasets）
- Table 1のVSpeechLMはChemでWER 12.5%、Spk Sim 78.9、UTMOS 3.73、MCD-DTW 5.16、MCD-DTW-SL 5.28。GRIDでは18.3%、69.7、3.94、3.91、3.90。WERは入力文章から生成した音声に対する認識器の単語誤り率であり、読唇だけの認識精度ではない。（pp. 4–5, Section 4.1 Metrics and Table 1）
- Table 1ではUTMOSがEmoDubberのChem 3.87・GRID 3.98より低く、全指標で最良ではない。WERとMCD系の比較値は既報結果から引用し、UTMOSとSpk Simは公開モデルで生成して評価している。（p. 5, Table 1 and its caption, Section 4.2）
- 本文に記す同期指標の改善率17.6%と60.9%は、Table 1のChem 6.51→5.28、GRID 6.42→3.90の通常の相対減少率と一致しない。Table 3の提案方式UTMOS 3.87もTable 1・2のChem 3.73と異なるため、原因は不明として主表の値を採用する。（pp. 5–6, Section 4.2, Tables 1–3）
- 主観評価はChemとGRIDから各50映像を選び10人の専門評価者が勝ち・引き分け・負けを判断する。比較相手はChemでEmoDubber、GRIDでStyleDubber。Figure 3の同期はChemで勝ち71.7%・負け15.0%、GRIDで勝ち32.3%・負け24.3%であり、GRIDでは引き分けが多い。信頼区間や統計検定は確認した本文にない。（p. 5, Section 4.3 and Figure 3 (rendered figure checked)）
- Chemで音素・映像対応器を使う方式はWER 12.48%・MCD-DTW-SL 5.28、映像なしは15.02%・6.49、映像前置は15.16%・6.94。UTMOSは順に3.73、3.81、3.51で、映像なしが提案方式を上回る。（p. 6, Table 2 and Section 4.5.1）
- 事前学習なし・生成器を固定して対応器のみ適応する条件ではTable 3のWERがそれぞれ151、829と報告され、通常方式12.5より悪い。著者は事前学習と生成器の適応の両方の必要性を論じるが、同表UTMOSには他表との不整合がある。（p. 6, Section 4.5.2 and Table 3）
- LRS2から無作為抽出した200映像で追加学習なしの評価を行い、VSpeechLMはWER 16.1%、Spk Sim 53.9、UTMOS 2.98、MCD-DTW-SL 7.59。これは文章と参考音声を使う吹き替え課題の転用で、無声構音の利用者評価ではない。（p. 6, Section 4.5.3 and Table 4; input contract in Section 3.1）
- 確認した本文は参考音声の詳細な選択条件、事前学習データとの重複除外、モデル規模、処理遅延を示していない。補足資料に設定詳細を委ねており、本レビューでは補足資料と独立実装を未確認とする。（pp. 3–4, Sections 3.2 and 4.1 Implementation Details; scope of inspected pp. 1–8）
- 著者は部分的に唇が見えない場合や低品質映像を将来課題に挙げる。評価した収録動画の結果だけでは、真の無声構音、患者の会話、携帯機器や歩行中の動作を実証したことにはならない。（pp. 4–6, Sections 4.1–4.5 and Section 5 Conclusion and Future Work）
- 生成器はESPnetの事前学習モデルから初期化し、AdamW、初期学習率1e-4、betas 0.9/0.95で学習する。推論はtop-k=30で、温度はChem 1.2、GRID 0.5と報告される。（p. 4, Section 4.1 Implementation Details）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
