# Evaluator: a language model separate from the writer

Date: 2026-11-27. Target: Brumberg, Wright, Andreasen, Guenther, Kennedy, Front. Neurosci. 5:65 (2011), doi:10.3389/fnins.2011.00065.
Sources I read: the review (`classification-of-intended-phoneme-production-from-chronic-intracortical-microelectrode-recordings-i.md`, the same text as `compact.md`), `claims.md`, `slots.json`, `verdict.json`, both audits, `notes.json` (spot checks), the target text (`papers/doi-10.3389-fnins.2011.00065/source/text.txt`, with section headings checked in `papers/pmc-3096823-phonintent/source/paper.xml`), and the source texts of Guenther 2009, Brumberg 2009 (Interspeech), Flinker 2010, Kellis 2010, Hueber 2008, Walliczek 2006, Willett 2023, Card 2024 (`pmc-11328962-rapidcal`) and the population folders of the M12 audit.

## Claim table

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target first public 12 May 2011, so the prior cutoff is 2010-11 and the [concurrent] window runs 2010-11 to 2011-11 (Appendix) | Target p.1 "published: 12 May 2011"; p.13 "Received: 17 September 2010; accepted: 24 April 2011" | correct | The cutoff is six months before the publication date. The manuscript was received in Sept 2010, so nothing in Oct–Nov 2010 can be held against the authors, and the review does not do so. |
| 2 | 38 of 39 phonemes analysed; 431 trials; five sessions; 59 sessions; 31 clusters; two channels (M06, M12) | § Experimental protocol; § Recording system; § Neurotrophic electrode design | correct | The authors give the selection rule for the five sessions ("no data collection technical problems and no biofeedback"). The review leaves it out (finding 15). |
| 3 | Bins "randomly partitioned into 10 mutually exclusive data sets ... between 180 and 216 data points per-phoneme"; 300-ms bins; 20 bins per trial (Verdict, M12, Leakage) | § Classification analysis; § Experimental protocol | correct, but the review misses a stronger reading | 10–12 repetitions × 20 bins = 200–240 bins per phoneme, and 0.9 of that is exactly 180–216. These are the per-phoneme bin counts in a 9-fold training set, so the bin is the unit of partition (inference). The review does not draw this out (finding 5). |
| 4 | No statement that a trial's 20 bins share a fold (Verdict) | § Classification analysis | correct | The paper has no such statement. |
| 5 | "Binomial tests treat correlated bins as independent" (§ Statistical analysis) | § Statistical analysis | insufficient evidence | The paper gives no n for the binomial test. Chance "varied depending on the number of phoneme repetitions (10–12)". The claim is the reviewer's inference but is not labelled as one. |
| 6 | "Conservative, lower-bound" quoted at (§ Discussion) | paper.xml section titles | wrong location | Both the sentence and "we do not expect the classifiers ..." are in Results, § Classification summary. The full sentence: "That our methods, including potential noise sources (spikes and user response), is capable of predicting phonemes at above-chance rates is impressive and the rates reported represent a conservative, lower-bound on the possible classification/prediction performance." |
| 7 | "Truly not great enough to be useful as a communication device" (Verdict) | § Utility for functional BMI | correct | |
| 8 | Attempt checked only by instruction and post-trial denial; rejected-trial counts not reported (Intended) | § Experimental protocol ("On rare occasions when he denied trial attempts the data were rejected"); § Discussion (spasm and railing rejections) | correct, but the authors' own caveats are not credited | The authors write "we were not able to determine precisely when the study participant began" (§ Experimental protocol) and "It is not possible to obtain instantaneous verification" (§ Classification summary, not § Discussion). They also say the attempt-versus-imagery hypothesis "was not explicitly tested". |
| 9 | Sorting parameters reused for all sessions; single and multi-units pooled; the five sessions not identified (Unit stability) | § Recording system | correct, but partly the authors' own point | The authors pool single and multi-units on purpose (§ Phonetic and articulatory relationships) and concede "Improved spike sorting will likely reduce ..." (§ Classification summary). |
| 10 | "Two authors own the electrode maker" (COI) | Conflict of Interest Statement | insufficient quote | The text says Kennedy is a 98% owner and Andreasen a 2% owner of Neural Signals Inc. The target's text does not say that this company makes the electrode (only `notes.json` t40 does). |
| 11 | Guenther 2009: three-vowel task, hit rate 45% to 70%, feedback within 50 ms [2] | pmc-2784218 Abstract | correct | |
| 12 | Kellis 2010: ten words, 48% with the best five electrodes [3] | pmc-2970568 Sec. 3.3 | correct | "Selecting the five electrodes over FMC with best overall accuracy ... (48% for the ten-word combination)". |
| 13 | Hueber 2008: 40 phonetic classes, 60%, no LM, one speaker reading aloud [4] | Sec. 2.1, 3.1, 3.2 | correct | The task is continuous HMM phone recognition of read, voiced sentences, not classification of isolated cued attempts (finding 14). |
| 14 | Walliczek 2006 "trained 45 phoneme units for EMG recognition of silent speech" [5] | Sec. 1, 4.1, 4.3 | wrong | The 45 comes from a general sentence in the introduction ("When using a phoneme based system 45 phonemes have to be trained ... for English"). The study used 32 expressions built from 21 syllables (Sec. 4.1), so its phoneme models cover only the phones in those words. |
| 15 | Leuthardt 2011 [concurrent], four phonemes [6] | audit read_fulltext | correct | Pei et al. 2011 (J Neural Eng 8:046028, vowel and consonant sets) is also [concurrent] in the audit and is not mentioned. That is optional. |
| 16 | Willett 2023: 39 phonemes at 62%, naive Bayes, 1 s per trial [7] (M06 SOTA) | Willett text, "Neural representation ..." | correct, and on the slot's step | This is isolated attempted-phoneme classification, so it is the right step for M06. |
| 17 | 21.0% SVM, "about a third" of 62% (inference) | Table 3; § Classification summary (LDA 16.9, SVM 21.0, FDA 17.6) | correct | 21/62 = 0.34. The conditions differ (bin vs trial, 2 channels vs arrays), and the review flags the bin difference. |
| 18 | Willett 2023: real-time, held-out sentences, 23.8% WER, 125,000 words (M12 SOTA) | Willett Intro and Abstract | correct value; not the best today | Card et al. 2024 (NEJM, in the wiki as `pmc-11328962-rapidcal`) reports online decoding with a 125,000-word vocabulary at 90.2% accuracy on day 2 and 97.5% sustained in self-paced conversation (finding 13). |
| 19 | "Twenty of 38 phonemes exceed chance for all three classifiers (Fig. 4)" | Fig. 4 caption; Abstract | correct, but the target contradicts itself | § Classification summary splits the phonemes into "above chance (N = 18) and those below (N = 20)". The review does not mention the conflict (finding 11). |
| 20 | M06 prior population: 3 intracranial studies, none with a discrete unit set (Verdict, M06, Appendix) | M06 audit prior_tally (isca-brumberg09_bcisynth, pmc-2784218-wireless, doi-10.1523-jneurosci.1809-10.2010) | tally correct; meaning misleading | Two of the three are reports of the same participant's formant-synthesizer experiment. The third is Flinker et al. 2010, a study of auditory-cortex suppression during speech, which is not a decoder (finding 3). |
| 21 | No prior discrete speech-unit decoder before 2010-11 (M06 usual approach) | Target § Classification summary and § Utility ("Blakely et al., 2008; Kellis et al., 2010"); notes t24; audit note | incomplete | Blakely et al. 2008 (micro-ECoG, four phonemes) is cited by the target as prior phoneme decoding and is recorded in the notes. The review never names it (finding 2). |
| 22 | M12: 12 priors; random trial split 3, k-fold 2, held-out session 1, online 4 (mentions) | M12 audit prior_tally | tally correct; "usual approach" label not supported | The three random-split mentions are Brumberg 2009 (Interspeech), Denby et al. 2010 (a review) and Brumberg et al. 2010 (a review). At least five of the 12 are not decoders: Besle 2008, Towle 2008, Sahin 2009, Edwards 2010 and Flinker 2010 (finding 4). |
| 23 | M12 "fewer than three prior studies hold out sessions" | audit held_out_session_or_day = 1 | correct | The online closed-loop count (4) meets the "behind" threshold on its face, and the text does not say why it does not apply (finding 4). |
| 24 | M06 verdict standard because there is no repetition | SKILL.md `ahead` rule; target (one participant, sessions pooled, no per-session result) | correct application | The Conclusion concedes the point: "may be specific to the current subject and study, and may not generalize well to others". |
| 25 | Full-text tally: 45 prior hits, 0 intracranial full-inventory (Appendix) | M06 audit fulltext_tally | correct as a tally | The audit's list of full-phone-set recognizers includes Walliczek, which is a false positive (see row 14). |

