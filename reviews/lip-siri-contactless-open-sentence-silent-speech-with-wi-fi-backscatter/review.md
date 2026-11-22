# Lip-Siri: Contactless Open-Sentence Silent Speech with Wi-Fi Backscatter

Tian, Y., Du, H., Gu, C., Zhang, J., Wang, S., Zhou, H., Hou, J., Li, X.-Y. · arXiv preprint · 2026 · [arXiv:2601.18177](https://arxiv.org/abs/2601.18177)

## Verdict

The paper [[1]](#ref-1) changes the sensor (M05), a passive Wi-Fi backscatter tag near the face, and the output (M08), subword sentences instead of class labels. Both are standard: contactless radio-frequency sensing is already usual, Wi-Fi lip reading predates it [[2]](#ref-2), and face-worn RFID tags already sense speech by backscatter (Table I). The open-sentence claim is untested: 340 scripted sentences, each read at least twice, are split 80/20 at random, so test sentences very likely also appear in training (inference), and no unseen-sentence test exists. The headline 36.87% WER is worse than the visual baseline's 32.3% in the same room (§VI-B), although the text calls the two comparable. The held-out-user test (M12, standard) is the paper's strongest evidence.

## Against the field, component by component

### M05 Sensors: passive Wi-Fi backscatter tag off the body

**Usual approach:** of 33 radio-frequency speech-sensing studies (pattern match, Appendix), 21 record radar in the ledger (slot-filled, same 33), as in [[3]](#ref-3); the target uses a tag on a bracket within 50 cm (§VI-A).

**State of the art:** Wi-Fi lip reading under a face mask reached 95% accuracy on five vowels plus closed lips (2022) [[2]](#ref-2); for sentences, the target's own Table I quotes mmWave radar at 9.5% WER on 1,000 fixed sentences and 4-D radar at 4.55% WER on 30, both closed-set (§VIII-A). The target's 36.87% is 27.37 points above the 9.5% (inference), on a different output, so the gap does not rank the sensors.

Contact-free operation (§VIII-A) is shared with every remote radar and Wi-Fi system, and backscatter is not new: Table I lists face-worn RFID tags for speech (RFID Tattoo, 86% on 100 words and 20 sentences; HearMe). Only the tag's placement off the body is new. Its low power and cost (§I) go unmeasured on the software-defined radio prototype; commercial Wi-Fi is out of scope (§VI-A). The authors concede that jumping breaks it (§VIII-B). Verdict: standard.

### M08 Output: subword sentences instead of class labels

**Usual approach:** among the 19 of 33 studies with a ledger output (slot-filled), the most frequent is a class label, 5; full-text counts give sequence decoding 12 and closed-set classification 11 (pattern match, upper bounds, Appendix), so neither output dominates. The deciding priors classify five vowels [[2]](#ref-2) or fixed sentences [[4]](#ref-4); the target decodes subword tokens from a lexicon built on its own corpus (§V-C.1).

**State of the art:** SoniSpeech [later] (2026) reports 26.3% open-vocabulary silent WER with acoustic eyewear, one speaker, on 1,000 sentences from a separate split [[5]](#ref-5); the target reports 36.87% on a random split.

One speaker on unseen sentences against 12 users on probably recurring ones (inference): the 10.57-point gap ranks neither system but names the missing control, a sentence-disjoint split. The authors limit the claim to compositions the lexicon covers (§V-C.1). Verdict: standard, because the move to sequences is not tested on new sentences.

### M12 Evaluation: three held-out users

**Usual approach:** of 32 radar and radio-frequency recognition studies (pattern match, Appendix), 22 name a speaker-dependent split and 17 a speaker-independent one (overlapping); the target holds out three users and splits the rest 80/20 at random (§VI-B).

**State of the art:** none external; the topic table's best entry is this paper's own new-user result (2026), 81.5–85.5% word accuracy and 36.3–39.6% WER (§VI-F), a baseline rather than a win.

New users fall within about 4 points of the overall 85.61% (inference), the best evidence against per-user memorisation, from three users and one split. Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Energy segments, K-means units | Supervised training (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Cluster pseudo-label pre-training | Paired targets (slot-filled 31) | Lineage: [[6]](#ref-6) (2022) | standard |
| M03 Training and adaptation | One split, no validation set | Train/test split (slot-filled 1,526) | – | not reported |
| M04 Use-time action | Silent, manual start/end | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | Wi-Fi backscatter tag, 50 cm | Radar front end (slot-filled 21) | 95%, 5 vowels [[2]](#ref-2) (2022) | standard |
| M06 Processing and decoding | Transformer encoder-decoder | Neural decoder (slot-filled 7,345) | – | standard |
| M07 Lexicon and LM | Corpus subword lexicon | Lexicon or LM (slot-filled 119) | Lineage: [[7]](#ref-7) (2022) | standard |
| M08 Output | Subword sentences | Class label (slot-filled 5) | 26.3% WER, one speaker [[5]](#ref-5) (2026) | standard |
| M09 Confirmation | Display only | None (slot-filled 82) | – | not applicable |
| M10 Correction | None | None (slot-filled 82) | – | not applicable |
| M11 Reference construction | Prompted sentences | Read script (slot-filled 234) | – | standard |
| M12 Evaluation | 3 held-out users, random split | Speaker-dependent (pattern match 22) | None external; this paper [[1]](#ref-1) (2026) | standard |
| M13 Device and cost | SDR prototype, 20 dBm | Device constraints (slot-filled 6,075) | – | not reported |

## Where the claims outrun the evidence

- "Open sentence" (Abstract) is untested: no split holds out sentences or words (§VI-B), and the lexicon comes from the evaluation corpus (§V-C.1).
- The text calls the system comparable to the visual baseline [[8]](#ref-8), yet its WER is 4.57 points, or 14% relative, higher in the same environment (inference). Whether that baseline was trained on the 340-sentence corpus is not stated (§VI-B); if not, the comparison favours Lip-Siri, which saw the recurring sentences (inference).
- The voice-assistant test (§VII-B) adds 50 dB audio noise, which drops the assistant from 98% to 31% while Lip-Siri scores 90.5% with a 100-word lexicon; such noise cannot reach a radio sensor, so the test favours it by construction (inference).
- The 717.5 ms latency starts at a manual end click (§VI-G), so it is not hands-free.
- After two months accuracy falls 4.3% and WER rises 5.6% (§VI-E), not saying whether in points or relative terms.

## What the field needs next

- M12: a sentence-disjoint and word-disjoint test on the same users.
- M05: measured power of tag and receiver, and a commercial Wi-Fi receiver instead of software-defined radios.
- M08: WER against lexicon size, including words outside the lexicon.

## Questions for the authors

- Is the 80/20 split by sample, utterance or sentence, and how many test sentences also occur in training?
- How large is the final subword lexicon, and how many distinct words does the corpus contain?
- Were z-score statistics fitted on training data only, and which data chose hyperparameters and checkpoints?
- How many runs or seeds stand behind each figure, and what is their spread?
- What beam width is used, and is any language model applied?

## Appendix: literature search

- M05 rf-articulator-sensing-placement. Inclusion rule: speech or silent-speech recognition studies that sense the articulators with radar or other radio-frequency signals; the design compared is the front end and where it sits. Ledger counts: 7,329 slot-filled (M05); 33 pattern match (unique studies). Usual design: radar, 21 (slot-filled). Read in full: [[2]](#ref-2). Known-item recall: 0.75 (the missed id is a duplicate version of [[2]](#ref-2)).
- M08 rf-ssr-output-granularity. Inclusion rule: the same radio-frequency population; the design compared is a class label from a closed list versus a variable-length token sequence scored by WER. Ledger counts: 3,268 slot-filled (M08); 33 pattern match (unique studies), 19 with a recorded output. Usual design: class label, 5 (slot-filled); full-text pattern counts: sequence decoding 12, closed-set classification 11 (pattern match, upper bounds). Read in full: [[5]](#ref-5), [[4]](#ref-4), [[2]](#ref-2). Known-item recall: 0.75.
- M12 radar-ssr-speaker-split (published topic table, appended). Inclusion rule: radar or radio-frequency recognition studies; the design compared is whether test speakers are held out. Ledger counts: 6,960 slot-filled (M12); 32 pattern match (unique studies). Usual design: speaker-dependent, 22 (pattern match). Read in full: [[3]](#ref-3). Known-item recall: 1.0.
- Inherited slots, lineage examples: M02 cluster pseudo-label pre-training [[6]](#ref-6); M07 sub-word token inventories [[7]](#ref-7).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Tian, Y., Du, H., Gu, C., Zhang, J., Wang, S., Zhou, H., et al. “Lip-Siri: Contactless Open-Sentence Silent Speech with Wi-Fi Backscatter.” *arXiv preprint*, 2026. doi:[10.48550/arXiv.2601.18177](https://doi.org/10.48550/arXiv.2601.18177). arXiv:[2601.18177](https://arxiv.org/abs/2601.18177). Target. Read as arXiv v1. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip-siri-contactless-open-sentence-silent-speech-with-wi-fi-backscatter) [wiki: arxiv-2601-18177-lipsiri](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2601-18177-lipsiri/article.md) [wiki: arxiv-2601.18177](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2601.18177/article.md)
2. <a id="ref-2"></a>Hameed, H., Usman, M., Tahir, A., Hussain, A., Abbas, H., Cui, T. J., et al. “Pushing the limits of remote RF sensing by reading lips under the face mask.” *Nature Communications*, 2022, 13, 5168. doi:[10.1038/s41467-022-32231-1](https://doi.org/10.1038/s41467-022-32231-1). Prior; deciding prior for M05 and M08; M05 state of the art. [wiki: doi-10.1038-s41467-022-32231-1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41467-022-32231-1/article.md) [wiki: pmc-9452506-rflip](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9452506-rflip/article.md) [wiki: pmc-9452506-rflipread](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9452506-rflipread/article.md)
3. <a id="ref-3"></a>Shin, Y. H., Seo, J. “Towards Contactless Silent Speech Recognition Based on Detection of Active and Visible Articulators Using IR-UWB Radar.” *Sensors*, 2016, 16(11), 1812. doi:[10.3390/s16111812](https://doi.org/10.3390/s16111812). Prior; read for the M12 topic table (speaker-dependent split). [wiki: doi-10.3390-s16111812](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3390-s16111812/article.md) [wiki: pmc-5134471-iruwb](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5134471-iruwb/article.md)
4. <a id="ref-4"></a>Ge, Y., Tang, C., Li, H., Chen, Z., Wang, J., Li, W., et al. “A comprehensive multimodal dataset for contactless lip reading and acoustic analysis.” *Scientific Data*, 2023, 10, 895. doi:[10.1038/s41597-023-02793-w](https://doi.org/10.1038/s41597-023-02793-w). Prior; deciding prior for M08. [wiki: doi-10.1038-s41597-023-02793-w](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41597-023-02793-w/article.md) [wiki: pmc-10719268-mmdataset](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10719268-mmdataset/article.md) [wiki: pmc-10719268-rvtall](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10719268-rvtall/article.md)
5. <a id="ref-5"></a>Zhang, R., Liu, J., Guimbretière, F., Zhang, C. “SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces.” *Proc. Interspeech 2026*, 2026. arXiv:[2608.00803](https://arxiv.org/abs/2608.00803). Later; M08 state of the art. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/sonispeech-a-large-scale-open-vocabulary-tri-modal-dataset-for-wearable-silent-speech-interfaces) [wiki: arxiv-2608.00803](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2608.00803/article.md) [wiki: isca-zhang26y-sonispeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-zhang26y-sonispeech/article.md)
6. <a id="ref-6"></a>Shi, B., Hsu, W., Lakhotia, K., Mohamed, A. “Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction.” *International Conference on Learning Representations (ICLR)*, 2022. arXiv:[2201.02184](https://arxiv.org/abs/2201.02184). Prior; lineage example for M02 (cluster pseudo-label pre-training). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/learning-audio-visual-speech-representation-by-masked-multimodal-cluster-prediction) [wiki: arxiv-2201.02184](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2201.02184/article.md)
7. <a id="ref-7"></a>Prajwal, K. R., Afouras, T., Zisserman, A. “Sub-word Level Lip Reading With Visual Attention.” *Proc. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2022. <https://openaccess.thecvf.com/content/CVPR2022/papers/Prajwal_Sub-Word_Level_Lip_Reading_With_Visual_Attention_CVPR_2022_paper.pdf> Prior; lineage example for M07 (sub-word token inventory). [wiki: cvf-prajwal22-subword-vtp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-prajwal22-subword-vtp/article.md)
8. <a id="ref-8"></a>Ma, P., Petridis, S., Pantic, M. “Visual Speech Recognition for Multiple Languages in the Wild.” *Nature Machine Intelligence*, 2022, 4. doi:[10.1038/s42256-022-00550-z](https://doi.org/10.1038/s42256-022-00550-z). arXiv:[2202.13084](https://arxiv.org/abs/2202.13084). Prior; the target's visual lip-reading baseline. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/visual-speech-recognition-for-multiple-languages-in-the-wild) [wiki: doi-10.1038-s42256-022-00550-z](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s42256-022-00550-z/article.md) [wiki: arxiv-2202.13084](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2202.13084/article.md) [wiki: doi-10.21203-rs.3.rs-1386805-v1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.21203-rs.3.rs-1386805-v1/article.md)
