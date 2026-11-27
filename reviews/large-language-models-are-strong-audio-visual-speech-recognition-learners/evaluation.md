# Evaluator: a language model separate from the writer

Date: 2026-11-27. Target: Cappellazzo et al., "Large Language Models are Strong Audio-Visual Speech Recognition Learners" (Llama-AVSR), arXiv:2409.12319 (v1 2024-09-18; v2 2025-03-07), ICASSP 2025.
Inputs checked: `compact.md`, the review `.md`, `slots.json`, `verdict.json`, `claims.md`, the three topic audits and `tools/*_2024-09.json`. Sources read: wiki `papers/arxiv-2409.12319/source/text.txt` (v2), `papers/arxiv-2402.15151/source/text.txt` (VSP-LLM v2), `papers/arxiv-2406.10082/source/text.txt` (Whisper-Flamingo v3), `papers/isca-rouditchenko24_interspeech/source/sc_text.txt` (Interspeech version), `papers/arxiv-2503.11315`, `papers/arxiv-2605.28456`, `papers/arxiv-2607.29112`. I also fetched arXiv v1 of the target and of Whisper-Flamingo, and the arXiv submission histories, to settle the version questions. The wiki and review files were not modified.

Version dates (arXiv submission histories): target v1 2024-09-18, v2 2025-03-07. VSP-LLM v1 2024-02-23 (prior, about 7 months earlier). Whisper-Flamingo v1 2024-06-14, v2 2024-11-07, v3 2024-11-19. MMS-LLaMA v1 2025-03-14.

## Claim table

