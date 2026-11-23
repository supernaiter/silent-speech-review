# Triage of the evaluation (15 required fixes)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | The split is stated as 70:15:15 (§2.1.2, t24); its unit is not (t43). | Verdict: "a 70:15:15 split of unstated unit". |
| 2 | applied | "without unit or speaker overlap" could be read as "has no speaker overlap"; t43 says overlap is unstated. | M12 usual-approach line rewritten. |
| 3 | applied | Chen et al. Sec. II: "produced from the dense layer was sent to the CTC decoder" (c21); Abstract: "four pieces of 64-channel electrode arrays" (c22). | notes c21, c22; M06 audit read_fulltext. |
| 4 | applied | The metrics differ: phrase classification (c11) vs. word ratio (t11). | M06 state of the art: "reports the same number ... a different metric". The 8.1% WER sentence was removed from M06. |
| 5 | applied (as inference) | 100 repetitions per word (t23), split unit unstated (t24, t43), training sentences concatenated from word recordings (t25). Leakage only follows if the split is at sample level, so it is marked "(inference)". | M12 paragraph names it the main obstacle to comparing 97.17%; Verdict says leakage is not excluded. |
| 6 | partly applied | In the wiki and read: Meltzner 2018 (doi-10.1088-1741-2552-aac965; 8.9% WER, 2,200-word vocabulary, subvocal, c30) and Benster 2024 (arxiv-2403.05583; CTC loss, 12.2% WER open vocabulary on the Gaddy silent benchmark, c31, c32). Gaddy & Klein 2020/2021 are in the wiki but are voicing (synthesis) papers; their benchmark enters through Benster, so they are not cited. Srivastava 2024 ("Unvoiced") is not in the wiki, so it is not used. Chen et al. stays the state of the art and is labelled "for a closed phrase set". | Verdict novelty sentence; M06 state of the art and evidence; Appendix (read in full); refs [2], [4]. |
| 7 | applied | Liu et al.: "92.0% ... (n = 7) ... 93 sentences while actually spoken in a natural and fluent way" (c23). Scenario 3 generates sentence data "directly without segmenting the word samples" (c24), so "zero parameters" means no segmentation. | notes c23, c24; claim table. |
| 8 | applied | The 4 word-concatenation matches are 4 wiki keys: two records of Liu et al. (doi-10.1126-sciadv.ado9576 and pmc-11204283-wearlipiface), Satterlee 2025 and a false hit (specom 2009). | M03 usual-approach line and Appendix; M03 audit usual_approach. |
| 9 | applied | The 8 full-text-only matches are folders and overlap the ledger studies (population_unique 20). The axis-comparison count of 4 covers 2 studies. | M05 Appendix wording. |
| 10 | applied | Hong et al.: 85.8% for 26 words (c25), stratified 5-fold subject-independent CV (c26), repeated 2 weeks later after reattachment (c27). | notes c25–c27; claim table. |
| 11 | applied | Target §2.1.2: "sixteen English words, two English sentences, and eight Chinese phrases" (t63). The 1–19 length range comes from the Fig. 3(a) axis (t12; figure value). | notes t63; claim table. |
| 12 | applied | No single section states the absence; the sentence is now worded as a list of absences (t32, t50, t51). | M06: "reports no second decoder, CTC search or language model (§2–3)". |
| 13 | partly applied | The bullet now states the two values plainly. The claim that 97.17% is "neither value" was rejected as a defect: a pooled mean over unequal word and sentence counts lies between 97.16% and 97.24%, and 97.17% does. | Claims bullet reworded. |
| 14 | applied | Maier-Hein et al.: 97.3% within-session (c28) to 76.2% after repositioning (c29). | M12: "from 97.3% to 76.2%". |
| 15 | partly applied | The counts cover all years. A by-year split was not computed. | Appendix M06: "(pattern match, all years)". |

Counts: 12 applied (5 as inference), 3 partly applied (6, 13, 15), 0 rejected outright, 0 unverified. The parts not applied are listed in the rows above.
