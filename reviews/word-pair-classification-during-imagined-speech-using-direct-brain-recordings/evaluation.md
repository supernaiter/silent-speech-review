# Evaluation: Word pair classification during imagined speech using direct brain recordings

Evaluator: a language model separate from the writer
Date: 2026-11-26. Inputs: the review (`.md`, `compact.md`), `claims.md`, `slots.json`, `verdict.json`, the three topic audits, `notes.json`, and these source texts in the wiki: the target (`doi-10.1038-srep25803/source/text.txt`), Suppes 1997 (`pmc-25146-brainwave`), Pei 2011 (`pmc-3772685-vowelcons`), Leuthardt 2011 (`doi-10.1088-1741-2560-8-3-036004`) and Suppes 1999 (`pmc-23179-invariance`). For published practice I read the sibling evaluation and triage (`decoding-spectrotemporal-features-of-overt-and-covert-speech-from-the-human-cortex`) and the published Pei 2011 review. Outside knowledge that I could not locate is marked "unverified".

## Claim table

| # | Claim (location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Imagined word pairs beat chance in 4 of 5 subjects (Verdict; M08) | Target Results > Classification, l.182; Methods > Statistics, l.386 | correct | Each subject is tested with a one-sample t-test over the 15 pair accuracies against 50%, with FDR correction. The 15 pairs reuse the same trials (each word is in 5 pairs), so the pairs are not independent. The fifth subject has a mean of 49.8% (p > 0.5). |
| 2 | "8 of 15 pairs after FDR correction" (M08 para. 2) | Target l.172 | insufficient evidence for the scope | The sentence follows "88.3% for one classification pair … (subject 4; Fig. 4a)", and Fig. 4a shows S4 only. The paper does not restate the subject scope (notes t27). The likeliest reading is S4 alone, not the group. The review pairs it with "4 of 5 subjects" as if both were group results. |
| 3 | Group mean 57.7% vs 50% chance (M06 SOTA line; outrun bullet 3) | Target l.191 | correct | One-sample t-test, p < 0.05, FDR. The n is the five subject means. |
| 4 | The abstract's 88% is one pair in one subject (outrun bullet 3) | Target l.172; notes t26/t26b | correct | 88.3%, S4. |
| 5 | STG-only 58.0% against 57.7% for all electrodes (outrun bullet 2) | Target l.182 block | correct | STG-only is significant in 4 of 5 subjects; S3 is not (p > 0.5). The review leaves out the 4 of 5 and S3. |
| 6 | The imagery epoch follows the auditory stimulus, with no same-delay control (Verdict; outrun bullet 2) | Target Methods > Experimental paradigm, l.272; notes q7–q9 | correct, incomplete | The cross appears 800 ms after the end of the word (mean word length 800 ms). The epoch is fixed at 1.5 s from the cue. Then a 500 ms blank, then the overt-repetition cue. The review does not give this timing, and it misses the second confound: the epoch ends 500 ms before an overt repetition of the same word. |
| 7 | "first demonstration of single-trial neural decoding of words during imagined speech" (Verdict) | Target Discussion, l.243 | wrong quotation | The source ends "…during imagined speech production". Subjects were told to "imagine hearing", "rather than kinesthetic (imagine saying words)" (l.272). The dropped word carries a scope mismatch that the review misses. |
| 8 | The claim holds only for intracranial recordings; Suppes 1997 recognised single internal-speech trials from EEG/MEG (Verdict) | Suppes 1997, Single-Trial Predictions | correct | 7 words; 46, 39 and 43% in three 105-trial blocks; S1, internal speech. |
| 9 | Suppes: "with prototypes from the same data" (outrun bullet 1) | Suppes 1997, l.370 | insufficient quote | The source says "by using the original prototypes", with the same subject and condition. It does not say the test trials overlap the prototype trials. It does say the p-value is for an "extreme order statistic", so the best sensor or filter was selected. |
| 10 | Leuthardt 2011 decodes imagined phoneme vs rest, not words (M08 usual approach) | Leuthardt §2.4 | correct | "imagined phoneme vs. rest (patients 3 & 4)". This is detection, not discrimination among words. |
| 11 | Pei 2011 decodes vowel or consonant classes inside imagined words, not words (M08 usual approach) | Pei §2.2, §2.5 | correct | 36 CVC words. Each vowel class pools 9 words, and each consonant-pair class pools 4 words. Word identity is never the label. The cue is visual, and only ECoG after 500 ms is used. |
| 12 | 3 of 4 priors are sub-word, 1 of 4 continuous, 0 of 4 whole-word (M08; table) | M08 audit `prior_tally` | correct | The denominator of 4 is stated. Guenther 2009 and Brumberg 2011 are excluded as attempted speech; they decode vowels or phonemes anyway, so the count would not change. |
| 13 | None of 44 full-text hits up to 2016 classifies imagined words besides the target (M08) | M08 audit `fulltext_recall_check` | correct as stated, scope-limited | The pattern requires intracranial terms, so scalp EEG/MEG word classifiers cannot appear in it. `fulltext_pattern` is null and `recall_sample` is empty, so the recall-sample step required for `ahead` (SKILL step 3.4) was not run in its standard form. |
| 14 | DTW gain: "p < 0.05; two-sample t-test", size in a supplementary figure, unit unstated (M06) | Target l.196; notes q1 | correct | The Verdict says "no stated unit or size", but the M06 section says the size is "in a supplementary figure" (Supp. Fig. S3, not read). The two statements conflict. |
| 15 | 0 of 4 priors align inside the decoder; 72 full-text DTW hits, 8 neural (M06; Appendix) | M06 audit `prior_tally`, `fulltext_recall_check` | correct | The audit also records DTW classifiers in surface-EMG silent speech (2010) and DTW-kernel SVMs in acoustic speech recognition (2005) before the target. |
| 16 | M12: at the target's time, 2 of 4 priors hold out covert trials within participant; none holds out a session or subject | M12 audit `prior_tally_<slug>` | correct count, imprecise wording | 2 of 4 is right. Leuthardt's online test on runs after a separate screening, with features fixed beforehand, is the strictest prior partition. "None holds out a session" needs that qualifier. The published M12 table lists the target as its own prior (`population_unique` 5, cutoff 2020). The review correctly uses the per-target tally instead. |
| 17 | Kunz 2025: 24%, 14% and 33% WER, 50 words, three intracortical participants, online (M08 SOTA) | notes xu1–xu4 | correct, condition incomplete | Evaluation ran in the same sessions as training. T15's decoder was retrained online during evaluation (xu3). The 125,000-word result (26–54%, two participants) is not given. |
| 18 | Kunz 2025: online test on sentences absent from training blocks (M12 SOTA) | notes xu2, xu3 | correct, condition incomplete | The same-session evaluation and T15's online retraining are omitted. |
| 19 | Zhao 2026: median 80.4%, 6- or 8-class imagined syllables, 9 participants, tenfold CV (M06 SOTA) | notes xm1–xm7 | correct numbers; weak fit | The value is overall imagined-decoding accuracy. It says nothing about how timing variability is handled, which is the M06 topic. Bibliographic data unverified. |
| 20 | The authors call the effect small and likely not clinically significant (M08) | Target Discussion, l.252 | correct | |
| 21 | The authors concede that cue timing limits accuracy and that DTW degrades with noise (M06) | Target l.197, l.245 | correct | |
| 22 | No listen-then-rest epoch or rest-label classification is reported (outrun bullet 2) | notes q8, q9 | correct | |
| 23 | Stimuli vary in syllable count, "yet accuracy is not related to length or duration" (outrun bullet 4) | notes q4 | wording wrong | The paper reports no such analysis. The sentence reads as if the paper had tested it and found no relation. |
| 24 | Whole-ledger totals (7,345 / 3,268 / 6,960) are not in the table; table counts are design counts with denominators | Rendered table; slots.json | correct | The table shows "of 4 priors (confirmed 3/3/2)". The totals appear only in the Appendix, labelled "Ledger counts". |
| 25 | Body restatement or process disclaimers | Whole body | none blocking | "The paper classifies six whole words…", "The paper puts per-electrode DTW…" and "The paper uses leave-one-out…" each state the departure that the Usual approach line requires; that is allowed. I found no banned process disclaimer in the body. |

