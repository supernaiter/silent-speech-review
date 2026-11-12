# ChatGPT 指摘（evaluation-chatgpt.ja.md、32 項目）の照合記録

対象：emg-to-speech-with-fewer-channels（.ja.md、.json、.slots.json、.bib の 4 ファイルを同じ内容で更新）。
照合日：2026-11-11。根拠は wiki repo の `papers/<id>/source/`（読み取りのみ）。web は使っていない。wiki に刊行版の本文や書誌がないものは「未照合」とし、反映していない。
判定：確認・反映 23（一部反映 4 を含む）／誤指摘 2／未照合 7。

| # | 判定 | 根拠 | 反映箇所 |
|---|---|---|---|
| 1 | 確認・反映 | doi-10.1044-2015_jslhr-s-14-0112/source/fulltext.html の citation_author 4 名（Wang, Samal, Rong, Green）。sc_text.txt 冒頭の著者欄も同じ | 参考文献 [18]（md、json、bib に Rong, P. を追加） |
| 2 | 未照合 | wiki は著者受理稿（doi-10.1109-jbhi.2020.3034158、registration は year 2020）のみで、刊行版の巻号・頁・年を持たない | なし |
| 3 | 未照合 | doi-10.1016-j.celrep.2025.116241 は bioRxiv 版で、manifest の venue は 44(7)。刊行版本文が wiki になく 44(9) を確かめられない | なし（[62] は従来どおり「manifest の記載による」） |
| 4 | 未照合 | cvf24-choi_av2av は CVF 版 PDF（頁 27325–）で DOI を含まない。manifest の DOI は 02571 のまま。正しい DOI を wiki で確かめられない | なし |
| 5 | 誤指摘 | arxiv-2509.26301/source/text.txt（v2 PDF）1 行目の題名は “BRIDGING PRETRAIN–DOWNSTREAM”。引用した版の題名と一致（arXiv の抄録頁表記は未照合） | なし |
| 6 | 確認・反映 | 対象 text.txt §4.1「16 hours of open vocabulary」。arxiv-2010.02960/source/text.txt 表2：3.6 h 無声／3.9 h 有声（並行）、11.2 h 非並行、計 18.6 h。§2.3 は記録詳細で時間を述べない | 「何をしたか」第1段（原典間の不一致として記載）、付録B 本文確認、json evidence（16 時間の項目に注記） |
| 7 | 確認・反映 | 対象 図1・[12] 表3 “2 left corner of chin” | 「何をしたか」電極一覧（「顎先の左端」） |
| 8 | 確認・反映 | arxiv-2106.01933/source/text.txt 87–91 行（MFCC、WaveNet ボコーダ）。対象 §4.1（mel を音響目標）、§4.2（HiFi-GAN） | 要点第1段（「エンコーダ構成を継ぐ」に改め、特徴量とボコーダの違いを明記） |
| 9 | 確認・反映 | 対象 PDF p.2 図2 を描画して確認：破線なし、8 チャネルは青い点（約 35%）。p.4 図3 は破線 | 主要数値表の 8 電極基準の出所 |
| 10 | 確認・反映 | 対象 要旨（text.txt 24–26 行）は “best dropout strategy depending on the number of channels” のみ。p=0 が 6・4 電極で最良とするのは §5.4 | 要点第2段、証拠を超えている主張、json expert_take_long／evidence |
| 11 | 確認・反映 | §1（text.txt 63–66 行）“yields additional performance gains”。§6 と貢献 3 はスクラッチ学習との比較で、図3（p=0 でも 4〜6 電極でスクラッチを上回る）と整合 | 要点第2段、証拠を超えている主張、json expert_take_short／long／evidence |
| 12 | 確認・反映 | 図3 転記値（図読み）：5 電極 43.4→39.5（p=0）=3.9、6 電極 42.9→39.2=3.7、4 電極 47.2→44.6=2.6。5.3 は 43.4−38.1（p=0.25）。描画した図3で各点の位置も確認 | M03「対象論文が加えたもの」、json expert_take_long、en.summary（2.6–3.9 at p=0） |
| 13 | 確認・反映 | 対象 §3.2・§5.4・図3 に p=0 条件があり、事前学習時ドロップアウトの除去比較になっている | M03「対象論文が加えたもの」第2文 |
| 14 | 確認・反映 | 対象 text.txt 全文に seed／run 数の記載なし（“repeated” は後退消去の手順のみ、187 行）。分散・CI もなし | 要点、mermaid M12、M05・M03「加えたもの」、条件一致表、総括表 M03／M12、証拠が支える主張、前進、限界、json（short／long／delta／position／axes_moved／evaluation_limits／en.limitations／verdicts.M03）、slots（M03 note、M12 choice） |
| 15 | 確認・反映 | 対象のテスト集合・正規化・学習条件は未記載（本レビュー自身の記述）。(35−26.75)/0.99 ≈ 8.33 | 条件一致表の下の段落（「約 8.3 標準偏差分」の記述的比較に変更） |
| 16 | 確認・反映 | [7] の SD は 8 電極基準の 10 シード分布。縮小条件の分散は対象に報告なし | M03「加えたもの」（参考値との比較にとどめる） |
| 17 | 確認・反映（一部） | doi-10.1109-taslp.2017.2740000/source/text.txt：Data Acquisition「simultaneously record sEMG signals from 8 locations」、4 センサー部分集合は同データ上の評価。一方、先行研究の部分集合解析で 11 から 8 に減らした配置（“a reduced set of 8 sensor locations that are used in this study”）で新たに記録している。4 センサーの再記録という読みは誤りなので修正、11→8 の削減配置での記録は残した | その他の構成要素 M13、総括表 M13、実用上の意味、json practical_value、slots M13 field |
| 18 | 確認・反映 | isca-han26f-tapets、isca-lee26v、isca-lee26r、isca-toussaint26 の本文ヘッダ「Interspeech 2026, 27 September - 1 October 2026」。対象は 2026-02-06（arXiv 透かし）。それ以前の公開版の有無は未確認 | 要点「後続研究」、条件一致表の年（後続）、M06、M12 例示（SVRA 後続）、総括表 M12、後退、json（short／long／canon_before／axes_regressed／en.key_result／evidence） |
| 19 | 確認・反映 | [23] arXiv 2603.20246v1（2026年3月）、[24] manifest version “biorxiv_v1_posted_2026-07-27”、[25] arXiv 2606.09667（2026年6月）。いずれも対象より後 | M03 深掘りの第2文（「いずれも後続」、チャネルドロップアウト自体の先行性は対象 §3.2 が引く他分野例に依拠）、json canon_before |
| 20 | 誤指摘 | [84][85] は付録A2 の台帳のみの例示で、先行性の主張に使っていない。初版年の書誌は誤りではない（版の日付は wiki manifest になく未照合） | なし |
| 21 | 確認・反映 | 本レビュー M12 段落と付録B（[10] 各点 10 RNN、[11] 選択乱数種 4・モデル乱数種固定、いずれも本文確認済み）と要点の書き方が不整合 | 要点第2段 |
| 22 | 確認・反映 | doi-10.3389-fnins.2026.1816455 本文：80/20 の学習・評価分割を 20 の乱数種で繰り返す。除去率は 10、30、50% | M03 深掘り（sEEG）、M12 例示、付録B、json axes_unresolved |
| 23 | 確認・反映 | isca-toussaint26_interspeech/source/sc_text.txt 表1「Linear probing accuracy (%) for phone classification」、EMG-to-speech&phones (finetuned) 84.68／52.74 | 証拠を超えている主張「表3の PER」 |
| 24 | 確認・反映 | pmc-12369848-voicesynth（著者稿）「Nature. 2025 Jun 12;644(8075):145–152. doi:10.1038/s41586-025-09127-3」、doi-10.1038-s41586-025-09127-3/source/text.txt の著者欄に Miller, L. M.（bioRxiv v1 にはなし）。題名のハイフンは同フォルダ manifest による（著者稿はハイフンなし） | 参考文献 [31]（刊行版を先に、bioRxiv v1 を本文数値の版として併記）、json pid、bib |
| 25 | 確認・反映（一部） | doi-10.1109-tim.2025.3583386/source/manifest.json：IEEE TIM、2025、DOI、題名 “Multichannel … into Headphones”。巻 74・頁 1–10 は wiki にない | 参考文献 [46]（誌名・DOI・題名を追加、巻・頁は未照合と明記）、json pid、bib |
| 26 | 未照合 | wiki は arxiv-2211.11275 のみで、TMM 刊行版の書誌を持たない | なし |
| 27 | 未照合 | Whisper は wiki 未収録。対象の文献リスト 17 番にも PMLR の巻はない | なし |
| 28 | 未照合 | doi-10.1088-1741-2552-ad8d0a は bioRxiv 版のみ。巻号・論文番号を確かめられない | なし |
| 29 | 確認・反映（一部） | 頁 1–4 は対象 text.txt 文献リスト 8 番（“IEEE, 2024, pp. 1–4”）。DOI は wiki になく未照合 | 参考文献 [37]（頁を追加）、bib |
| 30 | 確認・反映 | pmc-13391774-megdecode/source/source.xml：volume 54、issue 8、page-range 2450–2468 | 参考文献 [66]、bib |
| 31 | 未照合 | doi-10.1109-asru46091.2019.9004036 の本文は arXiv PDF で頁がない | なし |
| 32 | 確認・反映（一部） | 頁 1–5 は対象 text.txt 文献リスト 4 番（“IEEE, 2025, pp. 1–5”）。DOI は wiki になく未照合 | 参考文献 [97]（頁を追加）、bib |

