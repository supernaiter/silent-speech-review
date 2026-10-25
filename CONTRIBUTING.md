# Contributing

Corrections and new papers are welcome. The maintainer reviews every change so that the tables stay comparable.

## Report an error or suggest a paper

Open an issue:

- [Report an error in a review](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml). Please cite the section or table of the paper.
- [Suggest a paper](https://github.com/supernaiter/silent-speech-review/issues/new?template=add-paper.yml).

If you are an author of a reviewed paper and something is wrong or missing, an issue is the fastest way to get it fixed.

## Send a pull request

1. Edit `data/reviews.jsonl` only. Each line is one paper.
2. Fill the English fields under `en` (summary, sensor, task, vocabulary, speaker, session, mode, key_result, limitations). Use the fixed values for `speaker` (Speaker-dependent, Speaker-independent, Both, Not stated), `session` (Same session, Cross-session, Cross-day, Not stated, Not applicable) and `mode` (Online, Offline, Both, Not stated, Not applicable).
3. Report the paper's numbers under the paper's own conditions. Do not copy text from the paper beyond short quotes.
4. Run `python3 scripts/build.py` and commit the regenerated files. CI fails if they are out of date.

By contributing you agree that your contribution is licensed under [CC BY 4.0](LICENSE).