## Required fixes, ordered by impact

1. **Major. Verdict sentence 2; M06 body ("Walliczek et al. trained 45 phoneme units"); Appendix M06 ("surface EMG [5]").**
   Evidence: the "45 phonemes" is a general sentence in Walliczek Sec. 1. The experiment used a 32-expression vocabulary built from 21 syllables (Sec. 4.1, 4.3), so it is not a full-phone-set precedent. One of the two reasons for "standard, not ahead" therefore rests on a misread.
   Fix: drop [5] as a full-phone-set precedent, or recast it as "phoneme-unit EMG recognition over a 21-syllable vocabulary". If an EMG precedent is wanted, Walliczek Sec. 2 reports that Jorgensen and Binsted (HICSS 2005) "trained and recognized eighteen vowels and twenty-three consonant phonemes" recorded in isolation from subvocal EMG at 50%. That is an isolated-classification design closer to the target's, but it is second-hand and the original is not in the wiki, so label it so. The `standard` verdict still stands on Hueber [4] and on the missing repetition.

2. **Major. M06 Usual approach ("the 3 intracranial ledger studies decode no discrete speech-unit set"); Verdict sentence 1.**
   Evidence: the target cites Blakely et al. 2008 (micro-ECoG, four phonemes) as prior phoneme decoding (§ Classification summary; § Utility for functional BMI). `notes.json` t24 records it, and the audit notes it is not in the wiki. A reader of the review would conclude that no discrete phoneme classifier existed before the target, which the target itself contradicts.
   Fix: add one clause, for example "the target itself cites a prior four-phoneme micro-ECoG classifier (Blakely et al. 2008, not in the wiki)". This leaves the class-set step from four to 38 phonemes intact.

