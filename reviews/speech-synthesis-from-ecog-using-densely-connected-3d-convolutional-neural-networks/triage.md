# Triage: speech-synthesis-from-ecog-using-densely-connected-3d-convolutional-neural-networks

Evaluation: a language model separate from the writer (2026-11-25), 10 required fixes plus one unrequired note (claim-table row 5). Each finding was checked against the passage it names.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | The slot-filled numbers in the components table counted studies with a filled slot across the 7,388-study wiki, not studies using the design. | slots.json: inherited rows have no count; M06 79/180, M08 51/180, M12 122/173 shown with denominators; M13 design "Offline analysis"; M05 design label corrected |
| 2 | applied | Berezutskaya, Methods: "another trial for each word was selected for test (12 words in total)", so this is a trial-held-out split. Chen, Fig. 2b caption: "training and validation sets in each fold did not overlap in unique words". | "What the field needs next" M12: word-disjoint folds cited to Chen; identification and listener tests cited to Berezutskaya |
| 3 | applied | Kohler, Sec. 2.2.1: "we feed in raw time series, as we do for the recurrent architecture, instead of averages in windows as utilized in the original study"; Dutch sentences. | Verdict; M06 evidence paragraph; verdict.json |
| 4 | applied | Berezutskaya, Results: "Pearson correlations in DN were significantly greater compared to MLP and S2S: H = 14.26"; "Each model was optimized per subject using the Optuna"; the Discussion still calls the gains over S2S "marginal". | Verdict; M06 paragraph; verdict.json |
| 5 | applied | Chen's PCC is computed on spectrograms, so the waveform-inversion step cannot affect it. | Removed the Griffin-Lim inference from the M08 state-of-the-art line |
| 6 | applied | "Proved well chosen" implied ahead without a same-setting test. Arthur and Csapó, Table I: mean MCD 3D-CNN 5.04 vs FC-DNN 4.55 dB on ten sEEG speakers. | Removed from the Verdict and M06; Arthur Table I added to M06 and the M06 Appendix entry; M06 audit read_fulltext (role prior) |
| 7 | applied | "most natural acoustic output" (Abstract) is the stated rationale for the vocoder design. | "Claims outrun": now described as an unmeasured design intent; dropped from the Verdict list |
| 8 | applied | Target §3: "we took the randomized spectrogram that was better than 95% of the randomization". | M12 section |
| 9 | applied | Target §2.4: "a fixed number of 80 epochs". | Questions for the authors |
| 10 | applied | The [5] quote was read in another review's published table; this work folder has no reader text for it. | Appendix M12: "[Anumanchipalli] value from the published table" |
| n1 (claim row 5, unrequired) | rejected | No novelty verdict is given: the review only notes that the "first" claim is scoped to quality, which the paper does not measure. It makes no claim of absence, so no deciding prior is needed. | – |
