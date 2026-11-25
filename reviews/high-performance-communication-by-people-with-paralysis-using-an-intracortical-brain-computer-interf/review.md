# High performance communication by people with paralysis using an intracortical brain-computer interface

Chethan Pandarinath, Paul Nuyujukian, Christine H. Blabe, Brittany L. Sorice, Jad Saab, Francis R. Willett, Leigh R. Hochberg, Krishna V. Shenoy, Jaimie M. Henderson. eLife, 2017. [doi:10.7554/eLife.18554](https://doi.org/10.7554/eLife.18554)

## Verdict

The paper [[1]](#ref-1) changes the decoder (M06), a ReFIT Kalman cursor paired with an HMM click, and the evaluation (M12), peak copy-typing ccpm plus achieved grid bitrate without word completion. Both are standard: the paper adapts the ReFIT Kalman filter and the HMM click from earlier work (§Neural control algorithms), the same pairing ran in monkey typing [[2]](#ref-2), and human typing used a Kalman cursor with an LDA click [[3]](#ref-3). The record claim holds as performance, not as evidence for a component: each 1.4–4.2× gain compares across studies, tasks and partly the same participants (Table 1). No experiment isolates the HMM click from dwell selection. Today, [later] decoders of attempted handwriting and typing reach 90 and 110 characters per minute [[4]](#ref-4), [[5]](#ref-5).

## Against the field, component by component

### M06 Processing and decoding: cursor-and-click decoder

**Usual approach:** among 33 intracortical text-entry studies (pattern match, Appendix), recurrent-network decoders are named most (18), then Kalman cursors (14), click decoders (13) and dwell (10). The paper keeps the Kalman cursor and adds an HMM click for T6 and T5; T7 used dwell only (Table 3).

**State of the art:** attempted typing, 110 characters per minute at 1.6% WER (T18 peak, 5-gram LM) [[5]](#ref-5) (2026); handwriting, 90 characters per minute at 5.4% CER in T5 [[4]](#ref-4) (2021), 2.3× T5's 39.2 ccpm here (inference), with different error counting.

The pairing is inherited: the monkey study ran the HMM click "in parallel with the ReFIT-KF" [[2]](#ref-2), and BrainGate typing used a Kalman cursor with an LDA click [[3]](#ref-3) (both date unresolved). The only dwell-versus-click contrast is in monkeys, 10.0 to 12.0 and 7.2 to 7.8 wpm on different passages [[2]](#ref-2), gains of 20% and 8% (inference). In the target, T6 and T5 selected by click or dwell within the same block, with no split reported (Video 1 caption, Table 3). Verdict: standard.

### M12 Evaluation: rate metric and comparison protocol

**Usual approach:** in the same 33 studies (pattern match, Appendix), words per minute is named most (14), then word error rate (9), ccpm (7) and achieved bitrate (3). The paper reports ccpm and grid bitrate after same-session recalibration, measuring peak performance (Discussion).

**State of the art:** rate paired with word error rate, 110 characters per minute at 1.6% WER [[5]](#ref-5) (2026). The target's ccpm counts uncorrected errors as correct (§Correct characters per minute).

The record comparisons are uncontrolled. Typing gains of 3.4×, 4.2× and 1.4× are against one prior participant at 9.4 ccpm (Table 1). Bitrate gains of 2.4× and 2.2× for T6 and T7 are against their own free-typing results (0.93 and 0.64 bps), so task and decoder change together; the authors put the task effect at about 30% (Results). Verdict: standard.

### M04 Use-time action: attempted hand movement to a cursor

**Usual approach:** among 154 neural text-entry studies (pattern match, Appendix), imagined or inner speech is named most (68), cursor or keyboard typing in 37; the paper maps attempted hand movement to cursor velocity.

**State of the art:** decoding attempted finger typing directly, 110 characters per minute [[5]](#ref-5) (2026), 2.8× the target's best (inference).

T6 moved her hand freely during evaluation (Results); suppressed sessions differed by 0–20% (p>0.2), without EMG (Figure 4). Verdict: standard.

### M07 Lexicon and LM: none, by design

**Usual approach:** a language model is named in 15 of the 33 studies, word prediction or completion in 6 (pattern match, Appendix); the paper excludes both (Table 1 caption).

**State of the art:** a 5-gram LM at 110 characters per minute [[5]](#ref-5) (2026).

The claim that completion "should only increase" rates (Results) was measured [later]: +68% (T6), +13% (T9), +35% (T5) over predicted single-character rates [[6]](#ref-6). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Attempted hand movement | Attempted movement calibration (BrainGate lineage) | – | standard |
| M02 Training-only supervision | Cued targets and click periods | Cued calibration targets | – | standard |
| M03 Training and adaptation | Same-session recalibration | Session calibration (ReFIT lineage) | – | standard |
| M04 Use-time action | Attempted hand movement to cursor | Imagined or inner speech (pattern match 68) | [[5]](#ref-5) (2026): 110 chars/min | standard |
| M05 Sensors | 96-ch arrays; spikes, HF-LFP (T6) | Intracortical arrays (BrainGate lineage) | – | standard |
| M06 Processing and decoding | ReFIT-KF + HMM click; T7 dwell | Recurrent-network decoder (pattern match 18) | [[5]](#ref-5) (2026): 110 chars/min | standard |
| M07 Lexicon and LM | None (excluded) | Language model (pattern match 15) | [[5]](#ref-5) (2026): 5-gram LM | standard |
| M08 Output | Keyboard characters | On-screen keyboard text | – | standard |
| M09 Confirmation | HMM click or dwell | Dwell or click selection | – | standard |
| M10 Correction | Delete key | Delete-based correction | – | standard |
| M11 Reference construction | Prompted sentences; cued grids | Prompted copy typing and cued grid | – | standard |
| M12 Evaluation | Peak ccpm and bitrate | Words per minute (pattern match 14) | [[5]](#ref-5) (2026): 110 chars/min | standard |
| M13 Device and cost | BrainGate2, home sessions | Investigational implanted system | – | standard |

## Where the claims outrun the evidence

- "Highest rates for all three participants" (§Discussion): T7 used no HMM (Table 3), so the credited decoder did not produce one of the three records.
- T6 and T7 had 1.5 years of prior BCI use and were in the comparator study; no learning experiment was run (Table 2; Author response).
- T5's 4.0× bitrate gain compares a new participant with another study's best participant on another task (§Results; Table 1).
- Spike-only T5 beating hybrid-feature T6 is read as spikes sufficing (§Neural feature extraction); participant and array differ.
- T5 grid testing is 4 days and 29 blocks in Results but 2 days in the Fig. 3b caption.
- No multiple-comparison correction accompanies the p<0.01 tests (§Results; Fig. 4).

## What the field needs next

- M06: dwell-only, HMM-click and LDA-click blocks within participant on one layout.
- M12: ccpm with uncorrected character error rate, and frozen-decoder test days.
- M04: EMG during closed-loop typing when movement remains.
- M07: measured rates with and without completion in the same sessions.

## Questions for the authors

- What fraction of T6 and T5 selections were HMM clicks?
- How many calibration trials did T5 and T7 give, and how were feature-selection folds built?
- How many grid timeouts occurred?
- What uncorrected character error rate remained in copy typing?

## Appendix: literature search

- M04, neural-text-entry-action. Inclusion rule: neural BCI studies (intracortical, ECoG, sEEG, EEG, MEG) whose ledger names the recording modality together with a text output, a text error rate or a text-entry rate; the design compared is the user action that drives text at use time; a study counts under every action its full text names (upper bound); versions counted once. Ledger counts: slot-filled 5,595 unique studies; pattern match 154 unique studies (219 folders). Usual design: imagined or inner speech, 68 (pattern match); attempted speech 56; cursor or keyboard typing 37. Papers read: [[5]](#ref-5). Known-item recall for this review's seed: 0 of 1.
- M06, intracortical-cursor-click-communication-decoder. Inclusion rule: intracortical studies whose ledger names an intracortical recording together with cursor, point-and-click, keyboard, typing, text entry, characters per minute, ccpm or grid task; design = decoder that turns neural activity into selections; full-text pattern counts, reference list removed, target included (upper bound). Ledger counts: slot-filled 7,345 unique studies; pattern match 33 unique studies (46 folders). Usual design: recurrent-network decoder 18 (pattern match); Kalman-family 14; discrete click 13; dwell 10. Index year 2016 or earlier: 3 studies, Kalman-family 3, click 1. Papers read: [[3]](#ref-3), [[2]](#ref-2), [[4]](#ref-4), [[5]](#ref-5). Known-item recall: 1.0 (3 of 3).
- M07, intracortical-communication-language-assistance. Inclusion rule: the M06 population; design = use-time language model, or word prediction or completion; full-text pattern counts (upper bound). Ledger counts: slot-filled 119 unique studies; pattern match 33 unique studies. Usual design: language model 15 (pattern match); word prediction or completion 6. Papers read: [[6]](#ref-6), [[5]](#ref-5).
- M12, intracortical-communication-rate-benchmark. Inclusion rule: the M06 population; design = rate metric reported (achieved bitrate, information transfer rate, ccpm, words per minute, word error rate beside the rate); full-text pattern counts (upper bound). Ledger counts: slot-filled 6,960 unique studies; pattern match 33 unique studies. Usual design: words per minute 14 (pattern match); word error rate 9; ccpm 7; information transfer rate 5; achieved bitrate 3. Papers read: [[2]](#ref-2), [[5]](#ref-5). Known-item recall: 1.0 (3 of 3).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Pandarinath, C., Nuyujukian, P., Blabe, C. H., Sorice, B. L., Saab, J., Willett, F. R., et al. “High performance communication by people with paralysis using an intracortical brain-computer interface.” *eLife*, 2017, 6, e18554. doi:[10.7554/eLife.18554](https://doi.org/10.7554/eLife.18554). Target. Read as the Version of Record (PMC5319839). [wiki: pmc-5319839-ibcityping](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5319839-ibcityping/article.md) [wiki: pmc-5319839-hiprofiBCI](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5319839-hiprofiBCI/article.md)
2. <a id="ref-2"></a>Nuyujukian, P., Kao, J. C., Ryu, S. I., Shenoy, K. V. “A Non-Human Primate Brain-Computer Typing Interface.” *Proceedings of the IEEE*, 2017, 105(1). doi:[10.1109/JPROC.2016.2586967](https://doi.org/10.1109/JPROC.2016.2586967). Date unresolved (cited by the target as 2016). Read: Abstract, Methods (ReFIT-KF, HMM click decoder, typing task). [wiki: pmc-7970827-nhptyping](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-7970827-nhptyping/article.md)
3. <a id="ref-3"></a>Jarosiewicz, B., Sarma, A. A., Saab, J., Franco, B., Cash, S. S., Eskandar, E. N., et al. “Retrospectively supervised click decoder calibration for self-calibrating point-and-click brain-computer interfaces.” *Journal of Physiology - Paris*, 2016. doi:[10.1016/j.jphysparis.2017.03.001](https://doi.org/10.1016/j.jphysparis.2017.03.001). Date unresolved (2017 DOI, 2016 volume). Read: Methods (Kalman filter and LDA click decoder calibration). [wiki: pmc-5591042-clickcal](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5591042-clickcal/article.md)
4. <a id="ref-4"></a>Willett, F. R., Avansino, D. T., Hochberg, L. R., Henderson, J. M., Shenoy, K. V. “High-performance brain-to-text communication via handwriting.” *Nature*, 2021, 593. doi:[10.1038/s41586-021-03506-2](https://doi.org/10.1038/s41586-021-03506-2). Later. Read: Summary and Results (online copy typing, comparison with point-and-click). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/high-performance-brain-to-text-communication-via-handwriting) [wiki: doi-10.1038-s41586-021-03506-2](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-021-03506-2/article.md)
5. <a id="ref-5"></a>Jude, J. J., Levi-Aharoni, H., Acosta, A. J., Allcroft, S. B., Nicolas, C., Lacayo, B. E., et al. “Restoring rapid natural bimanual typing with a neuroprosthesis after paralysis.” *Nature Neuroscience*, 2026, 29. doi:[10.1038/s41593-026-02218-y](https://doi.org/10.1038/s41593-026-02218-y). Later; state of the art. Read: Abstract, Introduction, Results (sentence typing). [later] [wiki: pmc-13633126-bitype](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bitype/article.md) [wiki: doi-10.1038-s41593-026-02218-y](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41593-026-02218-y/article.md) [wiki: pmc-13633126-bimantype](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bimantype/article.md) [wiki: pmc-13633126-bimanualtype](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bimanualtype/article.md) [wiki: pmc-13633126-bityping](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bityping/article.md) [wiki: pmc-13633126-ibcityping](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-ibcityping/article.md)
6. <a id="ref-6"></a>Nuyujukian, P., Albites Sanabria, J., Saab, J., Pandarinath, C., Jarosiewicz, B., Blabe, C. H., et al. “Cortical control of a tablet computer by people with paralysis.” *PLoS ONE*, 2018, 13(11), e0204566. doi:[10.1371/journal.pone.0204566](https://doi.org/10.1371/journal.pone.0204566). Later. Read: Results (typing performance, Table 3). [later] [wiki: pmc-6248919-ibci-tablet](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6248919-ibci-tablet/article.md)