## Required fixes, ordered by impact

1. **High. The M08 "ahead" uses a setting boundary that published practice and the review's own Verdict do not support.**
   Location: Verdict sentences 2 and 6; M08 section; table row M08; slots.json M08; verdict.json `short` ("ahead within ECoG").
   - **Evidence.** The design of interest is the decoded unit, and a whole word as the decoded unit of imagined speech does not depend on the sensor. The review itself says the authors' claim fails outside intracranial recordings, because of Suppes 1997 (single internal-speech trials, 7 words, 39–46% against 14.3% chance).
   - **Published practice.** The sibling review of Martin 2014 had an intracranial-only "ahead" (M11) and downgraded it to standard, because an any-signal precedent existed (`…human-cortex.triage.md` row 1: "Under the any-signal rule … M11 is standard"). The published Pei 2011 review kept an intracranial-specific "ahead", but its search population was "any signal" (Appendix M04 inclusion rule), and it named EEG priors (Deng 2010) before restricting the design.
   - **This review.** It does neither. The population excludes scalp EEG/MEG at the search stage, so the wiki's own scalp word-recognition priors were never enumerated. Suppes 1999 (`pmc-23179-invariance`) recognises EEG words, including a condition where subjects "silently repeat each visual word". It is in the wiki and is not named.
   - **SKILL rule.** The `ahead` rule allows a topic-defined population, so the boundary is not illegal. But it is applied more loosely here than in published practice.
   - **Fix.** Downgrade M08 to standard: whole-word output of imagined speech, moved to intracranial recordings. State the intracranial novelty as a finding with an Appendix reference, as the sibling triage did for M11. If "ahead" is kept, the Appendix must report an any-signal count of imagined-word classifiers first public before 2016-05 and name Suppes 1997 and 1999 as deciding priors. The verdict must then read "ahead within intracranial recordings" in the Verdict, the section and the table.

