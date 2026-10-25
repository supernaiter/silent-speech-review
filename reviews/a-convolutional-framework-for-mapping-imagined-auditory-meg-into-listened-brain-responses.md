# A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses

Maryam Maghsoudi, Mohsen Rezaeizadeh, Shihab Shamma  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2512.03458)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

Maps imagined auditory MEG (melodies and poems) to listened-response MEG; 8-condition classification reaches 50.7% (chance 12.5%), and calibrated cross-subject CNN beats shuffled controls, but correlations are small.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Whole-head KIT MEG, 157 axial gradiometers |
| Task | Mapping imagined to listened auditory MEG |
| Vocabulary | 4 stimuli (2 melodies, 2 poems) |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 8-condition accuracy 50.7% (chance 12.5%); CNN mean r 0.0113 vs control 0.0063 |

**Limitations.** Very small correlations, no speech or text reconstruction, 11 trained musicians in a shielded room, and incomplete implementation and split details.

## 日本語レビュー

### 要点

音楽・詩を想像したときの脳磁図（MEG）から、聴取時の脳活動を予測する基礎研究。学習から外した参加者でも本人の一部データで調整すると比較用モデルを上回るが、相関は小さく、音声や文章の復元・実用的な意思伝達は未実証である。

### レビュー

本研究は、脳磁図（MEG）を用い、訓練済み音楽家が既知の2旋律・2詩抜粋を27秒間聴く／想像する課題で、想像MEGを聴取MEGへ変換できるかを検討したオフライン概念実証である。条件内相関は条件間より高く、相関ベース分類は平均50.7%（SEM4.1%、チャンス12.5%）だったが、これは8条件の分類であり、語や音の内容を読み出した成績ではない。個人別500msリッジ回帰は真の対応がシャッフルより高かった一方、被験者間には一般化しなかった。畳み込みニューラルネット（CNN）は2層ずつの1次元畳み込みencoder-decoderに被験者固有1x1較正層を加え、80:20訓練検証分割とAdam（学習率1e-4）、kernel7、ReLU、dropout0.1、早期停止、MSE・相関・時間差分・スペクトル損失を用いた。共有モデルの学習から外した参加者を本人の一部データで調整した真モデルの平均r=0.0113、シャッフル対照r=0.0063、p≪0.01と報告されたが、差の絶対値は小さく、Fisher変換後の集約方法も詳細不明である。想像内容の音声やテキストを復元した結果、実時間BCI、臨床ユーザー、歩行、別セッション・新規刺激での性能は示されない。取得157チャンネルに対して図5は155入力、DSSは最初の7成分を保持すると記すなど、再現に必要な詳細にも不明点が残る。

### この論文の価値

想像と聴取の神経応答を同一空間で比較し、個人内写像と被験者間共有写像を分けて検証した監査可能なデータ・設計例である。

### それまでの到達点

序論は、音楽想像が聴取に似た神経表現を示し得る一方、想像では試行ごとのタイミング変動、信号に対する雑音の大きさ、個人差が課題になると位置付ける。先行研究の時間軸を伸縮してそろえる処理にも言及する。

### 何が変わったか

想像MEGから対応する聴取MEGを予測する滑動窓リッジ回帰に加え、共有encoder-decoder時系列CNNへ被験者固有1x1畳み込み較正層を後段適用する。MSE・負相関・時間差分・スペクトル損失を併用する。

### 分野での位置づけ

imagined auditory neuroscience / non-invasive BCI proof of concept

### 実用上の意味

Low

### 前進した軸

想像と聴取の8条件を表現類似度・分類で監査し、個人内の滑動窓リッジ回帰から被験者間CNN写像へ評価軸を拡張した。

### 未解決の軸

新しい刺激、別セッション、本人データでの較正を使わない新規ユーザー、日常環境、想像内容の語句復元は未検証である。視覚メトロノームや共通の課題タイミングから独立した内容表現の検証も今後の課題と評価する。

### 後退・限定した軸

未学習被験者での平均相関は真モデル0.0113、シャッフル対照0.0063と小さく、仰臥位（あおむけ）・磁気シールド室・27秒試行に依存する。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | Map imagined auditory MEG responses to the corresponding listened-response MEG for melodies and spoken poems. |
| 入力 | 非侵襲MEG（157軸型グラジオメータ。図5のCNN入出力は155チャンネルだが、削減対応は記載されない）による聴取・聴覚想像の脳応答。 |
| センサ | Whole-head KIT MEG with 157 axial gradiometers; 1 kHz sampling, online 500-Hz low-pass and 60-Hz notch; magnetically shielded room. |
| 装着部位 | brain |
| 出力 | Predicted listened-response MEG time series; no decoded audio, transcript, or direct communication output is reported. |
| 語彙の種類 | Fixed musical and spoken-poem stimuli, repeatedly cued; no unseen content. |
| 語彙数 | 4 stimuli (2 melodies, 2 poem excerpts); no lexical vocabulary size reported. |
| 指標と結果 | 8条件分類の平均正解率50.7%（平均の標準誤差4.1%、偶然水準12.5%）。個人内リッジ回帰は真の対応がシャッフル対照より高くp≪0.001。共有学習から除外し本人データで較正した参加者で、CNNの平均r真0.0113、r対照0.0063、参加者群のWilcoxon検定p≪0.01。2人を除き真モデルが対照より高いと報告する。 |
| 評価方法 | 表現類似度の相関ベース条件分類、個人別500ms窓リッジ回帰、被験者間の符号化・復元型CNNを実施。CNNは試行順とチャンネル割当をシャッフルして同じ手順で再学習した対照と比較する。相関をFisher変換し、参加者群でWilcoxon符号付順位検定を行う。各参加者個別の有意差を示す検定ではない。 |

