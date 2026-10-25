# Multi-Subject Pretraining Enables Short-Calibration Personalization for Closed-Corpus Surface EMG Speech Decoding

Chenqian Le, Beatrice Fumagalli, Yasamin Esmaeili, Xupeng Chen, Tianyu He, Nikasadat Emami, Adeen Flinker, Yao Wang  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2609.21288)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text+summary

Multi-subject pretraining plus target fine-tuning for 8-channel face/neck sEMG decoding of a closed 50-sentence corpus (27 subjects, LOSO); 21.7% CER / 31.9% WER, with 3-minute calibration not significantly worse.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 8-channel lower-face/neck surface EMG |
| Task | Closed-corpus sEMG-to-text decoding |
| Vocabulary | 50 closed TIMIT-based sentences |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 21.7% CER / 31.9% WER, pretrain + fine-tune, closed 50 sentences; 78.6% CER on unseen sentences |

**Limitations.** Evaluation sentences can appear in other subjects' pretraining; performance collapses on unseen sentences; offline only, healthy adults, no latency or electrode re-donning tests.

## 日本語レビュー

### 要点

標準化8ch顔／頸部sEMG・閉じた50文・27人LOSOで、多被験者事前学習＋対象微調整は21.7% CER / 31.9% WER。3分キャリブレーションは約13分と有意差なし（20.5%/31.7%）。未見文では78.6% CERまで崩壊。開語彙や臨床完成ではない。

### レビュー

本論文はLeら（NYU）による閉じたコーパス上のクロス被験者sEMG文字復号の個人化研究であり、Kimuraの提案ではない。対象は27人の発話典型健常者で、各人が平均21.3分（各0.5時間未満）のAloudとMimedの顔／頸部8チャネルsEMGを提供する。コーパスはTIMIT由来の50文で、固定の45/5分割を全被験者で共有するleave-one-subject-outである。復号はGaddy & Kleinの公開畳み込み–Transformer＋CTCを初期化し、他26人で事前学習したのち対象者を微調整する。主結果（Table 1）ではPretrain + fine-tune (MLP) がマクロ平均21.7% CER / 31.9% WERとなり、対象者なしのゼロショット49.3% CER、公開チェックポイントの直接微調整68.0% CERを有意に上回る。ランダム初期化からの多被験者事前学習は5/27 foldで未収束を含み44.9% CERにとどまり、公開チェックポイント初期化の寄与が大きい。キャリブレーション分数スイープ（Table 2）では3分で20.5% CER / 31.7% WERとなり、約13分フル（21.7%/31.9%）との差は有意でない（p=0.27/0.88）。ただし同等性を示したわけではなく、最短で非有意だった予算としての解釈に留まる。被験者固有MLPアダプタに検出可能な利点はない（CER差−0.8pt、p=0.44）。事前学習人数を1から26へ増やすとCERは74.4%から21.7%へ下がる。一方、評価5文を全sEMG学習から除外した未見文条件では同一テストで78.6% CER / 99.9% WERまで崩れ（Table 3）、閉コーパス適応を開コンテンツ復号と読んではいけない。これはAESSI（耳周囲・較正なし別日）やSilentWear（繊維）、VTP（カメラ）、SilentSpeller（EPG）、SottoVoce（超音波）とはセンサも問も異なる。価値は、標準化モンタージュの限られたデータで「他者事前学習＋短い対象キャリブレーション」がどこまで効き、どこで文面記憶に依存するかを数値化した点にある。

### この論文の価値

閉じた50文・標準化顔／頸部sEMGにおける、多被験者事前学習のスケーリングと3分級キャリブレーション、および未見文崩壊というスコープ境界の定量資料。

### それまでの到達点

単一被験者の大規模sEMG–文字復号（Gaddy & Klein）やモード間比較（同グループ2604.18920）、AESSIの耳周囲較正なし別日再利用、SilentWearの繊維EMGは存在するが、標準化顔／頸部モンタージュでの多被験者事前学習×短時間キャリブレーション×未見文境界の同時定量は限定的だった。

### 何が変わったか

単一被験者長時間学習や閉集合分類精度競争から、限られた対象者データでの多被験者事前学習の効き方と、3分級キャリブレーションの実用性、および未見文での崩壊点を同一系で示す評価設計へ移す。

### 分野での位置づけ

非侵襲の顔／頸部sEMGによる閉コーパス文字復号のクロス被験者個人化研究。同グループのモード比較（2604.18920）の隣接。AESSI・SilentWear・VTP・SilentSpeller・SottoVoceとはセンサと評価問が異なる。

### 実用上の意味

新しい利用者に何分のラベル付きsEMGが要るか、他者データ事前学習がどこまで効くかを、閉じた文セット前提で見積もる参照になる。開コンテンツ入力の完成形ではない。

### 前進した軸

多被験者事前学習の被験者数スケーリングと、対象者キャリブレーション分数（1/3/5/10/≈13分）を同一閉コーパスLOSOで接続し、未見文崩壊をスコープ境界として明示した。

### 未解決の軸

電極再装着・縦断ドリフト、臨床構音障害利用者、開コンテンツ文生成、ランダム初期化の最適化再設計、より大きな事前学習コホートでのチェックポイント依存の解消。

### 後退・限定した軸

未見5文を全sEMG学習から除外するとCER 78.6% / WER 99.9%へ急落。開語彙・臨床・オンライン実時間は未検証。Subvocalは解析から除外。

### 評価条件