2. **High. The protocol does not show that the repeated effect is imagery, so the repetition condition of "ahead" is met by a result, not by the design.**
   Location: Verdict sentence 5; M08 para. 2 ("The design repeats across subjects…"); outrun bullet 2.
   - **Evidence, timing.** The imagery cross appears 800 ms after the offset of the spoken word, the epoch is fixed at 1.5 s from the cue, and a 500 ms blank then leads to the overt repetition of the same word (target l.272; notes q7, t12, t14). The window therefore sits between hearing word X and saying word X.
   - **Evidence, two confounds.** The just-heard trace is one confound. Word-specific preparation of the overt response is a second, and the review does not name it. No same-delay epoch without imagery and no rest-label classification exists (q8, q9).
   - **Evidence, the task.** The instruction was "imagine hearing", not imagine saying (l.272), and STG-only accuracy (58.0%) matches all electrodes (57.7%). Both fit an auditory trace at least as well as production imagery. The deciding priors avoided the auditory confound: Pei 2011 and Suppes 1997 cued with visual words, and Pei discarded the first 500 ms.
   - **Rule.** When a protocol cannot separate the claimed source from a confound, repeating the effect across subjects (4 of 5) shows only that a word-specific signal exists in that window. This is the same objection the sibling evaluation raised (finding 2: "met with a result, not with the protocol").
   - **Fix.** Treat this as a second, independent ground for standard in M08. Add the timing (800 ms gap, 1.5 s epoch, 500 ms to the overt cue) to the Verdict or outrun bullet 2, and add the overt-preparation confound. Rewrite M08 para. 2 as "a word-specific signal in the post-stimulus window repeats in 4 of 5 subjects; the design cannot attribute it to imagery".

