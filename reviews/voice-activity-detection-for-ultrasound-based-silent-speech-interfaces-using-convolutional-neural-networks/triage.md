# Triage: voice-activity-detection-for-ultrasound-based-silent-speech-interfaces-using-convolutional-neural-networks

Evaluation: a language model separate from the writer (22 findings, 11 required fixes). Checked against notes.json and only the needed source passages.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | no change (correct) | Sec. 1, 4.2, 5.3 quotes (t1, t10, q2) | – |
| 2 | applied (headers) | Table 6 orientation fits recall 0.95 = 8096/8514; Table 5/6 in notes t25, t35, q3 | Claim table rows 4, 25 |
| 3 | applied | All four MCDs drop with UTI-VAD (Tables 4, 7; t19, t20, t36, t37) | M12 synthesis paragraph; Verdict |
| 4 | applied, evaluator's reading corrected | Headers are "MSE (dev) MSE (test) MCD" under "Removing silence by VAD" and "VAD + keeping 180ms silence" (h1, h2). The two columns are dev and test, not with/without 180 ms. With 180 ms kept (Conv3D+BiLSTM), test MSE 0.29 -> 0.26 but dev MSE 0.259 -> 0.35 | Claims bullet "Mixed MSE"; Verdict "MSE changes of mixed sign" |
| 5 | no change (correct) | inference marked | – |
| 6 | no change | q2 quote re-cut to match source | – |
| 7 | applied (headers) | Cornu Tables 1/3 columns "Voicing accuracy VAD accuracy" (p7); 96.99 and 74.07 are VAD column | Claim rows 9, 17; notes p7 |
| 8 | applied | Sharma Table 1 header SdA/SiA x Frame Level %/End Point % (s6); 92.2 = SiA frame level. Smoothing feeds the end-point detector (s7), so "smoothed over 14 frames" was removed from the 92.2 claim | M06 State of the art; slots M12 sota |
| 9 | no change (correct) | s3 | – |
| 10 | applied | t4: train/test/validation = 1015/24/50 | M12 paragraph labelled "train 1015, validation 50, test 24"; question reworded |
| 11 | rejected (scale), applied (scale stated) | Gosztolya Sec. 2.3: MUSHRA test, "from 0 (very unnatural) to 100" (g1); 1.19 is on that 0-100 scale | M12 paragraph "on a 0 to 100 scale" |
| 12 | applied | Audit state_of_the_art (confirmed in text): WER 31.64% on TaL80 | M12 synthesis State of the art |
| 13 | no change (correct) | t14, t16, t23, t58 | – |
| 14 | applied | Audit M02: forced alignment 17, acoustic VAD 6, union 23 unique studies (audio_derived_union); manual 22 | slots M02 field/matched; M02 Usual approach; Appendix |
| 15 | applied (re-judged, standard kept) | Audio-derived labels (23) are as common as manual (22); target uses the VAD form, which the text now calls the coarser variant; deciding priors (Cornu, Sharma) use alignment labels | M02 Usual approach and Verdict sentence |
| 16 | applied | Checked prior held-out-speaker studies re-audited: Joosten 2013, Cornu 2015, Tao 2015, Sharma 2019 = 4 (Takeuchi 2009 dropped as audio-visual fusion; Navarathna 2010 dropped, snippet names a corpus not a protocol) | Verdict "four checked ... (of 46 pattern matches)"; Appendix; audit note |
| 17 | applied (condition stated, verdict kept) | Same setting = non-acoustic VAD; 4 earlier studies meet a held-out-speaker protocol; best read and named (Sharma 2019). Cross-modality and corpus gap stated; the like-for-like protocol gap is the session split, which TaL1 (six sessions, c7; session-held-out benchmark, c12) allowed | M12 protocol paragraph; Verdict |
| 18 | unverified | No ultrasound-image VAD found among the 119 pattern matches beyond the target; no further reading | – |
| 19 | applied (partly) | Sharma paper text lists "Pujitha A. K"; "Kandala" not in the wiki source, unverified | refs.json author "Pujitha A. K." |
| 20 | unverified | TSD 2021 version not in the wiki source text read; existing row DOI kept, not cited | – |
| 21 | applied | Duplicate label came from the note field | refs.json note for sonkar2026tongue2speech |
| 22 | applied | t6 (82 fps, Sec. 2); h4 (WaveGlow, Sec. 2) | Claim table rows 46, 47; notes h4 |
| extra | unverified | Tao & Busso 2019 (Speech Communication) and Guy et al. 2020/2021 visual VAD not checked; Guy et al. would be [concurrent] | – |
