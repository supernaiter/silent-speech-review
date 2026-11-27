# Evaluator: a language model separate from the writer

Date: 2026-11-27. Target text checked: TASLP 25(12) article, `source_article/text.txt` (author-hosted PDF, sha256 e1c396cc...), not the dissertation in the wiki folder. Also read: the review, `compact.md`, `claims.md`, `*.slots.json`, `verdict.json`, `extra.json`, `*.plan.json`, the four audit files (top-level tallies), and the wiki texts of Toth 2009, GETS 2026, Hueber and Bailly 2016 and Wairagkar 2025. Crossref record for the DOI checked. Nothing in the wiki or the review files was modified.

## Claim table

| # | Claim (location in review) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | 83 evaluation utterances, 10 to 20 per session | Table I | correct | Eval column 20, 10, 10, 13, 20, 10; total 83. |
| 2 | p < 0.01 with no named test | §V-B | correct | Also true for the p < 0.01 in §V-D (Table III), which the review does not mention. |
| 3 | DNN 5.21 against 5.42, 5.46, 5.69 | §V-B; Fig. 5 | correct | The DNN is lowest in all six sessions (Fig. 5 values). The mean is the unweighted session mean (5.61, 5.44, 5.29, 4.94, 5.44, 4.56 give 5.21, inference). |
| 4 | GMM and one LSTM on 32 LDA dimensions, DNN up to 5,425 TD15 dimensions | §V-A; Table II | correct | Table II covers run time only. Fig. 5 does not say which LSTM variant (TD15 or LDA) is scored, and no section gives the Unit Selection input. |
| 5 | Label-free claim against LDA on force-aligned phone sub-states | §I; §III-A | correct, but the framing is too strong | §III-A presents the LDA as the general step "before training an EMG-to-speech conversion system". The best system, the DNN, runs on TD15 without the LDA (Table II), so the claim holds for the headline mapping. |
| 6 | Best "4.51" against best session 4.56 | §V-B; Fig. 5 | correct | This is an internal inconsistency in the paper. |
| 7 | Naturalness test varies only F0, names no mapping; four speakers in a three-speaker corpus | §V-D; Table I | correct | "three different utterances from four different speakers" against "six sessions total, from three speakers". |
| 8 | Table III: 28 against 22 and 41 | Table III | correct | Reference 81, flat F0 7. |
| 9 | ASR proxy trained on synthesized training-set output, trigram LM, 108/905/2,111 words, two speakers | §V-C; Fig. 6 | correct | |
| 10 | 7.3% at 108 words against 10.9% for an EMG recognizer on 160 utterances; authors concede the comparison is not direct | §V-C | correct, quote incomplete | The text gives 7.3% as a "mean WER" without naming the vocabulary. The authors also attribute part of the gap to more training data, a caveat the review leaves out. |
| 11 | Toth et al.: 6.37 MCD, five electrodes, 380 training sentences, one speaker | target §I, §V-B; Toth wiki ev-007, ev-elect | correct | The authors state the five channels and 380 utterances themselves (§I). 18% relative is (6.37 − 5.21)/6.37 (inference), correct. |
| 12 | Toth: 79.8% to 94.90% silent WER over 27 sessions from 14 speakers | Toth wiki ev-swer, ev-27, ev-whisper | correct, condition missing | These are WERs of the EMG-to-Whisper variant (noise excitation, no F0) on EMG-PIT, scored by ASR. The target itself cites the best value as 20.2% word accuracy (§I). |
| 13 | Hueber and Bailly: about 30% silent word accuracy; 60.4% GMM, ten naive listeners, 30 sentences | claims rows 16 and 19 | correct | The study uses EMA, French, two speakers. The review never names the signal, so a reader cannot see that the comparator is not EMG. |
| 14 | GETS 11.89% WER, Gaddy silent test, Whisper | GETS wiki e_wer, e_tab, e_ab | number correct, condition missing | One subject. The 11.89% depends on SSR text guidance (MONA-LISA EMG-to-text plus GPT-4 refinement): with the guidance off (ω2 = 0) the WER is 32.78%, and Gaddy and Klein reach 25.74% under the same scorer. |
| 15 | Tongue2Speech 15.93% WER, single TaL speaker, Whisper Medium | claims row 13 | correct | |
| 16 | Wairagkar 43.75% median open-transcription WER, naive listeners | wiki ev-per, ev-open | correct | Attempted speech, one participant with ALS. |
| 17 | Real-time figure is batch feature mapping without vocoder or I/O | §V-A | correct, but unfair | §V-A goes on: "details of an implementation with optimized real-time speech output can be found in [92]" (Diener et al., EMBC 2016). The review credits EMA closed-loop work [10] and not the authors' own pointer. |
| 18 | Unit Selection in conference versions [3], [4]; DNN published before | §III-D refs [68], [71]; §III-E ref [72] | correct | |
| 19 | Question: "Were faulty channels excluded before evaluation?" | §IV | wrong as written | §IV: "visibly faulty channels were excluded for that session". The paper answers the question. |
| 20 | First public 2017-11 | Crossref (created 2017-11-23, issue 2017-12); PDF created 2017-08-01 | plausible; IEEE early-access date unverified | The 2017-05 prior cutoff changes no count that the review relies on. |

