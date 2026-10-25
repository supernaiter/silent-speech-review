# AVSRBench: A Multi-Condition AVSR Benchmark

Rishabh Jain, Naomi Harte  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2609.10366)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text+summary

Benchmark comparing visual-only, audio-only and audio-visual speech recognition across six datasets; sub-1% AV WER on LRS3, visual-only collapses out of domain, and AV fusion helps clearly mainly under Lombard speech.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | RGB camera and microphone (audio-visual) |
| Task | Audio-visual speech recognition benchmark |
| Vocabulary | Dataset-dependent; continuous open vocabulary (GRID fixed grammar) |
| Speaker | Not stated |
| Session | Not applicable |
| Online / offline | Offline |
| Key result | 0.79% AV WER on LRS3 (Llama-AVSR); visual-only WER 110.07% on RoomReader-AV (Auto-AVSR) |

**Limitations.** Uses fixed public checkpoints without retraining; camera-based AVSR rather than wearable SSI; no real-time or on-device measurement; limited speaker-split and statistical detail.

## 日本語レビュー

### 要点

LRS3のsub-1% AV WERは放送ドメインの指標。六条件比較では視覚のみが領域外で崩壊し、AV融合の明確な利点は主にLombard。RoomReader-AV（6.49h・10,324発話・118人）は会議会話の厳しさを示す。装着SSIの代替ではない。

### レビュー

AVSRBenchは、JainとHarteによる多条件AVSRベンチマーク研究であり、Kimuraのベンチマーク提案ではない。動機は明確で、LRS3でsub-1% WERに見える進歩が放送音声へのドメイン適応なのか真の汎化なのかを切り分けることにある。評価対象はAuto-AVSR、AV-HuBERT Large、Llama-AVSRの三方式。条件は制御された放送（LRS2/LRS3）、固定文法（GRID）、過構音のLombard（LombardGrid）、専門唇話者と非専門家の音読（TCD-TIMIT）、自発的な多人数ビデオ会話（RoomReaderを前処理したRoomReader-AV）である。Table IのRoomReaderは6.49時間・10,324発話・118話者で、自発会話条件として新規にAVSR評価へ導入される。結果の骨格は要旨とTable II–XIで一致する。LRS3ではLlama-AVSRのAV 0.79%、Auto-AVSRのAV 0.90%など放送内では音声に近い低WERが出る一方、GRIDの視覚のみはAuto-AVSR 66.53%、AV-HuBERT 83.80%、Llama-AVSR 116.39%まで崩れ、AVがAOより悪化する例もある。LombardGridではAuto-AVSRがAO 14.02%からAV 11.73%へ改善し（Δ+2.29）、AV融合が明確に効く稀な領域外条件となる。同じLombardGridで90°横顔の視覚のみはAuto-AVSR 64.88%→92.50%と急落するが、AVはほぼ横ばいで、極端姿勢では音響フォールバックが効いている。TCD-TIMITでは0°と30°の差は概ね3ポイント未満なのに対し、唇話者とマッチドボランティアの視覚ギャップはモデルにより約17〜44ポイントと大きく、構音の方が小角度より支配的である。RoomReader-AVではAuto-AVSRのVO 110.07 / AO 25.40 / AV 26.39、Llama-AVSRはVO 311.48かつAVがAOより40ポイント超悪化し、短いきき返しでのLLM幻覚が目立つ。価値は、スタジオ唇読取のSOTA数字を会話や横顔へそのまま外挿できないことを、公開モデルと公開データで示す点にある。これはカメラAVSRの汎化診断であり、SilentSpeller（EPG）・SottoVoce（超音波）・AESSI（耳周囲）・IR-UWBレーダーといった装着／非接触SSIの代替性能を示す論文ではない。サイトのVTP系カメラ唇読取ともセンサは近いが、問うているのはSOTA更新ではなく条件間の崩れ方である。

### この論文の価値

放送ベンチ飽和の読み方を矯正する比較資料。RoomReader-AV統計とLombard/横顔/構音の切り分けを、VTPやLipsFlowの紙面と並べて読む価値がある。

