# Review pipeline

This folder holds the procedure and the scripts that produce the component reviews in `reviews/`. It is written so that any agent can run it from this repository alone, with read access to the private wiki repository `supernaiter/deep-research-wiki-for-silent-speech` (the paper sources and per-paper ledgers).

- `SKILL.md`: the full procedure (steps 0–11), the verdict rules, the review format, the writing rules and the quality gates.
- `references/slot-notes.md`: what an empty ledger slot means, per component M01–M13.
- `references/evaluator-brief.md`: the fixed brief for the independent evaluation.
- `scripts/*.py`: deterministic helpers (Python 3 standard library only). No script calls a model.

## Never put these in this public repository

Paper full texts, PDFs, the wiki's `source/` files, `notes.json`, full-text snippets (`fulltext_snippet`), or any notes that carry verbatim quotes from the sources. Published reviews and topic tables contain at most one or two quoted sentences per item, with a location. Working files belong in a work directory outside this checkout or in the private wiki hand-off folder described below.

## Design in brief

- **Scripts count, number and check; models read, decide, judge and write.** Counts, reference numbering, chronology labels ([concurrent] within ±6 months of the target, [later] after), the 13-components table and every format check are scripts, so the same wiki commit and the same search patterns give the same numbers.
- **The field comparison comes from the wiki ledgers.** About 9,000 papers are already classified per component. The usual approach and the counts are ledger tallies with a named tier (slot-filled, or pattern match for sparse slots), never a re-reading of hundreds of candidates. Full text is read only for the target and the at most about 8 papers the review names (state of the art and deciding priors).
- **One writer, one separate evaluator.** No debate panel and no second writer. The evaluator is a different model from the writer, so their errors overlap less.
- **The search record is part of the output.** Each topic gets an audit file (inclusion rule written before the tally, counts, usual approach, state of the art, papers read). Topic tables in `components/` are reused and only appended to.
- **Reproducibility is measured, not assumed.** `diff_runs.py` compares two independent runs of the same review. Provisional targets: verdict agreement at least 11 of 13 with the same verdict on every changed slot, inclusion-decision kappa at least 0.7, confirmed-set Jaccard at least 0.8. Disagreements are the list of items a person should look at.
- **Known limits.** Slot classification and verdicts are model readings, so `human_verified` stays `false` until a maintainer checks the key sources. Absence and novelty claims hold only within the wiki's coverage. Only a minority of ledgers are verified against the full text, so a ledger value is a candidate until the reader confirms it in the source.

## Roles

| Role | Model | Does |
|---|---|---|
| Reader (prep) | reader model (capable, cheaper than the writer) | reads the target in full and the few named papers, extracts claims, numbers, conditions, unstated items and caveats with short quotes into `notes.json`; confirms the chosen state of the art and deciding priors in their sources; fills the claim table; answers the writer's targeted questions |
| Scripts | none | wiki index, ledger tallies, topic audits, references, 13-components table, `reviews.jsonl` row, claim-table skeleton, gates |
| Writer | writer model (top tier) | plans the slots, decides verdicts, writes the review, `slots.json`, `verdict.json`; reads only `notes.json`, the tallies and `references/slot-notes.md`, never full sources |
| Evaluator | evaluator model (top tier, a separate model from the writer) | one call without tools; sees only `references/evaluator-brief.md` and the output of `compact_for_chat.py` (the compact review plus the claim table); writes `<slug>.eval.md` |
| Triage | reader model; writer model for rewrites | checks each evaluator finding against the source passage it concerns; the writer model rewrites only the sentences that change; log in `<slug>.triage.md` |
| Publish | scripts and a maintainer-approved pull request | places the finished review in `reviews/<slug>/`, the row in `data/reviews.jsonl` and the topic tables in `components/`, following `docs/STRUCTURE.md`; runs `scripts/build.py` and `--check` |

## Steps and who may run them

"External agent" means an agent that is not the writer or the evaluator, for example one running in its own cloud. It may run the **pre-writing materials** steps and the mechanical steps marked below. It must not write the review, act as the evaluator, triage findings into the text, or publish.

