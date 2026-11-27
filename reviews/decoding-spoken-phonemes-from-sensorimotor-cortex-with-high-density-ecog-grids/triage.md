# Triage of the independent evaluation (round 1)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| F1 | applied | Target Sec. 3.3: "significant for the 4- and the 5-class classification at p<=0.05" in the 500 ms window (notes t84); 1-s window p=0.046 / 0.064 (t28) | Verdict sentence 5; the Timing bullet no longer repeats the significance claim |
| F2 | applied | Target cites Branco 2016 in Sec. 1, 2.1 (localization), 2.3 (re-referencing) and 4 (alignment) (t93, t82); Sec. 4 lists "Third ..." temporal concatenation and "Fourth ..." matched filter as distinguishing factors (t91, t92) | M06 paragraph rewritten: cited for other purposes, never as the classifier's source |
| F3 | applied | SKILL verdict rule: standard = matches, or the difference is not supported. SVM equal (p>0.3, t22); no density test (t81) | Verdict sentences 1–2; M06 and M05 verdict lines; slots notes "Departs; ... not supported" |
| F4 | applied | Sec. 2.3: trials cut on "VOT markers or rest trial temporal mid points" (t85); STMF 2-class 87.6% (t94) | New "Rest anchoring" bullet; Verdict confound sentence; SVM 92.8% dropped; M11 table row |
| F5 | applied | Sec. 4: "less accurate VOT determinations" and HFB alignment (t87, t82); single-class bias, four-phoneme analysis (t86); somatosensory confound (t88) | Timing, Rest and Feedback bullets credit the authors first; "lead with four phonemes" removed |
| F6 | applied (partly) | Wilson measured intracortical HLFP 125–5000 Hz (xw12); Roussel 2020 abstract read in the wiki (rs1, rs2); Micromed band-pass 0.15–134.4 Hz for 4 of 5 (t89); Table 1 sexes (t90). No contamination discussion anywhere in the paper (t80, all sections) | Acoustics bullet rewritten with Roussel [later], the band limit and a stated position; the male-speaker detail is noted in notes only, for length |
| F7 | applied | Target Sec. 4 and the reference list cite Blakely 2008, Bouchard & Chang 2014 EMBC, Mugler 2015 EMBC and Jiang 2016 EMBC (t97–t100); none is in the wiki index | Appendix setting line names them as not in the ledger; recall stated as 1.0 within the ledger, 7 of 11 cited (0.64); M05 count "at least 7" (inference); Blakely named in M05 |
| F8 | applied (partly) | Heger 2015 and Herff 2015: same seven Albany patients and the same authors → merged (population 16). Matthews 2012 reanalyses the Guenther/Brumberg participant with a different decoder: kept, justified in the audit. Kanas 2014 (speech activity detection): kept as a speech target, justified in the audit | Counts: M06 14/16, M12 k-fold 11/16, M05 bins recounted |
| F9 | applied | Inclusion rule: HD = about 4 mm; the target's L2 and L3 are 4 mm (Table 1) | M05 bins made disjoint (≤4 mm = HD or micro): 2 / 3 / 7 / 4; Appendix and audit |
| F10 | applied (partly) | Wilson abstract: onset differences "modestly increased decoding accuracy" (xw11) | Timing bullet. The oracle-onset sentence was dropped for length, because the timing point is carried by the latency argument |
| F11 | applied | Duraivel: mean P1 49.9% (xd6); four-way vowels micro-ECoG 71% vs ECoG 36.7% (xd5); full subsampling condition (xd7) | M05 state of the art; slots |
| F12 | applied (partly) | Zhao: awake surgery for brain tumours (xs8); six or eight classes (xs4). Mandarin and β1 features were not confirmed in the read text, so they are not added | M06 state of the art |
| F13 | applied | Chen: spectrogram PCC in a speech-synthesis pipeline (xch2). M12 tally_<slug> timing set to later; M05 tally_<slug> stale usual approach and read_prior replaced. The published keys are kept unchanged (append-only) | M12 state of the art; slots; audits |
| F14 | applied | Fig. 4 legend: templates "over trials and leave-one-out training sets" (t95); Sec. 2.4 screening excludes the test trial | Question narrowed to the run-wise z-score |
| F15 | applied | — | Branco details trimmed (patients, 76.25%); field-comparison bullet removed |
| F16 | applied | Target reference list: "NeuroImage. 2016;147:130–142" (t101) | refs.json volume 147, pages 130–142 |

Counts: 16 findings; 12 applied in full, 4 applied in part (F6 male-speaker detail, F8 Matthews and Kanas, F10 oracle-onset sentence, F12 Mandarin/β1, each with the reason above); 0 rejected outright. Verdicts unchanged.
