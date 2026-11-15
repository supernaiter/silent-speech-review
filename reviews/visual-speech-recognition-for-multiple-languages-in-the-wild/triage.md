# Triage of the ChatGPT evaluation (2026-11-15)

Source: visual-speech-recognition-for-multiple-languages-in-the-wild.eval-chatgpt.md. Findings checked against notes.json and short reads of the target text (Table S9, Table S13, Sec. 1.4, Sec. 2.2, Abstract).

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | t3 quote names both prediction targets (pretrained ASR and VSR representations) | claim table row 1 |
| 2 | rejected | Verdict rule: standard needs no identical prior; LiRA (p1), ASR-is-all-you-need (p3), Hearing Lips (p4) read and cited; joint placement is stated as the departure | none |
| 3 | applied | 'standard for its data scale' had no ledger support; replaced by usual-design wording and the 90,000 h non-public condition (t28, t113) | Verdict; M12 verdict line |
| 4 | applied | 'usually as pretraining or output distillation' not tallied; narrowed to the read priors | M02 usual approach |
| 5 | applied | t63 quote placed in claim table; joint placement from t3 | claim table row 5 |
| 6 | applied | Valid: 17.0% (t28, Table 2) is lower than 17.6%; now '17.0% overall (90,000 h non-public), 17.6% best with public labelled data' (t113 'non-publicly available', s1 '~2500 hours of unlabelled data') | M02 and M12 State of the art; slots M02/M12 |
| 7 | confirmed | Values match p2, p3 | none |
| 8 | applied | Denominator now the full model: 3.7/29.5 = 12.5%, 1.5/32.1 = 4.7%; t95 (33.6±0.6) and t99 caveat quoted | M02 evidence paragraph; claim table row 9 |
| 9 | applied | Added next category from ledger tally (paired audio 17) | M03 usual approach |
| 10 | applied | Supervised LRW initialization quoted from source (t111, 'on the LRW dataset for initialization') | M03 usual approach; notes t111 |
| 11 | applied | 23.7% / 30 h confirmed in published M03 topic table read_fulltext (arxiv-2602.19316 Table 2); row now cites it | claim table row 12 |
| 12 | applied | 44.9 confirmed in Table S9 baseline row (t112) | notes t112; claim table row 13 |
| 13 | applied | 32.6 quoted from Table 5 (t90) | claim table row 14 |
| 14 | applied | 641 h quoted (t68); distribution added (text 18, paired audio 17) | M12 usual approach; claim table row 15 |
| 15 | applied | Same as 6: comparison classes made explicit | M12 State of the art |
| 16 | confirmed | Arithmetic correct | none |
| 17 | applied | Target best 35.1% (t19) and CM-seq2seq 43.3% (t22) now stated; [7] is the target's reference [10], End-to-end AVSR with Conformers | M12 evidence; claim table row 18 |
| 18 | applied | Abstract phrase quoted (t113); sentence now says it leaves out the 90,000 h system | M12 evidence |
| 19 | applied | Quotes t80 (best of ten reported) and t48 (up to 0.8) placed; comparator rows show a single value without SD (t22 condition) | claim table row 20 |
| 20 | applied | Table S13 row verified in source: only CM-seq2seq [10] retrained on MTit (t110); wording narrowed from 'authors' own baseline' to that comparator; Verdict wording adjusted | claims-outrun item 2; Verdict |
| 21 | applied | 60% threshold and 641 h quoted (t68) | claim table row 22 |
| 22 | unverified | Code values rest on the reader's repository read (t83-t85 code_condition); repository not reopened | verification_status |
| 23 | applied | t72 replaced by t109 ('subject-independent [36] VSR ...') from Sec. 2.2 | claims-outrun item 5; notes t109 |
| 24 | rejected | Proposal, not a factual claim; 30 h setting is in the published M03 topic table | none |
| 25 | applied | M08/M11 notes now say what is given and what is not reported; verdict rules are in the procedure, not the review | slots M08, M11 |

Counts: applied 20, rejected 2, confirmed 2, unverified 1 (25 findings). Verdict classes unchanged; short verdict reworded to drop 'standard for 2022 scale'.
