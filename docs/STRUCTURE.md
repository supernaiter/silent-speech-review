# Repository structure

This file is the authority on where things live in silent-speech-review. People and the automated review loop both follow it; change this file first when the layout changes.

## Principles

1. **The paper folder is the entry point.** Everything about one paper (review, per-component verdicts, evaluation, figures, references) lives in `reviews/<slug>/`. Opening the folder shows the review.
2. **Field knowledge lives with the components.** Tables of candidate papers are maps of the field, not of one review, so they live in `components/<Mxx>/` and grow across reviews.
3. **Sources and generated files are separate.** People and the loop write sources only. Pages, figures, indexes and CSVs are written by `scripts/build.py`; CI runs `--check`. Never edit generated files by hand.
4. **One fact, one place.** Bibliographic data and classification: `data/reviews.jsonl`. Per-component verdicts: `slots.json`. Inclusion decisions: the topic table.
5. **No source texts.** Never publish the wiki's `source/` files (PDFs, full texts) or long excerpts. Quotes are one or two sentences with a location. Wiki links go to `papers/<id>/article.md` only.
6. **English only.** Reviews follow the published format (Verdict, component-by-component comparison, claims vs evidence, what the field needs next, questions, literature search appendix, references). They contain only what a reader cannot get from the paper itself.
7. **Stable URLs.** A published path does not move; if it must, every link to it is fixed in the same PR.

## Layout

```
README.md                          generated  component reviews first, then all papers by sensor, field figures
CONTRIBUTING.md, CITATION.cff, LICENSE
docs/STRUCTURE.md                  source     this file

reviews/README.md                  generated  component reviews first, then the earlier itemized summaries
reviews/<slug>/                    one folder per paper
  README.md                        generated  the page
  review.md                        source     the component review (English)
  verdict.json                     source     {"short": one-line position, "position": Verdict text}; used in indexes
  refs.bib                         source     references of review.md
  slots.json                       source     per component: this paper's choice, field practice, count, verdict
  figures.json                     source     figure definitions
  figures/*.svg                    generated  from figures.json (light and dark)
  evaluation*.md                   source     independent evaluation(s)
  triage.md                        source     how each evaluation finding was checked and resolved

components/
  README.md                        generated  index of the 13 components and their topics
  <Mxx>/README.md                  generated  topics of one component and their confirmed papers
  <Mxx>/<topic>.json               source     topic table: search, scope, inclusion rule, candidates, decisions, tally
  <Mxx>/<topic>.csv                generated  the same table, readable on GitHub

data/
  reviews.jsonl                    source     bibliographic data, classification, English index fields (one line per paper)
  field.json                       source     field-wide figure definitions
  papers.csv, metadata.json        generated  exports

figures/                           generated  field-wide figures
scripts/                           build.py (generation), figures.py (figures)
```

`<slug>` is the lower-case hyphenated title (`slug` in `data/reviews.jsonl`). `<topic>` is a short English kebab-case name (e.g. `ctc-vs-attention`).

## Paper page

For a component review: the review's title and citation line, the section link, figures, the review body, Materials (the folder's sources and the topic tables it used), related reviews. Papers without a component review show the older English itemized review until they are rewritten.

## Topic tables

- One topic per file, extended by each review that uses it. Changing an existing decision keeps a reason.
- Each candidate: `pid`, `title`, `year`, `via` (ledger / fulltext), `decision` (include / exclude / empty = unread), `reason`, `loc`, `quote` (one or two sentences). Full-text snippets are never written.
- `tally` and `wiki_commit` record the counts and the wiki state searched. `used_by` lists the reviews that rely on the table.