## Findings (ordered by impact)

1. **High.** Location: Verdict, sentence 3 ("so its case against recognition followed by synthesis targets a route prior work had barely used"); M08 Usual approach.
   Evidence: the M08 population counts only studies that produce audio. `extra.json` lists the excluded studies as "recognition only", so recognition-then-synthesis can only show up when a study actually synthesized speech. The authors contrast their method with EMG ASR whose text "can be synthesized using text-to-speech systems" (§I, refs [33], [34]). EMG recognition was the dominant output of the field: 20 of 27 prior EMG decoders in the review's own M06 count are HMM/GMM decoders, almost all of them recognizers. The conclusion follows from how the population was built, so the argument is circular.
   Fix: rewrite the sentence along these lines: "Among prior synthesis studies, direct mapping was already the default (11 of 12, Appendix). The route the authors argue against is EMG recognition with text output, the majority design among the 27 prior EMG decoders (M06, Appendix), which had not been paired with synthesis." Drop "barely used".

2. **High.** Location: M06 and M04 State of the art (GETS), and the table rows for M04 and M06.
   Evidence: GETS reaches 11.89% only with SSR-derived text guidance (MONA-LISA EMG-to-text plus GPT-4 ensemble refinement). With ω2 = 0 the WER is 32.78% (GETS ablation table), above Gaddy and Klein's 25.74% under the same Whisper scorer. The study has one subject. As a state-of-the-art line for an EMG-to-acoustic mapping model, the stated condition leaves out the mechanism that produces the gain. This also contradicts the M08 line "The vocoder changed, not the route": today's best EMG result brings recognition back into the route.
   Fix: M06: "GETS (2026) [5] [later] reaches 11.89% WER (Whisper-medium, Gaddy single-subject silent test) with SSR and GPT-4 text guidance; with the guidance off it reaches 32.78%, and Gaddy and Klein's direct mapping 25.74% under the same scorer." In M08, replace "The vocoder changed, not the route" with a sentence noting that the best current EMG system adds a recognition-derived guidance signal to direct synthesis [5]. Add "single subject" in M04.

3. **Medium.** Location: Appendix setting sentence ("The group's conference versions [3], [4] are merged with the target"), refs [3] and [4], and the M08/M12 counts.
   Evidence: Zahner et al. 2014 (Unit Selection) and Diener et al. 2015 (codebook clustering) are separate peer-reviewed papers. Each introduces a different method and reports its own experiments, and the TASLP article cites them as "our previous work" ([68], [71]). They are earlier designs by the same group, the same status the review gives Toth 2009, not versions of this article. The same applies to [65] (Janke et al., ICASSP 2012, GMM EMG-to-speech), [72] (Diener et al., IJCNN 2015, DNN) and [92] (Diener et al., EMBC 2016, real time), which the article cites and the wiki does not index. Counted as priors, the M08 direct-mapping count rises (EMG examples beyond Toth exist), the M12 denominator rises (5 of 12 becomes 5 of 14 or more, still 3 or more), and the M06 change shrinks to the BLSTM plus the four-way comparison. No verdict changes, and no novelty claim is affected, because no slot is `ahead`. Treating Toth 2009 as a distinct prior design is correct (five single electrodes, FestVox GMM, one speaker for the main set).
   Fix: list [3] and [4] as prior designs of the same group, not merged versions, and recount M08 and M12, or state the counts as "excluding the group's own 2014–2016 EMG-to-speech papers". Add one sentence in M06: "GMM [65], Unit Selection [3], [4] and the DNN [72] were all published before; the new mapping is the BLSTM." Reconsider listing M08 as a component the paper changed. Direct mapping with MLSA was the group's inherited route (Toth 2009, Janke 2012, Zahner 2014, Diener 2015), so M08 reads as inherited.

