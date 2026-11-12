# 指摘の判定（Deep Audio-Visual Speech Recognition、2026-11-12）
評価者：クラウド内の別モデル（evaluator-brief.md による）。ChatGPT 評価は未実施（chatgpt_pending）。

| # | 指摘 | 判定 | 原典 | 対応 |
|---|---|---|---|---|
| 1 | 付録E の向きの推論は誤り | 正しい | 対象 text.txt l.1316–1317「nm, ni, nd … matches, deletions, insertions respectively」 | 推論と残る問いを削除、記号の紛らわしさと誤記だけ残す |
| 2 | 70.4% を言語モデルなしと断定 | 正しい | 対象に条件記載なし、Deep Lip Reading 表1 l.231「MV-WAS [15] 70.4%」 | 仮定つきの計算に書き換え |
| 3 | Deep Lip Reading 50.0% との差が抜け | 正しい | Deep Lip Reading 表1 l.235 TM WER T2 50.0% | 1.7 ポイントを追記、「同じもの」→「同じ構成」 |
| 4 | 図7 がテスト集合とは断定できない | 正しい | 図7 説明文 | 推定に下げた |
| 5 | 融合方式の説明は著者自身のもの | 正しい | 対象 §6.3 l.727–731 | 著者の記述として書き換え |
| 6 | 未知話者でないの断定は強い | 正しい | LRS3 §2「likely」、WLAS l.549「speaker agnostic」 | 「保証されない」に弱め、WLAS の記述を追加 |
| 7 | M06 監査（Krishna 境界、未読 128、再現率の範囲、下限） | 正しい | 監査 JSON | 付録A に注記 |
| 7b | LCANet の除外理由 | 一部正しい | LCANet 表III | 本文には出ないため監査 JSON のみの問題として記録 |
| 8 | ±0.34 は 1 標準誤差と明記 | 正しい | 査読者の計算 | 明記 |
| 9 | GPU 文の重複、LSVSR の v1 引用値 | 正しい（任意） | — | 影響小のため未反映 |
