# A Parallel Ultra-Low Power Silent Speech Interface based on a Wearable, Fully-dry EMG Neckband

Fiona Meier, Giusy Spacone, Sebastian Frey, Luca Benini, Andrea Cossettini  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2509.21964)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text+summary

A fully dry wearable EMG neckband with ultra-low-power BioGAP-Ultra classifies 8 silently articulated words for one healthy user at 68% accuracy, dropping to 54% on an unseen re-wearing session; acquisition plus BLE uses 22.2 mW.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Dry-electrode textile neckband, 14-channel EMG |
| Task | Closed-set command word classification |
| Vocabulary | 8 commands |
| Speaker | Speaker-dependent |
| Session | Cross-session |
| Online / offline | Not stated |
| Key result | Silent 68% (pooled 5-fold), 54% leave-one-session-out, chance 12.5% |

**Limitations.** Single participant, cue-aligned 1.4 s segments, no on-device inference reported, and no walking, natural conversation or patient testing.

## 日本語レビュー

### 要点

完全乾式の首輪型筋電計測で、健康な1人の無声8語分類は68±3%。装着し直した未学習セッションでは54±7%に下がる。22.2mWは計測・無線通信の値で、自由会話や端末内実時間認識の完成を示すものではない。

### レビュー

この研究の価値は、首に巻く布製の装置で湿式参照電極も不要にし、計測・通信の省電力化と装着し直しの問題を同時に扱った点にある。14差動チャネルの筋電を取得し、健康な1人が8種類の命令語を通常発話または無声調音する。各条件3セッション・3360発話を収録し、画面提示後の最初の1.4秒から特徴量を作ってRandom Forestで分類する。全セッションを混ぜた5分割評価では通常発話87±3%、無声68±3%だが、装着し直した1セッションを丸ごと評価用にすると、それぞれ64±18%、54±7%に下がる。±は著者の標準偏差であり、参加者間のばらつきではない。8択の偶然水準12.5%を上回っていても、未知の装着条件に十分強い、あるいは日常の意思伝達に使えるとまではいえない。報告された22.2mWは継続計測とBluetooth Low Energyによる通信の消費電力で、首輪上の認識や受信側を含むシステム全体の電力・電池持続時間ではない。200ミリ秒ごとの区間も特徴抽出の単位であり、7区間を連結するため200ミリ秒で命令を出す実時間実験とは異なる。新しい筋電原理や自由文の復号ではなく、完全乾式の装着型機器の設計と、その再装着時の限界を把握するための初期検証として読むのが適切である。

### この論文の価値

乾式電極・無線・省電力の計測装置を、単なる分類精度だけでなく再装着時の性能低下と併せて評価できる点。

### それまでの到達点

表面筋電による無声発話分類と首輪型・無線計測は既存研究にある。本論文は、顔への電極装着、湿式参照電極、計測基板、装着位置の変化を実用化上の課題として位置付ける。

### 何が変わったか

27個の接続部を持つ布製首輪に乾式電極を取り付け、14差動チャネルの筋電をBioGAP-Ultraで取得する。分類法の刷新より、湿式参照を不要にする構成と、同一人物の装着し直しを切り分けた評価が中心。

### 分野での位置づけ

表面筋電を用いる首輪型の閉語彙命令認識。アルゴリズム競争より、完全乾式の電極・計測機器と同一人物のセッション変動の研究に位置付けられる。

### 実用上の意味

再装着を前提とする装着型の無声命令入力装置を設計する際に、計測電力と未学習セッションの精度を分けて検討する資料になる。

### 前進した軸

乾式の参照電極を含む首輪型計測、計測・通信の消費電力、装着し直したセッションを分けた評価。

### 未解決の軸

人数・語彙の拡張、連続動作からの発話検出、端末内認識、実時間遅延、長時間装着、歩行や日常動作、患者での意思伝達。

### 後退・限定した軸

同じ3セッションを学習・評価の双方に含む分割から、1セッションを丸ごと未学習にする分割へ変えると、無声時68±3%から54±7%、通常発話87±3%から64±18%へ下がる。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | 通常発話および無声調音の8語命令分類。提示された単語区間を分類する閉語彙課題。 |
| 入力 | 首の表面筋電。通常発話と無声調音を別条件として収録する。脳波や想像発話の計測ではない。 |
| センサ | 布製首輪、乾式SoftPulse電極、27接続部、前面10差動対と左右各2差動チャネルの計14チャネル、後面4電極を短絡した接地。BioGAP-UltraはGAP9、nRF5340、ADS1298を2個搭載する。計測基板は16差動チャネル対応だが首輪で用いるのは14。24ビット、増幅率12、500samples/s。 |
| 装着部位 | throat; 首の前面・側面の皮膚、後面の接地電極 |
| 出力 | 8命令語のクラスラベル。連続文字列や音声波形を生成する実験ではない。 |
| 語彙の種類 | 移動や制御を想定した固定8命令語。自由文・開語彙ではない。 |
| 語彙数 | 8語：up, down, left, right, forward, backward, go, stop。 |
| 指標と結果 | 全セッション混合・層化5分割の正解率：通常発話87±3%、無声68±3%。leave-one-session-out：通常発話64±18%、無声54±7%。通常発話のセッション内モデルの平均は85±7%、初回セッションは74%。8クラスの偶然水準は12.5%。±は著者記載の標準偏差。継続計測とBLE通信の電力は22.2mW。いずれも著者報告で独立再現ではない。 |
| 評価方法 | セッション内の7バッチを使う7分割交差検証、全3セッションを混ぜて無作為化した層化5分割交差検証、2セッションで学習し残る1セッションで評価するleave-one-session-out。通常発話と無声調音を区別し、語別と全体の正解率を報告する。 |

