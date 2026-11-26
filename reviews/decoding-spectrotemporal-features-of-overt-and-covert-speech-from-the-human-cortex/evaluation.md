# Evaluator: a language model separate from the writer

Date: 2026-11-26. Independent evaluation of `decoding-spectrotemporal-features-of-overt-and-covert-speech-from-the-human-cortex.md`, checked against the target source text (`papers/doi-10.3389-fneng.2014.00014/source/sc_text.txt`), Pasley 2012 (`papers/pmc-3269422-pasley/source/text.txt`), Kim 2025 (`papers/arxiv-2510.27247/source/text.txt`), Janke 2010 (both versions), Pei 2011 (`papers/doi-10.1088-1741-2560-8-4-046028`), the four topic audits, `claimfill/audit_summary.json`, `extra.json`, `claims.md`, `slots.json` and `verdict.json`.

## Claim table

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Covert r = 0.34, overt r = 0.50, rest r = 0.30 after DTW (Verdict, M04, M11) | Target, Results > Covert Speech > Spectrogram-based | correct | "rcovert = 0.34 < rovert = 0.50 ... rcovert = 0.34 > rbaseline = 0.30, p < 0.005". The 0.50 is the DTW-aligned overt value (Fig. 9); 0.41 is the unaligned value. |
| 2 | Modulation covert 0.46 vs rest 0.42 (Claims outrun) | Target, Results > Covert > Modulation | correct | Overt modulation is 0.66. |
| 3 | Covert identification above chance in 1 of 7 subjects (Verdict) | Target, Discussion | correct | "covert speech reconstruction in one subject (out of seven) was accurate enough to identify speech utterances better than chance". Authors themselves call it "only marginally significant" (Discussion); group p = 0.032. |
| 4 | Covert above rest in 5 of 7 (M11) | Target, Results > Covert > Spectrogram | correct but selective | 5 of 7 is the spectrogram result. Modulation is 4 of 7 ("significant in 4 out of 7 individuals"); identification is 1 of 7. The review reports only the best of the three. |
| 5 | Same stories read in both conditions (Claims outrun) | Target, Abstract and Experimental Paradigms | correct | "subjects read the same stories both aloud (overt) and silently (covert)". |
| 6 | 90/10 random split of 7-s blocks, no held-out story or session (Claims outrun) | Target, Decoding Model | correct | "data were first divided into 7 seconds blocks. From these blocks, 90% were randomly partitioned into a training set and 10% into a testing set"; 4-7 jackknife models; no seeds stated. |
| 7 | "covert data have no held-out partition" (Claims outrun) | Target, Covert speech decoding | wrong as worded | The decoder never sees covert neural data, so all covert data are held out from training. The real gap is text overlap: covert scoring uses overt audio of the same stories, and the paper does not say whether it was restricted to overt test blocks. |
| 8 | Authors warp rest identically and state that DTW inflates correlation (M11) | Target, Statistics; Fig. 3 caption | correct | "Since DTW induces an artificial increase in correlation ...". The rest baseline is "a separate resting state recording session" with no scrolling text. |
| 9 | "one fifth of the overt margin survives (inference)" (M11) | Arithmetic on #1 | correct, spectrogram only | (0.34 - 0.30) / (0.50 - 0.30) = 0.20. For modulation it is (0.46 - 0.42) / (0.66 - 0.42) = 0.17, about one sixth. Marked as inference, as required. |
| 10 | Overt rank 0.91, covert 0.55, rest 0.48; 24-140 candidate 5-s segments (M12) | Target, Evaluation; Fig. 11 | correct | |
| 11 | Pasley: median rank 0.89 trial-averaged, 0.76 single-trial, 47 words, DTW-based (M12) | Pasley text, Results, Fig. 8 | correct | "median identification rank = 0.89"; "median = 0.76"; DTW "to temporally align words of variable duration". |
| 12 | Komeiji 2024: 46.3% TER overt-trained vs 46.6% covert-trained, 16 patients, eight sentences (M04 SOTA) | claims.md k1-k3 (Abstract) | correct | The comparator fits the slot: an overt-to-covert intracranial transfer with a matched covert-trained arm. It is a closed set of eight three-token sentences. |
| 13 | Wairagkar 2025: median listener WER 43.75%, one participant (M08 SOTA) | claims.md w1-w2 | correct | Fits M08 (synthesis from production). The setting is attempted, not covert, speech, and the target produced no audio. The review says so. |
| 14 | Kim 2025: overt recording of the same sentence as target audio for imagined EEG, 15 participants, 30 unseen test sentences (M11 SOTA) | Kim text, Sec. II-A, III-A | correct; "reuses" wrong | Kim uses the overt audio as a training target with a DTW loss, and splits 444/30 sentences. It attributes the design to its refs [29] (Lee et al., NeuroTalk, AAAI 2023) and [35] (Gaddy and Klein, EMNLP 2020), not to the target. |
| 15 | Berezutskaya 2023: 92-100% word identification against 8% chance, 12 words (M12 SOTA) | claims.md b1-b2 | correct number; weak fit | This is a classifier trained on target audio over 12 overt words. It is a different metric and a different candidate structure from percentile rank over 24-140 segments. |
| 16 | M04 prior: 3 EMG/ultrasound transfer studies (Janke 2010, Wand 2011, Florescu 2010) | M04 audit; Janke BIOSIGNALS text ("Cross-modal Testing") | correct | No neural prior is included ("no prior study uses neural signals", audit_summary). The target cites none of the three; it cites Pei et al. 2011 four times. |
| 17 | M08 prior: only Guenther 2009 (formants, real-time synthesizer) | M08 audit; target Intro | correct | The target itself credits Guenther 2009 and Mesgarani 2009 (perception, ferret) for continuous spectrotemporal decoding. |
| 18 | First public 2014-05; prior cutoff before 2013-11 | Target footer: "Received: 06 March 2014 ... published online: 27 May 2014" | correct | The 6-month concurrency window is applied correctly. |
| 19 | "none of the 10 earlier neural studies in its population" (Verdict, M11) | audit_summary M11 note | wrong description | The 10 are pattern-match hits: the Denby 2010 silent-speech review (not a neural study), Tankus 2012 (vowel classification), Pasley 2012 (perception), five auditory or audiovisual ERP/perception studies, an entrainment study and a hearing-loss ERP study. Only 2 decode speech, and none decodes covert speech. |
| 20 | M11 usual approach: heard-stimulus reference (pattern match 1) | SKILL.md line 112; slot-notes M11 row | rule breach | "M11 gives no field-practice count". Slot fill is 0.027. The one hit is a perception study, not a covert one. |
| 21 | M12 "Across all years correlation leads (122 of 173)" in the Usual approach line | review-format; caller rule | rule breach | This is an all-years tally used as the usual approach. The usual approach at the target's time is Pasley (1 reconstruction among 5 pattern-match hits). |
| 22 | "3 of the 23 confirmed" (M04), "1 of the 15 confirmed" (M08) | M04 and M08 audits | wrong denominator | 23 and 15 are all-years confirmed counts and include the target and later work. At the target's time the counts are 3 of 3 prior (all non-neural) and 1 of 1 prior. The M04 local tally also says confirmed_unique 25 against n 23. |
| 23 | Whole-wiki full-text check finds no earlier neural instance (M11) | audit_summary fulltext_recall | correct for neural; misses non-neural | Pre-target hits include `w-2246823171`: whisper/NAM-to-clear acoustic conversion scored against a DTW-aligned audible target. That is the same reference construction for a non-audible input. It was dismissed only as "not neural". |
| 24 | Deciding priors for M11 = Pasley (heard words), Guenther (cue formants) | Target Intro; wiki | insufficient | Pei et al. 2011 (J Neural Eng 8:046028; wiki `doi-10.1088-1741-2560-8-4-046028`, also `pmc-3772685-vowelcons`) decodes ECoG overt and covert words with class-label references, trained within each condition. The target cites it four times. It is the closest neural covert prior, and it is not named, read or in the M11 population. |
| 25 | "later work reuses it [5]" (Verdict) | Kim refs [29], [35] | overstated | Kim reuses the design, but through the EMG (2020) and NeuroTalk (2023) line. An earlier neural reuse, NeuroTalk (wiki `arxiv-2301-07173-neurotalk`), is not named. |