| Step (`SKILL.md`) | What | Needs | External agent |
|---|---|---|---|
| 0 | `wiki_index.py build` (once per wiki commit) | wiki clone | **yes: pre-writing materials** |
| 1 | full reading of the target (text, PDF figures and tables, code for unstated conditions); quote extraction into `notes.json` | wiki `papers/<pid>/source/` | **yes: pre-writing materials** |
| 1 | `verify_quotes.py notes.json`; fix or drop every MISSING quote | `notes.json` | **yes: pre-writing materials** |
| 2 | slot plan (changed / incidental / inherited; topics and inclusion rules) | `notes.json` | writer; an external agent may write `plan.proposed.json` for the writer to accept or edit |
| 3 | slot candidates and ledger tallies: `slot_candidates.py`, `audit_tally.py --write` (index from `wiki_index.py`); confirm the state of the art and deciding priors in their sources | index, plan or proposed plan | **yes: pre-writing materials** |
| 5 (inputs) | `refs.json` entries for the target and every named paper, bibliographic data taken from each paper's first page, with locators; validate with `build_refs.py` (see below) | sources, wiki `article.md` pages | **yes: pre-writing materials** |
| 5 (inputs) | `slots.json` skeleton: per slot M01–M13 the target's `choice` and, for audited topics, `field`, `matched`, `matched_tier` from the tallies; `verdict` and `note` left empty | target ledger, tallies | **yes: pre-writing materials** |
| 4–5 | verdicts and the final writing (`draft.md`, `slots.json` verdicts and notes, `verdict.json`) | the materials above | **no: writer only** |
| 6 | `render_review.py`, `build_refs.py`, `fill_row.py` (row fill) | the writer's draft | yes (mechanical, after the draft exists) |
| 7 | `check_review.py` | assembled review | yes (mechanical) |
| 8 | claim table: `claim_table.py`, then the reader model maps each claim to its `notes.json` entry | assembled review, `notes.json` | yes (reader role, after the draft exists) |
| 9 | evaluation and triage | compact review + claim table | **no** |
| 10 | publish to this repository | gated, evaluated review | **no** |

Steps 6–8 depend on the writer's draft, so in a pre-writing hand-off they are only prepared (`refs.json` validated, `slots.json` skeleton, scripts ready); they are run again on the draft once it exists.

To validate `refs.json` before any draft exists, run `build_refs.py` on a stub draft that cites every key once (`[@key1; @key2; ...]`) with `--out-dir` set to a scratch directory. It fails on unknown keys, missing locators (DOI, arXiv id or URL) and wiki ids without an `article.md` page.

## Hand-off: pre-writing materials

Materials for paper `<pid>` are written in the **private** wiki repository `supernaiter/deep-research-wiki-for-silent-speech`, under `papers/<pid>/review-prep/`, and nowhere else. Nothing else in the wiki is changed; follow the wiki repository's own contribution rules when committing there.

```
papers/<pid>/review-prep/
  notes.json            reader notes with short verbatim quotes and locations (verify_quotes.py must pass)
  plan.proposed.json    optional: proposed slot plan, topics and inclusion rules, if the writer has not planned yet
  tallies/
    index.meta.json     wiki commit and counts of the index the tallies used
    <Mxx>-<topic>.audit.json   topic audit from slot_candidates.py, after audit_tally.py --write
    <Mxx>-<topic>.txt   stdout of slot_candidates.py and audit_tally.py (what the writer reads)
  refs.json             bibliographic entries for the target and named papers (validated with build_refs.py)
  slots.json            per-slot skeleton (choice, field, matched, matched_tier; verdict and note empty)
  claims.md             added only after the draft exists (claim_table.py, then the reader's mapping)
  status.json           which steps ran, wiki commit, verify_quotes summary, open questions
```

The writer reads these files and the script summaries only. The hand-off is complete when `verify_quotes.py` reports no MISSING quote, every audit passes `audit_tally.py`, and `refs.json` passes the stub `build_refs.py` run.

## Running the scripts

Set the paths once:

```
export WIKI_DIR=/path/to/deep-research-wiki-for-silent-speech   # private wiki clone, read-only except review-prep/
export REVIEWS_DIR=/path/to/silent-speech-review                # this repository
export WORK_DIR=/path/outside/the/checkout/<slug>               # working files; never committed here
```

Scripts that read the wiki take `--wiki`, which defaults to `$WIKI_DIR`. Every script prints its usage with `--help`. Example of the pre-writing script steps:

```
python3 pipeline/scripts/wiki_index.py build --out "$WORK_DIR/index.jsonl"
python3 pipeline/scripts/verify_quotes.py "$WORK_DIR/notes.json"
python3 pipeline/scripts/slot_candidates.py --index "$WORK_DIR/index.jsonl" --slot M05 --topic sensor-subset \
    --pattern 'channel (subset|selection)' --metric-pattern '\bWER\b' --better lower \
    --reuse "$REVIEWS_DIR/components/M05/sensor-subset.json" --out "$WORK_DIR/tallies/M05-sensor-subset.audit.json"
python3 pipeline/scripts/audit_tally.py "$WORK_DIR/tallies/M05-sensor-subset.audit.json" --write
```

`audit_tally.py` fails until the audit has an `inclusion_rule`; write it (from the plan or the proposed plan) into the audit before the tally.