3. **Medium. The repetition figures are mixed and incomplete.**
   Location: M08 para. 2; Verdict sentence 2.
   - **Evidence.** All figures in the paper are listed below. "8 of 15 pairs" is very likely S4 alone (it follows the S4 sentence; Fig. 4a is S4), not a group count. Each per-subject test is a one-sample t-test over 15 pair accuracies that share trials, which inflates significance (inference).
     - Imagined, per subject: 4 of 5 subjects significant over all pairs; the remaining subject has a mean of 49.8%, p > 0.5.
     - Imagined, per pair: 8 of 15 pairs significant, by randomization test with FDR, with S4 the likely scope.
     - Imagined, group: mean 57.7%, p < 0.05, n = 5.
     - Imagined, STG electrodes only: 4 of 5 subjects (S3 not significant), group mean 58.0%.
     - Listening: 12 of 15 pairs; group mean 89.4%; STG-only 89.5%.
     - Overt: 15 of 15 pairs; group mean 86.2%; STG-only 82.6%.
     - Listening and overt, per subject: 83.0–96.0%, "significant in all four subjects" (sic).
     - Best imagined pair: 88.3% (S4).
   - **Fix.** Write "significant in 4 of 5 subjects (subject-level t-tests over 15 non-independent pairs, inference); 8 of 15 pairs in the subject with the best temporal coverage". Alternatively, drop the 8 of 15 or mark its scope as unstated.

4. **Medium. The reason for M06 "standard" is wrong, although the verdict is right.**
   Location: Verdict sentence 3; M06 para. 2; slots.json M06 note.
   - **Evidence, the test.** An unpaired test applied to paired data is conservative (it has less power), so "reported only as an unpaired test" is not a weakness of the evidence. The supporting sentence "with and without DTW on the same pairs is a paired comparison (inference)" points the wrong way.
   - **Evidence, the real gaps.** The comparison unit is not stated (subjects or pooled pairs; notes q1). No per-subject effect is reported, so the repetition clause of the `ahead` rule fails. The size sits only in the unread Supp. Fig. S3.
   - **Evidence, internal conflict.** The Verdict says "no stated … size", while the section says the size is "in a supplementary figure".
   - **Second ground.** By the same any-signal logic as finding 1, M06 is standard anyway: the audit records DTW classifiers in surface-EMG silent speech (2010) and DTW-kernel SVMs in speech recognition (2005), and the authors credit the latter (notes t1b).
   - **Consistency.** M08 accepts per-subject repetition, and M06 has none, so the two verdicts are consistent only if the M06 reason is stated as missing repetition.
   - **Fix.** Replace the reason with "standard: the gain is not shown per subject, its unit is unstated and its size is only in Supp. Fig. S3; DTW kernels predate the target in speech recognition and EMG". Remove the paired-test inference, and align the Verdict and the section on whether a size is reported.

5. **Medium. The scope of the authors' claim is misquoted, and the review misses an inconsistency in the target.**
   Location: Verdict sentence 6; outrun bullet 1.
   - **Evidence.** The claim reads "during imagined speech production" (l.243), yet the task instructed auditory imagery: "imagine hearing", "rather than kinesthetic (imagine saying words)" (l.272). The review drops "production" from the quotation, which hides the mismatch.
   - **Fix.** Quote the claim in full. Add an outrun bullet: "The claim names imagined speech production, but subjects were told to imagine hearing the word (Methods, Experimental paradigm); the result is auditory imagery of a just-heard word."

6. **Medium. The search procedure behind "ahead" is non-standard and cannot see scalp priors.**
   Location: Appendix M08; M08 audit.
   - **Evidence.** `fulltext_pattern` is null and `recall_sample` is empty. The custom check requires intracranial terms. SKILL step 3.4 requires a `--fulltext-pattern` run and reading the recall snippets whenever `ahead` or an absence is claimed. Scalp precedents beyond Suppes 1997 exist:
     - Suppes 1999 is in the wiki.
     - Wester and Schultz 2006 (EEG "unspoken speech" word recognition) is outside the wiki; locator unverified.
     - Porbadnigk et al. 2009 (BIOSIGNALS) is outside the wiki; locator unverified. They showed that block-ordered designs let temporal artefacts drive "unspoken word" EEG recognition, a direct precedent for the protocol concern in finding 2.
   - **Fix.** Run an any-signal full-text pattern for imagined, unspoken or internal speech with word classification or recognition, first public before 2016-05. Read the snippets and report the count in the Appendix with its tier.

