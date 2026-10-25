# Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild

Sindhu B Hegde, K R Prajwal, Rudrabha Mukhopadhyay, Vinay P Namboodiri, C. V. Jawahar  
arXiv / imported corpus page 2022 · [DOI](https://doi.org/10.1145/3503161.3548081) · [arXiv](https://arxiv.org/abs/2209.00642)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

VAE-GAN lip-to-speech synthesis for arbitrary speakers in the wild; holds up on unconstrained LRW/LRS2, and multi-speaker pretraining with 5 h adaptation nearly matches a 20 h single-speaker model.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Silent lip/face video |
| Task | Speech synthesis from lip video |
| Vocabulary | Open vocabulary (LRW 500 words; LRS2 59k) |
| Speaker | Speaker-independent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Not reported |

**Limitations.** Struggles with severe or non-frontal head pose and lip-ambiguity; benchmark-only with a small human study and no latency or deployment test.

## Full review

### In short

The real contribution is not just another VAE-GAN; it is turning lip-to-speech into an arbitrary-speaker problem with credible low-data adaptation.

### Review

Table 3 is the core evidence. On LRW and LRS2, the model posts the best perceptual metrics in the table, including FDSD/KDSD/LSE-D of 1.638/0.8/8.173 on LRW and 1.273/0.2/8.155 on LRS2, while prior lip-to-speech baselines collapse more badly on LRS2. Table 4 then shows the human side moving the same way, with the proposed model scoring 3.22 intelligibility, 2.98 perceptual quality, 2.28 sync accuracy, and 2.69 voice match, clearly above the listed alternatives. Figure 5 matters too: the multi-speaker pretrain nearly matches the single-speaker baseline with only 25% of the target-speaker data. The limitations section is honest that drastic head motion, non-frontal views, and incorrect word generation remain unresolved.

### Why it matters

The full text backs a meaningful field move: the model is not best on every raw metric, but it holds up on harder unconstrained datasets and shows that multi-speaker pretraining can nearly match a 20-hour single-speaker model with only 5 hours of adaptation data.

### Prior state of the art

Most lip-to-speech systems were either single-speaker, constrained-lab models or needed much more per-speaker data to work at all.

### What changed

This paper pushes the task toward arbitrary identities in the wild and argues that distributional modeling plus speaker conditioning is necessary.

### Position in the field

Strong speaker-general lip-to-speech paper focused on unconstrained identity and vocabulary conditions.

### Practical value

Useful when collecting tens of hours per target speaker is unrealistic and the system must generalize across identities.

### Advanced

speaker generalization; problem framing; evaluation

### Unresolved

robustness to head pose; language modeling; live deployment

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | silent lip video |
| Body site | face; lip |
| Output | speech-audio |
| Vocabulary type | open vocabulary in the wild |
| Vocabulary size | LRW: 500 words; LRS2: 59k vocabulary |
| Metrics and results | PESQ; STOI; SED; FDSD; KDSD; LSE-C; LSE-D; human ratings; fine-tuning data-efficiency curves |
| Evaluation protocol | constrained GRID/TCD-TIMIT benchmarks, unconstrained LRW/LRS2 comparison, human evaluation, and low-data fine-tuning study |

### Limits

- **Technical:** The model still struggles with severe head movement, non-frontal heads, and language-level ambiguity that lip motion alone cannot resolve.
- **Evaluation:** The unconstrained evidence is benchmark-based and the human study uses 15 LRS2 samples rated by 20 participants, not a deployment scenario.
- **Deployment:** No live product path, robustness-to-camera-noise study, or interactive latency measurement is reported.
- **Scope of this review:** Arbitrary-speaker lip-to-speech synthesis from video only.

### Evidence

- The abstract says the model generates speech from silent lip videos for arbitrary speakers in the wild and is not restricted to a fixed number of speakers. (ABSTRACT)
- Section 3.3.1 says unconstrained evaluation is built on LRW and the full LRS2 train plus pre-train data, with LRS2 covering thousands of speakers and about 59k vocabulary. (3.3.1 Datasets and Training Strategy.)
- Table 3 reports the proposed model at 1.273 FDSD, 0.2 KDSD, 2.507 LSE-C, and 8.155 LSE-D on LRS2, outperforming the compared lip-to-speech baselines there. (Table 3: All models are pre-trained on LRW dataset and then trained on LRS2.)
- The limitations section says the model still struggles with drastic head movement, non-frontal heads, and outputs that do not form the right words or phrases. (6     LIMITATIONS AND FUTURE DIRECTIONS)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
