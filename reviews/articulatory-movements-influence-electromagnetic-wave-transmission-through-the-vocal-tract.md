# Articulatory movements influence electromagnetic wave transmission through the vocal tract

Remi Blandin, Martin Laabs, Rudolf von Bunau, Bryn Lloyd, Silvia Farcito, Denys Nikolayev, Gabriela Hossu, Peter Birkholz, Dirk Plettemeier  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2604.19362)

**Section:** [Radar, RF & Wi-Fi](../README.md#radar-rf--wi-fi) · **Review basis:** full_text+summary

Physical modeling and measurement of contact RF transmission through the vocal tract for three sustained vowels in two participants; simulations qualitatively agree with measurements below about 3 GHz.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Two cheek-mounted bow-tie antennas with lab VNA; MRI models |
| Task | Physical modeling of articulatory RF sensing |
| Vocabulary | 3 sustained vowels (/a/, /i/, /u/) |
| Speaker | Not stated |
| Session | Not applicable |
| Online / offline | Not applicable |
| Key result | Between-vowel transmission differences up to 15 dB near 1.5 GHz; repetition variation ~5-10 dB |

**Limitations.** Only two participants and three vowels; agreement mainly qualitative with no error metric; no recognition system, wearable device or patient use.

## Full review

### In short

A useful two-person physical model of contact-RF articulation sensing; qualitative agreement below about 3 GHz does not establish recognition accuracy or general-user robustness.

### Review

This paper is valuable as a physical explanation and simulation study for contact-RF silent speech sensing. It builds MRI-derived head geometries for three sustained vowels in two male participants and compares HFSS simulations with repeated scattering-matrix measurements from cheek-mounted antennas. The clearest result is qualitative agreement in transmission magnitude and some vowel-dependent spectral structure up to roughly 2-3 GHz; measurements above 3 GHz become too noisy to validate the detailed simulated patterns. The observed transmission differences between vowels can reach about 15 dB, whereas repeat variation is typically about 5 dB and sometimes 10 dB. These contrasts support articulation sensitivity, but they are not classification accuracy. In particular, the 99.17% recognition rate in Figure 1 belongs to a cited earlier study and must not be assigned to this paper. The field maps suggest that internal resonances, external scattering and antenna positions jointly shape the spectrum; they do not isolate tongue motion as the sole signal source. Several modeling choices are informed by the experimental response, including replacing unsegmented fat-like tissue with muscle-like properties and selecting a 1 micrometre antenna gap. Thus, agreement is partly calibration rather than an independent prospective prediction. Different MRI protocols, supine-versus-seated posture, missing anatomy, and tissue-property approximations limit precision. The work supplies a useful basis for studying antenna placement and anatomy effects, but further participants, controlled gesture perturbations, quantitative error analysis and an actual model-guided recognition experiment are needed to show practical SSI improvement.

### Why it matters

Makes the RF transmission mechanism inspectable and offers an anatomy-aware basis for future hardware optimization beyond trial-and-error recognition studies.

### Prior state of the art

Earlier contact-RF SSI studies demonstrated recognition from transmission spectra and optimized antennas empirically. Distant radar primarily senses external motion; contact antennas aim to improve coupling into tissue.

### What changed

Relates measured vowel-dependent transmission spectra to simulated internal resonances and external scattering patterns instead of treating the RF signal solely as a learned recognition feature.

### Position in the field

Physical foundations and sensor design for contact-RF articulatory SSI, rather than a speech-decoding benchmark.

### Practical value

Supports hypotheses about antenna location, usable bandwidth, anatomy effects and future controlled simulation studies; demonstrated improvement to recognition remains absent.

### Advanced

Physical interpretability of contact RF sensing, anatomy-specific modeling, and a simulation route for future antenna and frequency-band design.

### Unresolved

Quantitative predictive error, new-subject prediction, dynamic gestures, independent internal-versus-external motion contributions, and actual recognition gains from model-guided design.

### Narrowed or regressed

No matched end-to-end system comparison. Detailed anatomical modeling introduces substantial preparation and simulation complexity.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Physical modeling of articulatory RF sensing |
| Input | Contact radio-frequency transmission between cheek-mounted antennas; MRI supplies offline anatomical models. |
| Sensor | Two bow-tie antennas, conductor dimensions 27 mm by 11.5 mm on 0.8 mm FR4, taped near the mouth corners. Subject 1: Rohde & Schwarz ZVL6 VNA; Subject 2: Keysight M9374A in M9005A chassis. 3T MRI supplies anatomical geometry. |
| Body site | face; oral-cavity; tongue |
| Output | Reflection/transmission spectra and simulated electric-field distributions; no decoded speech output. |
| Vocabulary type | Static articulatory configurations, not a recognition vocabulary |
| Vocabulary size | 3 sustained vowel configurations (/a/, /i/, /u/); no word vocabulary. |
| Metrics and results | Measurements sweep 1-6 GHz at -10 dBm VNA output. Repetition variation is typically around 5 dB and reaches 10 dB; some between-vowel differences reach 15 dB near 1.5 GHz. Simulated transmission is generally of similar magnitude below 2-3 GHz, except Subject 1 /i/ is about 10 dB lower than measured. No new recognition accuracy, WER, latency or global simulation-error metric is reported. Separate simulations at 0.5 W input report approximately 17-40 W/kg over 10 g and 51-280 W/kg over 1 g across 1-6 GHz; these are model estimates at a different power from the experiments, not device certification. |
| Evaluation protocol | Same-subject comparison of measured and simulated reflection/transmission spectra and inspection of simulated electric fields; numerical RF absorption estimates. |

### Limits

- **Technical:** Model omits cables and balun, approximates unsegmented tissues as muscle, flattens local cheek surfaces and uses a fitted 1 micrometre antenna gap. Missing/cropped anatomy and posture mismatches affect agreement. Minima can depend on both internal and external fields and on moving antenna geometry.
- **Evaluation:** Only two male participants and three sustained vowels, with three RF repetitions per condition. Agreement is principally qualitative; no global prediction-error score, uncertainty interval, or held-out anatomy validation is reported. Tissue assignment and antenna gap are adjusted using the measured response. Above 3 GHz, measurement noise prevents useful comparison of spectral minima.
- **Deployment:** Two adhesive cheek antennas are connected to laboratory vector network analyzers. No complete wearable recognizer, live communication loop, mobility test, or patient use is evaluated.
- **Scope of this review:** Static sustained vowel production and same-person numerical/experimental comparison; not continuous silent speech decoding, speaker identification, or clinical rehabilitation testing.

### Evidence

- Two male participants, aged 54 and 33, provide MRI geometries for sustained /a/, /i/ and /u/. RF measurements use the same subjects and three repetitions per vowel, while MRI and RF acquisition differ in posture and institution. (Sections II-B and II-E; PDF pp. 3-5; Discussion p. 12)
- A custom CGAL-based MRI-to-surface-mesh workflow enables HFSS anatomical electromagnetic models, compared with measured scattering matrices and inspected through simulated electric fields. (Sections II-F and II-G; Figures 4 and 8-10; PDF pp. 5-10)
- Two cheek-mounted bow-tie antennas measure 1-6 GHz scattering matrices using vector network analyzers at -10 dBm output. The study does not train a speech recognizer. (Sections II-D and II-E; PDF pp. 4-5; Results pp. 6-11)
- Transmission magnitude is generally comparable below about 2-3 GHz, except the Subject 1 /i/ simulation is about 10 dB below measurement. Repetition variation is typically around 5 dB and can reach 10 dB; vowel differences can reach 15 dB near 1.5 GHz. (Section III; Figures 6 and 7; PDF pp. 7 and 10)
- Above 3 GHz, excessive measurement noise prevents meaningful comparison of the spectral minima. Some measured minima are absent in the corresponding simulations even below this range. (Section III and Discussion; PDF pp. 10 and 12)
- Unsegmented tissue initially modeled as fat was changed to muscle because it better matched measurement magnitude. An antenna-to-head gap of 1 micrometre was selected by parametric analysis to match reflection magnitude. Reviewer assessment: these are measurement-informed calibration choices. (Section II-G; PDF p. 6)
- Field maps relate transmission minima and maxima to local fields at antenna locations; internal resonances, external scattering and their combination can all contribute. Reviewer assessment: the results do not isolate tongue motion alone. (Section III and Discussion; Figures 8-10; PDF pp. 8-13)
- The 99.17% command-word recognition rate illustrated in Figure 1 is attributed to Wagner et al. 2022. The present paper validates a physical model and does not supply a new recognition accuracy. (Figure 1 and Introduction; PDF p. 2; Results and Conclusion pp. 6-14)
- Absorption simulations use 0.5 W input, separately from -10 dBm experimental measurements. Reported 10 g averages rise from about 17 to 40 W/kg, and 1 g averages from about 51 to 280 W/kg, over 1-6 GHz. Reviewer assessment: these are model-specific numerical results, not certification of a deployed device. (Section II-G and Section III; PDF pp. 6 and 11)
- The authors identify missing/cropped anatomy, segmentation and tissue-property approximations, antenna-position mismatch, posture and articulation variability as discrepancy sources, and call for a larger and more diverse participant sample. (Discussion and Conclusion; PDF pp. 11-14)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
