# Triage: Large-Scale Visual Speech Recognition

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| H1 | applied | Table 1 baselines retrained on LSVSR with the same 5-gram (t14d, t19-t25); Table 2 changes data, model, decoder, LM | M02 last paragraph, Verdict, slots M02 note |
| H2 | applied | Makino et al. 2019 trained only on YouTube 31k h, LRS3 visual-only 33.6% (arxiv-1911.04890 Sec. 4.5, Table 7; notes c7, c7b) | Verdict sentence 2; "lasting contribution" dropped |
| H3 | applied | Chang et al. train on YT and fine-tune on TED-LRS3 (arxiv-2302.10915 Sec. 5.1; c4b); 4.3x ratio removed; Makino added as zero-shot comparator | M02 State of the art, M06 State of the art, slots |
| H4 | applied | HMM 57 includes LipNet and WAS (mentions); human-reader pattern misses WAS, so at least 6; M07 33 is a mention count | M06/M07/M12 usual-approach lines relabelled as mentions; slots matched=null for M02, M06, M07, M12; Appendix |
| M1 | applied | Corpus sizes: TCD-TIMIT ~7 h (c1e), GRID 28 h (t37), ViaVoice 35 h (t38), LRS ~246 h (t40) | M02 usual approach |
| M2 | applied (relabelled) | Prior set still holds corpus papers, a review, a book chapter, enhancement/VAD items; not rebuilt, counts labelled upper bounds | Appendix setting line |
| M3 | applied | Sanabria video-only results are viseme accuracy (its Table 2; c2c); what survives: visual-only CTC phonemes decoded to words | M06 text, Verdict |
| M4 | partly applied | Almajai et al. 2016 is in the target's reference list and Sec. 2 credit (t47) but not in the wiki; sentence removed for length | not in text |
| M5 | applied | "essentially a uni-gram language model" (Sec. 5; t49) | M07 text, slots choice |
| M6 | rejected | Chang et al. text read names no external LM either way; USR 2.0 (published table, confirmed no external LM) kept as M07 state of the art, Chang cited in M06 | M07 unchanged |
| M7 | applied | Bootstrap SD of an error rate is its standard error | SD/SE bullet removed |
| M8 | applied | arxiv-1809.02108 Table 2: TM-seq2seq V 59.9% / 58.9% with extLM (c8); target Table 2 lists 57.9% | Claims-outrun bullet 1 |
| M9 | applied | USR 2.0 reports mean and SD over three seeds (Table 13; c5b) as evaluation-practice comparator | M12 State of the art |
| M10 | applied | wording | "never screened" -> "no stated exclusion" |
| L1 | applied | DOI on the paper's first page: 10.21437/Interspeech.2017-106 | refs.json |
| L2 | applied | Eesen recipe cited in Sec. 4 ("described in Miao et al. (2015)"; t51) | M06 usual approach |
| L3 | applied | "In both cases, V2P" quoted (t50) | Claims-outrun bullet 1 |
| L4 | applied | u2 | M12 "No repeated training runs are reported" |
| L5 | applied | LipNet (CTC) and WAS (attention) are the visual-only neural sentence readers; Sanabria is audio-visual | M06 usual approach |
| L6 | applied | 37-minute test (t15b), blur filter on validation/test only (t7f); M11 kept not_reported for split construction (u1) | slots M11 |
| L7 | applied | subset selection (>=12 words, first 6 words, title, category), whole-head vs mouth view (t15f, t15g) | M12 text |
| L8 | applied | Chang tokenizes at character level (c4c) | M06 State of the art |
| L9 | rejected | "Method language": no method walkthrough found beyond the minimal design statements each component needs | - |