### それまでの到達点

AVSR評価の中心はLRS2/LRS3放送コーパス。サイトのVTP・LipVoicer・AKVSR・LipsFlowはカメラ／イベント視覚、SilentSpeller・SottoVoce・AESSI・IR-UWBは装着／レーダーSSIで、本論文は前者の隣接ベンチマーク研究。

### 何が変わったか

単一放送テストセットのWER競争から、固定文法・Lombard・唇話者／非専門家・Zoom自発会話を含む多条件比較と、再利用可能な前処理パイプラインへ移す。

### 分野での位置づけ

カメラAVSRの汎化ベンチマーク。VTP・LipsFlow・AKVSR・LipVoicerとセンサが近く、SilentSpeller・SottoVoce・AESSI・IR-UWBの装着／レーダーSSIとは原理が異なる隣接分野。

### 実用上の意味

スタジオ唇読取スコアの適用範囲を説明するときの根拠。会議映像・横顔・非専門家構音で視覚がどこで崩れるかを設計前に確認する資料。

### 前進した軸

放送ドメイン外での視覚のみ崩壊、LombardでのAV融合利点、90°横顔での音響フォールバック、構音習熟が小角度より重要、LLM系のOOD不安定という比較軸を同一枠で提示。

### 未解決の軸

ウェアラブルSSI・無声構音・臨床利用者での性能、オンライン実時間、未知言語・未知語彙の開世界会話、前処理以外の学習データ刷新の効果。

### 後退・限定した軸

測定上の退行というより、放送ベンチ飽和が汎化を過大に見せていたことを示す。方式間の単純なSOTA更新を主張する論文ではない。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | dataset; speech-recognition |
| 入力 | RGB顔・唇映像と音声の音声視覚（AVSR）。比較はVO/AO/AV。EPG・超音波・筋電・レーダーなどの装着／非接触SSIセンサではない。 |
| センサ | データセット依存のRGBカメラとマイク。前処理はRetinaFace+68点ランドマークで96×96口元ROI、音声16 kHz mono。装着電極や超音波プローブではない。 |
| 装着部位 | face; lip |
| 出力 | 文字起こしテキストに対する単語誤り率（WER）。固定コマンド分類ラベルや音声波形合成が主出力ではない。 |
| 語彙の種類 | 連続音声認識の単語列。閉集合コマンドSSIのラベル分類ではない。 |
| 語彙数 | データセット依存。GRIDは固定六語コマンド文法。LRS/TCD/RoomReaderは連続音声の開いた語彙空間。単一の閉じたコマンド集合ではない。 |
| 指標と結果 | LRS3 AV: Llama-AVSR 0.79%、Auto-AVSR 0.90%、AV-HuBERT 1.47%（Table II）。GRID VO: 66.53 / 83.80 / 116.39%（Table III）。LombardGrid Auto AV 11.73%対AO 14.02%（Δ+2.29; Table V）。LombardGrid Auto VO 0°64.88%→90°92.50%（Table VI）。RoomReader-AV Auto VO/AO/AV 110.07/25.40/26.39、Llama VO 311.48・AVペナルティ約−40.5（Table IX）。RoomReader-AV: 6.49h・10,324発話・118参加者（Table I）。著者報告WERであり独立再現ではない。 |
| 評価方法 | VO/AO/AVのWER比較を六データセットで実施。LombardGridは0°/90°、TCD-TIMITは唇話者・ボランティア・マッチドボランティアと0°/30°、RoomReader-AVは個別音声とEasy/Hard、さらに学習規模別VO比較。 |

### 限界

