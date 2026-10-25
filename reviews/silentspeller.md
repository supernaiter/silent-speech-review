# SilentSpeller: Towards mobile, hands-free, silent speech text entry using electropalatography

Naoki Kimura, Tan Gemicioglu, Jonathan Womack, Yuhui Zhao, Richard Li, Abdelkareem Bedri, Zixiong Su, Alex Olwal, Jun Rekimoto, Thad Starner  
CHI '22 · [DOI](https://doi.org/10.1145/3491102.3502015)

**Section:** [Electropalatography & in-mouth sensors](../README.md#electropalatography--in-mouth-sensors) · **Review basis:** full_text+existing_expert_seed

SilentSpeller enables silent spelling text entry with an in-mouth electropalatography retainer, reaching 37 wpm at 87% accuracy in live entry and comparable accuracy while walking.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | SmartPalate retainer, 124 capacitive electrodes (EPG) |
| Task | Text entry by silent spelling |
| Vocabulary | 1164-word dictionary offline; 321 words live |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Both |
| Key result | Live entry 37 wpm at 87% accuracy (best 53 wpm, 91%); 92% word accuracy offline |

**Limitations.** Strongly user-dependent; requires an obtrusive custom-fitted in-mouth retainer; offline tuning used only two main participants.

## Full review

### In short

SilentSpeller is a strong, rigorously tested SSI system that reframes silent speech as silent spelling, enabling large vocabulary, live text entry, and walking robustness with in-mouth electropalatography sensors.

### Review

SilentSpeller offers a carefully validated alternative to classic silent speech interfaces by changing the recognition task from continuous silent speech to discrete silent spelling. This reframing produces a more structured signal that, together with electropalatography sensors and a user-dependent HMM recognizer, supports a large vocabulary of 1164 words with high offline accuracy. The system uniquely supports live interactive text entry at speeds around 37 wpm with 87% accuracy, including robust performance while walking, demonstrating tolerance to motion artifacts. Limitations include the requirement for custom dental impressions, obtrusive mouth hardware, strong user dependence for training, and struggles with user independence and social acceptability. Overall, the work advances SSI toward viable mobile, hands-free text entry applications in privacy-sensitive or hands-busy scenarios, providing extensive empirical evidence backing claims.

### Why it matters

The paper's main contribution is the novel problem reframing from silent speech to silent spelling using an electropalatography retainer, which yields practical live text entry over large vocabularies including unseen words, with empirical validation of robustness to walking and comparison to mainstream mobile text input.

### Prior state of the art

Most silent speech interfaces were limited to small vocabularies (~100 words), stationary use, and offline, non-interactive experiments, with little evidence for practical live text entry.

### What changed

The key change is reframing the task from silent speech recognition to silent spelling recognition, allowing a larger vocabulary (1164 offline words), robust unseen-word generalization, tolerance to walking motion, and live hands-free text entry at reasonable speeds (~37 wpm average).

### Position in the field

One of the clearest practical SSI task-reframing papers to date; less natural than silent speech but more usable for mobile text entry.

### Practical value

High for privacy-sensitive communication and hands-busy users; useful where speech is socially inappropriate and users can manage oral hardware.

### Advanced

large_vocabulary; unseen_word_generalization; walking_robustness; live_text_entry; hands_free_texting

### Unresolved

user_independence; comfort; social_acceptability; broader_symbol_input

### Evaluation details

| Item | Details |
| --- | --- |
| Task | text-entry using silent spelling |
| Input | electropalatography |
| Sensor | SmartPalate custom dental retainer with 124 capacitive electrodes sampled at 100 Hz, connected wired or wireless to processing device. |
| Body site | palate; tongue |
| Output | text |
| Vocabulary type | Dictionary-based silent spelling with triletter HMM decoding, phrase composition, and bigram correction |
| Vocabulary size | 1164 isolated-word dictionary offline; live text entry with 321 unique words in phrase corpus |
| Metrics and results | Offline HMM accuracy: ~97% character, 92% word; Unseen word offline test: 94.5% character, 85.5% word accuracy; Walking and seated phrase recognition: ~97.5% vs 96.5% character accuracy; Live text entry average 37 words per minute at 87% accuracy, best participant 53 wpm at 91%. |
| Evaluation protocol | Offline isolated word recognition with 10-fold cross validation; reserve testing on 100 unseen words; seated vs walking phrase recognition; live interactive text entry with push-to-talk interface and edit gestures. |

### Limits

- **Technical:** Recognition confusions occur mainly for letters with similar palatograms, especially EE-sound letters (B/P, D/T/Z). Strong user-dependence; user-independent recognition remains poor.
- **Evaluation:** Offline experiments rely on data from only two main participants for tuning; live text entry and walking tests include seven users but under constrained phrase tasks; vocabulary is limited to English letters and space without punctuation or capitalization.
- **Deployment:** The system requires a custom-fitted in-mouth SmartPalate retainer with 124 electrodes connected by a wired (now partially wireless prototype) interface. The retainer remains obtrusive, and the user-dependent training required limits scalability and ease of deployment.
- **Scope of this review:** The system targets discreet text entry, explicitly trading away naturalness of silent speech for reliability; not a conversational silent speech system.

### Evidence

- We introduce silent spelling as an alternative for silent speech interaction (SSI). In silent spelling, the user spells words without voicing, which increases signal reliability and enables larger vocabularies (1164 words in this work) and on-the-go interaction. (1 INTRODUCTION)
- Offline HMM recognition on 2328 isolated words (1164 unique) achieves an average of 97% character accuracy and 92% word accuracy; unseen word testing on 100 words removed from training achieves 94.5% character and 85.5% word accuracy; walking phrase recognition yields 97.5% character accuracy walking vs. 96.5% seated; live text entry across seven users averaged 37 words per minute at 87% accuracy, with a top participant reaching 53 wpm at 91% accuracy. (TUNING MODELS)
- SilentSpeller employs a custom in-mouth SmartPalate retainer with 124 binary capacitive electrodes at 100 Hz, which senses tongue-palate contact patterns; a custom dental impression is required. (3.2 SMARTPALATE)
- Evaluation includes offline isolated word recognition with ten-fold cross validation on two participants, unseen word tests with 100 randomly removed words, walking vs seated phrase recognition on two participants, and live interactive text entry experiments on seven participants using 321-word phrase vocabulary. (TUNING MODELS)
- SilentSpeller is wearable, hands-free, mobile suitable and real-time capable; however, current hardware requires a wired connection to external hardware, making it obtrusive. Wireless prototypes using Bluetooth Low Energy dongles have been developed, but the device remains obtrusive and requires custom dental impressions, limiting deployment readiness. (3.2 SMARTPALATE)
- The system's user-dependent training regime requires about 1-2 hours of data collection (2328 isolated words) per participant to reach optimal accuracy; user independent models tested so far yield poor accuracy (~55% character), limiting deployment readiness. (4.3 TUNING USER DEPENDENT RECOGNIZERS)
- Although SilentSpeller shows little performance degradation during walking, the current in-mouth retainer and wired setup remain intrusive and socially conspicuous, which social acceptability remains unresolved and limits deployment. (8 DISCUSSION)
- SilentSpeller recognizes sequences of 26 English letters spelled silently using tongue-palate contact patterns, decoding via HMMs with triletter states, using PCA features reduced to 16 top eigen-palate components, sampled at 100 Hz. (3.3 RECOGNIZER PIPELINE)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