3. **Major. M06 Usual approach and table cell ("base 3 prior intracranial studies"); Appendix ("Prior population 3 unique studies").**
   Evidence: the population is Brumberg, Kennedy and Guenther (Interspeech 2009) plus Guenther et al. (PLoS ONE 2009), which are two reports of one participant's synthesizer experiment, plus Flinker et al. (J Neurosci 2010), a study of auditory suppression during speech with no decoder. "3 prior intracranial studies" overstates the base. In effect it is one decoding experiment, counted twice, and one non-decoder.
   Fix: state the composition in the Appendix and in the Usual approach line, for example "3 ledger studies: two reports of the same participant's formant decoder and one auditory-suppression study". Either merge the two same-experiment reports under the "versions merged" rule or say why they are kept apart.

4. **Medium. M12 Usual approach, Verdict line and table cell ("Random trial split, base 12 (pattern match 3)").**
   Evidence: matched = 3 means that 3 of the 12 texts mention a random trial split. Online closed loop is mentioned by 4, so random split is not the modal design. The three random-split mentions are Brumberg 2009 and two reviews (Denby et al. 2010; Brumberg et al. 2010). At least 5 of the 12 are perception, mapping or suppression studies, not decoders. The `behind` rule (at least 3 earlier papers meet a condition the target does not) looks met by "online 4", and the text gives no reason why it does not apply. The reason is that all four are one group's reports of one participant's experiment, two of them reviews.
   Fix: (a) Change the table cell to "No common split; mentions mostly in reviews; base 12 (pattern match 3)", or name online closed loop as the most-mentioned design. (b) Add one clause to the M12 verdict: "the four online mentions are reports and reviews of one experiment [2], so `behind` is not met". (c) Add Kellis 2010 as the only independent offline classifier read: it split by trial, with 15 training and 15 decoding trials per word (§ Methods). That is the direct contrast with the target's bin-level split (inference).

