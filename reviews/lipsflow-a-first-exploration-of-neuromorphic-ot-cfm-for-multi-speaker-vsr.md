# A First Exploration of Neuromorphic OT-CFM for Multi-Speaker VSR

Lin Chen, Jingping Fang, Hairui Liu, Chenyang Xu, Junhao Chen, Xiaorui Li, Weidong Cai, Xiaoming Chen  
ECCV 2026 · [DOI](https://doi.org/10.1007/978-3-032-37281-9_8) · [arXiv](https://arxiv.org/abs/2606.31225)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text+summary

Neuromorphic OT-CFM (LipsFlow) for multi-speaker visual speech recognition from event streams; 22.3% WER and 19.8% VER on DVS-Lip with 240 ms latency.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Event streams from RGB video or DVS dataset (camera) |
| Task | Visual speech recognition (multi-speaker) |
| Vocabulary | Not stated |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 22.3% WER, 19.8% VER on DVS-Lip, 240 ms latency |

**Limitations.** Camera-based, not a wearable SSI; author-reported benchmark results only; vocabulary and speaker split details limited; on-device, walking and clinical use untested.

## 日本語レビュー

### 要点

イベントストリームのマルチ話者VSR。DVS-LipでWER 22.3%・VER 19.8%・240 ms。カメラVTPとも装着SSIともセンサが異なる。

### レビュー

LipsFlowは、カメラのRGBフレーム唇読取（サイトのVTP系）や、SilentSpellerのEPG・SottoVoceの超音波・AESSIの耳周囲電気生理といった装着SSIではなく、RGBを高時間分解能のイベントストリームへ変換してマルチ話者の視覚音声認識（VSR）を行う枠組みである。マルチ話者はByteTrackで追跡しTalkNetの能動話者検出で単話者クリップへ分割する。復号はOptimal Transport Conditional Flow Matching（OT-CFM）で、決定的な直線軌道により推論を約2 ODEステップ（NFE=2）に抑え、Table 1ではDVS-Lip上でWER 22.3%、VER 19.8%、Latency 240 ms、RTF 0.18、Params 45.8Mを報告する。Table 4ではNFE=1がWER 28.5%なのに対しNFE=2で22.3%となり、追加ステップで誤差が大きく減る。ホモフィーン対策としてトークン級BERT重み共有と文級Sentence-BERT事前の二重意味監督を置く。価値は、モーションブラーに弱いフレームVSRと、サンプリングの重い拡散系のあいだで、イベント表現と直線フローによる低遅延テキスト化を具体化した点にある。一方、これは視覚イベントの唇読取であり、無声の構音を皮膚・口腔センサで読むSSIの代替ではない。SOTAはDVS-Lip等の報告テーブル範囲で読むべきで、オープンワールド会話や臨床入力の完成を主張する根拠にはならない。Kimuraの研究ではなく、Lin ChenらによるECCV 2026採択論文のレビューである。

### この論文の価値

フレームVSRの時間分解能限界と拡散生成の遅延を、イベント変換＋OT-CFM（NFE≈2）で同時に攻める具体例。視覚イベント唇読取とウェアラブルSSIを混同しないための対比材料になる。

### それまでの到達点

従来のRGB VSRは25–30 FPSのモーションブラーと低時間分解能に弱く、拡散系生成は多数サンプリングで遅延が大きい。イベントベース唇読取（MSTP・SNN-Lip等）はあるが、マルチ話者シナリオと低遅延生成の両立は限定的だった。サイト上のVTP（カメラ唇読取）やLipVoicer（唇→音声）はフレーム視覚系であり、SilentSpeller/SottoVoce/AESSIのような装着SSIとはセンサが異なる。

### 何が変わったか

マルチ話者シーンをByteTrack+TalkNetで単話者化し、学習可能イベント表現とOT-CFM（NFE=2）でDVS-Lip上のイベントVSR精度と240 ms級遅延を同時に狙う。カメラフレームVTPや装着SSIの代替ではなく、イベントストリームVSRの系統。

### 分野での位置づけ

イベント／ニューロモルフィック視覚に基づくマルチ話者VSR。サイトのカメラVTP・LipVoicer（視覚）とはセンシングが近く、SilentSpeller・SottoVoce・AESSI（装着SSI）とはセンサ原理が異なる隣接分野。

### 実用上の意味

高速頭部運動や低照度でフレームが崩れる場面の視覚音声認識を検討するときの、イベント表現と低NFE生成の参照。ウェアラブル無声入力の設計書ではない。

### 前進した軸

フレームベース唇読取のモーションブラー・低フレームレート制約に対し、イベントストリーム表現と直線軌道のOT-CFMで精度と低遅延の両立を狙った。マルチ話者は追跡＋能動話者検出で単話者区間に落とす。

### 未解決の軸

オープンワールド会話、装着型SSIとの公平比較、イベント変換パイプラインなしの純粋RGB現場、著者実装の独立再現、話者数・語彙の詳細な公開条件の完全な確認。

### 後退・限定した軸

ウェアラブル構音センサ（EPG・超音波・耳周囲電気生理）や無音の想像発話は扱わない。カメラ／イベント視覚に依存し、音響が使えない無声発話そのものを計測するSSIではない。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | マルチ話者シーンの視覚音声認識（VSR）。イベントストリームからテキストを生成する。無声の想像発話解読や装着センサSSIではない。 |
| 入力 | RGB動画から変換した高時間分解能イベントストリーム（および比較用のRGB分岐）。DVS-Lipではデータセット提供のイベントを直接使用。EMG・超音波・EPGではない。 |
| センサ | RGBカメラ映像からのイベントストリーム変換（学習可能なしきい値ネット等）。DVS-Lipではデータセットの実イベント入力。装着電極や超音波プローブではない。 |
| 装着部位 | 顔・唇の視覚領域（カメラ／イベント）。口腔内センサや皮膚電極ではない。 |
| 出力 | テキスト（意味トークン経由の語彙復号）。音声波形は主出力ではない。 |
| 語彙の種類 | 視覚音声認識の単語／トークン列。閉集合コマンドSSIではない。 |
| 語彙数 | 本文抽出では具体的な語彙サイズを確定できない。BERT語彙空間への写像と記載。 |
| 指標と結果 | DVS-Lip（Table 1）LipsFlow: WER 22.3%、VER 19.8%、RTF 0.18、Latency 240 ms、Params 45.8M。比較例: Llama-AVSR WER 23.9%/Latency 2500 ms、MSTP 30.5%/280 ms、SynthVSR 25.1%/6000 ms。AVA Clean 22.3%、Rapid Motion 24.1（↑1.8）、Low Light 22.9（↑0.6）、Severe Occlusion 26.5（↑4.2）。NFE=2が主設定。著者報告値であり独立再現ではない。 |
| 評価方法 | DVS-LipでのWER/VER/RTF/Latency/Params比較（Table 1）、AVA劣化条件でのWER（Table 2）、融合・復号・NFE・損失のアブレーション（Table 3–5）。 |

### 限界

- **技術：** イベントはRGB変換またはデータセット提供に依存。ホモフィーンは言語事前で緩和するが視覚のみの原理的曖昧性は残る。TalkNet等の前段誤りが後段に伝播しうる。
- **評価：** 主結果は著者報告のDVS-Lip / AVA比較。独立再現や第三者実装の確認はない。語彙・話者分割の詳細は抽出テキストだけでは限定的。AVA側は自前のイベント変換と人手注釈カテゴリに依存。
- **実運用：** 評価はベンチマーク推論遅延・RTF中心。オンデバイス携帯、歩行、完全なプライバシー無声音声、臨床利用者は未評価。マルチ話者前処理に追跡とTalkNet ASDを要する。
- **このレビューの範囲：** arXiv 2606.31225v2全文抽出（要旨、§3–6、Table 1–5、Fig.2）とPDFハッシュを確認。図表OCRの取りこぼしや著者コードの実行、独立再現はしていない。

### 根拠

- 著者はLipsFlowを、RGBを高時間分解能イベントストリームへ変換しByteTrack+TalkNetで単話者化し、OT-CFMと二重意味監督でマルチ話者VSRを行う枠組みだと主張する。（Abstract）
- センサはカメラ由来のイベントストリーム（DVS-Lipではデータセットの実イベント）であり、EPG・超音波・耳周囲電気生理などの装着SSIセンサではない。（Abstract; §5.1 Datasets）
- マルチ話者前処理にByteTrack追跡とTalkNet能動話者検出を用い、シーンを単話者クリップへ時間分割する。（Abstract; §4 Multi-Stage Data Process Pipeline）
- 復号はOptimal Transport Conditional Flow Matching（OT-CFM）で、決定的2ステップEuler（Δt=0.5）により意味トークンを復元すると記載。（Abstract; §3.3 Speaker-Conditioned OT-CFM）
- Table 1（DVS-Lip）でLipsFlowはWER 22.3%、VER 19.8%、RTF 0.18、Latency 240 ms、Params 45.8Mと報告される。（Table 1; §5.2）
- 要旨および§5.2は、競争的ベンチマーク上でWER 22.3%・240 ms遅延のSOTA級結果だと述べる。範囲は報告テーブルに限定して読む。（Abstract; §5.2）
- Table 2（AVA）Clean Set WER 22.3%。Rapid Motion 24.1（↑1.8）、Low Light 22.9（↑0.6）、Severe Occlusion 26.5（↑4.2）。（Table 2; §5.3）
- Table 4でNFE=1はWER 28.5%/180 ms、NFE=2は22.3%/240 ms。主結果の2ステップ設定に対応する。（Table 4; §5.4）
- Table 3でVisual-Only ARはWER 27.8%、最終LipsFlow（Cross-Attn + OT-CFM）は22.3%/19.8%。イベント分岐とOT-CFMの寄与を示すアブレーション。（Table 3; §5.4）
- 新規性の中心は、マルチ話者イベントVSRとして追跡・ASD・イベント符号化・OT-CFM・二重意味監督を一貫接続し、DVS-Lipで低NFEと競合WERを同時報告した点。個別モジュール単体の初出主張ではない。（§1; §3.1; §5.2）
- 評価はDVS-Lipと、フレームからイベントへ変換したAVAの劣化カテゴリが中心。装着SSIや想像発話、臨床利用者は対象外。（§5.1 Datasets; §6 Conclusion）
- 本レビューはカメラ／イベントのVSR論文として位置付ける。サイトのVTP唇読取とはセンシングが近く、SilentSpeller/SottoVoce/AESSIの装着SSIとは混同しない。（Abstract; §2 Related Work framing）
- ホモフィーン曖昧性は言語事前で緩和するが、視覚のみでは原理的に残る。著者も従来法の限界としてホモフィーンと非音声口腔動作を挙げる。（Abstract; §3.4; §6）
- NFE=2で240 ms・RTF 0.18と効率を強調するが、オンデバイス常時運用や歩行・野外の独立実時間測定は本文にない。（Table 1; Table 4; §5.4）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