| # | Claim (location in review) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | VSP-LLM: LoRA-tuned LLaMA2-7B, linear projector, token reduction (Verdict, M06) | VSP-LLM Sec. 4.2 l.436-442; Sec. 1 l.102 | correct | QLoRA rank 16; "single linear layer"; deduplication of clustered visual speech units cuts length by about 50%. That is content-adaptive merging, not the fixed-rate pooling the target uses (K = 3). |
| 2 | VSP-LLM(FT) 25.4% vs Llama-AVSR 25.3% at 433 h (Verdict, bullet 1) | VSP-LLM Table 1 l.520 (pre-train 1,759 h, labelled 433 h); target Table I (AV-HuBERT V, 48M, 433 h, 25.3) | correct (numbers); "matched" overstated | Both use AV-HuBERT Large pre-trained on 1,759 h and 433 labelled hours. VSP-LLM(FT) unfreezes the whole visual encoder after 18K steps (l.448-450), also trains on translation (VST), and decodes with beam 20. Llama-AVSR adds a rank-64 LoRA (about 6M) to the encoder and uses beam 15. Call it the closest configuration, not a matched one. |
| 3 | Table I lists VSP-LLM at 26.7% (bullet 1) | target Table I (v1 and v2) | correct | VSP-LLM is prior work, so leaving out the 25.4% row is a fair criticism. |
| 4 | "rests on 0.1 points at 433 hours (28.4% against 29.8% at 30 hours)" (bullet 1) | target Table I 30 h row 28.4; VSP-LLM Table 1 30 h row 29.8 | numbers correct; sentence self-contradictory | At 30 h the margin is 1.4 points in the target's favour, so the claim does not rest only on 0.1 points. |
| 5 | 0.77% "sits 0.01 points from the 0.76% of the [concurrent] Whisper-Flamingo" (Verdict) | WF v3 Table 3 l.322; WF v1 Table 3; Interspeech Table 3 | wrong framing (chronology and condition) | 0.76% is not in WF v1 (2024-06) or in the Interspeech paper, where the best AVSR figure is 1.5% at 433 labelled hours and no 1,759-h labelled row exists. It first appears in v2/v3 (Nov 2024), two months after the target's v1. It is also "w/o noise, Beam 1". The noise-trained figure is 0.86% at beam 1 and 2.0% at beam 15. |
| 6 | "at the target's time, Whisper-Flamingo (2024) reported 0.76%" (M12 State of the art) | same as #5 | wrong | At the target's first public date (2024-09) Whisper-Flamingo reported 1.5% (433 h). |
| 7 | Table I omits WF's 0.76% / 0.86% at 1,759 h; "the 0.77% leads only the latter" (bullet 2) | target Table I (v1, v2) row "Whisper-Flamingo [47] 631 433 1.5"; WF v3 l.322, 327 | numbers correct; framing unfair for v1 | The rows did not exist when v1 was posted. A fair criticism is that v2 (2025-03) did not update them. The noise-trained row is the closer match to Llama-AVSR's noise-augmented training, and the target leads it (0.77 vs 0.86). |
| 8 | 2.3% Whisper fine-tuning row = Whisper-Large, noise, beam 15, "matching Llama-AVSR's own setup" (M03) | WF v3 Table 3 l.326; target Sec. III-A (babble from NOISEX at SNR uniform over {-5,...,20, ∞}; beam 15, temperature 0.6) | partly correct | Numbers are right. "Matching" is overstated: WF adds 0-dB babble, Llama-AVSR samples SNRs including clean, Whisper-Large vs Whisper-medium, temperature differs. |
| 9 | Whisper-FT without noise, greedy: 1.0% / 0.68%, below 1.1% / 0.79% (M03) | WF v3 Table 3 l.320; target Table I | numbers correct; later evidence | These rows exist only from WF v2/v3 (Nov 2024). The review leaves out WF's noise-trained greedy row (1.1% / 0.85%, l.325). That row shows beam search alone moves 2.3% to 1.1%, and that with noise training the target's 0.79% still beats 0.85%. |
| 10 | Whisper encoder "saw 680k hours of speech" (M03) | WF Sec. 1 l.56; target ref [39] | correct but understated | Whisper's 680k hours are weakly labelled (transcribed) hours. That is the real problem with a "Labeled Hours" column of 433, and the review should cite Whisper itself (target ref [39]). |
| 11 | 42M trainable excludes the frozen 8B decoder (M03) | target Table I ("Trainable Par. (M)"), Sec. III-A (LoRA about 27M, projectors about 15M) | correct | The column header says "trainable", so this is an inference-cost omission (M13), not a mislabel. |
| 12 | 0.79% → 0.77%, about 2.5% relative (M12) | target Table I; Sec. III-B l.367 | correct; not credited | The authors state this themselves: "the gain is reduced when more data are available (0.79%→0.77%)". v1 gave 0.81% → 0.77%. |
| 13 | 0.95% at 433 h is above LP Conformer's 0.9% (bullet 3) | target Table I (LP Conformer 570M, 100K h, 0.9; ViT3D-CM 90K h, 1.6) | correct; condition missing | The authors' sentence cites [7] and [8]. 0.95% beats [7] (1.6%) but not [8]. At 1,756 h, 0.77% beats both. |
| 14 | §III-B reverses 1.5% / 1.1% for 433 h / 30 h (bullet 4) | target Sec. III-B vs Table I (v1 and v2) | correct | |
| 15 | VSR trails BRAVEn 20.1%; authors concede (bullet 5) | target Table I; Sec. IV; Sec. III-B "the gap with methods like RAVEN and BRAVEn is more noticeable" | correct | Credited. The concession is also in Sec. III-B. |
| 16 | DoubleHelix 0.68% at 1,759 h; 12% lower (M06 State of the art) | DoubleHelix l.32, 136, 502; frozen Whisper-medium + AV-HuBERT, LoRA LLaMA-3.2-3B (l.228-229, 259-262) | correct | Single-author arXiv v1 (2026-07), not peer reviewed. Condition: clean. Arithmetic: 0.09 / 0.77 = 11.7%. |
| 17 | DLLM-VSR 19.4% at 433 labelled hours (M06 State of the art) | DLLM-VSR Table l.387 | correct; condition missing | Uses the USR 2.0 encoder pre-trained on 3,305 h. With the same AV-HuBERT encoder (1,759 h) it reaches 21.9% (l.386). The same table lists Yuan et al. (ICCV'25), AV-HuBERT + Llama3-8B, 22.0% at 433 h (l.384). |
| 18 | MMS-LLaMA "applies QLoRA to LLaMA 3.1 8B ... reaches 0.72%" (M03 State of the art) | MMS-LLaMA Table 1 l.506-507; Sec. 4.2.2 l.520-522 | wrong | The 0.72% row uses LLaMA 3.2 3B. The 8B results in that table are Llama-AVSR's own (0.95 / 0.77). |
| 19 | Concurrent: 7 of 50 name an LLM decoder; SynesLM OPT, Personalized LR LLaMA3-8B, MMS-LLaMA 86% (M06) | M06 audit dated counts (9 hits, 7 kept; WF and a cued-speech MLLM excluded with reasons); quotes c18, c19, c14 | correct | |
| 20 | Prior counts: 55 hybrid / 407; LLM decoder 1 (M06) | M06 audit; tools/m06_llm_2024-09.json | tally correct; framing weak | See fix M3. |
| 21 | Prior counts: 193 end-to-end, 17 frozen, 3 LoRA (M03) | M03 audit, design_regex | tally correct; label overstated | The end-to-end regex is `end[- ]to[- ]end`, which matches architecture descriptions and related-work mentions, not a training regime. |
| 22 | At least 143 of 182 prior AVSR studies report no run variability (M12) | M12 audit target block (182 minus 39 hits) | correct as a lower bound | Labelled "pattern match" and "at least". The variability regex includes "standard deviation", which also matches input normalisation (the target itself has "dividing by the standard deviation", Sec. III-A), so 39 is inflated, as stated. LRS3 subset: 51, of which 9 have a hit. |
| 23 | Authors do not acknowledge VSP-LLM (implied by Verdict "already decoded ... seven months earlier") | target Sec. I l.60-66, Sec. III-B "the only prior LLM-based method", refs [31]-[36] | insufficient credit | The authors present Llama-AVSR as extending LLM-ASR [31]-[35] and VSP-LLM [36]. They do not claim the decoder design is new. |

## Required fixes, ordered by impact

1. **High: Verdict sentence 3, M12 "State of the art", bullet 2, Question 2. Chronology of the Whisper-Flamingo 0.76%.**
   - Evidence: WF arXiv v1 (2024-06-14) and the Interspeech 2024 paper have one AVSR row, 1.5% clean at 433 labelled hours. There is no 1,759-h labelled row and no 0.76%. The 0.76% / 0.86% / 0.68% rows first appear in v2 (2024-11-07) and v3 (2024-11-19), after the target's v1 (2024-09-18). The target's Table I cites WF at 1.5% in both v1 and v2.
   - Fix: drop "at the target's time, Whisper-Flamingo reported 0.76%". Reframe the SOTA criticism as later evidence: "two months after the target's v1, Whisper-Flamingo's revision reported 0.76% (v3, Table 3), and the target's v2 (2025-03) kept 'two new SOTA' without updating that row". Reword Question 2 to "Why did v2 not add Whisper-Flamingo's November 2024 1,759-hour rows?". The VSP-LLM(FT) half of the question is fair as written.
2. **High: Verdict sentence 3 ("strongest overreach") and bullet 2. Condition mismatch on 0.76%.**
   - Evidence: 0.76% is "Fine-tuned w/o noise, Beam 1" (WF v3 l.322). With beam 15 the same model gives 1.8%. The noise-trained model gives 0.86% at beam 1 and 2.0% at beam 15 (l.327-328). Llama-AVSR trains with babble augmentation and decodes with beam 15 (Sec. III-A).
   - Fix: state the conditions. Under the closer-matched condition (noise-trained) the target's 0.77% beats Whisper-Flamingo's 0.86%. The remaining point is single runs against margins of 0.01 to 0.09 points. Either demote this from "strongest overreach" or put the VSP-LLM(FT) omission (prior work, fair) first.
3. **High: M03 "State of the art" and slots M03 `sota`. Wrong LLM for MMS-LLaMA.**
   - Evidence: MMS-LLaMA Table 1 gives 0.72% for "Whisper AV-HuBERT LLaMA 3.2 3B, 1759" (l.507). Sec. 4.2.2 lists 1B, 3B and 8B variants.
   - Fix: "applies QLoRA to LLaMA 3.2 3B (Sec. 4.2.2-4.2.3, Table 1)". You may add that it uses fewer LLM parameters than the target's 8B.
4. **Medium: M03 paragraph 3. Whisper fine-tuning rows are later evidence, and "matching Llama-AVSR's own setup" is overstated.**
   - Evidence: the 1.0% / 0.68% and 1.1% / 0.85% rows are in WF v3 only. The original 2.3% row (v1 and Interspeech) uses 0-dB babble, Whisper-Large and beam 15. Llama-AVSR samples SNR uniformly with clean included, uses Whisper-medium, and decodes with temperature 0.6.
   - Fix: replace "matching" with "close to". Mark the 1.0% / 0.68% rows as reported in November 2024. Add the noise-trained greedy row (1.1% / 0.85%): beam size alone accounts for most of the 2.3% vs 1.1% gap, while the target's 0.79% still beats the noise-trained 0.85%.
5. **Medium: M03 paragraph 3. The labelled-hours point is understated.**
   - Evidence: Whisper's 680k hours are transcribed (weakly supervised) data (target ref [39], Radford et al.). Table I counts 433 labelled hours for every Whisper row. The authors claim to outperform "methods that exploit tens of thousands of hours [7], [8]" (100K and 90K labelled hours).
   - Fix: write "680k hours of weakly labelled speech" and cite Whisper. Connect it to the "tens of thousands of hours" sentence: the target's audio encoder saw more labelled audio than LP Conformer's 100K hours.
6. **Medium: M06 "Usual approach", Verdict "the field's hybrid CTC/attention decoder", slots M06 `field`. Denominator and family framing.**
   - Evidence: 55 of 407 is 14%. No counts are given for the other decoder families (CTC-only, attention encoder-decoder, transducer), so "usual" is not shown. The 407 population (VSR/AVSR plus WER|CER|accuracy) includes word-level classification studies with no sequence decoder, outside the Appendix's stated "sentence-level" setting. "trained end to end with its encoder" is not part of the regex.
   - Fix: give the other family counts from the same audit, or write "the most-named decoder family in the ledger (55 of 407 prior studies, pattern match; other families not counted)". Drop "trained end to end" or support it with a count.
7. **Medium: M03 "Usual approach" and slots M03 `field`. "End-to-end training" label.**
   - Evidence: the regex `end[- ]to[- ]end` matches "end-to-end AVSR" as an architecture term and in related-work text.
   - Fix: "193 of 407 mention end-to-end or full fine-tuning (pattern match, upper bound)".
8. **Medium: Verdict sentence 2 and M06 "Verdict: standard; the deciding prior has the design". Incomplete deciding priors and missing credit.**
   - Evidence: VSP-LLM is video-only. The audio and audio-visual parts follow LLM-ASR designs the target cites as its basis (Sec. I; [33] SLAM-ASR, arXiv 2402.08846; [35] Fathullah et al., arXiv 2307.11795; [34] Yu et al., arXiv 2309.13963). These lie outside the VSR/AVSR ledger. The authors name VSP-LLM themselves as "the only prior LLM-based method" (Sec. III-B).
   - Fix: name the LLM-ASR priors next to VSP-LLM, and state that the paper's novelty is putting both modalities into one frozen LLM, which neither prior does. Under the rule that is still `standard` (`ahead` would also fail: single runs, one dataset). Say that the authors cite VSP-LLM as their predecessor, so this is not the reviewer's discovery. Also note that VSP-LLM reduces tokens by unit deduplication, not fixed-rate pooling.
9. **Medium: M12 "State of the art" and slots M12 `sota`. Wrong kind of state of the art.**
   - Evidence: M12 is the evaluation protocol, but the line gives a WER (0.68%). The M12 audit already holds a protocol state of the art: arxiv-2602.19316, LRS3 AVSR mean ± SD over three seeds (2.9 ± 0.1).
   - Fix: give the best protocol (seeds or intervals on LRS3 AVSR), with year and form. You may keep a pointer to 0.68% as the accuracy frontier.
10. **Medium: M03 "State of the art". Not the current best with the same regime.**
    - Evidence: DoubleHelix (2026, [later]) keeps Whisper-medium and AV-HuBERT frozen and trains fusion plus LoRA on LLaMA-3.2-3B (l.228-262, 505), reaching 0.68% at 1,759 h. That is better than MMS-LLaMA's concurrent 0.72%.
    - Fix: make DoubleHelix the M03 state of the art and keep MMS-LLaMA as the [concurrent] reference point.
11. **Medium: M06 "State of the art" (VSR). DLLM-VSR condition.**
    - Evidence: 19.4% uses the USR 2.0 encoder pre-trained on 3,305 h. With AV-HuBERT (the target's encoder) it reaches 21.9%. The same table lists Yuan et al. (ICCV'25), AV-HuBERT + Llama3-8B, at 22.0%.
    - Fix: "19.4% with a 3,305-h pre-trained USR 2.0 encoder; 21.9% with the target's AV-HuBERT encoder, both at 433 labelled hours (DLLM-VSR Table 1)".
12. **Medium: bullet 1. Self-contradictory margin, and "matched".**
    - Evidence: 28.4% vs 29.8% at 30 h is a 1.4-point margin. VSP-LLM(FT) differs in encoder tuning (full vs LoRA), extra VST training and beam size (see claim table #2).
    - Fix: "the claim holds by 1.4 points at 30 h (VSP-LLM's 30-h row is not in Table I) and by 0.1 points at 433 h against VSP-LLM(FT), the closest configuration, which Table I leaves out". Use "closest" in the Verdict too.
13. **Low: M12 verdict sentence. Uncredited caveat.**
    - Evidence: Sec. III-B: "the gain is reduced when more data are available (0.79%→0.77%)".
    - Fix: "as the authors note (Sec. III-B), adding video at 1,756 h moves 0.79% to 0.77%". Keep the single-run point as the reviewer's own.
14. **Low: bullet 3. Condition and scope.**
    - Fix: add "(570M parameters, 100K labelled hours)". Say the sentence holds against ViT3D-CM [7] (1.6% at 90K h) and at 1,756 h, and fails only against LP Conformer [8] at 433 h.
15. **Low: reference [1] / M03 / M12. Version drift.**
    - Evidence: v1 reports ASR 0.81% (Abstract, Sec. III-B). v2 reports 0.79%.
    - Fix: one clause noting that the values are from v2 and that v1 gave 0.81% for ASR.
16. **Low: M03 "Usual approach" last sentence. Inconsistent with Sec. III-A.**
    - Evidence: for VSR, a rank-64 LoRA (about 6M) is added to AV-HuBERT, so the encoder is not fully frozen. Bullet 1 relies on that.
    - Fix: "keeps the encoders frozen (LoRA on AV-HuBERT for VSR only)".
17. **Low: M12 "Usual approach". Off-population denominator.**
    - Evidence: the 182 prior AVSR studies include non-LRS3, digit and word tasks. The audit has a closer denominator: 51 LRS3 studies, 9 with a variability hit.
    - Fix: add "on LRS3, at least 42 of 51 (pattern match)" next to the 143 of 182.
18. **Low: References.**
    - Evidence: the chronology tags are duplicated ("[later] [later]", "[concurrent] [concurrent]") in [3]-[8]. [3] gives Interspeech as the venue, but every number cited comes from arXiv v3, which differs from the Interspeech text. DoubleHelix [4] is a single-author, unrefereed arXiv v1.
    - Fix: remove the duplicate tags. In [3], write "values from arXiv:2406.10082v3 (2024-11-19); not in the Interspeech version". In [4], note "preprint, v1".

Additional state-of-the-art candidates: I know of no named LRS3 AVSR result below 0.68% that I can locate with a value and year. Treat this as unverified, not as a required fix.

## Praise (brief)

The VSP-LLM(FT) omission, the reversed 1.5% / 1.1% pairing in Sec. III-B, the 0.95% vs LP Conformer point and the 42M-trainable vs 8B-frozen point all check out against the sources. The Appendix counts are honestly labelled as pattern matches with upper and lower bounds.

## Scores

- Procedure: 7/10. Deciding prior read, tallies labelled, and comparator quotes are accurate. But no Whisper-Flamingo version check, and two state-of-the-art lines are on the wrong kind of evidence for their slot.
- Final text: 6/10. The central overreach rests on a value published after the target and measured under a different condition, and one comparator's LLM is wrong.

Counts by severity: High 3, Medium 9, Low 6.