## Findings (severity, location, evidence, fix)

### High

1. **M11 "ahead" and M04 "standard" use contradictory population rules.** Location: Verdict sentence 4; M11 section; M04 section.
   - **Evidence.** M04 is called standard because EMG and ultrasound systems had the design first (any signal qualifies; M04 inclusion rule). M11 is called ahead because no *neural* study had it. The M11 inclusion rule excludes "acoustic whisper conversion" as not neural, and the full-text check set aside pre-target non-neural hits on that basis: NAM/whisper-to-speech conversion scored against a DTW-aligned audible recording of the same sentence (`w-2246823171`), and EMG/ultrasound DTW work. Scoring a non-audible rendition against the same speaker's time-aligned audible recording of the same text was established practice in NAM/whisper conversion. Toda and Shikano, "NAM-to-speech conversion with Gaussian mixture models", Interspeech 2005, is unverified as to locator. The target only moves this practice to ECoG, which is exactly what M04 calls standard.
   - **Fix.** Apply one rule to both slots. Either:
     - judge M11 against any-signal priors, name the non-audible-input DTW reference as prior practice, and downgrade M11 to standard ("moved to neural covert decoding"); or
     - judge M04 against neural priors only. Then M04 has 0 neural priors, and its usual approach is covert-trained label decoding (see High 3).

     Either way, state the rule in one sentence.