5. **Medium. Leakage bullet; M12 Usual approach ("180 to 216 per phoneme").**
   Evidence: 0.9 × (10–12 repetitions × 20 bins) = 180–216. The figure is therefore the per-phoneme bin count in a training set of nine folds, so bins, not trials, were partitioned (inference). As written, "180 to 216 per phoneme" reads as a total and does not support the leakage claim. Separately, "binomial tests treat correlated bins as independent" is not in the paper: n is not stated.
   Fix: write "180–216 training bins per phoneme, which equals 0.9 × 20 bins × 10–12 trials, so the bin is the unit of partition (inference)". Rewrite the binomial clause as "the binomial test's n is not stated; if it counts bins, it treats correlated bins as independent (inference)".

6. **Medium. Verdict last sentence ("their reading of them as 'a conservative, lower-bound' does not [hold]").**
   Evidence: the paper never states fold assignment. With the arithmetic in fix 5, the inference becomes strong, but it is still an inference about an unstated procedure, while the sentence states it as fact.
   Fix: keep a plain position but tie it to the evidence: "is unsupported: the fold counts show bins, not trials, were partitioned, which biases accuracy upward (inference)".

7. **Medium. Location errors in "Where the claims outrun the evidence".**
   Evidence: "Conservative, lower-bound" is cited as (§ Discussion) but sits in Results, § Classification summary, in the same paragraph as "we do not expect the classifiers ...". The "Intended" bullet cites § Discussion for the lack of instantaneous verification, which is also in § Classification summary.
   Fix: change both to § Classification summary (Results). In the Verdict or the bullet, quote the lower-bound sentence in full or by its clause "the rates reported represent a conservative, lower-bound on the possible classification/prediction performance".

8. **Medium. Fairness: the Verdict ("Intended rests on ... no attempt onset"; "nothing repeats ... one participant") and the "Intended" and "Unit stability" bullets.**
   Evidence: the authors state each of these themselves. On attempt timing: "we were not able to determine precisely when the study participant began" (§ Experimental protocol). On generalization: "may be specific to the current subject ... may not generalize" (Conclusion). On spike sorting: "Improved spike sorting will likely reduce ..." (§ Classification summary). On attempt versus imagery: "not explicitly tested" (§ Experimental protocol). The review presents these as its own findings.
   Fix: open each point with "The authors concede X". Then keep only what they do not address: no rejected-trial counts, sorting parameters fixed over 10 months, and the consequence of an unknown onset for the lower-bound claim under a bin-level split.

9. **Medium. The "Help prove the feasibility" bullet.**
   Evidence: the authors themselves separate feasibility from usefulness ("did not evaluate the tested methods for usefulness in a functional BMI"; "truly not great enough"), so the contrast is weak. The real overreach is in the next sentence of § Utility for functional BMI: "the results presented here are immediately applicable to use in online applications". That claim rests on offline, bin-level cross-validation with no causal or online test.
   Fix: replace the feasibility quote with the "immediately applicable to use in online applications" quote and contrast it with the bin-level split and the group's own online test [2].

