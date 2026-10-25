# Non-invasive electromyographic speech neuroprosthesis: a geometric perspective

Harshavardhana T. Gowda, Lee M. Miller  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2502.05762)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text+summary

Decodes silently articulated sEMG into phoneme sequences and English text without alignment to recorded audio, using a geometric representation of multi-site muscle activity. One healthy participant: PER 48.47% and WER 73.53% on large vocabulary; WER 14% on a 67-word date task.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 31-electrode wet surface EMG on face, jaw, lips and neck |
| Task | Silent speech to text (phonemes and words) |
| Vocabulary | Large vocabulary (over 6500 words); also 67-word closed set and NATO code words |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | PER 48.47%, WER 73.53%, held-out sentences, one participant; WER 14% on 67-word closed set |

**Limitations.** Main result from one healthy participant with 31 gel electrodes, a stationary amplifier and manual segmentation; word decoding depends on a language model; streaming and day-to-day stability are untested.

## 日本語レビュー

### 要点

声を出さない口の動きの筋電から、録音音声との対応付けなしで文字を推定する研究。健康な1人の大語彙条件で音素誤り率48.47%、単語誤り率73.53%。67語の日付文では単語誤り率14%だが、自由会話・未知人物・患者・逐次利用の性能ではない。

### レビュー

この研究は、録音音声を用意できなくても、声を出さずに動かした口や首の筋電と書き起こしから、発話内容を文字へ変換できるかを問う。主実験では31部位の筋電を記録し、計測点間の相関を行列にまとめる。その行列を学習データから求めた共通の座標系へ移し、時間変化を扱うモデルで音素列を予測して、言語モデルで単語に戻す。音声の時刻合わせは不要だが、音素書き起こしは必要で、収録の開始・終了は本人がマウスで指定する。健康な1人の約8時間、6500語を超える無声調音を使い、学習8000文・検証1000文・試験1970文に分けた。主結果は音素誤り率48.47%、単語誤り率73.53%。同じ再帰モデルへ周波数特徴を入れた比較の89.25%・100%より良いが、これはその入力とモデルの組み合わせにおける比較で、既存の無声認識全般を上回った証拠ではない。単語誤り率は文ごとの編集距離に基づく値で、73.53%正解や文章の成功率と読んではいけない。付録には異なる条件もある。1人が67語から作る日付文500件を調音した課題では、試験100文の音素誤り率13%、単語誤り率14%。一方、4人がアルファベットをNATO符号語で表す課題の文字誤り率は55.0～70.4%で、少ない学習データから実用的な綴り入力が完成したとはいえない。4人の結果があることも、未知人物へそのまま使えることとは別だ。手首筋電によるキーボード入力の8人評価では文字誤り率の改善を報告するが、これは無声発話の成績ではなく、特徴表現に加えて学習回数なども変えている。本研究の価値は音声教師なしの文字化と筋電表現の設計にある。双方向のモデルは文が終わるまで待つ必要があり、多数電極の装着、長期の再装着、患者、未知語、別人への適応は未解決である。

### この論文の価値

声を収録できない条件でも学習できる設計と、複数部位の筋活動の関係を入力表現へ明示する点。音声への同期を省く意義はあるが、書き起こしや収録区間の指定まで不要になるわけではない。

### それまでの到達点

先行する筋電音声合成の多くは、有声筋電・音声の対応や有声と無声の転送を利用する。共分散の幾何表現は筋電の動作分類などに既にあり、本論文は連続した無声文の音素列推定へ拡張する。

### 何が変わったか

音声を教師にせず、無声筋電と文の音素列だけで学習する。計測点間の相関を表す行列を共通基底に変換し、時間方向を扱う再帰モデルへ渡す。音声合成ではなく文字への変換を評価する。

### 分野での位置づけ

実際の無声調音を扱うSSI、すなわち声を出さずに情報を伝える手法の基盤研究。脳内の言葉を読む研究ではなく、顔や首の筋活動を伴う調音が必要。大語彙の直接文字化を示すが、臨床用の完成装置ではない。

### 実用上の意味

音声との対応付けが難しい利用者に向けた学習経路を検討する材料となる。主実験の単語誤り率は高く、少数語彙への制約で成績が変わるため、自由な会話と定型入力を分けて設計する必要がある。

### 前進した軸

algorithm; system_design; problem_reframing; 音声への時間対応を使わない無声筋電からの文字化と、計測点間相関の入力表現。限定された同一モデル比較でPERとWERが改善。

### 未解決の軸

大語彙の単語精度、未知語・未知人物、臨床、電極再装着と長期安定性、電極削減、逐次処理・遅延・電力、音素誤り率のランダム基準の実測、学習条件を揃えた表現比較。