2. **The M11 repetition criterion is met selectively, and it is met with a result, not with the protocol.** Location: M11 paragraph 2 ("The design holds across subjects, with covert above rest in 5 of 7. Verdict: ahead.").
   - **Evidence.** 5 of 7 is the spectrogram result only. Modulation is 4 of 7 (Results > Covert > Modulation). Identification is 1 of 7 (Discussion). The rest control comes from "a separate resting state recording session" (Methods, Baseline control) without the scrolling text, eye movement or reading rhythm of the covert runs. So covert > rest under identical DTW does not isolate a speech-specific match to the overt reference. DTW-aligned rest reaches 0.30 of covert's 0.34 (88%).
   - **Fix.**
     - Report all three repetitions: "5 of 7 (spectrogram), 4 of 7 (modulation), 1 of 7 (identification)".
     - Say that the repeated quantity is a 0.04 r margin over a 0.30 DTW floor against a task-unmatched rest session.
     - Judge the protocol on its own terms: the reference has no mismatched-text null, and the null it has is not task-matched.

     If "ahead" survives Finding 1, it must rest on the design being absent in the priors. Mark the 5-of-7 result as weak evidence that the protocol separates signal from floor, not as the protocol's success.

3. **The M11 population and deciding priors do not fit the setting.** Location: Verdict ("none of the 10 earlier neural studies"); M11 Usual approach; table row M11; Appendix M11.
   - **Evidence.** The 10 pattern-match hits include a silent-speech review (Denby 2010) and seven perception, ERP or entrainment studies (audit_summary M11 note). Only Pasley 2012 and Tankus 2012 decode speech, and neither decodes covert speech. SKILL.md says "M11 gives no field-practice count" (slot fill 0.027). The usual approach given ("heard-stimulus reference, pattern match 1") is a perception design. The relevant neural covert prior is Pei et al. 2011 (J Neural Eng 8:046028, in the wiki, cited four times by the target). It scores covert ECoG decoding against class labels with within-condition training. It is not named, read or counted.
   - **Fix.**
     - Replace "10 earlier neural studies" with an accurate description: "10 prior pattern-match hits, 2 of which decode speech and none covert speech (Appendix)". Better, drop the count from the Usual approach line per the M11 slot rule.
     - State the usual approach as class-label references for covert speech (Pei 2011).
     - Add Pei 2011 as a deciding prior and read it.
     - Change the table cell to "Class-label reference for covert speech (prior)", with no count, or with the denominator.

### Medium

