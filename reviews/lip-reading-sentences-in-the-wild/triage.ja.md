# 指摘の判定（Lip Reading Sentences in the Wild、2026-11-12）
評価者：執筆者と別の言語モデル（クラウド内、evaluator-brief.md による）。ChatGPT による評価は未実施。
各指摘を wiki の原典（papers/<id>/source の本文）で照合した。書誌の DOI 2 件は wiki の別フォルダの manifest で照合した。

| # | 判定 (確認・反映 / 誤指摘 / 未照合) | 根拠 | 反映箇所 |
|---|---|---|---|
| 1 | 確認・反映 | 参考文献 LRW の DOI は wiki の doi-10.1007-978-3-319-54184-6_6 の manifest で 10.1007/978-3-319-54184-6_6（LNCS 10111）。従来の 54427-4_7 は w2594690981-lrw の manifest の誤りを引き継いだもの。87–103 頁は評価者の登録メタデータ照合による | refs.json、.bib、.refs.json、.json（DOI・頁・wiki id 追加） |
| 2 | 確認・反映 | isca-ma09_avcon §4「The visual-only HMMs perform better than the human participants」。isca-potamianos01_eurospeech は大語彙の機械と人間の比較だが人間の条件に映像のみがない | M12 監査に 4 件追加（Ma include、別版 2 件、Potamianos は境界例として exclude）、主張の範囲、分野での位置づけ、付録A、slots M12、参考文献 [ma2009] |
| 3 | 確認・反映 | cvf 版 text.txt §5.1「reduced from 16.2% for audio only to 13.3%」、同版 表5 は 10.4%・7.9%。arXiv v2 本文は 10.4→7.9 | 限界、付録B、JSON evaluation_limits |
| 4 | 確認・反映 | cvf 版 表3 に「MODALITY [12] Sent. 182 5,880 8,085」、LRW 450,000。arXiv v2 は GRID と LRW のみ、400,000 | 冒頭の固定版の行、それまでの到達点 M11 |
| 5 | 確認・反映 | 「This dataset will be released」は arXiv v2 §1 にあり、cvf 版 text.txt にはない（該当箇所は「ethnic origin. The performance…」と続く） | 要点、M13 の行、slots M13 |
| 6 | 確認・反映 | arxiv-2110.07603「the boost in performance does not come from the curriculum learning but from … data augmentation」。対象 §3.1 の「presumably … augmenting the data」、§3.5 の 5,000 反復の停止規則 | 何が変わったか M03、slots M03、JSON position_in_field |
| 7 | 確認・反映 | 対象 表8 に LRW・GRID の結果があり、両者は LRS で学習したモデルの微調整（§5.3–5.4） | 分野での位置づけ（表の下の段落）、slots M06、JSON position_in_field |
| 8a | 確認・反映 | 表2 脚注は「6,641 are in the audio-only training data」 | 何が変わったか M11 の言い換え |
| 8b | 確認・反映 | w2594690981-lrw §2「There are a few people who appear repeatedly in the videos (e.g. news presenter in BBC News…)」 | 何が変わったか M11（「推測」を LRW の記述に置換） |
| 8c | 確認・反映 | M03 監査で後続 17 本のうち本文確認 13、台帳のみ 4 | 何が変わったか M03 |
| 8d | 確認・反映 | M12 監査の 1979 年・2007 年の候補の除外理由が LipNet 引用の定型文だった | M12 監査の除外理由を候補ごとに書き直し |
| 8e | 確認・反映 | M11 監査の arxiv-2510-22716-lrwpersian と別版が未判定。題名・台帳から単語単位データ | M11 監査（exclude）、付録A の未読数 293 |
| 8f | 確認・反映（一部） | arxiv-1704.08028 の本文に「978-1-5090-4023-0/17 … 2017 IEEE」。会議名と頁は本文から確定できない | 参考文献 VLRF に注記（会議版の書誌は未照合） |
| 8g | 確認・反映 | cvf 版 text.txt の頁下の数字 6447–6456 | 参考文献 1 の注 |
| 8h | 確認・反映 | JSON verification_status が未評価のままだった | .json verification_status |
| 9 | 確認・反映 | arxiv-1807.05162 表「Baseline-Seq2seq-Ch … 76.8±0.8」、V2P 40.9% | 何が変わったか M06（後続の同一データ比較を追記） |
| 10 | 確認・反映 | Miao らは「Following [12, 24]」とデータ設定を先行研究から継ぐ | それまでの到達点 M11 の言い回し |
| 11 | 確認・反映 | 「文単位・開語彙で人間と比べた点が新しい」は範囲と再現率なしの新規性主張。Potamianos 2001 は大語彙の文 | 主張の範囲（映像のみに限定、検索範囲と再現率、見落としの注記） |

集計：確認・反映 19（うち一部反映 1）、誤指摘 0、未照合 0（VLRF の会議版書誌だけは原典から確定できず、注記として残した）。
