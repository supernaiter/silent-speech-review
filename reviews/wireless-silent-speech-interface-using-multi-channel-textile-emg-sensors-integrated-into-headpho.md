# Wireless Silent Speech Interface Using Multi-Channel Textile EMG Sensors Integrated into Headphones

Chenyu Tang, Josée Mallah, Dominika Kazieczko, Wentian Yi, Tharun Reddy Kandukuri, Edoardo Occhipinti, Bhaskar Mishra, Sunita Mehta, Luigi G. Occhipinti  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2504.13921)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text+summary

Integrates dry textile EMG electrodes into headphone earcups to classify 10 silently mouthed command words. Reports 96% accuracy on a random 80/20 sample-level split across 4 participants.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 4-channel dry textile EMG electrodes in headphone earcups |
| Task | Silent command word classification |
| Vocabulary | 10 English commands |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 96% accuracy, 10 words, 4 participants, random sample-level 80/20 split (76.5% without filtering) |

**Limitations.** Only 4 participants with a sample-level random split; unseen users, other days, re-wearing, walking, latency and power consumption are untested.

## 日本語レビュー

### 要点

ヘッドホンの布製筋電電極で無声の10語を識別し、4人の標本を無作為に分けた試験で正解率96%を報告。装着方法と信号処理の統合に価値がある一方、未知の利用者・別日・自由会話への有効性や、実機の応答時間・消費電力は未確認。

### レビュー

この論文は、顔や首に電極を貼る代わりに、ヘッドホンの耳当てを無声の操作語入力に使えるかを調べる。導電材料を塗った布製の乾式電極で4チャネルの筋電を取り、Wi-Fiで外部の計算機へ送る。1秒に1000点を収録し、各語に対応する3秒区間を周波数フィルタで整えてから、信号の特徴に重みを付ける1D SE-ResNetで分類する。出力はOpenやStopなど事前に決めた英語10語で、自由文や合成音声ではない。4人から収録した標本を無作為に学習80%・試験20%へ分け、全体正解率96%を報告する。フィルタを外すと本文の値は76.5%となり、単一チャネルでも成績が下がる。この比較は、モデルだけでなく前処理と複数計測点が重要であることを示す。ただし4人を学習と試験で分けた結果ではなく、初めて使う人や別日の性能は分からない。各語100回という記載の集計単位、試験の繰り返し回数、図の誤差棒の意味も不明である。接触のよいチャネルほど重みが大きい例は示すが、ネットワーク内部の特徴チャネルから物理的な4電極へ重みを対応付ける方法は十分に説明されない。重みの図や特徴がまとまる図だけで、接触状態を正確に測れたことや日常動作での頑健性が証明されたとは読めない。また、著者のマイクロ秒単位の処理時間は演算量からの見積もりで、3秒の入力収集と無線通信を含む実測ではない。消費電力、電池持続時間、装着感の定量評価も示されていない。評価すべき点は、既存の布電極と認識方式をヘッドホンへまとめた装着型の試作である。96%を日常会話や発声困難者への製品性能に広げず、人物・日・装着し直しを分けた試験と実機の応答計測を次の課題としたい。

### この論文の価値

顔に貼り付ける装置とは別の装着方法を提示し、フィルタと複数の計測点が小語彙認識を支えることを比較している点。高い分類成績そのものより、装着の容易さと接触安定性を両立するための試作として意味がある。

### それまでの到達点

表面筋電による無声語認識、乾式タオル電極、残差ネットワーク、特徴チャネルの重み付けは既存研究にある。顔や首へ貼る電極は装着負担があり、乾式電極では接触圧の変化が信号を乱す。

### 何が変わったか

既存のタオル電極を日常的なヘッドホンへ組み込み、無線4チャネル計測と1D SE-ResNetを組み合わせる。中心的な差分は計測部の装着形態と接触変動への処理の統合で、新しい筋電計測原理ではない。

### 分野での位置づけ

表面筋電を使う装着型SSI、つまり声を出さずに操作語を伝える装置の試作研究。脳信号による内言の解読でも、任意の会話を復元する研究でもない。

### 実用上の意味

ヘッドホンを利用した少数の操作語入力の設計参考になる。ただし未知の利用者、装着し直し、別日、歩行、患者、長時間利用で性能を維持するかは未確認。

### 前進した軸

system_design; problem_reframing; 耳当てへの無線筋電計測の統合。フィルタと4チャネルを使う固定10語分類で96%を報告。

### 未解決の軸

