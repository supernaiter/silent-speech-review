# Real-time decoding of question-and-answer speech dialogue using human cortical activity

Moses, D. A.; Leonard, M. K.; Makin, J. G.; Chang, E. F. Nature Communications 10, 3096 (2019). [doi:10.1038/s41467-019-10994-4](https://doi.org/10.1038/s41467-019-10994-4)

## Verdict

The paper [[1]](#ref-1) changes two components. Its use-time context (M07), a soft answer prior from the decoded likelihoods of the perceived question, is ahead: no study among the 36 dialogue-context matches in 1,280 brain-signal decoding studies (pattern match, Appendix) used such a prior earlier, the deciding priors constrain output only with a fixed sentence set or an n-gram model [[2]](#ref-2), [[3]](#ref-3), and the gain is significant in each of three participants. Its decoder (M06), neural speech-event detection plus phone-HMM Viterbi utterance scoring, is standard, extending the group's perception decoders [[4]](#ref-4) to produced speech. The real-time claim outruns the evidence: every accuracy is an offline simulation and the bedside runs give no accuracy figure (§Methods, Real-time decoding). The context gain is a closed-set grammar effect, since answers outside the decoded question's set get zero prior, so open conversation remains untested.

## Against the field, component by component

### M07 Use-time auxiliary information: context from a decoded utterance

**Usual approach:** Among 1,280 brain-signal speech decoding studies (pattern match), full texts most often name a language model (341), then a pronunciation lexicon (116) and a grammar or finite-state network (103) [[3]](#ref-3). The paper takes the prior from a second decoded signal.

**State of the art:** Card et al. (2024) [[5]](#ref-5) [later] reach 90.2% word accuracy with a 125,000-word vocabulary on day 2. The nearest design, Meunier et al. (2024) [[6]](#ref-6) [later], feeds the partner's question as context but transcribes it from audio instead of decoding it from the brain.

All 36 dialogue-context matches were inspected; those before July 2019 use the words in unrelated senses (Appendix). Full-system answer accuracy rises with context in all three participants (p = 1.9×10⁻³, 7.9×10⁻⁵ and 0.029, §Results). Verdict: ahead on the design, not on the size of the gain: a hard predicted-question prior did not help, and the true question improved classification in only one of three participants (§Discussion).

### M06 Processing and decoding: event detection plus phone-HMM utterance scoring

**Usual approach:** In the closed-vocabulary population (360 studies, pattern match), the recorded decoder family is most often "other" (82 of 355, slot-filled), then CNN (35) and HMM (25); 142 full texts name an HMM or Viterbi decoding (pattern match, upper bound).

**State of the art:** Card et al. (2024) [[5]](#ref-5) [later] reach 99.6% accuracy on 50 words on the first day of use; the paper's best is 61% over 24 answers, under a different signal, population and task (inference).

Phone-HMM scoring is inherited from [[4]](#ref-4) and the per-sentence HMMs of [[2]](#ref-2); new are a neural event detector, replacing the 2018 audio onset trigger, and produced speech. Phone accuracy is 25.12% over 37 phones against 2.70% chance (pooled, §Results), so utterance accuracy rests on the redundancy of a small closed set. The [later] same-group system replaced phone HMMs with word classifiers [[7]](#ref-7). Verdict: standard.

### M12 Evaluation: what a real-time claim reports

**Usual approach:** Among 134 intracranial speech studies that mention real-time, online or closed-loop operation (pattern match), full texts give an online accuracy figure in 18, a latency figure in 18 and an offline simulation or replay in 12 (upper bounds).

**State of the art:** Card et al. (2024) [[5]](#ref-5) [later] report 99.6% accuracy on 50 words from the first day of system use, and Moses et al. (2021) [[7]](#ref-7) [later] a median word error rate of 25.6% at 15.2 words per minute; the group's 2018 system already reported real-time accuracy of 90% or higher for each of two subjects [[2]](#ref-2). Verdict: standard for the field, below the group's 2018 practice.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | 10 repetitions per item | Overt speech trials (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Aligned phone labels | Paired-audio phone alignment (slot-filled 31) | – | standard |
| M03 Training and adaptation | Per-participant; block-wise tuning | Per-subject training (slot-filled 1,526) | – | standard |
| M04 Use-time action | Heard questions, overt answers | Overt speech (slot-filled 5,595) | – | standard |
| M05 Sensors | Clinical ECoG, high gamma, 3 patients | ECoG (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | Neural event detection + phone-HMM Viterbi | Decoder family 'other' (slot-filled 82) | [[5]](#ref-5) (2024) [later]: 99.6% on 50 words | standard |
| M07 Lexicon and LM | Answer prior from decoded question | Language model (pattern match 341) | [[5]](#ref-5) (2024) [later]: 90.2% with a 125,000-word vocabulary, day 2 | ahead |
| M08 Output | 1 of 9 questions, 1 of 24 answers | Closed-set labels (slot-filled 3,268) | – | standard |
| M09 Confirmation | None described | Offline results (slot-filled 82) | – | not applicable |
| M10 Correction | None described | Offline results (slot-filled 82) | – | not applicable |
| M11 Reference construction | 9 recordings, one speaker; shown options | Fixed stimulus set (slot-filled 234) | – | standard |
| M12 Evaluation | Offline simulation; best-participant headline | Online accuracy figure (pattern match 18) | [[5]](#ref-5) (2024) [later]: 99.6% on 50 words, day 1 | standard |
| M13 Device and cost | No online accuracy or latency figure | System described (slot-filled 6,075) | – | not reported |

## Where the claims outrun the evidence

- Bedside runs used trial-and-error hyperparameters and report no accuracy; all accuracies are offline simulations (§Methods, Real-time decoding).
- 61% (answers) and 76% (questions) are maxima over three participants, unnamed in the main text; answer ratios to chance span 3.5–7.2 (§Results).
- Question decoding re-identifies the same nine recordings by one speaker heard in training (§Methods, Experimental task design): repeated stimuli, not new speech.
- Answers were read aloud in training and chosen from displayed options at test; the authors concede that visible options could affect processing (§Discussion).
- Finalization before speech offset (94 correct trials) uses transcribed event times, not the detector (§Results).

## What the field needs next

- M07: an ablation separating set restriction from soft likelihood weighting, and questions that vary in wording and speaker.
- M12 and M13: online accuracy and end-to-end latency with hyperparameters fixed before the session.
- M04: the same paradigm with attempted or imagined speech in paralysis (§Discussion).

## Questions for the authors

- How many test blocks did each participant contribute, and who reached 61% and 76%?
- What were the bedside online accuracy and latency?
- How were the z-score statistics initialized between blocks?
- What seeds were used for the bootstrap, sample draws and hyperparameter search?
- How accurate is answer decoding with a flat prior over the valid answers?

## Appendix: literature search

- M07, task-context-prior-from-decoded-utterance. Inclusion rule: brain-signal (ECoG, sEEG, intracortical, EEG, MEG) speech or language decoders whose ledger text names a speech unit and decoding or classification; designs counted from full text: language model, grammar or finite-state network, pronunciation lexicon, context prior from another decoded utterance; training-only priors excluded; versions once. Ledger counts: 119 slot-filled; 1,274 pattern match (unique studies), 1,280 with full-text additions. Usual design: language model, 341 (pattern match); lexicon 116; grammar or finite-state 103; dialogue context 36, none earlier than the target with the design. Read in full: [[3]](#ref-3), [[2]](#ref-2), [[4]](#ref-4); state of the art [[5]](#ref-5). Known-item recall 1.0 (3 seeds).
- M06, closed-vocabulary-word-classification (published table reused). Inclusion rule: decoding of words or utterances from non-acoustic signals by classifying each detected segment into a closed set of at most a few hundred items, with or without a language-model or context prior; open-vocabulary decoders without a closed-set test and acoustic-only ASR excluded. Ledger counts: 7,345 slot-filled; 360 pattern match (unique studies). Usual design: model family "other", 82 of 355 (slot-filled); HMM 25 (slot-filled); HMM or Viterbi named in 142 full texts (pattern match). Read in full: [[2]](#ref-2), [[4]](#ref-4), [[3]](#ref-3); state of the art [[5]](#ref-5). Known-item recall 0.5 (2 seeds).
- M12, real-time-intracranial-speech-online-evaluation. Inclusion rule: intracranial speech decoding studies whose ledger text mentions real-time, online or closed-loop operation; designs counted from full text: online accuracy figure, offline simulation or replay, latency figure; listening-only and review papers enter through the pattern; versions once. Ledger counts: 6,960 slot-filled; 134 pattern match (unique studies). Usual design: online accuracy figure, 18 (pattern match); latency figure 18; offline simulation 12. Read in full: [[2]](#ref-2), [[3]](#ref-3); state of the art [[5]](#ref-5). Known-item recall 1.0 (3 seeds).

## References

Numbered by first citation. BibTeX in the same order and keys: [real-time-decoding-of-question-and-answer-speech-dialogue-using-human-cortical-activity.bib](real-time-decoding-of-question-and-answer-speech-dialogue-using-human-cortical-activity.bib).

1. <a id="ref-1"></a>Moses, D. A., Leonard, M. K., Makin, J. G., Chang, E. F. “Real-time decoding of question-and-answer speech dialogue using human cortical activity.” *Nature Communications*, 2019, 10, 3096. doi:[10.1038/s41467-019-10994-4](https://doi.org/10.1038/s41467-019-10994-4). Target. Read as the published open-access article. [wiki: doi-10.1038-s41467-019-10994-4](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41467-019-10994-4/article.md) [wiki: pmc-6667454-qa](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6667454-qa/article.md) [wiki: pmc-6667454-qadecode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6667454-qadecode/article.md) [wiki: pmc-6667454-qadialogue](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6667454-qadialogue/article.md)
2. <a id="ref-2"></a>Moses, D. A., Leonard, M. K., Chang, E. F. “Real-time classification of auditory sentences using evoked cortical activity in humans.” *Journal of Neural Engineering*, 2018, 15(3), 036005. doi:[10.1088/1741-2552/aaab6f](https://doi.org/10.1088/1741-2552/aaab6f). Prior; deciding prior for M06, M07 and M12. [wiki: doi-10.1088-1741-2552-aaab6f](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-aaab6f/article.md)
3. <a id="ref-3"></a>Herff, C., Heger, D., de Pesters, A., Telaar, D., Brunner, P., Schalk, G., et al. “Brain-to-text: decoding spoken phrases from phone representations in the brain.” *Frontiers in Neuroscience*, 2015, 9, 217. doi:[10.3389/fnins.2015.00217](https://doi.org/10.3389/fnins.2015.00217). Prior; deciding prior for M06 and M07. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/brain-to-text-decoding-spoken-phrases-from-phone-representations-in-the-brain) [wiki: pmc-4464168-brain2text](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-4464168-brain2text/article.md)
4. <a id="ref-4"></a>Moses, D. A., Mesgarani, N., Leonard, M. K., Chang, E. F. “Neural speech recognition: continuous phoneme decoding using spatiotemporal representations of human cortical activity.” *Journal of Neural Engineering*, 2016, 13(5), 056004. doi:[10.1088/1741-2560/13/5/056004](https://doi.org/10.1088/1741-2560/13/5/056004). Prior; deciding prior for M06. [wiki: pmc-5031534-nsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5031534-nsr/article.md)
5. <a id="ref-5"></a>Card, N. S., Wairagkar, M., Iacobacci, C., Hou, X., Singer-Clark, T. “An accurate and rapidly calibrating speech neuroprosthesis.” *New England Journal of Medicine*, 2024, 391(7), 609-618. doi:[10.1056/NEJMoa2314132](https://doi.org/10.1056/NEJMoa2314132). Later; state of the art for M06, M07 and M12. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-accurate-and-rapidly-calibrating-speech-neuroprosthesis) [wiki: doi-10.1056-nejmoa2314132](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-nejmoa2314132/article.md) [wiki: doi-10.1056-NEJMoa2314132](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-NEJMoa2314132/article.md) [wiki: pmc-11328962-rapidcal](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11328962-rapidcal/article.md)
6. <a id="ref-6"></a>Meunier, A., Žák, M. R., Munz, L., Garkot, S., Eder, M., Xu, J., et al. “A Conversational Brain-Artificial Intelligence Interface.” *arXiv preprint*, 2024. arXiv:[2402.15011](https://arxiv.org/abs/2402.15011). Later; conversation-partner question as use-time context. [later] [wiki: arxiv-2402.15011](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2402.15011/article.md)
7. <a id="ref-7"></a>Moses, D. A., Metzger, S. L., Liu, J. R., Anumanchipalli, G. K., Makin, J. G., Sun, P. F., et al. “Neuroprosthesis for decoding speech in a paralyzed person with anarthria.” *New England Journal of Medicine*, 2021, 385(3), 217-227. doi:[10.1056/NEJMoa2027540](https://doi.org/10.1056/NEJMoa2027540). Later; same group, online decoding of attempted speech. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/neuroprosthesis-for-decoding-speech-in-a-paralyzed-person-with-anarthria) [wiki: doi-10.1056-nejmoa2027540](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-nejmoa2027540/article.md) [wiki: pmc-8972947-nejmspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-8972947-nejmspeech/article.md)
