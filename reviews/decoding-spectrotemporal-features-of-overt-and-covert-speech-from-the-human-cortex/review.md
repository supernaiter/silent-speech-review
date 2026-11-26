# Decoding spectrotemporal features of overt and covert speech from the human cortex

Stéphanie Martin, Peter Brunner, Chris Holdgraf, Hans-Jochen Heinze, Nathan E. Crone, Jochem Rieger, Gerwin Schalk, Robert T. Knight, Brian N. Pasley. Frontiers in Neuroengineering 7:14, 2014. [doi:10.3389/fneng.2014.00014](https://doi.org/10.3389/fneng.2014.00014)

## Verdict

The paper [[1]](#ref-1) changes three components. Applying an overt-trained decoder to covert reading (M04) is standard: EMG and ultrasound systems had already tested vocalized-trained models on silent articulation [[2]](#ref-2), [[3]](#ref-3). Spectrogram and modulation output from production (M08) is standard against one earlier formant decoder [[4]](#ref-4). Scoring covert output against the participant's own DTW-aligned overt recording (M11) is ahead: none of the 10 earlier neural studies in its population builds such a reference (Appendix), and later work reuses it [[5]](#ref-5). The same design carries the main confound: equally warped rest reaches r = 0.30 against covert r = 0.34, and covert identification beat chance in one of seven subjects (Sec. Discussion), so covert decoding holds only as a small group effect.

## Against the field, component by component

### M04 Use-time action: overt-trained decoder on covert speech

**Usual approach:** 3 of the 23 confirmed overt-to-silent transfer studies are prior (confirmed, unique studies, Appendix), all EMG or ultrasound recognizers trained on audible speech and tested on silent articulation [[2]](#ref-2), [[6]](#ref-6), [[3]](#ref-3); the paper moves this design to ECoG.
**State of the art:** Komeiji et al. (2024) [later] [[7]](#ref-7) decode covert ECoG sentences with an overt-trained Transformer at 46.3% token error rate against 46.6% when covert-trained (16 patients, eight sentences).

The priors measure transfer as a loss against silent training [[3]](#ref-3). The target compares covert r = 0.34 only with overt (r = 0.50) and rest (r = 0.30), with no covert-trained arm, so its transfer cost stays unknown; a later sentence-level test finds none [[7]](#ref-7). Verdict: standard.

### M08 Output: spectrotemporal features from production

**Usual approach:** 1 of the 15 confirmed studies decoding continuous acoustics from production activity is prior (confirmed, unique studies, Appendix): two formants driving a real-time synthesizer [[4]](#ref-4); the target outputs 32 spectrogram bins and 60 modulation features but no audio.
**State of the art:** Wairagkar et al. (2025) [later] [[8]](#ref-8) synthesize voice from attempted speech at a median listener word error rate of 43.75% (one participant).

The 32 bins span consonant cues that two formants omit (inference), but no listener heard the output, so it has no place on the intelligibility scale of later synthesis [[8]](#ref-8). One prior comparator supports neither behind nor ahead. Verdict: standard.

### M11 Ground truth: own overt recording as covert reference

**Usual approach:** among 10 prior neural studies (pattern match, unique studies, Appendix), the only reconstruction is scored against the heard stimulus [[9]](#ref-9) and none constructs a reference for covert production; the paper DTW-aligns covert output to the same subject's overt reading of the same text.
**State of the art:** Kim et al. (2025) [later] [[5]](#ref-5) use the overt recording of the same sentence as target audio for imagined EEG, with 15 participants and 30 unseen test sentences each.

Of the deciding priors, Pasley et al. use heard words [[9]](#ref-9) and Guenther et al. cue formants for attempted speech [[4]](#ref-4); the whole-wiki full-text check finds no earlier neural instance (Appendix). The design holds across subjects, with covert above rest in 5 of 7. Verdict: ahead. The authors warp rest identically and state that DTW inflates correlation (Sec. Statistics). That control shows the cost: covert exceeds rest by 0.04 in r, DTW-aligned overt by 0.20, so one fifth of the overt margin survives (inference).

### M12 Evaluation: correlation and identification rank

**Usual approach:** of 5 prior pattern-match studies, only Pasley et al. [[9]](#ref-9) evaluate a reconstruction, by correlation and DTW-based identification rank (median 0.89 trial-averaged, 0.76 single-trial, 47 words); the paper reuses both. Across all years correlation leads (122 of 173, pattern match, Appendix).
**State of the art:** Berezutskaya et al. (2023) [later] [[10]](#ref-10) identify words from reconstructed spectrograms at 92%–100% against 8% chance, 12 words.

Overt rank 0.91 matches Pasley with 24–140 candidate 5-s segments of continuous reading. Covert rank is 0.55 against chance 0.5 and rest 0.48. Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Overt and covert reading | Overt speech production | – | standard |
| M02 Training-only supervision | Own overt audio features as targets | Paired audio targets | – | standard |
| M03 Training and adaptation | Per-subject linear fit | Per-subject fitting | – | standard |
| M04 Use-time action | Overt-trained, covert test | Overt-to-silent transfer, EMG/ultrasound (prior) (confirmed 3) | [[7]](#ref-7) (2024): covert TER 46.3% | standard |
| M05 Sensors | Clinical ECoG, high gamma | Clinical ECoG | – | standard |
| M06 Processing and decoding | Lagged linear map | Linear decoder | – | standard |
| M07 Lexicon and LM | None | None | – | not applicable |
| M08 Output | Spectrogram, modulation | Formant audio, real time (prior) (confirmed 1) | [[8]](#ref-8) (2025): listener WER 43.75% | standard |
| M09 Confirmation | Offline | Offline | – | not applicable |
| M10 Correction | Offline | Offline | – | not applicable |
| M11 Reference construction | Own overt audio, DTW | Heard-stimulus reference (prior) (pattern match 1) | [[5]](#ref-5) (2025): matched overt reference, unseen sentences | ahead |
| M12 Evaluation | Pearson r, identification rank | Correlation and rank (prior) (pattern match 1) | [[10]](#ref-10) (2023): 92-100% word ID | standard |
| M13 Device and cost | Epilepsy monitoring, offline | Offline clinical ECoG | – | not applicable |

## Where the claims outrun the evidence

- Covert beats warped rest by r 0.04 for spectrogram and for modulation, 0.46 against 0.42 [[1]](#ref-1); there is no mismatched-text control (covert output warped to another story's overt audio).
- The "partially shared" substrate (Abstract) rests on a transferred linear map; lower high-gamma SNR explains lower covert accuracy as well, as the authors concede (Discussion) [[1]](#ref-1).
- The same stories were read in both conditions and covert data have no held-out partition [[1]](#ref-1), so covert candidates share text with overt training targets.
- The 90/10 split of 7-s blocks has no seeds and no held-out story or session [[1]](#ref-1).

## What the field needs next

- M11: covert output scored against mismatched overt text under identical DTW, to measure the alignment floor directly.
- M04: a covert-trained arm on text or phoneme targets in the same subjects [[7]](#ref-7), to separate representation from SNR.
- M12: held-out stories in both conditions, with candidates from unseen text.
- M08: audio rendering and a listener test [[8]](#ref-8).

## Questions for the authors

- Were standardization statistics computed on training blocks only?
- How many random partitions were drawn, with which seeds?
- Did covert identification candidates come from stories whose overt blocks were in training?
- How was the 2-s DTW window chosen?

## Appendix: literature search

- M04 overt-to-silent-transfer (reused topic table). Inclusion rule: decoder trained only on overt or attempted overt speech applied to silent, mimed, inner or imagined speech without retraining, any signal; whisper transfer, perception-to-imagery transfer and similarity-only analyses excluded; versions count once. Ledger counts: slot-filled 5,595, pattern match 33 unique studies. Usual design: overt-to-silent transfer reported as degradation, 23 confirmed unique studies; 3 prior (first public before 2013-11), all EMG or ultrasound/video [[2]](#ref-2), [[6]](#ref-6), [[3]](#ref-3). Read in full: [[3]](#ref-3), [[7]](#ref-7). Known-item recall 1.0.
- M08 neural-speech-synthesis (reused topic table). Inclusion rule: continuous acoustic representations decoded from neural signals of speech production, output as speech or convertible to it; perception, text-then-TTS and limb-imagery control excluded. Ledger counts: slot-filled 3,268, pattern match 35 unique studies. Usual design (all years): output_types=audio, 11 slot-filled of 22. 15 confirmed unique studies, 1 prior [[4]](#ref-4). Read in full: [[4]](#ref-4), [[8]](#ref-8). Known-item recall 1.0.
- M11 covert-neural-reconstruction-reference (new topic). Inclusion rule: neural studies of covert, imagined, mimed or silent speech that state how the covert ground truth is built; design of interest is an acoustic reconstruction scored against the same participant's overt recording of the same text; class-label, heard-stimulus and text-only references are other designs; acoustic whisper conversion is not neural. Ledger counts: slot-filled 234, pattern match 167 unique studies. Prior population: 10 unique studies (pattern match), 1 reconstruction with a heard-stimulus reference, 0 with an overt reference for covert production. All years: label_only 54, dtw_alignment 35, overt_audio_reference 15 of 167 (pattern match). Full-text recall check over 8,947 wiki folders: 240 hits; before the target, 5 non-target hits, none neural covert (ultrasound and EMG DTW recognition, an acoustic whisper conversion thesis, an abbreviation list, [[9]](#ref-9)). Read in full: [[9]](#ref-9), [[4]](#ref-4), [[5]](#ref-5). Known-item recall 0.67.
- M12 neural-speech-reconstruction-identification-test (reused topic table). Inclusion rule: continuous acoustic reconstruction from neural recordings during perceived, produced, mimed or imagined speech, with evaluation; classification-only and text-only decoders excluded. Ledger counts: slot-filled 6,960, pattern match 173 unique studies. Usual design (all years): correlation, 122 of 173 (pattern match). Prior population: 5 unique studies, 1 reconstruction [[9]](#ref-9). Read in full: [[9]](#ref-9), [[10]](#ref-10). Known-item recall 0.67.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Martin, S., Brunner, P., Holdgraf, C., Heinze, H., Crone, N. E., Rieger, J., et al. “Decoding spectrotemporal features of overt and covert speech from the human cortex.” *Frontiers in Neuroengineering*, 2014, 7, 14. doi:[10.3389/fneng.2014.00014](https://doi.org/10.3389/fneng.2014.00014). Target. Read as the published article. [wiki: doi-10.3389-fneng.2014.00014](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fneng.2014.00014/article.md) [wiki: pmc-4034498-overtcovert](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-4034498-overtcovert/article.md) [wiki: pmc-4034498-spectemp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-4034498-spectemp/article.md)
2. <a id="ref-2"></a>Janke, M., Wand, M., Schultz, T. “A Spectral Mapping Method for EMG-based Recognition of Silent Speech.” *Proc. BIOSIGNALS 2010*, 2010. doi:[10.5220/0002814100220031](https://doi.org/10.5220/0002814100220031). Prior; M04 overt-to-silent transfer (EMG). [wiki: doi-10.5220-0002814100220031](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.5220-0002814100220031/article.md)
3. <a id="ref-3"></a>Florescu, V., Crevier-Buchman, L., Denby, B., Hueber, T., Pillot-Loiseau, C., Roussel, P., et al. “Silent vs Vocalized Articulation for a Portable Ultrasound-Based Silent Speech Interface.” *Interspeech*, 2010. <https://www.isca-archive.org/interspeech_2010/florescu10_interspeech.html> Prior; M04 overt-to-silent transfer (ultrasound and video). [wiki: isca-florescu10](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-florescu10/article.md) [wiki: isca-florescu10-silentvocal](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-florescu10-silentvocal/article.md) [wiki: isca-florescu10_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-florescu10_interspeech/article.md)
4. <a id="ref-4"></a>Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., Panko, M., et al. “A Wireless Brain-Machine Interface for Real-Time Speech Synthesis.” *PLoS ONE*, 2009, 4(12), e8218. doi:[10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218). Prior; deciding prior for M08 and M11. Versions pmc-2784218-wireless and pmc-2784218-wirelesssynth in the wiki. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis) [wiki: doi-10.1371-journal.pone.0008218](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1371-journal.pone.0008218/article.md)
5. <a id="ref-5"></a>Kim, D., Lee, S., Yin, K., Lee, S. “Reconstructing Unseen Sentences from Speech-related Biosignals for Open-vocabulary Neural Communication.” *arXiv preprint*, 2025. arXiv:[2510.27247](https://arxiv.org/abs/2510.27247). Later; state of the art for M11. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/reconstructing-unseen-sentences-from-speech-related-biosignals-for-open-vocabulary-neural-commun) [wiki: arxiv-2510.27247](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2510.27247/article.md)
6. <a id="ref-6"></a>Wand, M., Schultz, T. “Session-Independent EMG-Based Speech Recognition.” *Proc. BIOSIGNALS 2011*, 2011. doi:[10.5220/0003169702950300](https://doi.org/10.5220/0003169702950300). Prior; M04 overt-to-silent transfer (EMG). [wiki: doi-10.5220-0003169702950300](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.5220-0003169702950300/article.md)
7. <a id="ref-7"></a>Komeiji, S., Mitsuhashi, T., Iimura, Y., Suzuki, H., Sugano, H., Shinoda, K., et al. “Feasibility of decoding covert speech in ECoG with a Transformer trained on overt speech.” *Scientific Reports*, 2024, 14, 11491. doi:[10.1038/s41598-024-62230-9](https://doi.org/10.1038/s41598-024-62230-9). Later; state of the art for M04. [later] [wiki: doi-10.1038-s41598-024-62230-9](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41598-024-62230-9/article.md) [wiki: pmc-11106343-ecogtransformer](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11106343-ecogtransformer/article.md) [wiki: doi-10.1101-2024.02.05.578911](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2024.02.05.578911/article.md) [wiki: doi-10.21203-rs.3.rs-3927907-v1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.21203-rs.3.rs-3927907-v1/article.md)
8. <a id="ref-8"></a>Wairagkar, M., Card, N. S., Singer-Clark, T., Hou, X., Iacobacci, C., Miller, L. M., et al. “An instantaneous voice-synthesis neuroprosthesis.” *Nature*, 2025. doi:[10.1038/s41586-025-09127-3](https://doi.org/10.1038/s41586-025-09127-3). Later; state of the art for M08. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-instantaneous-voice-synthesis-neuroprosthesis) [wiki: doi-10.1038-s41586-025-09127-3](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-025-09127-3/article.md) [wiki: doi-10.1101-2024.08.14.607690](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2024.08.14.607690/article.md) [wiki: pmc-12369848-voicesynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12369848-voicesynth/article.md) [wiki: pmc-12369848-voice-synth-np](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12369848-voice-synth-np/article.md) [wiki: pmc-11370360-instvoice](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11370360-instvoice/article.md)
9. <a id="ref-9"></a>Pasley, B. N., David, S. V., Mesgarani, N., Flinker, A., Shamma, S. A., Crone, N. E., et al. “Reconstructing Speech from Human Auditory Cortex.” *PLoS Biology*, 2012, 10(1), e1001251. doi:[10.1371/journal.pbio.1001251](https://doi.org/10.1371/journal.pbio.1001251). Prior; deciding prior for M11 and M12. Versions doi-10.1371-journal.pbio.1001251 and pmc-3269422-speechrecon in the wiki. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/reconstructing-speech-from-human-auditory-cortex) [wiki: pmc-3269422-pasley](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3269422-pasley/article.md)
10. <a id="ref-10"></a>Berezutskaya, J., Freudenburg, Z. V., Vansteensel, M. J., Aarnoutse, E. J., Ramsey, N. F., van Gerven, M. A. J. “Direct speech reconstruction from sensorimotor brain activity with optimized deep learning models.” *Journal of Neural Engineering*, 2023, 20, 056010. doi:[10.1088/1741-2552/ace8be](https://doi.org/10.1088/1741-2552/ace8be). Later; state of the art for M12. [later] [wiki: doi-10.1088-1741-2552-ace8be](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-ace8be/article.md) [wiki: pmc-10510111-berezutskaya](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10510111-berezutskaya/article.md) [wiki: pmc-10510111-recon](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10510111-recon/article.md)
