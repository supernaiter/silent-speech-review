# リポジトリ構造の仕様

この文書は silent-speech-review の置き場所の正本である。手で書く人も自動運用も、ファイルを足す前にここに従う。変えるときはこの文書を先に直す。

## 原則

1. **入口は論文のフォルダ。** 1 本の論文に関わるもの（レビュー、判定データ、評価、図、文献）は `reviews/<slug>/` に集める。フォルダを開けばレビューが表示され、材料は同じ場所に並ぶ。
2. **分野の知識は部品の側に置く。** 候補論文の採否表は 1 本のレビューのためではなく分野の地図なので、`components/<Mxx>/` に置いて論文をまたいで育てる。レビューはそれを参照する。
3. **元データと生成物を分ける。** 人やループが書くのは元データだけ。ページ、図、索引、CSV は `scripts/build.py` が作り、CI が `--check` で一致を確かめる。生成物を手で直さない。
4. **事実は一か所。** 同じ値を二か所に書かない。書誌と分類は `data/reviews.jsonl`、部品の判定は `slots.json`、採否は話題の表が正本。
5. **原典は置かない。** wiki の `source/`（PDF、全文）、全文からの長い抜き出しは公開しない。引用は位置つきの 1〜2 文まで。wiki へのリンクは `papers/<id>/article.md` まで。
6. **URL は変えない。** 一度公開したパスは動かさない。動かすときは同じ PR で全てのリンク元を直す。

## 配置

```
README.md, README.ja.md            生成  全論文の索引（センサー別）と分野の図
CONTRIBUTING.md, CITATION.cff, LICENSE
docs/STRUCTURE.md                  元    この仕様

reviews/<slug>/                    論文ごとのフォルダ
  README.md                        生成  レビューのページ（下記の順に組む）
  review.ja.md                     元    構成要素別レビュー本文（日本語）
  refs.bib                         元    本文の参考文献
  slots.json                       元    13 部品それぞれの選択・分野の通例・該当数・判定
  figures.json                     元    この論文の図の定義（部品図ほか）
  figures/*.svg                    生成  figures.json から作る図（明暗 2 枚ずつ）
  evaluation.ja.md                 元    執筆者と別の評価者による検証（複数あれば evaluation-<評価者>.ja.md）
  triage.ja.md                     元    評価の指摘を原典で確かめた判定と対応

components/
  README.md                        生成  13 部品の索引：定義、記録率、話題、使ったレビュー
  <Mxx>/README.md                  生成  その部品の話題一覧と、各話題の確認済み論文
  <Mxx>/<topic>.json               元    話題の採否表（検索式、範囲、候補、採否、理由、集計）
  <Mxx>/<topic>.csv                生成  同じ表を GitHub で読める形に

data/
  reviews.jsonl                    元    全論文の書誌・分類・要約・英語項目（1 行 1 本）
  field.json                       元    分野全体の図の定義
  papers.csv, metadata.json        生成  外部向けの一覧

figures/                           生成  分野全体の図だけ（field-map、components）
scripts/                           build.py（生成）、figures.py（図）
```

`<slug>` は題名の小文字・ハイフン区切り（`data/reviews.jsonl` の `slug`）。`<topic>` は内容を表す英語の短い名前（例 `ctc-vs-attention`）。

## 論文ページ（reviews/<slug>/README.md）の組み立て

1. 題名、書誌、DOI・arXiv へのリンク、英語の要約と条件表（`reviews.jsonl` の `en`）
2. 図（`figures/`）
3. 構成要素別レビュー（`review.ja.md`）。無い論文は従来の項目別レビュー
4. **材料**：このフォルダの元データと、使った話題の採否表（`components/` へのリンク、確認済み数と未読数）の一覧
5. 関連論文と脚注

## 話題の採否表（components/<Mxx>/<topic>.json）

- 1 つの話題を 1 ファイルで持ち、レビューのたびに追記して育てる。既にある候補の判定を変えるときは理由を残す。
- 各候補：`pid`、`title`、`year`、`via`（ledger／fulltext）、`decision`（include／exclude／空＝未読）、`reason`、`loc`、`quote`（1〜2 文まで）。全文の抜き出し（`fulltext_snippet`）は書き出さない。
- 集計 `tally` と、走査した wiki のコミット `wiki_commit` を持つ。レビュー側はどのコミット時点の表を使ったかを本文の `**状態**` 行に書く。

## 移行（2026-11 時点の配置から）

| 旧 | 新 |
|---|---|
| `reviews/<slug>.md` | `reviews/<slug>/README.md` |
| `data/component/<slug>.ja.md`、`.bib` | `reviews/<slug>/review.ja.md`、`refs.bib` |
| `data/figures/<slug>.json` | `reviews/<slug>/figures.json` |
| `figures/<slug>/*.svg` | `reviews/<slug>/figures/*.svg` |
| `data/figures/_field.json` | `data/field.json` |
| 作業フォルダの監査 `*.audit.json` | `components/<Mxx>/<topic>.json` |

移行の PR で、README、プロフィール README、nao-ki-mura.com の `reviews/<slug>.md` へのリンクを全て張り替える。