7. **Medium. The M06 state of the art does not address the component.**
   Location: M06 State of the art; table row M06.
   - **Evidence.** Zhao 2026 is a headline accuracy (median 80.4%, 6- or 8-class syllables). It says nothing about trial-timing variability, and the review itself calls it "not on a common scale".
   - **Fix.** Name what the best current imagined-speech decoders do about timing. For example, Kunz 2025 decodes inner speech online with a sequence decoder that needs no per-trial alignment (verify the decoder description in its STAR Methods before citing). Alternatively, label Zhao as the accuracy benchmark only and state the timing method it uses.

8. **Low. The M08 and M12 state-of-the-art conditions leave out qualifiers, and a closer word-level comparator exists.**
   Location: M08 and M12 State of the art lines; table rows.
   - **Evidence.** Kunz's evaluation shares sessions with training, and T15 was retrained online during evaluation (xu2, xu3). The 125,000-word result (26–54% WER, two participants) is not given.
   - **Closer comparator.** Wandelt et al. (2024, Nature Human Behaviour) classify 8 internally spoken words online from single neurons in supramarginal gyrus, at about 79% and 23% in two participants. This is a multiclass word classification closer to M08. Values and locator are unverified.
   - **Fix.** Add "same sessions; T15 retrained online". Consider Wandelt 2024 as the word-level comparator, after reading it.

9. **Low. The Suppes condition is overstated.**
   Location: outrun bullet 1.
   - **Evidence.** The source says "by using the original prototypes" and reports a p-value "for this extreme order statistic". It shows sensor or filter selection, not that the test trials were the prototype trials.
   - **Fix.** Write "with prototypes from the same subject and condition and the best sensor and filter selected".

10. **Low. The review misses inconsistencies within the target.**
    Location: outrun section.
    - **Evidence.** The paper states listening and overt accuracy were "significant in all four subjects" when it has five subjects (l.182; notes t31). It reports a "repeated measure 1-way ANOVA" with F(2,12) for 5 subjects. A repeated-measures ANOVA on 5 subjects would give error df 8, while 12 fits a between-subjects ANOVA on 15 means (inference).
    - **Fix.** Add one bullet marked "(inference)" for the df point.

11. **Low. The M12 wording and its source table need care.**
    Location: M12 Usual approach; Appendix M12.
    - **Evidence.** "None holds out a session" overlooks Leuthardt's online test after separate screening (features fixed beforehand). The appended published table counts the target as its own prior (cutoff 2020, n = 3 including the target). The review's 2 of 4 is correct.
    - **Fix.** Write "none holds out a session or subject; Leuthardt et al. test online after a separate screening [3]". Note in the hand-off (not the text) that the published M12 table's prior population includes the target.

12. **Low. The Appendix count labels are imprecise.**
    Location: Appendix M06, M08 and M12; M06 and M08 body text ("72 full-text DTW hits", "44 full-text hits").
    - **Evidence.** "Ledger counts: slot-filled 7,345 / 3,268 / 6,960 unique studies" follows each inclusion rule and reads as the topic size, but these are whole-wiki slot-fill totals. The topic is 89 pattern-match studies, and the design denominator is 4. The full-text hit counts carry no tier label.
    - **Fix.** Write "whole-wiki slot-filled M06: 7,345 unique studies; topic: 89 unique studies (pattern match); priors: 4 (confirmed)", and label the full-text checks "(pattern match, unique studies)".

13. **Low. One sentence misstates what the paper reports.**
    Location: outrun bullet 4.
    - **Evidence.** "yet accuracy is not related to length or duration" implies a tested null result, but no such analysis exists (q4).
    - **Fix.** Write "yet no analysis relates pair accuracy to syllable count or duration".

## Scores

- Procedure: 6/10. Every target and comparator number checked is in the quoted source. Deciding priors were read, the denominators are stated, and whole-ledger totals stay out of the table. The `ahead` search excluded scalp signals at the source and skipped the standard recall sample, and the M06 reason inverts the logic of the test.
- Final text: 6/10. Positions are clear, and the heard-word confound is identified. M08 "ahead" survives only through a setting boundary and a repetition that the protocol cannot attribute to imagery, and the repetition figures mix subject-level and pair-level scopes.

Counts by severity: high 2, medium 5, low 6.
