# Triage of the evaluation (lipreading-using-convolutional-neural-network)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Target Sec. 4 ("image sequences from all 300 words were used") and Sec. 5 (5/6 of shuffled frames trained the CNN); Sec. 6.3 (PCA and 6 × 6 are unsupervised). The leak and the supervision both favour the CNN in the Fig. 5 comparison. | Verdict (strongest confound); claims-outrun bullet 1 |
| 2 | applied | Heckmann 2001 Sec. 2: inputs are chroma-key lip parameters, not PCA. Duchnowski 1994 Table 1: 384 gray levels 55/44, 32 PCs 52/45 (notes p6). | M06 section; claims-outrun bullet 1 no longer cites Heckmann |
| 3 | applied | 79 counted HMM mentions only. Recount of the conjunction (HMM and hand-crafted both named) on the revised population: 80 of 110. | M06 usual approach, slots.json (n 110, matched 80), Appendix |
| 4 | applied | matched 36 was the speaker-independent mention count; now 46 of 110 on the revised population, labelled as such. | slots.json M12 field, M12 usual approach, Appendix |
| 5 | applied | Duchnowski Sec. 3: PCA and LDA "computed using only the training set", one speaker (notes p4, p5). Named as the best comparable prior. | Verdict, M12 section |
| 6 | applied | Ngiam Sec. 4: "We ensured that no test data was used for unsupervised feature learning" (notes n3). | M12 section |
| 7 | applied | Cox Sec. 3: multi-speaker mode "is widely adopted" (notes c4). Behind now rests on the test-word leak only. | Verdict, M12 section, verdict.json short, slots.json M12 note |
| 8 | applied | Ligatures (fi, fl, ff) normalised in the text loader of population.py and counts.py; all counts recomputed (variability or significance 28 of 110 on the revised population). | Both audits, Appendix, M12 usual approach |
| 9 | applied | Frame-split pattern now matches the target's and the journal version's split sentences; a broader shuffle or random-split pattern hits 2 prior studies (isca-lucey07-multipose, isca-shao06_interspeech), both utterance-level, read. 0 of 110 holds. | M12 audit, Appendix |
| 10 | applied | Duchnowski's MS-TDNN is a shared-weight temporal convolution over lip-pixel vectors. | Verdict, M06 section ("spatial (2-D) convolution") |
| 11 | applied | Noda 2015 Sec. 2.3 and ref. 19 cite Huang and Kingsbury 2013 (notes j5). | M06 section |
| 12 | applied (partly) | Lan 2010, Luettin 1996 and Yoshida 2010 were missed because their ledger text lacks task terms. The population now also admits optical-camera studies whose title names the task; 22 decoders were added after a hand check of all new prior and [concurrent] rows, and 53 new non-decoders were listed out. Nakadai 2003 not added: its visual stream serves source localization for a humanoid robot, not lip reading. | population.py, exclude.txt, all counts; Lan cited in M12, Yoshida in the Appendix |
| 13 | applied | Sec. 4 sentence added as notes t50 and cited in the text and claim table. | Verdict, M12 section, claims.md |
| 14 | applied | Sec. 4 answers the old first question. | Questions: now asks how word accuracy changes with a CNN retrained without the test words |
| 15 | applied | Sec. 6.3 "closed-speaker" is the authors' own label. | Verdict |
| 16 | applied | Noda 2015 Sec. 5.2 trains on 360 words without naming the change; 40 classes have higher chance than 84. | M12 section ("without naming the change", "at higher chance") |
| 17 | applied | Monophone word HMMs over 84 test words imply a pronunciation lexicon (Sec. 6.3). | slots.json M07 |
| 18 | applied | Sec. 7 (speaker-independent model with more speakers) and Sec. 6.1 (better target labels) are the authors' recommendations. | What the field needs next, M12 and M02 items |
| 19 | applied | Sec. 7 "the prepared training dataset is insufficient to acquire a speaker-independent model" (notes t51). | M12 section |
| 20 | applied | Process wording. | "meeting the rule of three" removed |
| 21 | applied | arXiv 1904.01954 (2019), Pattern Recognition Letters 2020. | M12 state of the art; refs note |
| 22 | applied | SyncVSR states vq-wav2vec tokens (notes s3) and cites the self-supervised vq-wav2vec paper (notes s5); the outside-audio wording without a quote was removed. | M06 state of the art |
| 23 | rejected | 10.5555/3104482.3104569 returns 404 at doi.org (handle not found). | Reference kept with URL |
| 24 | applied | Contradiction with the M12 leak finding. | M06 state of the art: "84 test words unseen by the HMM" |
| 25 | applied | Fig. 2 gives mean and SD over six speakers for the CNN alone (notes t53). | M06 section |
| 26 | applied | "Hand-labeled data" in Sec. 1 refers to lip-shape models. | Claims-outrun bullet now says mouths are still cropped by hand |
| 27 | applied | Sec. 7 repeats "significantly outperforms" (notes t52). | Claims-outrun bullet |
| 28 | not applied | Petridis's "non-standard" remark on random 60/40 splits is recorded (notes e6) but left out of the text to stay within the length limit. | notes.json, M12 audit |
| 29 | applied (partly) | The chance level for 84 words is about 1.2% (inference). It is in the M07 slot note; it was cut from the prose for length. | slots.json M07 note |

Verdict changes: none (M06 standard, M12 behind). M12 behind now rests on the test-word frames in CNN training only; seen speakers are labelled as typical of the field at the time.