4. **Medium.** Location: Appendix M08 and M12 populations; M08 Usual approach "none from EMG".
   Evidence: the target's own reference list contains prior direct-mapping synthesis studies that are missing from the 12: Lam et al. 2006 [45] (sEMG to speech), Tsuji et al. 2008 [46] (EMG speech synthesizer), Toda et al. [50], [51] (EMA-to-spectrum GMM, the basis of the target's GMM), and the group papers in finding 3. `extra.json` says "EMG among the prior direct studies: Toth 2009 only", and the M08 known-item recall is 0.17. The direction of the error (more direct-mapping priors) leaves "standard" unchanged, but "11 of 12" is not the population at the target's time.
   Fix: write "11 of 12 indexed prior synthesis studies (pattern match, Appendix); the article's own references add at least five more direct-mapping studies, two from EMG other than the group's ([45], [46]), and no recognition-then-synthesis study". Add [45], [46] and Toda et al. to the references if they are cited.

5. **Medium.** Location: M12 Usual approach and table row M12 ("Listener transcription; 12 prior (confirmed 5)").
   Evidence: 5 of 12 is a minority: 7 of the 12 prior synthesis studies did not run listener transcription, and none of the five is an EMG study (`extra.json` pids: ultrasound and video, three EMA, one neural). Calling it the usual approach contradicts the count, although the `behind` verdict on the "best comparable work" yardstick satisfies the rule (3 or more earlier studies meet the condition, best read and named). The tier is also mixed: the numerator is labelled confirmed, but the denominator is the M08 population, which is pattern match checked by title.
   Fix: table cell "Listener transcription in 5 of 12 prior (numerator confirmed, denominator pattern match); none from EMG". In the prose, keep "Verdict behind, best comparable work" and add that the best comparable [8] uses EMA.

6. **Medium.** Location: Verdict, sentence 5 ("The strongest overreach is the label-free claim").
   Evidence: the DNN, the method the paper recommends, uses TD15 without the LDA (§V-A, Table II), so the claim is true of the headline system. The overreach is that §III-A presents the LDA as the general preprocessing, and the GMM and one LSTM use it. The paralinguistic claim is stated as fact in the Abstract ("retaining important paralinguistic speech cues for information such as speaker identity and mood") and in §VI, and is never measured. The only prosody test keeps the reference MFCCs (Table III). That is the stronger overreach.
   Fix: "The strongest overreach is the Abstract's claim that speaker identity and mood are retained, which no experiment measures (Abstract; §VI; Table III). The label-free claim (§I) holds for the DNN on TD15 but not for the GMM and the LDA-based LSTM, which use an LDA trained on audio force-aligned phone sub-states (§III-A; Table II)." Apply the same change to the first bullet of "Where the claims outrun the evidence".

7. **Medium.** Location: "Where the claims outrun the evidence", bullet 4 (real time).
   Evidence: §V-A: "details of an implementation with optimized real-time speech output can be found in [92]". The review credits EMA closed-loop work [10] and omits the authors' own pointer to a real-time EMG implementation (EMBC 2016). This is a caveat the authors state themselves.
   Fix: "Real time in this article is batch feature mapping without vocoder or I/O (§V-A); the authors defer end-to-end real-time output to their EMBC 2016 paper ([92] of the article), which this article does not evaluate." Keep [10] only as a cross-modal precedent, or drop it.

8. **Medium.** Location: M06 body and M12 body (ASR proxy).
   Evidence: the paper's two objective metrics disagree on the GMM. It has the worst MCD (5.69, Fig. 5) but the second-best WER, "outperforming LSTM and Unit Selection" (§V-C). Because each recognizer is trained on the same mapping's synthesized training output (§V-C), the WER measures how learnable each mapping's output is, not human intelligibility. The review mentions the training detail but not the disagreement, which is the strongest evidence that the MCD ranking does not carry intelligibility.
   Fix: add one sentence to M06: "MCD and the ASR proxy disagree on the GMM, worst in MCD and second in WER (§V-B, §V-C); the ranking depends on the metric."

9. **Medium.** Location: M06 body, Toth comparison.
   Evidence: the authors themselves report Toth's five channels and 380 utterances (§I). The review presents the starting-point confound as its own finding without crediting that. A closer like-for-like comparison is available in the article: the two single-electrode sessions (six channels, 930 TD15 dimensions, §V-A), on which the authors find "no clear tendency" between single electrodes and arrays (§V-B).
   Fix: "The authors' comparison with Toth et al. (6.37 against 4.51, §V-B) sets one speaker, five electrodes and 380 training sentences (§I) against sessions of 450 to 1,771; on the single-electrode sessions the DNN reaches [value from Fig. 5], and the authors report no clear single-electrode versus array effect (§V-B)." Use the 4.51 the authors compare, or say why 5.21 is used.

