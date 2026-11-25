# A Wireless Brain-Machine Interface for Real-Time Speech Synthesis

Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., et al. · PLoS ONE 4(12), e8218 · 2009 · [doi:10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218)

## Verdict

The paper [[1]](#ref-1) changed the decoder into a closed loop (M06, Kalman filter to formants, audio 30–70 ms after neural firing), the output into two formants of a Klatt synthesizer (M08) and the link into transcutaneous telemetry (M13). All three are standard under our rules: the ledger holds no earlier closed loop from a non-acoustic signal (Appendix), but one participant with one electrode gives no repetition. The main claim, that a locked-in user learns to steer synthesized vowels, holds. Its measure is weak: the 45% to 70% hit rate between the opening and closing blocks (Discussion) is helped by an attractor force in the target regions and has no chance level or decoder-off control (Methods). Nothing measures speech, so "near-conversational synthetic speech output" (Abstract) is a projection; this is the protocol ancestor of the [later] sentence closed loop at 43.75% WER [[2]](#ref-2), not a performance reference.

## Against the field, component by component

### M06 Decoding: closed-loop formant decoding

**Usual approach:** Of 87 studies on real-time or causal speech synthesis (pattern match, unique studies; Appendix), 50 name closed-loop audio feedback, 24 offline whole-utterance decoding and 9 causal frame-level models (upper bounds). The 5 dated before 2009 fall outside the rule (Appendix): this paper sets the design.

**State of the art:** Brain2voice 2.0 (2026, [later]): 5.24% listener WER, offline with simulated real-time inference [[3]](#ref-3); in closed loop, causal sentence synthesis within 10 ms at 43.75% open-transcription WER (2025) [[2]](#ref-2). With no intelligibility score there is no common metric; the paper's 50 ms average delay is twice the 25 ms latency given for the 2025 system [[3]](#ref-3) (inference).

The decoder is refit each session on one minute of mimicking four heard vowels, the stimulus standing in for intended formants (Results); the number of units kept per session is unstated. The [later] sEEG closed loop on imagined speech still gave audio its authors call not yet intelligible [[4]](#ref-4). The attractor force runs in every session (Methods), so the decoder's share of hits is not isolated. Verdict: standard.

### M08 Output: two formants of a Klatt synthesizer

**Usual approach:** Of 180 intracranial speech-synthesis studies (pattern match, unique studies; Appendix), 51 name a pretrained neural vocoder, 15 a parametric vocoder and 11 Griffin-Lim; 9 match a formant-synthesizer pattern, and the only ones driven by brain signals are this paper and work by the same group (Appendix). The paper steers 2 of 63 synthesizer parameters, F1 and F2 (Methods).

**State of the art:** 5.24% listener WER from continuous and tokenized acoustic features (2026, [later], offline) [[3]](#ref-3); the paper's three vowels have no listener score.

Two dimensions made the task learnable from a single 3-wire electrode (Discussion) and set the ceiling: with 61 parameters fixed (inference), no consonant, voicing or pitch change is possible, as the authors concede (Discussion). The field moved to vocoder features instead of a larger formant space (51 of 180, Appendix). Verdict: standard.

### M13 Device: transcutaneous telemetry

**Usual approach:** Of 382 implanted-sensor speech or communication studies (pattern match, unique studies; Appendix), 35 name a percutaneous connector, 52 wireless telemetry and 51 a fully implanted system, the last two upper bounds. The paper's FM link with inductive power needs no wires or connectors through the skin (Discussion).

**State of the art:** Home use of a 192-electrode intracortical BCI with wireless transmitters (2021, [later]), mounted on the percutaneous pedestal [[5]](#ref-5); the [later] speech system used at home for 19 months still records through percutaneous wired connections and names wireless or fully implantable systems as future work [[6]](#ref-6).

The paper kept the skin closed at a cost of 2 channels against 192 [[5]](#ref-5) (inference). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Cued attempted vowels | Training action noted (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Heard stimulus formants | Supervision noted (slot-filled 31) | – | standard |
| M03 Training and adaptation | Per-session Kalman fit | Training recorded (slot-filled 1,526) | – | standard |
| M04 Use-time action | Attempted vowel | Use-time action noted (slot-filled 5,595) | – | standard |
| M05 Sensors | 2-channel Neurotrophic Electrode | Sensors recorded (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | Closed-loop Kalman decoding | Closed-loop audio feedback (pattern match 50) | [[3]](#ref-3) (2026): WER 5.24% | standard |
| M07 Lexicon and LM | None | Lexicon or LM recorded (slot-filled 119) | – | standard |
| M08 Output | F1/F2 of a Klatt synthesizer | Pretrained neural vocoder (pattern match 51) | [[3]](#ref-3) (2026): WER 5.24% | standard |
| M09 Confirmation | Audio; cursor late | Confirmation recorded (slot-filled 82) | – | not applicable |
| M10 Correction | None | Correction recorded (slot-filled 82) | – | not applicable |
| M11 Reference construction | Vowel targets | Reference recorded (slot-filled 234) | – | standard |
| M12 Evaluation | Hit rate, endpoint error | Evaluation recorded (slot-filled 6,960) | – | standard |
| M13 Device and cost | FM telemetry, skin closed | Percutaneous connector (pattern match 35) | [[5]](#ref-5) (2021): 192 electrodes | standard |

## Where the claims outrun the evidence

- No floor for hit rate: three targets at the corners of the F1/F2 space, a 500 ms stay inside regions of about 150 by 300 Hz with an attractor force, and no chance level, shuffled or decoder-off block (Methods; Fig. 7).
- The Abstract's "25% improvement" is 25 percentage points, 56% relative (inference); 89% is the single best block (Discussion); block counts behind Fig. 7 are not given.
- The cursor shown in the last 15 of 25 sessions gets "no difference" without a statistic, confounded with practice; Fig. 7 pools both.
- Fig. 6 shows r = .69 and .68 fitted on the whole dataset; cross-validated values are 0.49 and 0.57 (Results).
- "Decode and synthesize intended words" (Discussion) rests on three vowels played to the participant before each attempt (Methods; Fig. 7), with no listener test.

## What the field needs next

- M12: chance-calibrated hit rates (shuffled or decoder-off blocks) and listener identification of the vowels.
- M06: attractor-on and attractor-off blocks within sessions.
- M08: closed-loop output spaces between F1/F2 and vocoder features, scored by listeners.
- M13: closed-loop speech synthesis through a fully implanted link [[6]](#ref-6).

## Questions for the authors

- How many trials enter each block position in Fig. 7?
- What hit rate does a shuffled decoder reach with the attractor on?
- How many units passed the F-test per session?
- How does the "first telemetric implant" claim relate to the computer control in refs. 32 and 33?

## Appendix: literature search

- M06, causal-closed-loop-speech-synthesis (published table, reused). Inclusion rule: studies that synthesize speech acoustics from a non-acoustic signal (neural, EMG, articulography, ultrasound, video) online, with the audio played back while or right after the user speaks; offline studies only when they simulate causal frame-level inference; offline acausal reconstruction, text decoding read out by TTS and conversion from acoustic input excluded; versions count once. Ledger: 7,345 unique studies slot-filled for M06; 87 unique studies pattern match. Usual design: ProcessingStep role "generate" 24 (slot-filled); linear model 12 (slot-filled); closed-loop audio feedback 50, offline whole-utterance 24, causal frame-level 9 (pattern match, published counts). Chronology of the 87: 5 before 2009 (talking-head, lip-parameter and MRI studies, outside the rule), 3 in 2009 (this paper, the same group's [concurrent] Interspeech paper, one acoustic-to-articulatory inversion study), 1 in 2010, 61 from 2011, 17 date unresolved. Read in full: [[3]](#ref-3) (state of the art), [[2]](#ref-2), [[4]](#ref-4). Known-item recall 1.0 (4 seeds).
- M08, intracranial-synthesis-waveform-generation (published table, reused). Inclusion rule as published: speech acoustics reconstructed from intracranial recordings during produced, attempted or imagined speech; heard speech and text-only decoding excluded. Ledger: 3,268 unique studies slot-filled for M08; 180 unique studies pattern match. Usual design: pretrained neural vocoder 51; unit selection 30, parametric vocoder 15, Griffin-Lim 11 (pattern match, published counts); formant synthesizer 9 (pattern match), those driven by brain signals being this paper and same-group work. Read in full: [[3]](#ref-3). Known-item recall 1.0.
- M13, wireless-implanted-speech-bci (new). Inclusion rule: speech or communication studies with implanted neural sensors (intracortical, ECoG, sEEG, depth), classified by how the signal leaves the body: percutaneous connector or pedestal, wireless telemetry (including a transmitter on a pedestal), or a fully implanted system; reviews and related-work mentions inflate full-text counts (upper bounds); wearable EMG or EEG devices excluded by the ledger modality filter. Ledger: 6,075 unique studies slot-filled for M13; 382 unique studies pattern match. Usual design: system implemented and evaluated 216 of 296 (slot-filled); wireless telemetry 52, fully implanted 51, percutaneous connector 35 (pattern match, upper bounds). Read in full: [[5]](#ref-5) (state of the art), [[6]](#ref-6). Known-item recall 1.0 (3 seeds).

## References

Numbered by first citation. BibTeX in the same order and keys: [a-wireless-brain-machine-interface-for-real-time-speech-synthesis.bib](a-wireless-brain-machine-interface-for-real-time-speech-synthesis.bib).

1. <a id="ref-1"></a>Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., Panko, M., et al. “A Wireless Brain-Machine Interface for Real-Time Speech Synthesis.” *PLoS ONE*, 2009, 4(12), e8218. doi:[10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218). [wiki: pmc-2784218-wireless](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wireless/article.md) [wiki: pmc-2784218-wirelesssynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wirelesssynth/article.md) [wiki: doi-10.1371-journal.pone.0008218](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1371-journal.pone.0008218/article.md)
2. <a id="ref-2"></a>Wairagkar, M., Card, N. S., Singer-Clark, T., Hou, X., Iacobacci, C., Miller, L. M., et al. “An instantaneous voice-synthesis neuroprosthesis.” *Nature*, 2025, 644(8075), 145–152. doi:[10.1038/s41586-025-09127-3](https://doi.org/10.1038/s41586-025-09127-3). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-instantaneous-voice-synthesis-neuroprosthesis) [wiki: doi-10.1038-s41586-025-09127-3](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-025-09127-3/article.md) [wiki: doi-10.1101-2024.08.14.607690](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2024.08.14.607690/article.md) [wiki: pmc-12369848-voicesynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12369848-voicesynth/article.md) [wiki: pmc-12369848-voice-synth-np](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12369848-voice-synth-np/article.md) [wiki: pmc-11370360-instvoice](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11370360-instvoice/article.md)
3. <a id="ref-3"></a>Wairagkar, M., Srinivasan, A., Card, N. S., Singer-Clark, T., Hou, X., Iacobacci, C., et al. “Brain2voice 2.0: High-performance voice synthesis brain-computer interface.” *bioRxiv*, 2026. doi:[10.64898/2026.06.30.735633](https://doi.org/10.64898/2026.06.30.735633). [later] [wiki: doi-10.64898-2026.06.30.735633](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.64898-2026.06.30.735633/article.md)
4. <a id="ref-4"></a>Angrick, M., Ottenhoff, M. C., Diener, L., Ivucic, D., Ivucic, G., Goulis, S., et al. “Real-time synthesis of imagined speech processes from minimally invasive recordings of neural activity.” *Communications Biology*, 2021, 4, 1055. doi:[10.1038/s42003-021-02578-0](https://doi.org/10.1038/s42003-021-02578-0). [later] [wiki: doi-10.1038-s42003-021-02578-0](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s42003-021-02578-0/article.md) [wiki: pmc-8460739-realtimesynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-8460739-realtimesynth/article.md)
5. <a id="ref-5"></a>Simeral, J. D., Hosman, T., Saab, J., Flesher, S. N., Vilela, M., Franco, B., et al. “Home Use of a Percutaneous Wireless Intracortical Brain-Computer Interface by Individuals With Tetraplegia.” *IEEE Transactions on Biomedical Engineering*, 2021, 68(7), 2313–2325. doi:[10.1109/TBME.2021.3069119](https://doi.org/10.1109/TBME.2021.3069119). [later] [wiki: doi-10.1109-tbme.2021.3069119](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tbme.2021.3069119/article.md)
6. <a id="ref-6"></a>Card, N. S., Singer-Clark, T., Peracha, H., Iacobacci, C., Hou, X., Wairagkar, M., et al. “Long-term independent use of an intracortical brain-computer interface for speech and cursor control.” *Nature Medicine*, 2026, 32(7), 2504–2510. doi:[10.1038/s41591-026-04414-6](https://doi.org/10.1038/s41591-026-04414-6). [later] [wiki: pmc-13375540-ltbci](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13375540-ltbci/article.md) [wiki: pmc-13375540-ibciterm](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13375540-ibciterm/article.md) [wiki: pmc-13375540-ltc-speechbci](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13375540-ltc-speechbci/article.md)
