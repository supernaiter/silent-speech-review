# LipLearner: Customizable Silent Speech Interactions on Mobile Devices

Zixiong Su, Shitao Fang, Jun Rekimoto  
arXiv / imported corpus page 2023 · [DOI](https://doi.org/10.1145/3544548.3581465) · [arXiv](https://arxiv.org/abs/2302.05907)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

LipLearner enables customizable few-shot silent speech commands on smartphones with on-device keyword spotting and incremental learning; reaches 98.8% five-shot accuracy on 30 commands in a live study.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Smartphone front camera (lip video) |
| Task | Command recognition |
| Vocabulary | User-defined commands, 25-30 tested |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Both |
| Key result | 98.8% five-shot (81.7% one-shot) accuracy, 30 commands, mobile app; ~422 ms on-device latency |

**Limitations.** Modest vocabulary and study scale; confuses similar commands, requires visible lips, and incremental learning adds user burden.

## Full review

### In short

LipLearner is a strong mobile silent speech system that uniquely closes the loop from few-shot lipreading model design to practical on-device customization and keyword spotting, demonstrated robustly in real-world conditions and a user study.

### Review

LipLearner advances the state-of-the-art in mobile silent speech interfaces by leveraging contrastive pretraining on public lipreading data to extract robust visual speech embeddings suitable for few-shot adaptation. Through a simple linear classifier trained on just a few shots per command, combined with Voice2Lip—a novel automatic annotation method using vocalized speech for registering new silent speech commands—the system allows efficient, practical personalization on commodity smartphones. Their mobile app prototype further integrates a visual keyword spotting mechanism that avoids misactivation common in mouth-opening triggers, and supports on-device incremental learning to refine recognition during usage. The paper thoroughly evaluates the approach on extensive datasets with challenging real-world conditions, showing strong generalizability and robustness, and validates usability in a 16-participant user study with customizable multilingual commands. Remaining challenges include user effort in active learning and disambiguation of similar commands, as well as limited scale relative to open vocabulary applications. Overall, the paper makes a significant contribution in closing the loop from model design to practical mobile silent speech interaction.

### Why it matters

The key advance is enabling end-to-end on-device silent speech interaction with few-shot customizable command registration via Voice2Lip, practical keyword spotting, and incremental learning, rather than just offline lipreading accuracy. This system design and evaluation close a major gap towards real mobile SSI deployment.

### Prior state of the art

Mobile lipreading interfaces were typically fixed-vocabulary or relied on costly per-user data collection and retraining from scratch, limiting personalization and deployment on commodity devices.

### What changed

LipLearner replaces training-from-scratch approaches with a few-shot mobile workflow incorporating Voice2Lip for easy command enrollment, a keyword spotting system robust to misactivation, and on-device incremental fine-tuning enabling practical customization.

### Position in the field

One of the clearest mobile SSI papers tying model design directly to practical enrollment and real-time use on commodity devices.

### Practical value

High for enabling privacy-preserving, hands-free silent speech command input on smartphones that users can adapt with minimal effort.

### Advanced

few_shot_customization; mobile_ssi; keyword_spotting; on_device_learning

### Unresolved

open_vocabulary_interaction; lower_effort_active_learning

### Evaluation details

| Item | Details |
| --- | --- |
| Task | command-recognition |
| Input | video (front camera lip region) |
| Sensor | smartphone front camera |
| Body site | lip |
| Output | commands |
| Vocabulary type | command vocabulary; multilingual user-defined |
| Vocabulary size | customizable user-defined with tested 25 to 30 commands |
| Metrics and results | One-shot 25-command F1 0.8947; mobile app 30-command one-shot accuracy 81.7%, five-shot 98.8%; keyword spotting average EER 6.75%; on-device latency about 422 ms. |
| Evaluation protocol | few-shot with cross-condition robustness, keyword spotting evaluated by EER, one-shot F1, user study involving real-time silent speech command issuance and incremental learning |

### Limits

- **Technical:** Fails on very similar commands causing confusion; requires visible lip movements; incremental learning demands user participation.
- **Evaluation:** Evaluation on 25-command classification, and 30-command live study, both limited scale and vocabulary; testing mainly on frontal lip videos under defined lighting/posture/gesture manipulations; unknown performance on open vocabulary or completely unseen environments beyond tested conditions.
- **Deployment:** User burden remains due to active learning and need for correction when similar commands cause confusion; reliance on visible lips limits use in occluded conditions; current vocabulary and study scale modest relative to open natural language; threshold tuning for keyword spotting remains user-dependent.
- **Scope of this review:** Mobile silent command interaction on smartphone, not general open-vocabulary speech recognition.

### Evidence

- The paper proposes customizable mobile silent-speech interaction with few-shot lipreading, Voice2Lip registration, visual keyword spotting, and on-device incremental learning. (ABSTRACT)
- For 25-command classification, F1-score of 0.8947 was achieved with one shot; app study reports 30-command one-shot accuracy 81.7% and five-shot 98.8%; keyword spotting average EER 6.75%; on-device latency about 422 ms. (ABSTRACT)
- LipLearner runs on a commodity smartphone in real-time with latency about 422 ms, all processing on-device supporting hands-free silent speech interaction without network connection. (6.2 System Implementation)
- Evaluation conducted with LRW public dataset for contrastive pretraining plus an in-the-wild dataset collected with 11 participants in 7 conditions for a total of 9625 clips; a 16-participant live user study tested real-time activation, command registration, and recognition, including multilingual and user-defined commands. (4)
- Technical limits include reliance on visible lips, confusion between very similar commands, and cognitive and physical user burden in active learning. (10)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
