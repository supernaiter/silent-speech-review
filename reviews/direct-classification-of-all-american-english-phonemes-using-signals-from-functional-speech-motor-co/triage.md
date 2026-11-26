# Triage of the evaluation (2026-11-26)

Evaluator: a language model separate from the writer. Each finding was checked against notes.json, the audits and the specific source passage.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| F1 | applied | Audit population held `isca-manca13_interspeech` (scalp-EEG ERP) and `pmc-3127251-tempo` (Ghitza 2011, oscillator model); the audit note already flagged Brumberg 2011 and Bouchard 2013 as text-only subset matches. Recounted before 2013-11: 9 studies, small subset 4, full inventory 1, no discrete unit set 4, ECoG 5 with full inventory 0. | M06 inventory audit prior_tally and usual_approach; M06 Usual approach; Appendix |
| F2 | applied | Wilson et al. 2020 Results: "the T5 dataset accuracy was 36.8% across 24 consonant classes (vs. 36.1% in Mugler et al.'s best participant) and 27.7% across 16 vowels classes (vs. 23.9%)"; matched trial count and 600-ms window (notes w5, w6). Chance-ratio paragraph removed. | M06 comparison paragraph; Verdict sentence 5 |
| F3 | applied (verdict changed) | Target Sec. 4: "It is also the first to successfully analyze and classify individual phonemes within word production." New audit `within-word-phoneme-onset-classification`: 51 intracranial speech studies before 2013-11 (full-text pattern), phoneme onset within words 0, trial/stimulus/word onset 27. Deciding priors read: Brumberg 2011 (isolated phonemes), Pei 2011 (word-level classes), Leuthardt 2011 (isolated phonemes), Tankus 2012 (five cued vowels). Repetition: four subjects above chance (Sec. 3.1), and both Wilson participants (w11). M06 verdict standard -> ahead (protocol only). | New audit; slots M06; Verdict; M06 section; verdict.json |
| F4 | applied | Target Sec. 1 cites "up to 21% classification success of all phonemes" (t53). | Verdict sentence 2 |
| F5 | applied | Target Sec. 3.1 does not say how 20.4% was formed; notes q1b unstated. "Pools two classifiers" removed. | Outrun bullet 1; Question 1 |
| F6 | applied | Target Sec. 2.4: "300 ms prior to 300 ms after phoneme onset"; "These 12 time bins" (q8). | Outrun bullet 2 |
| F7 | applied | Sec. 2.5 "fully independent"; Sec. 2.4 neighbouring-phoneme sentence (q4); fold grouping by trial not stated. Overlap stated as (inference). | Outrun bullet 3; Next M12; Question 3 |
| F8 | applied | Wilson: onset-bias realignment 12.9% reduction, "inflate ... but only modestly so" (w7, w8); LRR 29.3% to 25.8%, microphonic artifacts in ECoG (w9, w10). "Governs" -> "depends on". | Verdict sentence 4 (strongest confound); M06 last sentence |
| F9 | applied | 2013 items checked by month (all before 2013-11); Pasley 2012 versions (pmc-3269422-pasley, pbio.1001251) merged: 33 studies, k-fold 9, random split 8. | M12 audit prior_tally; M12 section; slots M12; Appendix |
| F10 | applied (partly) | Sec. 2.5 peak-performance procedure and time-bin loop (q6, q7). The text does not say the Sec. 3.1 figures use the peak configuration, so this is asked rather than asserted. | Outrun bullet 4; Question 2 |
| F11 | applied | Ratio sentence deleted (replaced by F2). | M06 section |
| F12 | applied | 132/618 removed from the Usual approach line, kept in Appendix as all-years data. | M12 section |
| F13 | applied | LDA/140-feature and 5x10-fold restatements removed; M12 keeps only the comparison with the field. | M06, M12 sections |
| F14 | applied | Notes p17: four-class matched groups from nine consonant pairs. | M06 Usual approach |
| F15 | applied | Bouchard 2013 read in the Methods passage: kNN classification of cortical sites by articulator, no speech-unit classifier (bo1); ECoG count among the 9 stated (5, full inventory 0). Wiki folder doi-10.1038-nature11897 carries DOI 10.1038/nature11911 in the paper text. | M06 Usual approach; Appendix; refs |
| F16 | applied | Word-identification bullet dropped; the ITR remains in bullet 2. | Outrun section |
| F17 | applied | Chen et al. 2024 Methods: PCC between decoded and actual spectrograms (ch2). | M12 State of the art; slots M12; refs note |
| F18 | applied (checked) | Tankus et al., Nat Commun 3:1015, published 21 Aug 2012, depth-electrode units, five vowels (tk1); in the wiki but outside the M06 ledger pattern, so used as a read deciding prior, not added to the 9-study count. | M06 Usual approach; onset audit read_fulltext; refs |

Counts: 18 findings; 18 applied (F10 partly: asked, not asserted); 0 rejected; 0 unverified.

Gate after triage: check_review.py 0 FAIL / 0 WARN (body 6,993 characters); verify_quotes.py 0 missing. check_review.py compares deciding-prior pids with reference pids joined as a string, so Brumberg 2011 and Pei 2011 now carry a single pid each in refs.json (their duplicate wiki folders are no longer linked).
