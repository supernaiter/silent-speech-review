# Lip-Siri: Contactless Open-Sentence Silent Speech with Wi-Fi Backscatter

Ye Tian, Haohua Du, Chao Gu, Junyang Zhang, Shanyue Wang, Hao Zhou, Jiahui Hou, Xiang-Yang Li  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2601.18177)

**Section:** [Radar, RF & Wi-Fi](../README.md#radar-rf--wi-fi) · **Review basis:** full_text+summary

Lip-Siri senses lip motion contactlessly with Wi-Fi frequency-shifted backscatter and decodes lexicon-constrained sentences, reporting 85.61% word accuracy and 36.87% sentence WER on a random 80/20 split plus three held-out users.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Wi-Fi backscatter tag with SDR (USRP) transceivers |
| Task | Lexicon-constrained sentence recognition |
| Vocabulary | 340 handbook sentences, 3,398 reported words; lexicon-composed |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 85.61% word accuracy, 36.87% sentence WER, random 80/20 split; new users 81.5-85.5% |

**Limitations.** Lexicon composition is not unseen-word recognition; main split is not sentence-disjoint, and SDR hardware, manual start/end clicks and 50 cm geometry limit deployment.

## Full review

### In short

A credible contactless Wi-Fi backscatter SSI prototype with 85.61% word accuracy and 36.87% sentence WER, but lexicon-composed sentences are not unseen-word recognition and deployment still requires SDR hardware plus manual boundaries.

### Review

Lip-Siri is a useful contactless RF prototype: it places a frequency-shifted backscatter tag on a nearby object rather than on the user's face, then turns filtered lip-motion traces into variable-length subword sequences. The reported base experiment uses 15 volunteers, 340 sentences and 3,398 word occurrences, with three users held out; average word accuracy is 85.61% and sentence WER is 36.87%. Those results support feasibility, not a general open-vocabulary claim. The lexicon is built from a handbook and new words are usable only when composed from existing subwords; the paper does not test words outside that lexicon or provide a sentence-disjoint split for the other users. The SDR prototype also depends on a tag within 50 cm, a PC, and manual start/end clicks. Its 717.5 ms figure is measured from the end click to the displayed result for a 10-second signal, not end-to-end hands-free streaming latency. Figure 13 shows useful tolerance to moderate conditions but a large RF WER under jumping and materially higher WER with a mask. Whole-system power, rejection coverage, exact lexicon/beam settings, and component ablations remain unresolved.

### Why it matters

Demonstrates a non-wearable near-field RF sensing architecture and a practical path from lip-motion traces to lexicon-constrained sentence output, with explicit held-out-user and scenario tests.

### Prior state of the art

Sensing-based silent speech interfaces commonly use wearable or held sensors, or dedicated radar, and usually classify a fixed list of words or sentences. Wireless backscatter lip sensing has also generally required a tag near the face.

### What changed

Moves the sensing tag from the user's body or chin to a nearby stand or monitor and decodes continuous lip-motion traces into variable-length subword sequences constrained by an extensible lexicon.

### Position in the field

A contactless Wi-Fi backscatter sentence-decoding prototype that extends RF silent-speech work beyond fixed command sets, while remaining an SDR-based laboratory system with lexicon and split limitations.

### Practical value

Moderate: nearby-object placement and no on-body sensor are promising for quiet or privacy-sensitive settings, but manual segmentation, 50 cm geometry, SDR hardware, and unmeasured whole-system power limit immediate deployment claims.

### Advanced

contactless-near-field-sensing; lexicon-composed-sentence-decoding; radio-interference-suppression; non-wearable-input

### Unresolved

Unseen-word recognition; sentence-disjoint evaluation; speaker/session independence; continuous hands-free operation; rejection coverage; tag and receiver cost/power; robustness to violent motion and tag-facing geometry

### Narrowed or regressed

The prototype still uses USRP SDR hardware, a PC, a tag within 50 cm, and manual start/end buttons; no measured whole-system power or complete commercial-Wi-Fi deployment is provided.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | Contactless Wi-Fi frequency-shifted backscatter sensing of lip-motion traces; SDR transmitter/receiver prototype. |
| Sensor | Frequency-shifted passive backscatter tag on a bracket or nearby object, connected antenna, USRP-RIO transmitter, USRP-2943R receiver, LabVIEW control, Ethernet-connected PC with Intel Core i5-11500 and 32 GB RAM; a camera records lip motion for visual comparison. |
| Body site | face; lip |
| Output | text |
| Vocabulary type | Lexicon-guided subword sequence decoding; composable sentence combinations within a scenario lexicon. |
| Vocabulary size | The base handbook is organized into 340 sentences and 3,398 reported words; unique-word count and final subword lexicon size are not reported. |
| Metrics and results | Overall average word prediction accuracy 85.61% and continuous sentence WER 36.87%; representative visual SSI WER 32.3% on recorded videos. Three new users range from 81.5% to 85.5% word accuracy and 36.3% to 39.6% WER. The silent-assistant 100-word lexicon case reports 92% accuracy and 90.5% under 50 dB audio interference. Reported latency is 717.5 ms from end-button click to displayed result for a 10-second signal, consisting of no more than 50 ms transmission, 525 ms processing, and 142.5 ms inference. Values are author-reported and not independently reproduced. |
| Evaluation protocol | Offline word accuracy and continuous-sentence WER on a random 80/20 split plus three held-out users; sentence-length, signal-strength, time-interval, office/library/bedroom, silent-assistant, and eight-condition motion/lighting/mask comparisons; visual-SSI comparison from recorded video; end-button-to-result latency measurement. |

### Limits

- **Technical:** The tag isolates a shifted component but does not remove all non-target paths; contaminated windows are discarded and the rejection rate is not reported. The main cohort uses random sample splitting, leaving possible sentence or repetition overlap unspecified. Lexicon composition is not evidence of unseen-word recognition. Manual start/end clicks prevent a hands-free streaming interpretation of the reported latency. Jumping substantially worsens RF WER, while tag geometry and whole-system power are unmeasured.
- **Evaluation:** The 12-user experiment uses a random 80/20 sample split without an explicit sentence-disjoint protocol, while only three users are held out as new users. The lexicon is initialized from a fixed English handbook and its final size is not reported; adding words is only supported when they can be composed from existing subwords. Rejection rate from contamination gating, confidence intervals, repeated-seed variation, ablations, exact beam width, optimizer settings, and full power are not reported.
- **Deployment:** The demonstrated system is an SDR prototype using a USRP-RIO transmitter, USRP-2943R receiver, Ethernet-connected PC, and a backscatter tag within 50 cm. Users manually click start and end buttons, the tag is fixed on a bracket, and a complete commercial-Wi-Fi implementation is explicitly outside scope. Violent motion can substantially degrade RF recognition, and tag-facing geometry is not characterized beyond the tested scenarios.
- **Scope of this review:** Fifteen-volunteer SDR prototype evaluation with 340 handbook sentences, 3,398 reported word occurrences, three held-out users, and selected indoor/motion scenarios. No clinical participants, unrestricted vocabulary, sentence-disjoint split for the main cohort, adversarial privacy analysis, or continuous hands-free use.

### Evidence

- The abstract presents Lip-Siri as a Wi-Fi backscatter SSI supporting open-vocabulary sentence recognition through lexicon-guided subword decoding, with a frequency-shifted tag and Transformer encoder-decoder. (Abstract; PDF p. 1)
- The prototype uses a frequency-shifted passive backscatter tag placed on a stand or monitor, allowing the user to face the tag without attaching or holding it near the chin. (Section V-A1; PDF pp. 5-6)
- The system extracts a first-order shifted backscatter component, computes phase differences, applies a 0–50 Hz low-pass filter, rejects windows above median plus three MAD, and uses VMD to suppress slower modes. (Section V-A2; PDF p. 6)
- Lip-motion units are approximately segmented with 0.2 s, 5 s, and 0.1 s windows; 67-dimensional time/frequency/differential features are standardized and clustered with K-means. The signal-processing description separately cites VMD with K=4 as its implementation example. (Sections V-B1–V-B2 and Algorithm 1; PDF pp. 6-7)
- The lexicon starts from characters in a scenario corpus and repeatedly merges frequent adjacent symbols; the decoder predicts variable-length subword sequences with a 12-layer, 12-head encoder, 6-layer, 4-head decoder, and beam search. (Sections V-C1–V-C2; PDF pp. 7-8)
- The paper defines open-sentence recognition as variable-length decoding over a lexicon and states that adding a word does not require retraining only when it is composable from existing subwords. This does not test recognition of words outside the lexicon or unrestricted open-vocabulary speech. (Section V-C2 and Table I caption; PDF pp. 8 and 11)
- The evaluation recruits 15 volunteers over six months, uses 340 handbook sentences and 3,398 reported words, asks users to repeat base sentences at least twice, and collects 11,700 base samples. Three users are reserved as new users; the remaining data use a random 80/20 training/testing split. (Sections VI-A–VI-B, Data Collection and evaluation setup; PDF pp. 8–9)
- The reported overall result is 85.61% average word accuracy and 36.87% average continuous-sentence WER; a recorded-video visual SSI comparison reports 32.3% WER. (Section VI-B; Fig. 9; PDF p. 9)
- For three new users, average word accuracy ranges from 81.5% to 85.5% and sentence WER ranges from 36.3% to 39.6%. (Section VI-F; Fig. 11; PDF pp. 9–10)
- The paper does not specify sentence-disjoint grouping for the random 80/20 split, unique vocabulary size, final subword lexicon size, beam width, optimizer, epochs, contamination rejection rate, confidence intervals, or component ablations. (Sections VI-A, V-B, and V-C; PDF pp. 6-9)
- The interface requires a user to click start before lip-reading and end afterward. For a 10-second signal, the paper reports no more than 50 ms transmission, 525 ms signal processing, 142.5 ms inference, and 717.5 ms total latency from end click to displayed result. (Section VI-G; PDF p. 10)
- In eight scenario comparisons with two volunteers, RF WER is 35.8% in normal conditions, 38.5% with head rotation, 83.5% while jumping, 33.4% while typing, 39.0% while walking, and 46.5% with a mask; the prototype uses SDR hardware and the paper does not measure whole-system power. (Sections VIII-A–VIII-B; Fig. 13; PDF p. 11)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