10. **Low.** Location: M04 Usual approach (Toth numbers).
    Evidence: 79.8% to 94.90% is the EMG-to-Whisper variant (noise excitation, predicted MFCCs only), ASR-scored on EMG-PIT (Toth §4; wiki ev-whisper, ev-swer). The target cites the same result as 20.2% word accuracy (§I).
    Fix: "Toth et al.'s audible-trained EMG-to-Whisper variant at 79.8% to 94.90% ASR WER on silent EMG (27 sessions, 14 speakers) [2], cited by the authors as 20.2% word accuracy (§I)".

11. **Low.** Location: M04 verdict.
    Evidence: the `behind` verdict follows the rule (six earlier studies meet the condition; [8] and [2] read and named). The paper states its scope explicitly ("In this paper we use EMG recorded during audible speech", §I), yet frames the system as a Silent Speech Interface (Abstract). The review mentions §I, so the gap is fair. Two of the six (Florescu 2010, the Biosignals 2010/2011 entries) are recognition studies, and only [2] uses EMG synthesis. Calling [8] "best comparable" without naming its signal hides that the comparator is EMA.
    Fix: append "(EMA)" to [8] in M04 and M12. Add "Toth et al. [2] is the only EMG synthesis study among the six".

12. **Low.** Location: Questions for the authors, item 4.
    Evidence: §IV states that visibly faulty channels were excluded per session.
    Fix: replace it with "Was channel exclusion decided before the evaluation sets were scored, and how many channels were dropped per session?" Or delete it.

13. **Low.** Location: M06 body, input mismatch.
    Evidence: Fig. 5 reports one "LSTM" without saying whether it is the TD15 or the LDA variant, and §III-D does not give the Unit Selection input features.
    Fix: add "Fig. 5 does not say which LSTM input is scored" and fold it into question 2.

14. **Low.** Location: M12 body, intelligibility test.
    Evidence: §V-E says outputs were compared "to each other and to the given reference and resynthesized reference", which is six variants, yet says each utterance is synthesized "in 5 variations", and Fig. 7 shows only the four mappings. This is an internal inconsistency in the paper that the review missed. The p < 0.01 in §V-D also names no test.
    Fix: add the variant-count mismatch to the questions, and extend question 1 to the §V-D p-value.

15. **Low.** Location: M12 body (7.3% against 10.9%).
    Evidence: the authors add "The increased amount of training data may result in the fact that we get even better results" (§V-C), and the text does not tie the 7.3% to the 108-word vocabulary.
    Fix: "its mean 7.3% WER against 10.9% for an EMG recognizer trained on 160 utterances at 108 words is, the authors concede, not a direct comparison and partly a training-data effect (§V-C)".

16. **Low.** Location: Verdict sentence 2 ("the field's usual time-domain EMG features") and M06 Usual approach.
    Evidence: TD or E4 features appear in 12 of 27 (pattern match), fewer than half. The 20 HMM/GMM decoders are mostly recognition acoustic models, not regression mappings. "The lineage of the paper's GMM baseline" conflates the two. The Appendix's "Setting for every count" (any non-acoustic signal) does not match the M06 population (surface EMG only).
    Fix: "time-domain EMG features used by 12 of 27 prior EMG decoders (pattern match)". Split the M06 usual approach into "HMM/GMM recognizers (most of the 20)" and "GMM regression mapping in prior synthesis [2], [65]". In the Appendix, state that M06 uses the EMG subset of the setting.

17. **Low.** Location: References [1], [5], [7].
    Evidence: the wiki link in [1] opens the 2016 dissertation, not the article reviewed. "[later]" appears twice in [5] and [7]. The process wording "Read as the author-hosted journal manuscript" is acceptable as a version note.
    Fix: label the [1] wiki link "(wiki holds the 2016 dissertation, a different version)" and remove the duplicate tags.

Dating check: first public 2017-11 matches the Crossref record (created 2017-11-23, issue 2017-12). The PDF metadata (created 2017-08-01) and the DOI number suggest an earlier accepted manuscript. Its public date is unverified and changes no prior used in the review. Treating Toth 2009 as a distinct prior is correct. Merging Zahner 2014 and Diener 2015 is not; see finding 3.

Body text: there is no paper summary and there are no methodological disclaimers in the component sections. The only process wording is in the Appendix and in ref [1], which is acceptable.

## Scores

- Procedure: 6/10. Target numbers check out against the article. The populations miss the article's own cited priors, the version merge is wrong, and the M08 population is built so that it decides the Verdict's route argument.
- Final text: 6/10. The numbers are accurate and the target caveats are mostly credited. One circular judgment (finding 1), a state-of-the-art line without its decisive condition (finding 2), and the overreach ranking (finding 6) need fixing.

Counts by severity: High 2, Medium 7, Low 8 (17 findings).
