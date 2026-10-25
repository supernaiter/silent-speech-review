# Advancing NAM-to-Speech Conversion with Novel Methods and the MultiNAM Dataset

Neil Shah, Shirish Karande, Vineet Gandhi  
arXiv 2024 · [arXiv](https://arxiv.org/abs/2412.18839)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text+summary

Compares ways to create target speech for converting non-audible murmur (NAM) to speech and releases the 7.96-hour MultiNAM dataset. Diff-NAM gives final WER 32.39%/38.94% for two speakers, below Lipvoicer but behind MFA-TTS (26.38%/32.61%).

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Bluetooth digital stethoscope behind the ear (NAM vibration) |
| Task | NAM-to-speech conversion; dataset |
| Vocabulary | Read sentences from LJSpeech (size not stated) |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Final WER 32.39%/38.94% (two speakers) for Diff-NAM vs 26.38%/32.61% for MFA-TTS |

**Limitations.** Only two healthy speakers whispering prompted text; data splits and test isolation unclear; no listening test, no patients, re-wearing, noise or latency evaluation.

## 日本語レビュー

### 要点

耳の後ろの微弱な振動を音声に変えるため、学習用音声の作り方を比較した研究。Diff-NAMの最終単語誤り率は2人で32.39%・38.94%と比較した映像利用法より低いが、両話者のNAMと文字を使うMFA-TTSの26.38%・32.61%には及ばない。価値は7.96時間の同時収録と教師音声設計にあり、患者向けの無音会話機器を実証したわけではない。

### レビュー

本論文は、非可聴つぶやき（NAM）の皮膚振動から音声を作る際、同時に録れない通常音声の代わりに何を学習目標にするかを扱う。市販の無線聴診器を耳の後ろに当て、健康な31歳の男女各1人からNAM・ささやき・顔映像・文章を計7.96時間集めた。小声のささやきで指定文を読む条件であり、口を動かさない内言や完全な無音会話ではない。提案Diff-NAMは映像と合成NAM特徴を条件にした拡散生成で教師音声を作り、別の系列変換器が実測NAMから最終音声を出す。ここを分ける必要があり、表IIの17.24%・21.73%は教師音声の単語誤り率で、最終出力では32.39%・38.94%となる。正解文字を使うLipvoicer教師による最終出力54.11%・59.66%より低い一方、両話者のNAMと文字を用いたMFA-TTSは26.38%・32.61%でさらに低い。したがって映像系との比較の改善であって、全条件で最高ではない。また教師音声作成に正解文字を使い、合成NAM生成器も実測NAMで学習するため、文字もNAM収録も不要な音声復元とはいえない。本文では学習と試験の分割や評価文数が明確でなく、対象の全映像・文字による特徴モデル追加学習と試験例の関係も未確認である。自動認識器の誤り率を人の聞き取り率に読み替えることはできず、部品別の効果、未知人物、患者、遅延、装着負担も未検証。SSI（声を出さずに伝えるための入力技術）研究としての意義は、教師音声を用意する選択肢と同時収録の基盤を示した点にある。

### この論文の価値

最終変換器の改良だけでなく、合成する教師音声の条件と質を切り分けて議論できる点。データ量があるMFA-TTSと映像系Diff-NAMの結果を並べ、利用可能な情報に応じた選択を促す。

### それまでの到達点

NAMでは通常の発声音声を同時に得られないため、別録り音声の時間変形、ささやきからのHuBERT-HiFi合成、NAMと文字の音素時間対応を用いるStethoSpeech系MFA-TTSが教師作成に使われてきた。映像からの合成にはCross-AttentionやLipvoicerがある。

### 何が変わったか

2人・7.96時間の4種類同時収録と、教師合成に使う情報を変えた比較を追加する。Diff-NAMは映像・合成NAMの条件付き拡散を取り入れるが、両話者を使うMFA-TTSを超える全面的な性能更新ではない。

### 分野での位置づけ

非可聴つぶやきの音声化における教師データ不足を扱う、データセットと学習目標設計の研究。無音入力の完成製品ではなく、学習用の音声をどう用意するかを検討する資料として重要。

### 実用上の意味

ささやきの収録が使えないときに、NAM・文字・映像のどの組合せを教師作成に利用できるかを比較する出発点となる。市販聴診器の収録例も参考になるが、そのまま患者向けの利用性能を示すものではない。

### 前進した軸

教師音声作成の選択肢; ささやきなしの学習目標; NAMと映像の同時収録基盤; 映像系教師を使う最終変換の誤り率

### 未解決の軸

未知人物・未知語への一般化; データ分割の独立性; 人の聞き取り; 各構成の独立効果; 患者利用; 手放し固定; 実時間・携帯利用

### 後退・限定した軸

Diff-NAMの最終WERは両話者のNAMと文字を使うMFA-TTSより高い。処理量や収録負担の増減は測定されていない。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | NAMから音声への再構成; 同時の通常発声音声を得られない条件での時間整合した教師音声作成; MultiNAMデータセットの構築 |
| 入力 | 耳の後ろの皮膚で拾う非可聴つぶやき（NAM）の振動。教師音声の合成には条件別にささやき音声、口元映像、正解テキストを用い、Diff-NAMは口元映像とNAM特徴、正解テキストを利用する。最終段のNAMから音声への変換と教師音声作成を分けて評価する。 |
| センサ | 市販のBluetooth接続デジタル聴診器を耳の後ろに当て、MacBook Proで顔映像と口元のささやきを記録。映像1920×1080・25 fps、NAMとささやき48 kHz。 |
| 装着部位 | 耳の後ろの皮膚; 口唇・顔 |
| 出力 | speech-audio |
| 語彙の種類 | LJSpeech由来の文章を読む課題。固定命令の分類ではないが、教師音声作成に正解テキストを利用し、未知語だけを分離した検証はない。 |
| 語彙数 | 語彙の固有語数は不明。MultiNAMはS1の2354発話とS2の969文を収録し、これは語彙数や独立した試験例数ではない。 |
| 指標と結果 | Whisper音声認識器による単語誤り率（WER）と文字誤り率（CER）。表IIのDiff-NAM: 教師合成音声のWERはS1/S2で17.24/21.73%、最終NAM変換音声は32.39/38.94%、そのCERは19.47/24.91%。Lipvoicerの正解文字条件の最終WERは54.11/59.66%、両者のNAMと文字を用いるMFA-TTSは26.38/32.61%、本人別MFA-TTSは56.65/69.45%。表Iのささやきから作るMFA-TTS教師音声は5.84/11.23%であり、最終NAM変換の成績ではない。 |
| 評価方法 | 保存済み収録に対する話者別の自動音声認識誤り率比較。表Iはささやき由来の教師合成音声、表IIはささやきを使わない教師合成音声と、それを使って学習した最終変換音声を分けて報告。人の聞き取り試験や実時間対話試験ではない。 |

### 限界

- **技術：** 正解文字を使う教師合成と、未知の発話内容をNAMから推定する最終課題を混同できない。Diff-NAMは学習時の合成NAM作成に実測NAMを必要とし、表IIでもLip・NAM・textを条件とする。映像だけ・NAM収録不要の系とはいえない。
- **評価：** 学習・検証・試験の分割割合、評価文数、文章重複の排除方法が本文では不明。AV-HuBERTを利用可能な全映像・文字で追加学習すると書かれ、試験例を隔離したか確認できない。誤り率の信頼区間、検定、反復学習、人の聞き取り評価は報告されない。
- **実運用：** 発話障害のある利用者、未知人物、別日・再装着、歩行や雑音条件の比較、装着負担、総遅延、消費電力は未評価。オフィス収録だけで雑音耐性や実用性は保証できない。
- **このレビューの範囲：** 健康な2人が小声のささやきで指定文を読む収録と、別の女性1人の既存データによる比較。完全な無音の口の動き、内言、自由会話や患者への適用の検証ではない。

### 根拠

- NAM振動・ささやき・顔映像・文字を同時収録し、市販Bluetooth聴診器を耳の後ろの皮膚に当てる。MacBook Proで1920×1080・25 fpsの映像と口元の音声、NAMとささやきを48 kHzで記録した。（p.2 Section II Datasets; Figure 1）
- 参加者は既知の聴覚・発話障害がない31歳の男性S1・女性S2で、LJSpeechの異なる文章を小声のささやきで読む。S1は2354発話・5.66時間、S2は969文・2.30時間、合計7.96時間。（p.2 Section II Datasets）
- 補助のCSTR NAM TIMIT Plusは女性1人の421文・40分・16 kHzのスタジオ収録で、NAM・ささやき・文字を含む。新規の患者試験ではない。（p.2 Section II Datasets, CSTR paragraph）
- 評価はWhisper認識器による誤り率。生のささやきのWERはCSTRで1.07%、MultiNAMのS1/S2で5.54/12.97%、生NAMはそれぞれ66.99%、200.50/192.77%と報告される。これらは人の聞き取り試験の結果ではない。（p.2 Section II Datasets, final paragraph）
- 処理は時間整合した教師音声の合成とNAMから音声への系列変換学習の二段階。ささやきからのHuBERT-HiFiと、NAMまたはささやきに正解文字を対応させMFAで音素長を求めFastSpeech2に与えるMFA-TTSを比較する。（p.2 Sections III, III-A, III-B）
- 映像系教師生成は通常の正解音声が対象データにないためLRS3で学習する。口元を88×88の灰色画像にし、対象の利用可能な全映像・文字対でAV-HuBERTをCTC損失により追加学習して特徴を抽出すると記述する。（pp.2–3 Section III-C, Data Preprocessing）
- Diff-NAMは映像と合成NAMで拡散モデルを条件付ける。LRS3の音声から合成NAMを得るためのHiFiGANは対象の実測NAMで学習するため、NAM収録を一切使わない方式ではない。（p.3 Section III-C, Diffusion Process）
- Diff-NAMは口元とNAM特徴を結合した1536次元の条件を用い、本人の画像特徴による条件付けを避ける。推論時の教師音声生成は読唇予測文字ではなく利用可能な正解文字を使う。（p.3 Section III-C, right-column continuation）
- 最終変換では6層の非自己回帰TransformerがNAM特徴から教師音声特徴を予測し、平均二乗誤差と文字予測のCTC損失を用いる。HiFiGANで予測特徴を音声化する。（p.3 Section III-D Seq2Seq learning network and speech decoder）
- ささやき由来の教師音声のWERは、HuBERT-HiFi/MFA-TTSがCSTRで23.77/41.07%、S1で100.14/5.84%、S2で84.53/11.23%。表Iは最終NAM変換出力ではない。（p.3 Table I; pp.3–4 Section IV-A）
- Diff-NAMの教師合成音声はS1/S2のWERが17.24/21.73%、CERが11.31/13.97%。最終NAM変換音声はWER32.39/38.94%、CER19.47/24.91%。（p.4 Table II, Diff-NAM row; Section IV-B NAM-to-speech conversion）
- 両話者のNAMと文字を使うMFA-TTSの教師WERはS1/S2で12.37/19.64%、最終WERは26.38/32.61%。本人別MFA-TTSでは教師WER23.81/33.62%、最終WER56.65/69.45%。（p.4 Table II, MFA-TTS all-speaker/per-speaker rows）
- Lipvoicerの正解文字条件は教師WER27.01/33.94%、最終WER54.11/59.66%。予測文字条件は教師WER39.04/49.99%、最終WER74.51/79.46%。正解文字のある条件と予測文字条件を分ける必要がある。（p.4 Table II, Lipvoicer GT/Pred rows; Section IV-B）
- Cross-Attentionの最終WERはS1/S2で93.04/87.98%、Mspec-Netは141.23/156.19%。Diff-NAMの最終WERは比較された映像系より低いが、両話者MFA-TTSより高い。（p.4 Table II, Cross-Attention, Mspec-Net, Diff-NAM, MFA-TTS rows）
- 本文は教師音声合成におけるNAM・ささやきへの依存を除くことを目指すが、Diff-NAMの合成NAM生成器は実測NAMで学び、表IIもLip・NAM・textを入力条件としている。映像のみやNAM収録不要という一般化は支持されない。（p.3 Section III-C; p.4 Table II Modality; pp.4–5 Section V）
- 学習・検証・試験の割合、試験文数、文章重複排除は本文に明示されない。対象の全映像・文字でAV-HuBERTを追加学習する記述があり、試験例の隔離は不明であって、漏洩があったと断定する証拠でもない。（pp.2–4 Sections II–IV, especially III-C Data Preprocessing and Tables I–II）
- 表I・IIの誤り率には信頼区間・検定・反復学習のばらつきが示されない。人の聴取評価や、前処理とNAM条件付けの各要素を独立に除いた比較も報告されない。（pp.3–4 Tables I–II; Section IV）
- 両話者と本人別のMFA-TTS比較は対象の2人を含む学習であり未知人物の試験ではない。人物ごとに文章と収録量が異なるため、差をデータ量だけの因果効果と確定できない。（p.2 Section II; p.4 Table II and Section IV-B）
- 図1では聴診器を手で耳の後ろに保持する。Bluetooth聴診器を用いることは確認できるが、手放し固定、携帯端末上の動作、長時間装着を検証した記述はない。（p.2 Figure 1 and Section II; pp.3–5 Sections III–V）
- 1秒のメルスペクトログラムは拡散モデルの学習区間であり、総応答遅延ではない。推論速度、電力、歩行・雑音条件比較、別日や再装着による評価は本文にない。（p.3 Section III-C Diffusion Process; pp.2–5 Sections II–V）
- 患者や極端に発声困難な場合は動機として議論されるが、MultiNAMの実験参加者は健康な2人。正解文字を使う教師生成と指定文収録から、患者の自由会話や未知語への一般化は実証されない。（p.2 Section II; p.3 Section III-C; p.4 Section IV-B）
- 著者は7.96時間のMultiNAMと試聴例・データの配布先を提示し、今後の課題として異なる情報間の時間対応改善を挙げる。配布物の完全性や実験の独立再現は今回確認していない。（p.1 Abstract and Introduction; pp.4–5 Section V Conclusion）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
