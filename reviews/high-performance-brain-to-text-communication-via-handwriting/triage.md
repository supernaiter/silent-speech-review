# Triage of the evaluation (2026-11-25)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Target reports no correct-characters-per-minute rate for itself (searched sc_text.txt); 90 cpm at 5.4% CER (t16) vs 39.2 ccpm (c1). | Verdict states what each number measures; ~85 correct cpm marked (inference). |
| 2 | applied | Pandarinath 2017 used a ReFIT Kalman filter + HMM click decoder (p1); target Fig. 4 analysis: 72% larger nearest-neighbour distances, characters easier to classify than lines (t36, t74). | Verdict: action and decoder change together; letters-vs-lines evidence added. |
| 3 | applied | Audit M04 now uses one basis, full-text pattern counts over 154 studies (imagined or inner speech 68, attempted speech 56, cursor 37). | M04 Usual approach, table row M04, Appendix. |
| 4 | partly applied | Card 2024 text names neither a CTC loss (c22) nor a sentence-disjoint split (searched text). | M02 and M06/M07 state of the art = Card 2024, with "loss not named"; CTC attributed only to Willett 2023 (c14). M12 keeps Willett 2023 because only it states the split; reason given in the text. |
| 5 | applied | Wiki-wide search of 3,363 folders dated 2020 or earlier for attempted or imagined handwriting, letter writing, character trajectories: 2 hits, both reference-list mentions (hw_prior_search.txt). The 2020 "imagined handwriting" preprint is a version of the target. | Verdict wording "no wiki study dated 2020 or earlier decodes handwriting (Appendix)"; Appendix M04 entry. |
| 6 | applied | c29: 110 cpm is T18's peak; T17 peaked at 47. | Verdict and M04 state of the art: "peak ... in one of two participants". |
| 7 | applied | Abstract says ">99% accuracy offline with a general-purpose autocorrect" (t23). The corpus is not in the main text; the BNC is named only for sentence prompts, not for the language model. | Verdict and claims bullet reworded: the figure is labelled offline; the remaining issues are the unstated corpus and OOV substitutions. |
| 8 | applied | Moses 2021 vocabulary is 50 words (c26). | M07 labels it the [concurrent] small-vocabulary study. |
| 9 | applied | Herff 2015 imposed audio-derived forced-alignment labels on ECoG (h1, h2), read in the passage. No CTC comparison in target notes. | M02 usual approach names Herff 2015; verdict reason changed to "difference not tested". |
| 10 | applied | Pattern count cannot separate online from offline LM use. | M07 usual approach: "named in 134 of 1,162 studies (online or offline not separated)". |
| 11 | applied | Levin 2026 evaluated decoders offline (c41); T18 decoder trained from scratch on one session (c37). | M04 section: "an offline [later] analysis". |
| 12 | applied | t47 single participant is the authors' own statement. | Verdict: "as the authors state". The target does not itself claim "more than double" in the notes, so that wording stays the reviewer's. |
| 13 | partly applied | Denominators are correct but opaque. | Appendix M06 line now names which population each count uses; table counts kept as slot-filled tiers. |
| 14 | rejected / unverified | eLife volume, Brain2Char 17(6):066015 and Nature 620:1031-1036 are not in the wiki texts; left out rather than added from memory. DOIs of [5] and [6] are taken from the wiki manifests and their first pages (bioRxiv 10.64898 prefix). | none |

Counts: 14 findings; 11 applied, 2 partly applied, 1 rejected/unverified.