未知人物・別日・装着し直しへの汎化、物理電極と内部重みの対応、SE単体効果の統制、語数拡張、誤作動、長時間装着、携帯端末実測、低電力性、臨床適用。

### 後退・限定した軸

顔面貼付電極に対して接触圧が変わりやすいと著者が認める。フィルタ除去で96%から76.5%へ低下し、単一チャネルでも大きく低下。従来装着形態との同条件の性能差は不明。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | 声を出さずに口を動かしたときの筋電から、機器操作用の英語10語を識別する。自由文の認識や音声合成ではない。 |
| 入力 | ヘッドホンの耳当てに組み込んだ乾式布電極による4チャネルの表面筋電。無声の調音に伴う筋活動を入力とする。 |
| センサ | グラフェン/PEDOT:PSSを塗布したタオル繊維電極、4個のSeeedStudio筋電読出し回路、ESP32-S3、LiPo電池。1kHzで収録し、Wi-Fiで外部のPCまたは携帯端末へ送る構成。図1には4計測点に加えて参照と接地も示す。 |
| 装着部位 | 耳当てが接触する耳周囲の皮膚。図1に配置図はあるが、各電極の解剖学的位置や間隔の詳細は不明。脳内の言葉を読む方式ではない。 |
| 出力 | 10種類の操作語の分類ラベル。文章や音声波形を生成するものではない。 |
| 語彙の種類 | closed-set：事前に定めた英語の操作語。 |
| 語彙数 | 10語：Open、Close、Start、Stop、Yes、No、Next、Back、Okay、Cancel。 |
| 指標と結果 | 著者報告の全体正解率96%。フィルタなしは本文で76.5%、差は19.5ポイント。単一チャネルでは約40%低下と本文にあるが、相対比かポイント差かは明示されず、正確な値を補わない。図6は1D SE-ResNet、1D ResNet、1D VGG、SVM、RF、MLP、XGBoostを比較するが、棒上の数値や誤差棒の定義はない。図4ではOpen・Start・Cancelが100%、Backが90%、残り6語が95%。 |
| 評価方法 | 4人・10語の標本単位の無作為80/20分割で正解率を評価。複数分類器、フィルタの有無、4チャネルと最良単一チャネルを比較し、混同行列、重みの例、特徴分布の図を示す。人物別・日別の独立試験ではない。 |

### 限界

- **技術：** 乾式接触の圧力変動、ずれ、繊維間の空隙が信号を乱し得る。SEが重み付けする内部特徴と物理電極の対応手順は不明。3秒の切り出し開始条件や連続入力中の無発話の扱いは示されない。
- **評価：** 4人・固定10語・標本単位の無作為分割。100回の集計単位、人物別内訳、セッション構成、検証集合、反復・誤差棒の定義・統計的有意差は不明。図6の他分類器との詳細な条件統一も十分に示されない。
- **実運用：** 外部計算機へ無線送信する構成で、実機全体の遅延・電力・電池持続時間は不明。長期装着、歩行、装着し直し、未知利用者、患者、自由会話は未検証。銀ペースト接着による試作は量産性に課題があると著者自身が述べる。
- **このレビューの範囲：** 固定arXiv 2504.13921v1の全9ページを読み、PDF画像で図1–7・表I・Algorithm 1を照合。書誌情報は固定コンテキストを保持。外部のデータやコードの配布状況の調査、コード実行、独立再現、臨床的有効性の検証はしていない。

### 根拠