### 限界

- **技術：** 0.1–8Hz zero-phase Butterworth、DSS最初7成分、チャンネルz-score、100Hzダウンサンプル。CNNは27秒×100Hz全系列、kernel7、複数損失。実装コード、padding・batch size・epoch数、損失係数の詳細、較正サンプル数、分割・前処理境界が不足する。
- **評価：** リッジ回帰は1試行ずつ、CNNの共有学習は1人ずつ除外する評価だが、CNNの80:20分割単位、除外した人の較正データ量、前処理の学習範囲は明記されない。これは情報混入の証明ではなく、再現時の確認事項である。DSSによる7成分保持と図5の155入力（取得157）との対応も不明。損失係数を決める構成比較には言及するが、具体的な係数と比較結果は示されない。
- **実運用：** 157軸型グラジオメータのMEG、磁気シールド室、仰臥位、イヤホン、視覚メトロノームを要し、27秒全系列を入力するオフライン解析である。遅延、電力、移動、患者通信は評価されていない。
- **このレビューの範囲：** 音楽・詩の4刺激、8条件、11人の訓練済み音楽家、27秒試行、磁気シールド室でのオフライン評価に限定される。

### 根拠

- 11人の訓練済み音楽家（男性7人）が、2旋律と2詩抜粋の聴取・想像を各10試行ずつ実施し、各刺激27秒、合計80試行だった。（Experimental Paradigm, PDF pp.2–3）
- 相関ベース分類は8条件（聴取/想像×4刺激）を対象に平均50.7%、SEM4.1%、チャンス12.5%と報告される。これは条件識別であり音楽・詩の内容復号ではない。（Representational Similarity, PDF p.3）
- CNNは1次元畳み込みencoder-decoderに被験者固有1x1較正層を続け、想像MEGから聴取MEGを予測する。（Convolutional Neural Network, PDF pp.4–5）
- 共有学習から外し本人の一部データで較正した参加者の未使用データで、真モデルの平均r=0.0113、シャッフル対照r=0.0063、参加者群のWilcoxon検定p≪0.01と報告する。2人を除き真モデルが対照より高い。図はFisher変換後の相関を表示し、平均値の集約手順の詳細は不明である。（Section V.B, held-out-subject results and Figure 7, PDF p.5）
- CNNは被験者間共有写像を学習した後、held-out被験者の小サブセットで較正するが、そのサンプル数と分割単位は明記されない。（CNN training and calibration, PDF pp.4–5）
- 取得157チャンネルに対して図5は155チャンネル入力を示し、DSSで最初の7成分を保持する記述との対応も明確でない。（Sections II–III and Figure 5, PDF pp.3–4）
- 試行全体27秒を用いるオフライン解析で、実時間制約、可搬利用、臨床通信、移動下評価は報告されない。（Experimental Paradigm, PDF pp.2–3; CNN architecture/results, PDF pp.4–5）
- 著者は想像聴覚応答を聴取応答空間へ変換し、CNNが未見被験者へ転移すると主張する。（Abstract and Conclusion, PDF pp.1,5）
- 157軸型グラジオメータを備えたKIT装置で1kHz収録し、磁気シールド室で参加者はあおむけになった。前処理は0.1–8Hz帯域通過、DSSの最初の7成分保持、チャンネルごとの標準化、100Hzへのダウンサンプルと記載される。（Sections II–III, PDF p.3）
- 個人別リッジ回帰は500ms窓・100ms刻み、1試行ずつ除外する交差検証で評価され、真の対応は試行シャッフル対照より高い（Wilcoxon p≪0.001）。他の参加者で学習して除外した参加者で試すと低性能だったと述べるが、その数値は示さない。（Section V.A and Figure 3, PDF p.3）
- CNN共有部は他の参加者のデータを訓練80%・検証20%に分け、Adamの学習率10^-4、カーネル幅7、ReLU、dropout0.1、早期停止を使う。振幅誤差・負の相関・時間差分・スペクトルの4損失を組み合わせる。対照では試行順とチャンネル割当をシャッフルし、共有部と較正層を同じ手順で再学習する。（Section V.B, Equations 1–5, PDF pp.4–5）
- 損失の重みは構成比較によって決めたと述べるが、係数と比較結果は本文に掲載されない。評価出力は聴取MEG応答であり、語句認識の誤り率、音声復元の品質、実際の意思伝達成績は報告されない。（Section V.B (loss weights and results) and Section VI, PDF pp.4–5）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