## 追加点検：Meltzner 2018 図6A の最良 4 センサー

doi-10.1088-1741-2552-aac965/source/paper.pdf の 21 頁（図6A）を描画して読んだ。軸（0〜40%）の画素位置から、4 センサーの点は約 16.1%、8 センサーは約 10.2%（本文値 10.4%）。約 16% は維持し、相対悪化を 16/10.4 ≈ +54%（図読み値に依存）と明記した（M05「対象論文が加えたもの」、付録B 査読者の計算、json expert_take_long）。旧記述「約 +5 割」と矛盾はないが数値を揃えた。

## 反映しなかった理由の要約

- 未照合 7 件（#2、#3、#4、#26、#27、#28、#31）：刊行版の書誌が wiki にない。web での確認が必要。
- 誤指摘 2 件：#5 は保持版 PDF の題名と一致、#20 は時系列の主張に使っていない。
- 状態行（md 冒頭）と json の verification_status に、この照合を反映した旨を 1 文追記した。

## Codex（途中停止）の追加指摘（2026-11-11）
| # | 判定 | 根拠 | 反映箇所 |
|---|---|---|---|
| C1 刊行版とプレプリントで著者順が違う文献 | 未照合（対象文献の特定なし） | Codex の出力が途中で停止 | なし |
| C2 Meltzner 型の録り直し | 既に反映済み（ChatGPT #17） | — | M13 |
| C3 [50] 42 チャネルで +18〜28 | 確認・反映 | isca-duraisamy25 text.txt l.304–352：選択のみ Model 2 は +4.7/+10.1、+18〜28 は周波数帯分解の Model 3 | 付録A EEG 行 |