- **技術：** 評価は公開チェックポイントの固定復号。視覚表現の再学習や融合ゲートの改変はしない。RoomReaderはセッション音声ではなく個別話者ストリームを報告。
- **評価：** 公開事前学習チェックポイントの公式復号設定を固定。再学習や新規視覚表現の提案はしない。RoomReaderはEasy(≥2s)/Hard(<2s)分割を導入するが、話者非依存分割の詳細や統計検定は限定的。
- **実運用：** カメラ映像とマイクのAVSR。ウェアラブル電極・超音波・EPG・レーダーは対象外。実時間ストリーミングやオンデバイス常時運用の測定はない。RoomReaderは個別話者ストリーム評価。
- **このレビューの範囲：** arXiv 2609.10366v1全文8ページ（要旨・Table I–XI・議論・結論）とPDFを確認。数値は本文表から転記し、独立再推論や公式以外のチェックポイント比較は行っていない。書誌はarXiv APIのv1を保持。

### 根拠

- 著者は、LRS3のsub-1% WERが真の汎化か放送ドメイン適応かを調べるため、三AVSR方式を六条件で評価し、RoomReader-AVと統一前処理を公開したと主張する。（Abstract; §I; §VI）
- 評価データはLRS2、LRS3、GRID、LombardGrid、TCD-TIMIT、RoomReaderの六つ。条件は放送、固定文法、Lombard過構音、専門唇話者／非専門家音読、自発多人数会話をカバーする。（Abstract; Table I; §II-A）
- Table IのRoomReaderは6.49時間・10,324発話・118話者で、自発会話条件。前処理後のデータセットをRoomReader-AVと呼ぶ。（Table I; §II-B）
- 比較モデルはAuto-AVSR、AV-HuBERT Large、Llama-AVSR。いずれも公式事前学習チェックポイントと公式復号設定を用い、VO/AO/AVのWERを測る。（§III; §IV）
- Table IIのLRS3 AV WERはAuto-AVSR 0.90%、AV-HuBERT 1.47%、Llama-AVSR 0.79%。放送内ではAVがAOに近い低誤差になる。（Table II; §IV-A）
- GRIDの視覚のみWERはAuto-AVSR 66.53%、AV-HuBERT 83.80%、Llama-AVSR 116.39%。AutoとLlamaではAVがAOより悪化する（Δ −8.90 / −41.88）。（Table III; §IV-B）
- LombardGridではAuto-AVSRがAO 14.02%からAV 11.73%へ改善（Δ+2.29）。領域外でAV融合が安定して効く主例として報告される。（Table V; §IV-C）
- LombardGridの視覚のみは0°から90°でAuto-AVSR 64.88%→92.50%、AV-HuBERT 87.06%→102.53%、Llama-AVSR 111.01%→180.62%。AVはほぼ横ばいで音響フォールバックを示唆する。（Table VI; §IV-C; §V）
- TCD-TIMITでは0°と30°のWER差は概ね3ポイント未満。一方、唇話者とマッチドボランティアの視覚ギャップはAuto約16.9、AV-HuBERT約21.6、Llama約44.1ポイントと大きい。（Table VII; Table VIII; §IV-D）
- RoomReader-AV全体でAuto-AVSRはVO 110.07 / AO 25.40 / AV 26.39。Llama-AVSRはVO 311.48、AV 128.54でAO 88.01より約40.5ポイント悪化する。（Table IX; §IV-E）
- 本論文はカメラとマイクのAVSR汎化診断であり、EPG・超音波・耳周囲電気生理・IR-UWBレーダーなどの装着／非接触SSI性能を評価しない。（Abstract; §II; §VI）
- LRS3のsub-1% AV WERは放送ドメインの結果として読む。開世界会話やウェアラブル無声入力の準備完了を示す設計ではない。（Abstract; §IV-A; §V; §VI）
- 視覚のみの領域外崩壊は学習規模だけでは解けない。Auto-AVSRを1.7kから3.4k時間へ増やしてもRoomReader-AVのVOは110.07対113.20とほぼ変わらない。（Table XI; §IV-F; §V）
- 新規性の中心はRoomReader-AV導入と六条件横断、およびAuto-AVSR/AV-HuBERT互換前処理の公開。新規AV融合アーキテクチャや装着SSIセンサの初提案ではない。（§I; §II-B; §VI）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