4. **The M04 usual approach is drawn from a different setting.** Location: M04 Usual approach; slots.json M04 note ("Design borrowed from silent-speech recognition"); verdict.json position.
   - **Evidence.**
     - The 3 priors test silently *articulated* speech, where the measured articulatory signal is still produced. Covert reading has no articulation, so the transfer gap is of a different kind.
     - The audit confirms no neural prior.
     - The target cites none of the three priors. It frames the transfer as a test of shared representation (Introduction: "if speech imagery and perception share neural substrates ... a neural decoding model trained from overt speech should be able to predict speech features in the covert condition"). "the paper moves this design to ECoG" and "borrowed" therefore assert a lineage that the paper does not show.
   - **Fix.**
     - Write "3 prior transfer studies, all EMG or ultrasound on mouthed speech; 0 neural (confirmed, unique studies, Appendix)".
     - Add that prior neural covert decoders trained on covert labels (Pei 2011).
     - Replace "moves this design" with "the same design appeared earlier in EMG and ultrasound".
     - Credit the authors' own framing as a representational test.

5. **Counts use all-years denominators and an all-years usual approach.** Location: M04 Usual approach ("3 of the 23"); M08 Usual approach ("1 of the 15"); M12 Usual approach ("Across all years correlation leads (122 of 173 ...)").
   - **Evidence.** 23 and 15 include the target and later studies (M04 and M08 audits). The M12 sentence puts an all-years tally into the Usual approach line, against the caller's rule and the format's "at this time" intent.
   - **Fix.**
     - M04: "3 of 3 prior confirmed studies, all non-neural".
     - M08: "1 prior confirmed study".
     - M12: delete the all-years sentence from the body. It may stay in the Appendix.
     - Resolve the 23 versus 25 confirmed discrepancy in the M04 tally.

6. **"later work reuses it [5]" implies lineage that Kim does not show.** Location: Verdict sentence 4; M11.
   - **Evidence.** Kim 2025, Sec. II-A, attributes overt-audio targets for imagined and whispered speech to its refs [29] (NeuroTalk, AAAI 2023) and [35] (Gaddy and Klein, EMNLP 2020). It does not cite the target.
   - **Fix.** Write "the same reference recurs in later neural work (NeuroTalk 2023; Kim et al. 2025 [5])". Do not claim reuse of the target.

7. **"covert data have no held-out partition" is wrong as worded.** Location: Where the claims outrun the evidence, bullet 3.
   - **Evidence.** Covert neural data never enter training (Covert speech decoding: "the same model ... was applied to data from the covert condition"). The issue is shared text.
   - **Fix.** "Covert scoring uses overt audio of the same stories, and the paper does not say whether it was restricted to overt test blocks, so covert references overlap overt training targets in text."

8. **The verdict.json position is stronger than the review text.** Location: verdict.json `position` ("so the covert effect is mostly alignment") against the review Verdict ("holds only as a small group effect").
   - **Fix.** Use one wording in both places. "Most of the covert r is the DTW floor (0.30 of 0.34)" is supported. "The covert effect is mostly alignment" conflates magnitude with effect.

9. **The body contains process and rule language.** Locations:
   - M11: "the whole-wiki full-text check finds no earlier neural instance (Appendix)";
   - M08: "One prior comparator supports neither behind nor ahead."

   **Evidence.** SKILL.md bans process notes in the body ("within the wiki search" type wording). The second sentence explains the verdict rule rather than giving a position.

   **Fix.** Replace the first with "None of the prior hits builds an overt reference for covert production (pattern match, Appendix)". Replace the second with a substantive position, for example "With one formant prior and no audio output, the gain over Guenther is in representation richness only (inference)".

### Low

10. **The M12 paragraph restates results.** Location: M12, "Covert rank is 0.55 against chance 0.5 and rest 0.48."
    - **Evidence.** These are restated results with no comparison to the field.
    - **Fix.** Either tie them to the comparator ("covert rank 0.55 is 0.34 below Pasley's perceived-speech 0.89 (inference)") or cut the sentence.