### 後退・限定した軸

主実験の比較より悪化した指標は報告されない。ただし手首筋電の個人別比較ではUSER6が改善せず、図5では悪化する。67語の低誤り率を大語彙・符号語条件へ持ち込めない。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | 無声調音の筋電から音素列を推定し、英語の文字列へ変換する。補助評価は67語の日付文、NATO符号語による綴り入力、および手首筋電によるキーボード入力。 |
| 入力 | surface electromyography (sEMG) |
| センサ | 顔・顎・頬・唇・首の31計測電極、別途基準電極と接地電極。BrainVision actiCHamp Plusと能動単極電極、電解質ゲルを使い5000 Hzで収録。付録のNATO符号語課題は22計測部位。 |
| 装着部位 | face; jaw; lips; neck; cheek |
| 出力 | phoneme sequences; text |
| 語彙の種類 | 大語彙英語の文から音素列を予測し、語彙辞書付き言語モデルで単語へ変換。付録は閉じた67語または26種類の符号語。 |
| 語彙数 | 主収録は6500語超。単語復号にはLibriSpeech-100書き起こし約38000文・35000語を使用。付録は67語、またはアルファベット26文字に対応するNATO符号語。 |
| 指標と結果 | 主実験の平均音素誤り率PER48.47%、単語誤り率WER73.53%。同じGRUにスペクトログラムを入れる比較はPER89.25%、WER100%。67語の日付文ではPER13%、WER14%。4人のNATO符号語の文字誤り率CERは55.7/55.0/70.4/56.4%。別の手首筋電入力では8人平均の試験CERが言語モデルなし15.38±5.88%から14.03±5.27%、6-gramあり9.55±5.16%から7.95±4.54%へ改善。 |
| 評価方法 | offline; subject-dependent; held-out sentences; separate closed-vocabulary and typing benchmarks |

### 限界

- **技術：** 共通基底は個人の生理・計測条件に依存する。単語への復号は辞書と4-gram言語モデルに依存し、筋電だけで意味が一意に復元されるわけではない。双方向処理と文ごとの正規化は、報告構成のままの逐次処理を支えない。
- **評価：** 主結果は健康な1人・1種類の分割で、信頼区間や複数学習試行のばらつきは不明。試験文非重複と未知語評価は別。主比較は同一GRUへの入力置換に限定される。EMG2QWERTYではデータ拡張の省略、150対250エポック、重み減衰も異なり、表現だけの因果効果とはいえない。表2はp<0.015を記すが検定手順や±の定義の詳細は不明。
- **実運用：** 31計測電極・ゲル・配線・据置増幅器と手動区間指定を用いる。本文は逐次処理、日・月単位の安定性、電極ずれや疲労の検証を未実施とする。患者での成果を別の追試への言及から本研究へ取り込まない。
- **このレビューの範囲：** 固定arXiv 2502.05762v3の全15ページ、付録A–C、図1–9・表1–5を全文で確認し、PDF画像で電極配置、主要成績、少数語彙・4人評価を照合した。外部プロジェクト・コード・データの取得と実行、独立実験再現は未実施。書誌情報は固定コンテキストどおり保持する。

### 根拠

