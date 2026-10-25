# IR-UWB Radar-Based Contactless Silent Speech Recognition with Attention-Enhanced Temporal Convolutional Networks

Sunghwa Lee, Jaewon Yu  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2509.26409)

**Section:** [Radar, RF & Wi-Fi](../README.md#radar-rf--wi-fi) · **Review basis:** full_text+summary

Contactless IR-UWB radar in front of the lips with an attention-enhanced TCN classifies 50 English words for one user at 91.1% mean accuracy, versus 74.0% for a hand-crafted baseline.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Novelda IR-UWB radar near lips (5-10 cm) |
| Task | Isolated word recognition |
| Vocabulary | 50 English words |
| Speaker | Speaker-dependent |
| Session | Cross-session |
| Online / offline | Not stated |
| Key result | 91.1% mean accuracy, 50 words, leave-one-session-out (baseline 74.0%) |

**Limitations.** Single participant, requires alignment before each utterance, no ablations or statistics, and no unseen users, words or free posture tested.

## 日本語レビュー

### 要点

唇の近くに置いた非接触レーダーで、1人の英単語50語を平均91.1%の正解率で分類し、従来方式の74.0%を上回った。別の人、未知語、自由な姿勢や日常会話での性能は未実証。

### レビュー

この研究の価値は、新しいセンサの発明ではなく、非接触レーダーの反射信号から単語の特徴を直接学習できることを、同じ人の未学習セッションで比較した点にある。唇の正面5〜10cmに置いたIR-UWBレーダーを使い、30歳の男性1人が英単語50語を20回ずつ発音した計1000標本を収録する。各発音前には基準信号との相関による位置合わせがある。軽い前処理後の信号を時間方向の畳み込みと注意機構で処理し、既知50語のいずれかに分類する。20セッションを順にテストへ回した平均正解率は91.1%で、手設計特徴とDNN–HMMの74.0%を17.1ポイント上回る。提案方式の各回の正解率は84〜98%、著者報告の標準偏差は3.3%で、従来方式の10.3%より小さい。ただし全回で勝つわけではなく、第7回は92%対94%で従来方式が上回る。表の20値から平均と標本標準偏差の丸め値は確認できるが、有意差検定や注意機構を外す比較はなく、改善を注意機構だけの効果とは断定できない。これは20人の実験でも、未知の単語を読める結果でもない。声を入力しない方式として有望だが、無声収録を音響で確認した手順、別日への安定性、距離や姿勢の変化、患者での性能は不明。約100フレーム毎秒の信号取得も認識の実時間性を意味せず、全区間を集約する分類器の実測遅延は報告されない。現時点では、位置を合わせた1人の限定語彙認識を改善した研究として評価すべきで、日常会話や一般利用者での実用性能に広げてはいけない。

### この論文の価値

レーダー信号の手設計特徴から学習可能な特徴へ移る際の、限定条件下の比較資料。セッションを分離した成績と、非接触でも位置合わせが必要という実用上の条件を併せて読む価値がある。

### それまでの到達点

本文が引用する従来のIR-UWB方式は手設計特徴を用い、単語や母音・子音・句の認識を扱ってきた。本論文は既存装置と収録画面を引き継ぎ、唇の正面のレーダー1台を使用する。

### 何が変わったか

レーダーの時間・距離方向の信号に軽い前処理を施し、手設計特徴とDNN–HMMの組から、特徴抽出と50クラス分類を同時に学習する構成へ移す。同じ人の未学習セッションでの比較であり、未知語や話者非依存への拡張ではない。

### 分野での位置づけ

唇付近の電波反射を使う非接触の無声発話インターフェース。固定語分類に対する学習方式の改善であり、開放語彙や汎用会話システムではない。

### 実用上の意味

身体にセンサを貼らずに限定語を入力する方式の候補。位置合わせを伴う単一利用者の研究室評価なので、実際の意思伝達の使いやすさや臨床的価値は不明。

### 前進した軸

この1人・固定50語のセッション分離評価で、平均分類正解率とセッション間の安定性を改善。手設計特徴への依存を減らす学習方式を示す。

### 未解決の軸

未学習の利用者・単語、自由会話、距離や姿勢の変化、別日での再現性、注意機構の個別寄与、実時間処理、患者での有効性。

### 後退・限定した軸

測定に基づく退行は不明。計算量、推論遅延、消費電力、学習データ量と精度の関係は従来方式と比較されない。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | speech-recognition |
| 入力 | radar |
| センサ | Novelda NVA-R661を唇正面に1台使用。元装置は正面と頬下の2台だが、本実験は正面のみ。距離5〜10cm、MATLAB収録画面、各発音前の基準位置との信号相関による位置合わせ。1フレーム256距離ビン、約100フレーム毎秒。 |
| 装着部位 | lip |
| 出力 | 既知の英単語50クラスのラベル。自由文の文字列生成や音声合成ではない。 |
| 語彙の種類 | 固定された英単語50語の閉じた集合。各単語を20セッションで反復する。 |
| 語彙数 | 50 |
| 指標と結果 | 表I: 20回の平均単語分類正解率は提案91.1%、手設計特徴＋DNN–HMM74.0%（差17.1ポイント）。提案の範囲84〜98%、比較方式56〜94%。第7回は提案92%対比較94%。本文のセッション間標準偏差は3.3%対10.3%で、表の20値の標本標準偏差を小数第1位に丸めた値と一致する。検定法・p値・信頼区間は未報告。文章の単語誤り率ではない。 |
| 評価方法 | 20セッションのうち1つをテストに回す評価を20回実施。残る19のうち16を学習、3を検証に使用し、検証セッションは固定乱数種で各回選択。同一利用者・既知50語の単語標本分類正解率を算出。 |

### 限界

- **技術：** 前処理なしの生信号ではなく、静的反射と平均値の除去、距離ビン1〜100の選択を含む。可変長系列のバッチ化やマスクの詳細は不明。自己注意・SEの除去比較がなく、個別の改善寄与は識別できない。
- **評価：** 参加者1人の20分割であり20人評価ではない。別日の収録かは不明。注意やSEを外す比較、複数乱数設定の再学習、信頼区間・有意差検定、語ごとの混同行列は示されない。従来方式の具体的な再学習・調整条件も本論文では十分に説明されない。
- **実運用：** 卓上装置で唇とアンテナの距離は5〜10cm。各発音前に基準信号との相関で位置を合わせる。自由な頭部運動、歩行、遮蔽物、異なる環境、患者、連続会話での試験はない。
- **このレビューの範囲：** arXiv v1全5ページの本文・式1〜8・参考文献を確認し、図1〜3と表IをPDF表示で照合。表の平均・標準偏差のみ再計算。引用先の実験を本論文の実績として補わず、コード・原データによる独立再現は行っていない。書誌情報は固定コンテキストを保持。

### 根拠

- 著者は、軽い前処理後のIR-UWB信号に時間畳み込み・自己注意・SEを組み合わせ、手設計特徴方式より高い50語分類正解率を得たと主張する。（p.1 Abstract; pp.1–2 I Introduction; p.4 V Conclusion）
- 先行研究由来の2台構成のうち、本実験はNovelda NVA-R661の唇正面1台のみを使用。唇から5〜10cmで、各発音前に基準信号との相関を使って位置を合わせる。（p.2 II.A Data Collection, paragraphs 1–3; Fig.1）
- 参加者は30歳の韓国語母語男性1人で、英語教育20年以上、既知の発話・聴覚障害なし。英単語50語を20セッションで反復し、計1000標本を得る。（p.2 II.A Data Collection, participant and stimulus paragraphs continuing below Fig.1）
- 1フレームは256距離ビンで約100フレーム毎秒。α=0.95の指数移動平均で静的反射を除去し、ビン1〜100を選択、各フレームの平均を減算してM×100の入力を得る。前処理が完全に不要な方式ではない。（p.2 II.B Data Representation）
- 入力64チャネルから5段で96/128/256/384/512へ拡張し、間隔1/2/4/8/16の畳み込み、自己注意、SE、残差接続を用いる。全区間平均と512→256→50の分類部で単語ラベルを出力する。（p.3 II.C, Figs.2–3, Eqs.1–5; p.4 II.C, Eqs.6–8）
- 20セッションから1つをテスト、残りを学習16・検証3に分ける評価を20回行う。検証セッションは固定乱数種で選ぶ。同一人の既知語のセッション分離であり、未知の利用者・単語を評価する設計ではない。（p.4 III Experiments, first and final paragraphs; p.2 II.A）
- AdamWの初期学習率0.0008、重み減衰1e-4、暖機付きcosine、batch32、ラベル平滑化0.15、早期終了patience18、勾配上限1.0を記載し、通常70〜140epochで学習する。dropoutは0.25。（p.4 III Experiments, training paragraph; p.3 II.C convolution description; p.4 classifier description）
- 表Iの20回平均は提案91.1%、手設計特徴＋DNN–HMM74.0%で、差は17.1パーセントポイント。提案84〜98%、比較56〜94%。文章の単語誤り率ではなく単語標本分類の正解率である。（p.4 Table I; III Experiments metric definition; IV Results）
- 表I第7回は提案92%対比較94%であり、全回で提案方式が優れるわけではない。著者報告のセッション間標準偏差3.3%対10.3%は、表の20値から計算した標本標準偏差を小数第1位に丸めた値と一致する。（p.4 Table I, session7 and all20 rows; IV Results, consistency paragraph; reviewer arithmetic check）
- 評価に注意機構やSEを外す比較はなく、改善を個々の要素へ因果的に割り当てられない。本文はsignificantと表現するが、検定法・p値・信頼区間・複数乱数設定での再学習成績を示さない。（pp.3–4 II.C; p.4 III Experiments, IV Results and Table I (reported comparison scope)）
- 収録は1人・固定語彙・位置合わせ付き。セッションの日程、正確な語一覧、無声を音響で確認する手順は本文から不明。20セッションを20人・20日や未知語認識と読み替える根拠はない。（p.2 II.A Data Collection; p.4 III Experiments (reported collection and split scope)）
- 序論は日常環境での安定性やプライバシーの利点を述べるが、本実験は5〜10cmで位置を合わせた収録に限られる。距離・姿勢・環境の変化、歩行、患者、プライバシー脅威への評価は報告されない。（p.1 I Introduction, IR-UWB advantages; p.2 II.A and Fig.1; p.4 III–IV）
- 約100フレーム毎秒は計測速度であり認識遅延ではない。全時間位置間の自己注意と全区間平均を含む分類器のオンライン動作、計算機、実測遅延や消費電力は報告されない。（p.2 II.B; p.3 II.C Eq.4; p.4 Eq.8 and III–IV）
- 既存のレーダー・収録系を使い、手設計特徴＋DNN–HMMから軽い前処理と学習特徴の分類器へ変えた点が中心。センサの初提案でも、自由文生成・音声合成の実証でもない。比較方式の具体的な再学習・調整の詳細やデータ・コード公開先は本論文では確認できない。（p.2 I–II.A; pp.3–4 II.C and III Experiments; p.5 References [26]–[29]）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
