# Vid2speech: Speech Reconstruction from Silent Video

Ariel Ephrat, Shmuel Peleg  
arXiv / imported corpus page 2017 · [arXiv](https://arxiv.org/abs/1701.00495)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

Vid2speech reconstructs intelligible speech from silent face video on GRID with speaker-specific models and LPC-style resynthesis, reaching about 80% human intelligibility and partial out-of-vocabulary recovery.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (GRID face video, 25 fps) |
| Task | Speech synthesis from silent video |
| Vocabulary | 51 words (GRID grammar) |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 82.6% audio-only intelligibility (S4) vs 40.0% prior work; OOV 51.6% vs 10% chance |

**Limitations.** Speaker-specific training, constrained GRID grammar, unnatural-sounding resynthesis, and a small listening study without open-vocabulary or live testing.

## Full review

### In short

Real lip-to-speech progress, still tightly benchmark-bounded.

### Review

The full text backs a stronger claim than the abstract-only version. On the constrained GRID setup, reconstructed speech becomes much more intelligible than prior work: Table 2 shows 82.6% audio-only intelligibility on S4 and about 80% audio-visual intelligibility on S4 and S2, versus 40.0% and 51.9% in the cited baseline. The OOV experiment is also real rather than decorative: Table 3 reports 51.6% accuracy when two digits are held out of training, far above the 10% chance rate. The limits are equally clear: speaker dependence, LPC-like synthesis artifacts, and a fixed 51-word grammar keep this from being a practical open-world SSI.

### Why it matters

The paper is an early but real lip-to-speech milestone: within GRID, silent video can drive intelligible reconstructed speech and even partial OOV recovery.

### Prior state of the art

Most visual silent-speech work focused on recognition rather than direct speech reconstruction, and earlier reconstruction quality was substantially lower.

### What changed

The paper models automatic speechreading as regression to acoustic features and shows materially improved human intelligibility, including a held-out-digit OOV test.

### Position in the field

Important early visual speech-reconstruction paper in SSI-adjacent lip-to-speech research.

### Practical value

High as a proof of concept for lip-to-speech generation, though still too constrained for open deployment.

### Advanced

problem framing; evaluation; speech reconstruction

### Unresolved

speaker independence; naturalness; unconstrained vocabulary and capture

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | silent face video |
| Sensor | 25 FPS, 720x576 video from the GRID audiovisual corpus |
| Body site | face / lips |
| Output | speech audio |
| Vocabulary type | GRID sentence grammar |
| Vocabulary size | 51 words |
| Metrics and results | Table 2 reports 82.6% audio-only intelligibility for S4 and 79.9% / 79.0% audio-visual intelligibility for S4 / S2, compared with 40.0% audio-only and 51.9% audio-visual in prior work [10]. Table 3 reports 51.6% OOV audio-visual intelligibility versus 10.0% chance and 93.4% when no digits are held out. |
| Evaluation protocol | Human intelligibility studies on reconstructed audio-only, audio-visual, and out-of-vocabulary settings using MTurk listeners. |

### Limits

- **Technical:** The system depends on speaker-specific training, a constrained GRID grammar, and an LPC-style resynthesis path that still sounds unnatural.
- **Evaluation:** Evidence is limited to GRID and a relatively small listening study rather than an open-vocabulary or in-the-wild evaluation.
- **Deployment:** No live camera-to-audio system or user-facing deployment is shown.
- **Scope of this review:** Constrained lip-to-speech reconstruction study.

### Evidence

- The paper presents an end-to-end CNN-based model that generates an intelligible audio signal directly from silent video of a speaking person and shows promising results for out-of-vocabulary words. (Abstract)
- The main reconstruction experiment uses the 1000 videos of speaker S4 from GRID, while the corpus as described here contains 51 words and fixed 3-second clips. (4.2. Sound prediction tasks)
- Table 2 reports 82.6% audio-only intelligibility for speaker S4 and 79.9% / 79.0% audio-visual intelligibility for speakers S4 / S2, versus 40.0% audio-only and 51.9% audio-visual in prior work [10]. (Table 2. Our reconstructed speech is significantly more intelligible than the results of [10].)
- Table 3 reports 51.6% OOV audio-visual intelligibility, compared with 93.4% when no digits are held out and 10.0% chance. (Table 3. Out-of-vocabulary (OOV) intelligibility results.)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