- 主貢献は健康な1人の無声筋電約8時間・6500語超のデータと、時間対応した音声を使わない筋電から音素・単語への変換である。（PDF p.2, §2.1 Our contribution）
- 計測点間の共分散を正定値化し、学習データの幾何平均から求めた共通基底Qで近似対角化した行列を時間列モデルへ入力する。正定値化の係数はη=0.1。（PDF p.3, §3.1 EMG data representation）
- CTC損失で筋電と音素列の厳密な時間対応を不要にし、40音素の確率を予測する。音素列から単語へは言語モデルを使う。（PDF pp.3–4, §3 Methods, §3.2; Figure 1）
- 共通基底Qは個人固有で、異なる人物の生理・解剖学的差は座標基底の変化として解釈される。人物間で同じ性能を得たという実験ではない。（PDF pp.4–5, §3.3 Geometric perspective aligns well with biology）
- 主収録は約11000文・6500語で、無声筋電だけを集め、有声筋電や音声を収録しない。単語復号用にLibriSpeech-100の書き起こし約38000文・35000語を用いる。（PDF p.5, §4 Data; p.6, §5 Results）
- 主実験は31部位の単極計測電極、別途耳の基準・接地電極、actiCHamp Plus能動電極、電解質ゲルで5000 Hz収録。80–1000 Hz帯域通過後、文ごと・チャネルごとに正規化する。（PDF p.5, §4.1 Experimental details; p.6, Figure 2）
- 参加者は座位で無声調音し、各文の開始・終了をマウスクリックで指定する。手動操作なしの常時認識を評価した手順ではない。（PDF p.5, §4.1 Experimental details）
- 主実験の学習・検証・試験は8000/1000/1970文。試験文は他分割にない。50 ms窓・20 ms刻みの31×31行列を3層GRUで100エポック学習し、最小検証損失を選択する。未知語だけの成績は示されない。（PDF p.6, §5 Results）
- 単語復号は音素から語への辞書とKenLMの4-gramモデルを組み合わせたWFSTを用い、探索幅は50。録音音声不要でも書き起こし・辞書・言語モデルは必要。（PDF p.6, §5 Results, WFST decoding paragraph）
- 表1の主実験は提案PER48.47%、WER73.53%、スペクトログラム比較はPER89.25%、WER100%。いずれも低い方が良い誤り率である。（PDF p.7, Table 1; p.6, §5 metric definitions; p.12, Figure 6 and Appendix B）
- 主比較は時間分解能と31×31入力形状を合わせ、同じGRUへ異なる表現を入れる。スペクトログラム側は少数の音素列へ崩れる。著者脚注もこの入力・復号器の条件内で解釈するよう求める。（PDF p.6, §5 spectrogram comparison; p.7, footnote 2）
- 図3・4はモデル規模と学習文数を増す範囲でPERが低下する傾向を示すが、調査範囲外の性能や実用水準を保証するものではない。（PDF p.7, Figures 3–4 and §5 Results）
- EMG2QWERTYは手首筋電によるキーボード入力であり、無声調音ではない。8人それぞれを一から学習し、100人事前学習や未知人物への評価は対象外。（PDF pp.7–8, §5.1 Comparison with prior work）
- EMG2QWERTY比較では入力置換のほか、SpecAugmentを省略し、学習を150から250エポックへ変更、Adamへ重み減衰10^-3を加える。表現だけの効果を分離した比較ではない。（PDF p.7, §5.1 final paragraphs）
- 手首入力8人の平均試験CERは言語モデルなし15.38±5.88%対14.03±5.27%、6-gramあり9.55±5.16%対7.95±4.54%。表2はp<0.015と記す。図5はUSER6以外の改善を示す。これは無声会話の成績ではない。（PDF p.8, Table 2, Figure 5, §5.1）
- 双方向GRUは文全体を必要とし、逐次・低遅延利用を支持しない。大語彙の健康な1人という制限と、日・月単位の安定性、電極移動、疲労を評価していないことを明記する。（PDF p.9, §7 Limitations）
- 本文が言及するALS利用者や因果モデルは別の追試であり、本論文の主実験で患者の通信や実時間音声を検証した結果として扱えない。（PDF p.9, §7 Limitations, follow-up study references）
- 先行研究のWERと本研究のWERは、収録、教師、時間対応、課題、評価法が異なるため一対一で比較しないよう付録Aが明記する。（PDF p.11, Appendix A Detailed literature review）
- 付録Bは1970試験文のPER・WER分布と平均48.47%・73.53%を示す。偶然基準97.5%は40音素の一様選択から計算するが、同じ復号条件で編集距離を測ったランダム対照の記載ではない。（PDF p.12, Appendix B, Figure 6 and chance-level formula）
- 少数語彙課題は1人が67語で構成する曜日・月・日・年の500文。各語群を時刻指定で提示し、31部位・5000 Hzで収録、370/30/100文に分割する。（PDF p.13, Appendix C.1 DATA SMALL-VOCAB）
- 少数語彙課題は1層GRUで100エポック学習し、67語集合への最小編集距離で単語に戻す。表3の平均PERは13%、WERは14%。自由な大語彙文の成績ではない。（PDF p.13, Appendix C.1 Results, Table 3 and Figure 8）
- NATO符号語課題は4人、22部位・5000 Hz、26文字を符号語で表現する。416/104/1968調音に分割し、1層GRUで学習する。本文は学習10分・試験50分と説明する。未知人物を保持した試験分割は示さない。（PDF pp.13–14, Appendix C.2 DATA NATO-WORDS）
- NATO符号語の文字誤り率は被験者1–4で55.7%、55.0%、70.4%、56.4%。26候補の音素列との近さで文字を選ぶ。図9は人物ごとのモデル規模とPERを示し、表4のCERとは区別する。（PDF p.14, Table 4, Figure 9, Appendix C.2）
- 表5は最良3文と最悪3文の定性的な復号例で、平均的な会話品質や患者での利用成績を示すものではない。（PDF p.15, Table 5）
- 倫理審査手続、参加者の書面同意・匿名化データ公開への同意を記す。著者は大学所有の未許諾の関連知的財産の発明者であることを開示する。（PDF p.9, §8 Ethical considerations and Conflict of interest）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
