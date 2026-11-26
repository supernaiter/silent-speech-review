# Generalizable spelling using a speech neuroprosthesis in an individual with severe limb and vocal paralysis

Sean L. Metzger, Jessie R. Liu, David A. Moses, Maximilian E. Dougherty, Margaret P. Seaton, Kaylo T. Littlejohn, Josh Chartier, Gopala K. Anumanchipalli, Adelyn Tu-Chan, Karunesh Ganguly, Edward F. Chang. Nature Communications 13, 6510 (2022). [doi:10.1038/s41467-022-33611-3](https://doi.org/10.1038/s41467-022-33611-3)

## Verdict

The paper changes the letter-selection action (M04, silently attempted NATO code words), the language assistance (M07, letter beam search over a 1,152-word lexicon) and the stop command (M09, attempted hand squeeze) [[1]](#ref-1). All three are standard: spellers at the time used evoked potentials or motor and cursor selection (191 each of 252 studies, pattern match, Appendix), and silently mouthed NATO-word sequences had been decoded from sEMG [[2]](#ref-2). The main claim holds for one participant and 1,152 words: 29.41 characters per minute at 6.13% median character error rate. That is about a third of attempted handwriting in 2021 [[3]](#ref-3) (inference), with another implant and participant. The overreach is "generalizable": the 9,170-word result is an offline replay, and 6 of 39 live conversational trials failed on out-of-vocabulary words and were excluded (§ Data exclusions).

## Against the field, component by component

### M04 Use-time action: silent code words for letters

**Usual approach:** Of 252 spelling studies dated 2022 or earlier, 191 name an evoked-potential speller and 191 motor or cursor selection; NATO code words appear in none (pattern match, Appendix). Implanted spellers reached 39.2 correct characters per minute by point-and-click [[4]](#ref-4) and 1.08 by auditory neurofeedback in locked-in ALS [[5]](#ref-5).

**State of the art:** In 2021, 90 characters per minute at 5.4% character error rate from attempted handwriting [[3]](#ref-3); in 2026, 110 characters per minute at 1.6% word error rate from finger typing [[6]](#ref-6) [later], about 3.7 times the target (inference).

Across signal types the design had precedents: 4 sEMG subjects silently produced sequences from a 202-word vocabulary including the NATO alphabet, decoded with an "unrestricted NATO grammar" [[2]](#ref-2), and silent spelling text entry used an in-mouth sensor [[7]](#ref-7). Repetition spans 150 copy-typing trials and sessions of one participant (§ Limitations). Verdict: standard.

### M07 Lexicon and language model: closed-lexicon beam search

**Usual approach:** Among the 252 studies a language model is named in 39, a lexicon constraint in 25, word prediction in 23 (pattern match, Appendix). A 2016 review held that language models raise speller speed and accuracy and that word-based models cannot handle out-of-vocabulary words [[8]](#ref-8).

**State of the art:** In 2026, a 5-gram model at 110 characters per minute and 1.6% word error rate [[6]](#ref-6) [later].

The classifier alone gave 35.1% median character error rate (§ Decoding performance), cut by 82% in the full pipeline (inference). The cost is the closed lexicon the review warned about [[8]](#ref-8). Verdict: standard.

### M09 Confirmation: hand squeeze as stop command

**Usual approach:** Among the 252 studies, a hybrid BCI is named in 71, click selection in 57, an attempted or imagined hand command in 53 (pattern match, Appendix). Intracortical typing already selected keys with a hand-motor click [[4]](#ref-4).

**State of the art:** In 2023 the same group separated silent code words from finger flexions in 569 of 570 test trials [[9]](#ref-9) [later].

The squeeze was classified at 98.43% (§ Multimodal control). The authors write "Our approach is the first to combine the two cortical areas to control a BCI" (§ Discussion); the Appendix counts do not test it, and no fixed-time or dwell stop was compared. Verdict: standard.

### M12 Evaluation: rates without information transfer rate

**Usual approach:** Information transfer rate is named in 67 of the 252 studies, characters per minute in 21 (pattern match, Appendix); the paper reports error rates and rates only.

**State of the art:** In 2026, 110 characters per minute [[6]](#ref-6) [later].

Exclusions are reported with both values: 13 of 163 trials removed on the participant's report, 8.52% and 13.75% median character and word error rates with them (§ Data exclusions). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Cued silent attempts; 10-model ensemble | Cued attempted production | – | standard |
| M02 Training-only supervision | Cued labels; four detector classes | Cued labels | – | standard |
| M03 Training and adaptation | Prior-session data, no day-of recalibration | Accumulated-session training | – | standard |
| M04 Use-time action | Silent NATO code words, 2.5 s per letter | Evoked potential or motor/cursor (tie) (pattern match 191) | [[6]](#ref-6) (2026): 110 characters per minute | standard |
| M05 Sensors | 128-channel ECoG, HGA + LFS | Implanted electrodes | – | standard |
| M06 Processing and decoding | Detector + GRU code-word classifier | Detector + closed-set classifier | – | standard |
| M07 Lexicon and LM | Beam search, 1,152 words, trigram + DistilGPT-2 | Language model (pattern match 39) | [[6]](#ref-6) (2026): 5-gram LM, 1.6% WER | standard |
| M08 Output | 26 letters, auto spaces | Characters | – | standard |
| M09 Confirmation | Hand squeeze ends sentence | Hybrid BCI (pattern match 71) | [[9]](#ref-9) (2023): 569 of 570 separated | standard |
| M10 Correction | No user editing | No correction step | – | standard |
| M11 Reference construction | Prompted text; nod or AAC entry | Prompted text | – | standard |
| M12 Evaluation | CER, WER, CPM; 13 of 163 trials excluded | Information transfer rate (pattern match 67) | [[6]](#ref-6) (2026): 110 characters per minute | standard |
| M13 Device and cost | One participant, percutaneous connector | Single-participant implant | – | standard |

## Where the claims outrun the evidence

- The 9,170-word result (8.23% character error rate) reuses the real-time neural outputs offline with a retrained n-gram model (§ Generalizability to larger vocabularies); live use stayed at 1,152 words.
- Conversation: 28 of 39 trials analysed; the reference was the participant's nod or device entry (§ Data exclusions; § Performance evaluation).
- The Discussion's "immediately practical and clinically viable" modality was not usable independently because of the percutaneous connector (§ Deployment limitations).
- The chance condition is described without its error rates (Fig. 2 caption).

## What the field needs next

- M04: code words, direct words and letter names compared within several participants at matched pace.
- M07: a live open-vocabulary fallback tested at 9,170 words or more.
- M09 and M10: the hand channel extended to edit or backspace, with user pacing.
- M12: information transfer rate and numeric chance error rates.

## Questions for the authors

- Were earlier attempts of the copy-typing sentences among the zero-error trials added to training before their second attempt?
- What were the chance character and word error rates?
- How many days did the 34 real-time blocks span, and which seeds initialized the 10 ensemble models?

## Appendix: literature search

Setting for all four topics: text entry by spelling, any signal type in the ledger; full-text pattern (speller, letter-by-letter entry, spelling out words, letters or sentences; reference list removed): 483 unique studies, 252 dated 2022 or earlier with the target excluded (target first public 2022-11). Counts are pattern match, upper bounds (mentions and reviews count), versions once. Recall-sample check: 30 snippets read; none describes a speech-driven speller dated before the target. Known-item recall 1.0 (6 seeds) for each topic.

- M04, speech-or-motor-spelling-action. Inclusion rule: the setting above; design compared is the action that selects each letter; a study counts under every action its text names. Ledger: 5,595 unique studies slot-filled for M04; 483 unique studies pattern match. At the target's time (252): evoked-potential speller 191, motor or cursor selection 191, attempted handwriting 5, speech production of letters 4, NATO code words 0. Full-text NATO-alphabet check over all papers: 28 folders; those dated 2022 or earlier are isolated-word or grammar vocabularies in sEMG and dysarthric speech, none a speller. Read in full: [[2]](#ref-2), [[5]](#ref-5), [[4]](#ref-4), [[3]](#ref-3), [[6]](#ref-6), [[9]](#ref-9). Known-item recall 1.0.
- M07, spelling-language-assistance. Inclusion rule: the setting above; design compared is use-time language assistance. Ledger: 119 unique studies slot-filled for M07; 483 unique studies pattern match. At the target's time (252): language model 39, lexicon constraint 25, word prediction or completion 23, neural rescoring 1, beam search 0. Read in full: [[8]](#ref-8), [[6]](#ref-6). Known-item recall 1.0.
- M09, spelling-selection-and-termination-command. Inclusion rule: the setting above; design compared is how a selection or end of message is issued. Ledger: 82 unique studies slot-filled for M09; 483 unique studies pattern match. At the target's time (252): hybrid BCI 71, click selection 57, attempted or imagined hand command 53, end-of-sentence command 36, dwell or timeout 26. Read in full: [[4]](#ref-4), [[9]](#ref-9). Known-item recall 1.0.
- M12, spelling-rate-and-error-metrics. Inclusion rule: the setting above; design compared is the reported metric. Ledger: 6,960 unique studies slot-filled for M12; 483 unique studies pattern match. At the target's time (252): information transfer rate 67, characters per minute 21, words per minute 21, word error rate 10, character error rate 2. Read in full: [[5]](#ref-5), [[6]](#ref-6). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [generalizable-spelling-using-a-speech-neuroprosthesis-in-an-individual-with-severe-limb-and-vocal-pa.bib](generalizable-spelling-using-a-speech-neuroprosthesis-in-an-individual-with-severe-limb-and-vocal-pa.bib).

1. <a id="ref-1"></a>Metzger, S. L., Liu, J. R., Moses, D. A., Dougherty, M. E., Seaton, M. P., Littlejohn, K. T., et al. “Generalizable spelling using a speech neuroprosthesis in an individual with severe limb and vocal paralysis.” *Nature Communications*, 2022, 13, 6510. doi:[10.1038/s41467-022-33611-3](https://doi.org/10.1038/s41467-022-33611-3). Target. Read as the published version (2022-11-08). [wiki: doi-10.1038-s41467-022-33611-3](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41467-022-33611-3/article.md) [wiki: pmc-9643551-bravospell](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9643551-bravospell/article.md) [wiki: pmc-9643551-bravospelling](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9643551-bravospelling/article.md)
2. <a id="ref-2"></a>Meltzner, G. S., Heaton, J. T., Deng, Y., De Luca, G., Roy, S. H., Kline, J. C. “Development of sEMG sensors and algorithms for silent speech recognition.” *Journal of Neural Engineering*, 2018, 15(4), 046031. doi:[10.1088/1741-2552/aac965](https://doi.org/10.1088/1741-2552/aac965). Prior; deciding prior for M04 (silently mouthed NATO-alphabet word sequences decoded from sEMG with a grammar). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/development-of-semg-sensors-and-algorithms-for-silent-speech-recognition) [wiki: doi-10.1088-1741-2552-aac965](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-aac965/article.md)
3. <a id="ref-3"></a>Willett, F. R., Avansino, D. T., Hochberg, L. R., Henderson, J. M., Shenoy, K. V. “High-performance brain-to-text communication via handwriting.” *Nature*, 2021, 593(7858), 249-254. doi:[10.1038/s41586-021-03506-2](https://doi.org/10.1038/s41586-021-03506-2). Prior; best implanted spelling rate at the target's time (M04). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/high-performance-brain-to-text-communication-via-handwriting) [wiki: doi-10.1038-s41586-021-03506-2](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-021-03506-2/article.md) [wiki: pmc-8163299-b2thand](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-8163299-b2thand/article.md)
4. <a id="ref-4"></a>Pandarinath, C., Nuyujukian, P., Blabe, C. H., Sorice, B. L., Saab, J., Willett, F. R., et al. “High performance communication by people with paralysis using an intracortical brain-computer interface.” *eLife*, 2017, e18554. doi:[10.7554/eLife.18554](https://doi.org/10.7554/eLife.18554). Prior; deciding prior for M09 (hand-motor click selection in an intracortical keyboard) and M04 rate. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/high-performance-communication-by-people-with-paralysis-using-an-intracortical-brain-computer-interf) [wiki: pmc-5319839-ibcityping](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5319839-ibcityping/article.md) [wiki: pmc-5319839-hiprofiBCI](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5319839-hiprofiBCI/article.md)
5. <a id="ref-5"></a>Chaudhary, U., Vlachos, I., Zimmermann, J. B., Espinosa, A., Tonin, A., Jaramillo-Gonzalez, A., et al. “Spelling interface using intracortical signals in a completely locked-in patient enabled via auditory neurofeedback training.” *Nature Communications*, 2022, 13, 1236. doi:[10.1038/s41467-022-28859-8](https://doi.org/10.1038/s41467-022-28859-8). Prior; implanted speller (M04, M12). [wiki: pmc-8941070-clisspelling](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-8941070-clisspelling/article.md)
6. <a id="ref-6"></a>Jude, J. J., Levi-Aharoni, H., Acosta, A. J., Allcroft, S. B., Nicolas, C., Lacayo, B. E., et al. “Restoring rapid natural bimanual typing with a neuroprosthesis after paralysis.” *Nature Neuroscience*, 2026. doi:[10.1038/s41593-026-02218-y](https://doi.org/10.1038/s41593-026-02218-y). Later; state of the art for M04, M07 and M12 (character rate with a 5-gram language model). [later] [wiki: pmc-13633126-bitype](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bitype/article.md) [wiki: doi-10.1038-s41593-026-02218-y](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41593-026-02218-y/article.md) [wiki: pmc-13633126-bityping](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bityping/article.md) [wiki: pmc-13633126-bimanualtype](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bimanualtype/article.md) [wiki: pmc-13633126-bimantype](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bimantype/article.md) [wiki: pmc-13633126-ibcityping](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-ibcityping/article.md)
7. <a id="ref-7"></a>Kimura, N., Gemicioglu, T., Womack, J., Zhao, Y., Li, R., Bedri, A., et al. “SilentSpeller: towards mobile, hands-free, silent speech text entry using electropalatography.” *Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems*, 2022. doi:[10.1145/3491102.3502015](https://doi.org/10.1145/3491102.3502015). Prior (CHI 2022, published 2022-04-29); silent spelling text entry with an in-mouth sensor (M04); not in the ledger. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/silentspeller)
8. <a id="ref-8"></a>Speier, W., Arnold, C., Pouratian, N. “Integrating language models into classifiers for BCI communication: a review.” *Journal of Neural Engineering*, 2016, 13(3), 031002. doi:[10.1088/1741-2560/13/3/031002](https://doi.org/10.1088/1741-2560/13/3/031002). Prior; deciding prior for M07 (language models in BCI spellers). [wiki: pmc-5495144-lmbci](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5495144-lmbci/article.md)
9. <a id="ref-9"></a>Metzger, S. L., Littlejohn, K. T., Silva, A. B., Moses, D. A., Seaton, M. P., Wang, R., et al. “A high-performance neuroprosthesis for speech decoding and avatar control.” *Nature*, 2023, 620, 1037-1046. doi:[10.1038/s41586-023-06443-4](https://doi.org/10.1038/s41586-023-06443-4). Later; same lineage, silent NATO code words with attempted finger flexions (M04, M09). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control) [wiki: doi-10.1038-s41586-023-06443-4](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-023-06443-4/article.md) [wiki: pmc-10826467-avatarnp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10826467-avatarnp/article.md)
