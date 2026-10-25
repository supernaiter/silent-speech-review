# Convolutional Neural Network-Based Age Estimation Using B-Mode Ultrasound Tongue Image

Kele Xu, Tamas Gabor Csapo, Ming Feng  
arXiv / imported corpus page 2021 · [arXiv](https://arxiv.org/abs/2101.11245)

**Section:** [Ultrasound & tongue imaging](../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text

Exploratory CNN regression of child age from tongue ultrasound images, reaching validation MSE 2.03 on UXTD versus 3.64 for a mean-age baseline.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | B-mode ultrasound tongue images |
| Task | Age estimation from ultrasound |
| Vocabulary | Not applicable |
| Speaker | Not stated |
| Session | Not applicable |
| Online / offline | Offline |
| Key result | Validation MSE 2.03 on UXTD (baseline 3.64); 4.87 on UPX (baseline 5.35) |

**Limitations.** Not an SSI system; small child-only datasets, validation-set error only, and no external dataset or deployment test.

## Full review

### In short

Real signal, wrong target for SSI.

### Review

The paper is honest proof-of-concept work. It shows the CNN beats mean-age baselines on both child cohorts, reaching validation MSE 2.03 on UXTD and 4.87 on UPX, so the images do carry age-related information. But the contribution is not to silent speech or speech reconstruction; it is a side-channel articulatory analysis result whose main value is methodological and clinical rather than interface-oriented.

### Why it matters

The full text supports only a narrow claim: age-related signal is present in child tongue ultrasound images, but the paper is an exploratory regression study rather than an SSI system contribution.

### Prior state of the art

Ultrasound tongue imaging in SSI work is usually used for articulatory analysis, speech therapy, or articulatory-to-acoustic mapping rather than demographic regression.

### What changed

Recasts ultrasound tongue imaging as a speaker-age regression problem and treats age as a hidden signal in articulatory images.

### Position in the field

Adjacent ultrasound analysis paper outside the core SSI pipeline literature.

### Practical value

Useful if a speech-therapy workflow wants age-sensitive ultrasound analysis, but not useful as a communication interface result.

### Advanced

analysis; evaluation

### Unresolved

generalization; adult speakers; cross-site robustness

### Evaluation details

| Item | Details |
| --- | --- |
| Task | age estimation from ultrasound tongue images |
| Input | ultrasound tongue image |
| Body site | tongue |
| Output | age labels |
| Metrics and results | Validation MSE 2.03 on UXTD with random rotation; validation MSE 4.87 on UPX; mean-age baselines 3.64 and 5.35 |
| Evaluation protocol | validation MSE comparison on UXTD and UPX child cohorts against mean-age baselines |

### Limits

- **Technical:** Small child-only datasets, low-SNR ultrasound, and no evidence beyond two UltraSuite cohorts limit the result.
- **Evaluation:** The reported success is validation-set regression error only; there is no external dataset or deployment test.
- **Deployment:** No interface, runtime, or user-facing system is built.
- **Scope of this review:** Exploratory age estimation from tongue ultrasound rather than silent speech.

### Evidence

- The paper explores whether speaker age can be inferred from ultrasound tongue imaging using a deep convolutional neural network. (Abstract)
- For typically developing children, the minimum validation MSE is about 2.03, compared with a mean-age baseline of 3.64. (4.4. Experiments Results for Typically Developing Children)
- The authors state the ultrasound dataset is much smaller than speech-based age datasets and that performance needs validation on larger data. (5. Conclusions)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