- 耳当てに4つの乾式布製筋電電極を組み込み、4読出し回路、ESP32-S3、LiPo電池で構成する。図1は計測4点のほか参照・接地点も示す。（pp.2–3, II.A and Fig.1）
- 電極はグラフェン/PEDOT:PSSを塗布したタオル繊維で、著者らの既存電極研究を利用する。表面筋電の計測であり内言や脳活動の直接解読ではない。（pp.2–3, Introduction and II.A.1）
- 筋電は1kHzで取得し、Wi-Fiで外部のPCまたは携帯端末へ送る。認識部までESP32-S3で実行する構成とは記されていない。（pp.2–3, Fig.1 caption and II.A.2）
- 各操作語に対応する3秒の区間は1チャネル3000点で、4次Butterworthの20–450Hz帯域通過フィルタを各チャネルへ適用する。（p.3, II.B.1 Preprocessing and Fig.2）
- 1D SE-ResNetは残差構造の中で時間平均した特徴から重みを求め、特徴チャネルへ掛ける。最終出力は10語の分類確率。（p.4, II.B.2 equations and Fig.3）
- 本文の学習用拡張は最大±100msの時間ずらし、信号対雑音比30dBのガウス雑音、0.9–1.1倍の倍率、±0.1mVのオフセット。Algorithm 1は雑音の標準偏差0.02を記すが、両表現の換算条件は不明。（pp.4–5, II.B.2 augmentation bullets and Algorithm 1 Step 2 (PDF image)）
- 参加者は4人。各語を4人の間で100回反復したと記すが、全員合計か各人かの集計単位は十分明確ではない。均衡データの80%を学習、20%を試験へ標本単位で無作為に分ける。（p.5, III.A Collected Silent Speech Dataset）
- 表Iの10語はOpen、Close、Start、Stop、Yes、No、Next、Back、Okay、Cancel。未知語を独立に試験する設定ではない。（p.5, Table I and III.A）
- 著者は4チャネルの無声操作語分類で全体正解率96%を報告する。これは固定10語の標本無作為分割での結果。（p.5, III.B Model Performance; p.6 Fig.6 caption）
- 図4の対角値はOpen・Start・Cancelが100%、Backが90%、残り6語が95%。BackからCancelへの誤分類は10%と図示される。（p.5, Fig.4 confusion matrix (PDF image); p.6 III.B discussion）
- フィルタを外した1D SE-ResNetの正解率は本文で76.5%、標準構成は96%。19.5ポイントの差はこの2値の単純差である。図6の棒には正確な数値の注記がない。（p.7, III.D.1; p.6 Fig.6 (PDF image)）
- 単一チャネル条件は最良の1チャネルを用い、1D SE-ResNetの正解率が約40%低下すると本文に記す。相対比とポイント差の区別、正確な単一チャネル値は本文で明示されない。（p.7, III.D.1 Single Channel paragraphs）
- 図6は1D SE-ResNet、1D ResNet、1D VGG、SVM、RF、MLP、XGBoostについて標準・フィルタなし・単一チャネルを比較する。誤差棒の定義、反復回数、統計検定は本文に示されない。（pp.6–7, III.D.1 and Fig.6 (PDF image)）
- 図5の例では接触の安定したチャネル1・2に、不安定な3・4より大きな重みが付く。著者は適応的選択の根拠とする。接触状態別の集計試験規模は記されない。（p.6, Fig.5 and III.C）
- 数式とAlgorithm 1は畳み込み後の内部特徴チャネルにSEを適用するが、図5の4物理電極ごとの重みへどう対応させるかは十分に説明しない。重みの例だけから接触状態を因果的に検出したとは判断できない。（pp.4–6, II.B.2 equations, Algorithm 1, Fig.5 and III.C）
- 図7は生の入力と学習された特徴のt-SNE可視化を比較する。特徴分布のまとまりは示すが、未知の人物や別日の独立評価ではない。（p.7, III.D.2 and Fig.7）
- 著者は推論あたり約10^7演算とCPU性能10GFLOPs/msを仮定し、マイクロ秒単位の遅延を述べる。測定端末と実測結果は示されず、3秒入力、通信、前処理を含む応答時間を保証しない。（p.3, II.A.2 last paragraph and II.B.1; p.5 II.B.2 realtime claim）
- 乾式電極では接触圧変化、微小なずれ、繊維と皮膚間の空隙に伴う不安定さがあると著者自身が説明する。歩行や長時間装着の定量試験は示されない。（p.4, II.B.1; pp.7–8 IV. Discussion）
- 著者は銀ペースト接着による試作の量産性、少ない語彙と参加者、端末内処理の改善を課題として挙げる。大規模利用、未知の利用者、患者に対する検証済み性能ではない。（p.8, IV. Discussion limitation paragraphs）
- 電池駆動・低電力・快適さは主張されるが、消費電力、電池持続時間、重量、装着感の定量評価は本論文で報告されない。連続入力での無発話判定や誤作動率も不明。（pp.3–5, II.A.2 and II.B; pp.7–8 IV. Discussion and V. Conclusion）
- 本レビューの評価では、新規性の中心は既存の筋電用布電極・無線読出し・SE付き残差分類器をヘッドホンにまとめた装着設計。独立した新しい計測原理や汎用学習原理の提案ではない。（pp.2–4, Introduction, II.A and II.B.2; pp.8–9 references 22–25）
- 人物を分けた試験、別日や装着し直しの試験、収録セッション内訳、検証集合の分割、最適化法・学習率・学習反復数は明記されない。4人の標本分割の96%から人物非依存の性能を導くことはできない。（p.5, Algorithm 1 and III.A; pp.6–8 Results and Discussion）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