| 項目 | 内容 |
| --- | --- |
| 課題 | Closed 50-sentence corpus sEMG-to-text decoding with leave-one-subject-out personalization. Not open-vocabulary conversational SSI. |
| 入力 | Lower-face/neck surface EMG (8 channels). Aloud and Mimed used; Subvocal excluded from decoding analyses. Not around-ear AESSI, textile SilentWear, camera VTP, EPG, or ultrasound. |
| センサ | Standardized 8-channel lower-face/neck sEMG montage (same nominal placements as prior work [5]); raw 2222.22 Hz → 1000 Hz → filtered → 689 Hz model input. Released single-subject checkpoint used a different 8-channel montage. |
| 装着部位 | lower face and neck (standardized 8-channel montage) |
| 出力 | Character sequences decoded to text via CTC beam search + external KenLM (not refined on the 50-sentence inventory). Not waveform synthesis. |
| 語彙の種類 | Closed sentence inventory; character-sequence decoding within that inventory. Not open vocabulary. |
| 語彙数 | 50 closed sentences (TIMIT-based); fixed 45/5 calibration/evaluation split shared across subjects. |
| 指標と結果 | Table 1 (n=27, Aloud+Mimed macro): Pretrain+FT (MLP) 21.7% CER / 31.9% WER; Pretrain+FT (no MLP) 22.5/33.3; random-init Pretrain+FT 44.9/58.8; Pretrain zero-shot 49.3/63.1; Checkpoint+FT (MLP) 68.0/97.2. Table 2 calib: 1 min 25.4/36.6; 3 min 20.5/31.7 (vs full p=0.27/0.88); full ≈13 min 21.7/31.9. Scaling: 1 subject 74.4% CER → 26 subjects 21.7%. Table 3 unseen sentences 78.6% CER / 99.9% WER. Aloud vs Mimed CER 15.4% vs 27.9%. Author-reported; not independently reproduced. |
| 評価方法 | Leave-one-subject-out。主条件は公開チェックポイント初期化→26他者事前学習→対象者微調整。対照にゼロショット、Checkpoint直接微調整、ランダム初期化、MLP有無、キャリブレーション分数スイープ、未見文ストレス（評価文を全sEMG学習から除外）。 |

### 限界

- **技術：** 評価文が他者事前学習に現れうる閉コーパス主設定；言語モデルは50文在庫で再学習していないが文面記憶の余地は残る。Subvocal除外。固定エポック最終モデル報告。
- **評価：** 固定45/5文分割を全27人で共有。主結果は評価文が他者事前学習に現れうる閉コーパス設定。ハイパラは被験者横断で固定し最終エポックを報告。3分とフルの差は非有意だが同等性試験ではない。ランダム初期化は5/27 fold未収束。
- **実運用：** オフラインCER/WERのみ。通信レート・レイテンシ・閉ループ適応・歩行／騒音・電極付け直しは未測定。健常成人のみ。顔／頸部8chでありAESSI耳周囲やSilentWear繊維、VTPカメラ、SilentSpeller EPG、SottoVoce超音波ではない。
- **このレビューの範囲：** arXiv 2609.21288v1全文（20ページ）と抽出テキストを確認。Table 1–4と要旨・Limitationの数値を照合。著者コードの実行や独立再現、未公開データセットの実体確認はしていない。

### 根拠

- Primary setting is a closed 50-sentence TIMIT-based corpus with leave-one-subject-out personalization; not open-vocabulary conversational SSI.（Abstract; §3.1–3.2; §5.6 Limitations）
- 27 speech-typical participants each contributed less than 0.5 h of data (21.3 min on average) across Aloud and Mimed; Subvocal trials were recorded but unused in decoding analyses.（Abstract; §3.1）
- Surface EMG used a standardized eight-channel lower-face and neck montage shared by all 27 participants; the released single-subject checkpoint used a different eight-channel montage.（§3.1; Fig. 1(a)）
- Authors claim multi-subject pretraining plus target fine-tuning enables short-calibration personalization for closed-corpus sEMG speech decoding.（Abstract; §1 Contributions）
- Pretrain + fine-tune (MLP) achieved macro-averaged 21.7% CER and 31.9% WER across 27 held-out subjects (Aloud+Mimed).（Abstract; Table 1）
- Pretrain zero-shot (no MLP) reached 49.3% CER / 63.1% WER; Checkpoint + fine-tune (MLP) reached 68.0% CER / 97.2% WER.（Abstract; Table 1）
- Three minutes of target-subject calibration reached 20.5% CER / 31.7% WER versus full ≈13-min pool 21.7% / 31.9% (paired Wilcoxon p=0.27 and p=0.88); not an equivalence test.（Abstract; Table 2; §4.2）
- Macro-averaged CER declined from 74.4% with one pretraining participant to 21.7% with 26.（Abstract; §4.4; Fig. 4）
- Unseen-sentence stress test: excluding the five evaluation sentences from all sEMG model-training data yielded 78.6% CER and 99.9% WER on the identical 269 held-out trials.（Abstract; Table 3; §4.5）
- Subject-specific MLP adapter provided no detectable benefit (pooled CER change −0.8 points, 95% CI [−2.9,+1.2], p=0.44).（Abstract; §4.3）
- Authors state the main result should not be interpreted as open-vocabulary speech decoding; analyses are offline on healthy adults, without longitudinal or electrode-shift tests.（§5.6 Limitations）
- Novelty is the joint LOSO quantification of pretraining-cohort size and short calibration budgets with an explicit unseen-sentence collapse boundary, not a new sEMG sensor or decoder family.（§1; §2.3; §4.4–4.5）
- Decoding architecture follows Gaddy and Klein convolution–transformer mapping silent sEMG to characters with CTC; checkpoint trained on ≈18.7 h from one subject.（§3.4）
- De-identified dataset and code are planned for public release upon publication at huggingface.co/datasets/whisperle/multisubject-semg-text-v1; raw audio will not be released.（Data and Code Availability）

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
