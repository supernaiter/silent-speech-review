# Standing notes per slot (wiki commit 730b0b4, 8,995 readable folders, 7,388 unique papers)

Refresh with `scripts/wiki_index.py fill` when the wiki has grown by more than about 10%. Reuse these notes; do not redo the omission checks for every review.

| Slot | Label | Filled (folders) | Empty slot means | Where the content actually is |
|---|---|---:|---|---|
| M01 | Training-time action | 4,015 (45%) | often not recorded | M04 production facts, source text |
| M02 | Training-only supervision | 31 (0%) | **omission** (about 250 missed, 28-paper sample) | M03 `supervision_kind` (paired_audio 258, text_prompt 131, phoneme_label 92) |
| M03 | Training, calibration, adaptation | 1,608 (18%) | often not recorded | `TrainingRun.*` facts |
| M04 | Use-time action | 6,538 (73%) | mixed | |
| M05 | Measurement and sensors | 8,898 (99%) | reliable | topic content (subset selection etc.) sits in results facts: search with `--scope ledger` |
| M06 | Processing, intermediate representation, decoding | 8,925 (99%) | reliable | |
| M07 | Use-time lexicon and auxiliary information | 120 (1%) | **omission** (about 443 papers mention LM/beam/lexicon, about half really use one) | source text |
| M08 | Output | 3,760 (42%) | often not recorded | `output_types` |
| M09 | Presentation, confirmation, commit, operation request | 82 (1%; 17 of them say "none") | **mostly truly absent** (about 10–20 missed) | misses cluster in text-entry BCI and input systems |
| M10 | Correction, re-entry, action adjustment | 82 (1%) | **mostly truly absent** | same as M09 |
| M11 | Evaluation ground truth and reference construction | 239 (3%) | not checked yet: treat as unknown | |
| M12 | Evaluation, results, counting rules | 8,381 (93%) | reliable | observation `source_label` |
| M13 | Device, cost, safety, operating constraints | 6,721 (75%) | mixed | |

Rules that follow:
- A slot filled in under 5% of papers gives no usual-approach (field practice) count. Use the place in the last column, or a full-text pattern, and say which.
- The ledger cannot tell "absent in the paper" from "not read". Never write "the field does not do X" from an empty slot.
- Only about 106 papers have a full-text-verified ledger. A ledger value used for a comparator is `ledger only` until you read the source (then `text-verified`).
- Folder counts include version duplicates (preprint and published). Report unique papers.
