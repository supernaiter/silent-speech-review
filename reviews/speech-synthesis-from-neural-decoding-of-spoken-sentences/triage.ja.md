# 独立評価の照合：Speech synthesis from neural decoding of spoken sentences

照合日 2026-11-14。評価ファイル `speech-synthesis-from-neural-decoding-of-spoken-sentences.eval.ja.md` の指摘を、wiki（コミット `730b0b4`）の原典本文と、wiki にない書誌は Crossref と arXiv で照合した。評価者の記述をそのまま採ったものはない。

| # | 判定 (確認・反映 / 誤指摘 / 未照合) | 根拠 | 反映箇所 |
|---|---|---|---|
| 1 | 確認・反映 | Crossref で 10.1101/481267 は posted 2018-11-29、題「Intelligible speech synthesis from neural decoding of spoken sentences」。wiki の索引に 481267 はない | ヘッダ（初出と基準日）、refs の first_public 2018-11 と note、build_refs を --target-date 2018-11 で再実行 |
| 2 | 確認・反映 | Taguchi ら（Interspeech 2018-09）は 2018-11 の 6 か月以内 | M12 監査の理由、付録A、位置づけ表、slots の M12（先行 10→9） |
| 3 | 確認・反映 | Crossref で 10.1016/j.rlfa.2018.07.004 は DOI 登録 2018-09-14、冊子 2018-10、誌名 Revista de Logopedia, Foniatría y Audiología。wiki manifest の venue は「Revista de la Facultad de Medicina」で誤り。本文に「Twenty one raters」 | M12 監査（同時期）、付録A、付録B（書誌の日付、21 人を本文確認に） |
| 4 | 確認・反映 | Uttam ら（Interspeech 2019-09）は 2018-11 から 6 か月超 | M12 監査（後続）、付録A（後続 15→16） |
| 5 | 確認・反映 | 評価者は Saha らが後続になりうるとしたが未確認だった。arXiv API で 1904.05746 が 2019-04-08 公開と確認。基準 2018-11 から 6 か月以内なので同時期のまま | refs に arXiv と first_public 2019-04、M06 監査の理由、本文の Saha の注記 |
| 6 | 確認・反映 | Crossref で Neuron の Chartier ら は 2018-05-17 登録。2018-11 からちょうど 6 か月で同時期 | 本文「それまでの到達点」に（同時期）を付記 |
| 7 | 確認・反映 | Crossref で 10.1101/350124 は posted 2018-06-19 | refs の first_public 2018-06、本文と M12 監査 |
| 8 | 確認・反映 | Crossref で 10.1101/478644 は posted 2018-11-27（対象の bioRxiv 版の 2 日前） | 本文 M08、M08 監査 |
| 9 | 確認・反映 | 方法に反復回数・乱数種の記載はない。図 1 と図 3 の説明に「repeated 5 times with similar results」。「学習一回」は根拠なし | 要点、何が変わったか、位置づけ下の注記、残る問い、slots の M06・M12、JSON |
| 10 | 確認・反映 | 方法に「Originally we trained the direct acoustic decoder as a 6-layer bLSTM … we found performance was better with a 4-layer bLSTM」 | 要点、主張の範囲、JSON の technical_limits・en.limitations・evidence |
| 11 | 確認・反映（推測として） | 方法「10 sentences 12 times each alternating」、方法の評価「audible speech of the same sentence uttered immediately prior」。58 は約 60 試行から 2 を除いた数と読める。結果は「held-out set of 58 sentences」とも書くので推測と明記 | 主要数値表、Mermaid、何が変わったか M04、位置づけ表、限界、残る問い、slots の M04、M04 監査 |
| 12 | 確認・反映 | 方法は P3 n=98・P4 n=82、図 2c・2d・4e 説明は「n=101, 100, 93, 81, 44」 | 主要数値表、限界、残る問い、付録B |
| 13 | 確認・反映 | 刊行版側の ledger.json の f-vocab は vocabulary_regime=open_vocabulary、raw_value「several hundred sentences」。著者稿側の台帳にはない | 限界（「台帳の誤り」を「台帳の読み方」に）、付録B |
| 14 | 確認・反映 | Le Godais ら本文「Direct and indirect methods achieved comparable performance, with an advantage for direct decoding」 | 要点、位置づけ下の注記、slots の M06 |
| 15 | 確認・反映 | Akbari ら本文の図説明「Eleven subjects listened to digit sounds」 | 本文 M12（本文確認）、M12 監査の provenance、付録B |
| 16 | 確認・反映 | Janke 学位論文 6.3 節「since the audible reference data was not simultaneously recorded, the obtained MCD results give only a limited validity」 | 本文 M04 |
| 17 | 確認・反映 | Crossref で 10.3389/fnins.2019.01267 は 2019-11-22。監査の「2019-12」が誤り、refs の 2019-11 が正しい | M08・M12 監査の理由、付録B |
| 18 | 確認・反映（表現は原文に合わせた） | Martin ら本文「the subject was instructed to read it silently (covert condition)」。評価者の「想像発話」ではなく「声に出さずに読む」と書いた | 本文 M04、slots の M04 |
| 19 | 確認・反映 | `doi-10.1016-j.jphysparis.2017.07.002` 本文（HAL 版）が「Three representations of speech (phonetic, acoustic or articulatory) can be decoded from brain signals」とし、調音合成を論じる。Crossref で冊子 2016-11、DOI 登録 2017-08 | 付録A（設計論の先行、再現率の読み方）、refs に bocquelet2017 |
| 20 | 確認・反映 | 再現率の目安 0.74 は監査の候補に設計論が入っていない以上、実装例についての値 | 付録A |
| 21 | 確認・反映 | 結果「Removing any region led to some decreased decoder performance (Figure 2g) (p=3e-4, n=101, WSRT). However, excluding vSMC resulted in the largest decrease」。p=3e-4 は vSMC ではなく全領域の悪化に付く | 主要数値表 |
| 22 | 確認・反映（推測として） | 方法「std=21., min=4, max=13」、結果「p=1e10」。2.1 と 1e-10 の誤記と読めるのは推測 | 限界 |
| 23 | 確認・反映 | 方法「Models were stopped from training after the validation loss no longer decreased」。検証データの取り方は記載なし | 残る問い |
| 24 | 確認・反映 | 二つの wiki フォルダの XML は同一（SHA-256 `daae058d…5c8b7f`）、manifest の license は「PMC manuscript」。著者稿で読んだという記述は既にあり、bioRxiv 版も未照合と追記 | ヘッダ、限界、JSON の scope_limits |
| 25 | 未照合 | Nature の論文ページが購読者向けで本文が出ないという点は、こちらでアクセスしていない。刊行版未照合という扱いは変えない | なし |
| 26 | 未照合 | Gonzalez ら 2017 の平均明瞭度約 75% は本文で見つけられなかった。本文の「up to 92%」は確認済みで、査読は既に「最大 92%」と書いているので変更不要 | なし |
| 27 | 確認・反映（変更不要） | Ephrat ら 4.3 節の 23 人、Bouchard らの MTurk 同定、Bocquelet ら 2016 の 12 人、Janke の 5.54→6.81、Gonzalez ら 2017 の up to 92% は既存の記述と一致 | なし |
| 28 | 確認・反映（変更不要） | 判定 13 枠は規則どおりで変更不要という評価。基準日を直しても M04・M06・M08 の先行件数は変わらず、`behind` の条件（先行 3 件以上が対象にない条件を満たす）も満たさない | なし |

集計：確認・反映 26（うち変更不要 2）、誤指摘 0、未照合 2。