### 限界

- **技術：** 発話開始を画面提示で揃え、最初の1.4秒だけを処理する。自然な連続信号からの発話区間検出、無入力時の誤作動、会話中の遷移、装置上での推論性能は示されない。
- **評価：** 1人の反復収録なので参加者間のばらつきは測れない。全セッション混合の5分割評価は新しい装着セッションへの汎化ではない。本文は平均と標準偏差を報告するが、有意差検定、乱数・ソフトウェア版、独立した再現実験は示さない。
- **実運用：** 実験は1人への画面提示に同期した単語収録。受信・提示にノートパソコンを使い、搭載GAP9での認識実行は報告されない。歩行、食事、自然な会話、長時間の快適性、患者での使用は未検証。
- **このレビューの範囲：** arXiv 2509.21964v1の全4ページを読み、図1–4をPDF表示でも確認した。引用先の装置論文を独立に精査した結果ではなく、本論文に記載された構成と結果を評価する。コード実行、独立再現、追加資料の公開状況確認はしていない。

### 根拠

- 主眼は14チャネルの完全乾式筋電首輪、BioGAP-Ultraの低消費電力計測・通信、再装着を伴う評価であり、新しい認識原理ではない。（p.1, Section I contribution bullets; pp.1–2, Section II-A/B/E）
- 首輪は27接続部を備え、前面10差動対と左右各2チャネルを用いる。後面の4接地電極は電気的に短絡される。基板の16チャネル対応と首輪の14チャネルを区別する。（pp.1–2, Section II-A/B; p.2, Figure 1）
- BioGAP-UltraはGAP9、nRF5340、ADS1298を2個含み、信号を増幅率12・500samples/sで取得する。貢献の記述は24ビット計測とする。（p.1, Section I contribution bullets; p.2, Section II-B and Figure 1(d)）
- 対象は健康な1人で、up/down/left/right/forward/backward/go/stopの8語を通常発話と無声調音で収録する。未学習人物や未知語の認識ではない。（p.2, Section II-C）
- 各条件3セッション・各7バッチ・各語20反復で3360発話を収録する。提示後4秒の調音と1秒の休止、バッチ約14分と5分休憩を設け、セッション前に水で皮膚を清拭し首輪を付け直す。（p.2, Section II-C）
- 20Hz・4次の零位相高域通過と50Hzノッチの後、最初の1.4秒を7個の重ならない200ms窓に分け、特徴量を連結して1発話を表す。（p.2, Section II-D; Figure 2）
- 時間・周波数領域およびdb4ウェーブレットの特徴を使い、scikit-learnの既定設定のRandom Forestで8クラス分類する。特徴重要度に支配的な項目がないため全特徴を保持する。（p.2, Section II-D/E）
- 全セッション混合の層化5分割では各分割に全セッションが含まれる。leave-one-session-outは2セッションで学習し残る1セッションを評価するため、未知の人物を試す方式ではない。（p.2, Section II-E, Global model and Leave-one-session-out）
- 通常発話はセッション内モデルの平均85±7%、初回74%、全セッション混合87±3%、セッション除外64±18%と報告される。8クラスの偶然水準は12.5%。（p.3, Section III-A; Figure 3(a–c)）
- 無声調音の全セッション混合は68±3%、セッション除外は54±7%。著者は評価指標を正解率の平均と標準偏差と記載する。1人の実験なので参加者間標準偏差ではない。（p.2, Section II-E; p.3, Section III-B and Figure 4(b,c)）
- 22.2mWは継続的なデータ取得とBLE無線通信の電力として報告される。GAP9での分類実行や受信側を含む全体電力、電池持続時間は報告されない。（p.1, Section I contribution bullets; p.2, Section II-B/C/E; p.3, Section IV）
- 1人の提示同期・8語分類であり、自由文、患者、多人数、歩行、長時間装着、連続信号中の無入力や発話開始検出は評価しない。語彙と人数の拡張は今後の課題とされる。（p.2, Section II-C/D/E; p.3, Section IV future work）
- 無声での低下を活動筋数の減少に帰し、初回の低さを経験不足に帰す記述は著者の解釈である。要因を分離する対照実験や有意差検定は本文に示されない。（p.3, Section III-A/B）
- 200msは特徴抽出の窓長であり、7窓を連結する1.4秒の発話表現を使う。無線収録の実現を、200msの端末内オンライン認識が実証されたことと読み替えられない。（p.2, Section II-B/D/E and Figure 2）
- 先行研究の93%や89.6%との比較は語彙やクラス数、装置が異なると本文自身が述べる。同条件の直接比較や性能優位を示す試験ではない。（p.3, Section IV）
- 装着し直したセッションでの低下は測定されているが、全セッション混合の高い正解率や偶然水準超えだけで日常生活の信頼性・多人数汎化は保証できない。（p.2, Section II-C/E; p.3, Section III and Figures 3–4）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