10. **Medium. M12 State of the art (and the table cell).**
    Evidence: Card et al. 2024 (NEJM; wiki `pmc-11328962-rapidcal`) reports an intracortical speech neuroprosthesis with online decoding over a 125,000-word vocabulary: "90.2% accuracy" on day 2 and "sustained 97.5% accuracy for self-paced conversations". This is later and better than 23.8% WER, under an online held-out evaluation.
    Fix: name Card et al. 2024 [later] as the state of the art for online held-out evaluation, or keep Willett 2023 and add Card 2024 as the current best, with its metric and condition.

11. **Minor. Internal inconsistencies in the target that the review misses (M06 "Twenty of 38"; Questions).**
    Evidence: the Abstract and Fig. 4 say 20 of 38 phonemes are above chance for all three classifiers, while § Classification summary says "above chance (N = 18) and those below (N = 20)". Also, the 20 bins of 300 ms cover 6 s, but the paper describes binning "during the 10-s SPEAK period" (§ Experimental protocol), and which 6 s were used is not stated. That matters for the attempt-window and lower-bound arguments.
    Fix: add both points to "Questions for the authors" ("Which 6 s of the 10-s response period do the 20 bins cover?" and "18 or 20 phonemes above chance?").

12. **Minor. Conflict-of-interest clause in the feasibility bullet ("two authors own the electrode maker").**
    Evidence: the paper says Kennedy 98% and Andreasen 2% "owner[s] of Neural Signals Inc.". It does not say in the text that Neural Signals makes the electrode. A financial interest is not evidence that a claim outruns its data, and placing it next to an overreach charge implies motive. It is not a component difference.
    Fix: remove it from this bullet. If kept, put it neutrally in the M13 cell: "Kennedy (98%) and Andreasen (2%) own Neural Signals Inc. (Conflict of Interest Statement)".

13. **Minor. Restatement in the body.**
    Evidence: "Twenty of 38 phonemes exceed chance for all three classifiers (Fig. 4)" follows the M06 verdict and supports no comparison. "The paper uses 10-fold cross-validation over random bins, 180 to 216 per phoneme, from 431 trials in five of 59 sessions" restates the method beyond what the comparison needs.
    Fix: delete the Fig. 4 sentence, or move it into the repetition argument ("three classifiers on one split agree on 20 phonemes; that is agreement, not repetition"). Shorten the M12 line to the split unit and the session count.

14. **Minor. Comparability of Hueber 2008 [4] (Verdict and M06).**
    Evidence: Hueber performs continuous HMM phone recognition of read, voiced sentences. The target classifies isolated cued attempts. "Full phone sets were already the units of phone recognition" is accurate, but "the class set is not new" glosses over the difference between the tasks.
    Fix: add "as recognition units in continuous read speech, not isolated classification".

15. **Minor. "Five of 59 sessions" (M12).**
    Evidence: the 59 sessions include passive listening and biofeedback sessions. The authors state the criterion: no technical problems and no biofeedback (§ Experimental protocol).
    Fix: add the criterion so that the figure does not read as an unexplained selection. Keep "sessions not identified".

Dating check: the window is correct, and no later work is treated as prior. Pei 2011 and Leuthardt 2011 are correctly [concurrent]. Kennedy's earlier Neurotrophic Electrode reports and Bartels 2008 (implantation method) contain no speech-unit decoding, so their absence from the population is not an error.

What holds: the central confound (the bin-level random split), the M06 `standard` verdict under the repetition rule, the comparator numbers for [2], [3], [4] and [7], and the chronology labels.

## Scores

- Procedure: 6/10. Audits and reading are in place, but a misread comparator went into the verdict, a target-cited prior was dropped, and the population composition is unexamined.
- Final text: 5/10. The main confound is right, but one verdict reason is wrong, there are two location errors, and several authors' caveats are presented as the reviewer's findings.

Counts: major 3, medium 7, minor 5.
