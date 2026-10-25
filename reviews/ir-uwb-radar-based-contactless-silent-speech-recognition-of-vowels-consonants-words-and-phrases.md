# IR-UWB Radar-Based Contactless Silent Speech Recognition of Vowels, Consonants, Words, and Phrases

['', '', '', '']  
arXiv / imported corpus page 2023 · [DOI](https://doi.org/10.1109/ACCESS.2023.3344177) · [arXiv](https://arxiv.org/abs/2312.09572)

**Section:** [Radar, RF & Wi-Fi](../README.md#radar-rf--wi-fi) · **Review basis:** full_text

Proposes FERASEC feature extraction for contactless IR-UWB radar silent speech recognition of vowels, consonants, words and phrases. With the upper radar and DNN-HMM it reports 86.47% vowel and 81.59% consonant accuracy.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Two IR-UWB radars facing lips and below chin |
| Task | Contactless silent speech recognition |
| Vocabulary | 56 items: 8 vowels, 11 consonants, 25 words, 12 phrases |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Not stated |
| Key result | 86.47% vowels, 81.59% consonants, 88.95% words, 96.88% phrases (leave-one-out CV, upper radar) |

**Limitations.** Controlled lab study with prompted closed-set items and limited speaker diversity; sensitive to user alignment and tooth blockage; no open vocabulary or conversational speech tested.

## Full review

### In short

This paper introduces FERASEC, a novel radar feature extraction enabling the first contactless IR-UWB radar phoneme-level silent speech recognition with 86% vowel and 81% consonant accuracy, surpassing raw signal baselines and signifying a key advance in practical silent speech interfaces.

### Review

This work presents the first successful demonstration of contactless phoneme-level silent speech recognition using IR-UWB radar by introducing FERASEC, a radar-specific feature extraction method that transforms raw 2D radar frames into abbreviated envelopes, effectively capturing articulator movements despite noise and clutter. Comprehensive evaluations on 8 vowels, 11 consonants, 25 words, and 12 phrases show classification accuracies up to 86.47% for vowels and 81.59% for consonants using DNN–HMM classifiers with radar antenna positioned near the lips, outperforming baseline methods and prior radar SSR studies. The use of two radar placements reveals that upper lip-positioned radar better captures critical lip motions, necessary for phoneme discrimination. Although raw radar data or end-to-end deep learning on raw input perform poorly (<50%), engineered FERASEC features enable robust recognition. Controlled prompted speech data from 20 participants supports strong validation of phoneme recognition capability, although conversational and open-vocabulary scenarios remain untested. The study insightfully discusses practical deployment issues such as sensor alignment aiding and potential integration into consumer devices, marking a significant advance toward real-world contactless silent speech interfaces.

### Why it matters

A radar-specialized feature extraction and system design that enables realistic contactless phoneme-level silent speech recognition, a milestone beyond previous radar SSR word-only demos, verified with a large experimental dataset and classifier comparisons.

### Prior state of the art

Prior radar-based SSR showed limited small word-level demos with weak or unproven phoneme-level contactless recognition.

### What changed

Introduces FERASEC and demonstrates meaningful contactless IR-UWB radar SSR accuracy on phonemes, words, and phrases with radar antenna placement and aiding logic considerations.

### Position in the field

Core contactless SSI work establishing radar phoneme recognition feasibility with pragmatic sensor placement and aiding algorithms.

### Practical value

High potential for hands-free SSR in mobile or wearable devices if hardware integration and user alignment challenges are solved.

### Advanced

contactless_ssr; phoneme_level_radar; mobile_embedding_potential

### Unresolved

open_vocabulary; conversational_use; broader_speaker_variability

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | radar |
| Sensor | Upper and lower IR-UWB radar sensors; upper uses patch antennas facing lips, lower uses sinuous antennas below chin. |
| Body site | lip |
| Output | text |
| Vocabulary type | 8 vowels, 11 consonants, 25 words, and 12 phrases |
| Vocabulary size | 56 speech items across four task sets |
| Metrics and results | Classification accuracy evaluated via leave-one-out cross-validation across 20 reps per phoneme/word/phrase; vowels achieved 86.47%, consonants 81.59%, words 88.95%, phrases 96.88% with FERASEC + DNN-HMM upper radar. |
| Evaluation protocol | Leave-one-out cross-validation across repeated prompted articulation; separate experiments per speech unit type and radar position. |

### Limits

- **Technical:** Performance affected by articulator alignment; signal blockage by teeth can obscure tongue motion with upper radar; FERASEC depends on effective clutter mitigation and engineered transforms.
- **Evaluation:** Controlled lab study with prompted closed-set items, limited speaker diversity (mostly Korean with American English speakers), no open vocabulary or conversational speech tested.
- **Deployment:** Needs robust user-position handling, mitigating signal blockage (e.g. teeth), and hardware integration to small devices for daily use.
- **Scope of this review:** Closed-set prompted isolated and short phrase recognition; no open vocabulary, spontaneous speech, or broader speaker variability tested.

### Evidence

- This study represents the first demonstration of phoneme-level SSR using contactless radar and proposes a novel speech feature extraction algorithm specifically designed for IR-UWB radar-based SSR. (ABSTRACT)
- The study uses a data set of 20 participants pronouncing 8 vowels, 11 consonants, 25 words, and 12 phrases, with 20 repetitions each, recorded using two IR-UWB radar antennas positioned in front of lips and below chin. (A SPEECH STIMULI)
- Introduces FERASEC, a novel radar-specific speech feature extraction algorithm reducing dimensionality of IR-UWB radar frames into envelope features capturing articulator movement, essential for phoneme-level SSR accuracy. (A PROPOSED FEATURE EXTRACTION ALGORITHM)
- FERASEC utilizes concatenation of raw and clutter-reduced radar frames, envelope detection, downsampling, DC removal, plus first and second derivatives, creating six-dimensional feature set for classification. (A PROPOSED FEATURE EXTRACTION ALGORITHM)
- Evaluation conducted on 20 native or semi-native English-speaking participants trained on closed-set prompted 8 vowels, 11 consonants, 25 phonetically balanced words, and 12 phrases repeated 20 times with leave-one-out cross validation. (A SPEECH STIMULI)
- FERASEC combined with DNN-HMM and upper radar antenna placement yields recognition accuracies of 86.47% vowels, 81.59% consonants, 88.95% words, and 96.88% phrases. (HMM)
- Without engineered feature extraction (FERASEC), using raw or clutter-reduced frame sets alone for end-to-end DNN-HMM phoneme recognition yields accuracies below 50%. (1 Necessity of Developing a Feature Extraction Algorithm for IR)
- Although current proof-of-concept uses a hardware testbed, IR-UWB radar modules based on CMOS transceiver chips and antenna integration feasibility imply potential embedding of contactless SSR into smartphones or wearables. (BASED SSR STUDIES)
- A supporting aiding algorithm checks that the user's lips are properly aligned and within radar detection range before silent speech capture, improving usability for consumer device integration. (2 IR)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