11. **The authors' own caveats are not credited for M11.** Location: M11; What the field needs next (M11).
    - **Evidence.** The authors state that "there is no simple ground truth" and that overt speech "is used as the 'ground truth'" (Methods, Covert speech decoding). They also write that "a major difficulty in this approach is the alignment of covert speech reconstructions to a reference speech segment" and propose better alignment or HMMs (Discussion).
    - **Fix.** Add one clause crediting this before the mismatched-text proposal.

12. **The one-fifth figure is reported for the spectrogram only.** Location: M11, last sentence.
    - **Fix.** Add "(spectrogram; one sixth for modulation, (inference))", or say "spectrogram".

13. **The M12 state-of-the-art comparator fits poorly.** Location: M12 State of the art.
    - **Evidence.** Berezutskaya 2023 is a 12-word overt closed-set classifier, a different metric and candidate structure from the target's percentile rank.
    - **Fix.** State the metric mismatch in one clause, or name listener intelligibility (Wairagkar 2025 [8], already cited) as the field's stronger evaluation today.

14. **A possible M04 state-of-the-art addition (optional).**
    - **Evidence.** Kunz et al. 2025 (Cell, doi:10.1016/j.cell.2025.06.015, read in prep but unused) tests decoders trained on attempted speech on inner speech, intracortically. It is later and larger in vocabulary, but its headline 26-54% WER is for inner-speech-trained decoders. Komeiji remains the better matched comparator.
    - **Fix.** None required. You may mention it as a later intracortical transfer test.

15. **Table counts lack denominators.** Location: table rows M04, M08, M11, M12.
    - **Evidence.** "confirmed 3", "pattern match 1" are given with no population.
    - **Fix.** Use "confirmed 3 of 3 prior" and "1 of 1 prior". Per Finding 3, M11 gets no count.

16. **Bibliographic detail.** Location: ref 1.
    - **Evidence.** "Heinze, H." should be "Heinze, H.-J." (author line: Hans-Jochen Heinze).

## Absence and novelty check (M11)

- **Neural absence before 2013-11.** I know of no EEG, MEG, ECoG or intracortical covert or imagined speech reconstruction before 2013-11 that was scored against the participant's DTW-aligned overt recording. Pre-2014 neural covert decoders (Pei 2011 ECoG; DaSalla 2009 EEG vowel imagery; Leuthardt 2011 ECoG control) use class labels.
- **The neural-only claim is plausible but too narrow.** The regex full-text check and a pattern-match population dominated by perception studies are adequate for the neural-only claim, but the population is mis-described (Finding 3). The related M04 table has a recall estimate of 0.35, but this does not undercut the M11 absence, which rests on the separate full-text check.
- **The claim does not hold for non-neural inputs.** Non-audible-input conversion, NAM and whisper (from about 2005), and the EMG/ultrasound parallel-recording designs already built references from the same speaker's audible rendition. This decides the verdict only if the M04 any-signal rule is applied consistently (Finding 1).

## Required fixes, ordered by impact

1. Apply one population rule to M04 and M11, and re-decide M11, most likely as standard (Finding 1).
2. Report all three repetition results, and name the separate, task-unmatched rest session as the confound for the M11 protocol (Finding 2).
3. Correct the "10 earlier neural studies" description, drop the M11 field-practice count, and name and read Pei 2011 as the deciding neural covert prior (Finding 3).
4. Re-anchor the M04 usual approach in the neural covert setting and remove the lineage claim (Finding 4).
5. Replace the all-years denominators and remove the 122 of 173 sentence from the M12 body (Finding 5).
6. Correct "reuses" for Kim 2025 (Finding 6).
7. Fix "no held-out partition" (Finding 7).
8. Align the verdict.json wording with the review (Finding 8).
9. Remove the process and rule language from the body (Finding 9).
10. Apply Low items 10-16.

## Scores

- Procedure: 6/10. Every target number checked matches the source, and the comparators are quoted correctly. The M11 population, its deciding priors and the cross-slot consistency are weak.
- Final text: 6/10. The text holds clear positions with correct numbers. The M11 "ahead" verdict rests on an inconsistent rule and a selective repetition, and the counts use all-years denominators.

Counts by severity: High 3, Medium 6, Low 7.
