# Speech Synthesis from Text and Ultrasound Tongue Image-based Articulatory Input

Tamas Gabor Csapo, Laszlo Toth, Gabor Gosztolya, Alexandra Marko  
arXiv / imported corpus page 2021 · [arXiv](https://arxiv.org/abs/2107.02003)

**Section:** [Ultrasound & tongue imaging](../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text

Limited-data TTS augmented with ultrasound tongue images; combined text plus ultrasound gives the lowest test MCD for all 8 speakers, while ultrasound-only input remains far worse.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Micro ultrasound system with probe-fixing headset |
| Task | Speech synthesis from text plus ultrasound |
| Vocabulary | Not applicable |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Test MCD 5.442 (text+ultrasound) vs 5.652 (text-only) vs 7.153 (ultrasound-only), speaker 03mn |

**Limitations.** Not a standalone SSI: best system still needs text input; speaker-dependent, limited data, sensitive to probe misalignment, and no listening tests.

## Full review

### In short

Helpful side information, not standalone SSI.

### Review

The paper earns its improvement claim. For every speaker in Table 1, the combined text-plus-ultrasound system beats text-only MCD by a small but consistent margin, which is exactly what you want from side information in a limited-data setup. But the same full text also states the system is not suitable for direct SSI because the best pipeline needs both text and articulatory input, and probe misalignment remains a serious failure mode.

### Why it matters

The full text supports a narrower claim than the title suggests: the best system is not a standalone SSI but a text-to-speech system helped by ultrasound side information under limited data.

### Prior state of the art

Articulatory-to-speech work usually used ultrasound alone, while DNN-TTS usually used text alone.

### What changed

Combines conventional text-side linguistic features with ultrasound-derived articulatory features inside one DNN-TTS pipeline.

### Position in the field

Adjacent articulatory-synthesis paper relevant to SSI but not itself a complete silent-speech interface.

### Practical value

Useful when limited-data TTS can exploit synchronized articulatory recordings to improve spectral prediction.

### Advanced

system design; limited-data synthesis analysis

### Unresolved

speaker independence; direct SSI without text; probe-robust capture

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech synthesis from text plus ultrasound articulatory input |
| Input | text and ultrasound tongue images |
| Sensor | Articulate Instruments Micro ultrasound system with probe-fixing headset |
| Body site | tongue |
| Output | speech audio |
| Metrics and results | Combined text plus ultrasound yields the lowest test MCD for all 8 speakers, for example 5.442 for 03mn and 5.236 for 06fe versus 5.652 and 5.447 for text-only; ultrasound-only remains far worse at 7.153 and 7.050 |
| Evaluation protocol | 8-speaker dev/test evaluation with MCD, BAP, F0-RMSE, F0-CORR, F0-VUV and probe-misalignment analysis |

### Limits

- **Technical:** Speaker-dependent training, limited data, and sensitivity to probe misalignment constrain the result.
- **Evaluation:** All evidence is speaker-dependent offline synthesis metrics without listening tests.
- **Deployment:** The best system still requires text input and a probe-mounted headset.
- **Scope of this review:** Articulatory-augmented TTS, not pure silent-speech reconstruction.

### Evidence

- The study extends traditional vocoder-based DNN-TTS with articulatory input estimated from ultrasound tongue images and compares text-only, ultrasound-only, and combined inputs. (Abstract)
- For every reported speaker in Table 1, the combined text-plus-ultrasound system has lower test MCD than text-only, for example 5.442 versus 5.652 for 03mn and 5.236 versus 5.447 for 06fe. (Table 1: MCD errors on the dev/test set.)
- The transducer-position analysis shows several speakers have clearly separated test utterances in the misalignment matrix, and those speakers also show higher MCD errors. (4. Effect of ultrasound transducer position)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
