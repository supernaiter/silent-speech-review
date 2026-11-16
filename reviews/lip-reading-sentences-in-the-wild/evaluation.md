# Evaluation: "Lip Reading Sentences in the Wild" review

Date: 2026-11-16. Independent evaluator, single pass. Input: the compact review only (no claim table, no sources opened). Checks rely on the review's internal consistency and on the evaluator's knowledge of the literature. A note of "insufficient evidence" means the claim could not be confirmed without its quote and locator. It does not mean the claim is wrong.

## Claim table

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Lipreader 73.8% WER vs machine 50.2% WER | Verdict; "Where the claims outrun" | correct | Matches the target's reported lips-only best and the professional's result (about 26% of words correct). |
| 2 | Lipreader saw the full face and the programme context, and had about ten times the clip length (§5.2) | Outrun list | correct | Consistent with the target's description of the human protocol. |
| 3 | 73.8% excludes declined clips; 87.6% with them | Outrun list | insufficient evidence | No quote available. Plausible, but it carries the "margin does not hold" position. |
| 4 | Machine also learned from 342,644 audio-only sentences | Outrun list | insufficient evidence | Needs locator. The same corpus underlies the 96.5% vocabulary-overlap argument in M11. |
| 5 | Curriculum 76.5% to 61.1% WER (15.4 points) | Verdict; M03 | insufficient evidence | The arithmetic is consistent (76.5 - 61.1 = 15.4). Table values not verified. |
| 6 | LRW 23.8% vs 38.9% error; GRID 3.0% vs LipNet 4.8% (overlapped-speaker split) | M06 | correct | 38.9% is the earlier LRW result from the same group. LipNet's 4.8% is the overlapped split (11.4% unseen speakers). |
| 7 | Clean AV 17.7% to 13.9%; Kaldi audio-only 16.8%; 0 dB 62.9% to 42.0% | Outrun list | insufficient evidence | Values are plausible. The inference drawn from them is too strong (see fix 4). |
| 8 | CER 16.2→13.3 in CVF §5.1 text vs 10.4→7.9 in Table 5; LRW 400k vs 450k utterances | Outrun list | insufficient evidence | A useful inconsistency finding if the quotes support it. "CER is defined over words" is unclear (fix 6). |
| 9 | Beam width 4, no external LM | Table M07 | correct | Consistent with the target. |
| 10 | 120 px mouth crop, 25 Hz video, MFCC audio | Table M05 | correct | |
| 11 | LRS vocabulary 17,428 words; test 6,882 words, of which 6,641 (96.5%) appear in the audio-only text | M11 | correct (arithmetic); insufficient evidence (source) | 6,641/6,882 = 96.5%. The review does not say whether these are word types or tokens. |
| 12 | LRS itself was never released; its pipeline became LRS2-BBC and LRS3-TED | Verdict; M11 | correct | Consistent with the Deep AVSR paper and the LRS3 release. |
| 13 | arXiv v2 promises a data release; the CVF version drops it | Outrun list | insufficient evidence | Needs both quotes. |
| 14 | LSVSR: attention 76.8% vs CTC 40.9% WER | Verdict | number plausible; framing wrong | The models differ in more than the decoder (fix 1). |
| 15 | LSVSR professionals 86.4% and 92.9% WER | M12 | correct | 92.9% without context, 86.4% with context. |
| 16 | WAS scored 70.4% on LRS2-BBC [3] | M06 | correct | Matches the Deep AVSR comparison table. |
| 17 | VTP 22.6% LRS2, 30.7% LRS3 WER (2022) | M06 SOTA | number correct; not the state of the art | Better and more recent results exist (fix 2). |
| 18 | VTP keeps only sub-sequence augmentation and attributes the gain to it, not to ordering | Verdict; M03 SOTA | insufficient evidence | This claim decides the M03 verdict. A quote and locator are needed (fix 8). |
| 19 | Makin et al. cortical decoding dropped the attention | M06 | correct | The Nature Neuroscience encoder–decoder used no attention. |
| 20 | Usual approach in 2016: classifiers or CTC (LipNet) | M06 | correct | |
| 21 | GRID 51 words; LRW 500 words | M11 | correct | |
| 22 | LRS is the first in-the-wild sentence set of five | M11 | insufficient evidence | The deciding distinction from Miao and Metze's YouTube data is not stated (fix 5). |
| 23 | First of seven to test a professional on in-the-wild sentences | M12 | plausible | LSVSR (later) is the main follow-up. No earlier counterexample known. |
| 24 | Jain and Harte (2026): 65% vs 83% WER on identical material | M12 SOTA | insufficient evidence | Recent preprint; could not be checked. |
| 25 | Ref 11: LRW in ACCV 2016, LNCS 10111 | References | wrong (likely) | The DOI 978-3-319-54184-6 is ACCV 2016 Part II, which is LNCS 10112 (fix 7). |

## Required fixes (ordered by impact)

1. **Sentence:** "The decoder is standard: LAS carried over from ASR, later beaten by CTC on fixed data, 76.8% against 40.9% WER [4]."
   **What is wrong:** The LSVSR comparison holds the data fixed, not the decoder alone. V2P predicts phonemes with CTC and decodes through a large finite-state language model. It also has a different visual front end. The 76.8% attention model differs in output unit, front end and decoding as well, so the gap cannot be credited to CTC. The M06 section itself says "Method and data scale stay confounded", and "What the field needs next" asks for decoders "on identical data", which contradicts this sentence.
   **Fix:** "The decoder is standard: LAS carried over from ASR. On the same LSVSR data, a phoneme-CTC system with an external language model later reached 40.9% WER against 76.8% for an attention model [4], but output units, front end and decoding differ, so the decoder's share of the gap is unknown."

2. **Sentence:** "**State of the art:** Transformer decoders with CTC or sub-word outputs, e.g. VTP [5] (2022, 22.6% LRS2 and 30.7% LRS3 WER); WAS itself scored 70.4% on LRS2-BBC [3]."
   **What is wrong:** VTP is no longer the state of the art. Hybrid CTC/attention Conformer models report far lower visual-only WER. Examples are Auto-AVSR (Ma et al., ICASSP 2023), about 19% on LRS3 and about 15% on LRS2, and the LP-Conformer of Chang et al. (ICASSP 2024), about 12.8% on LRS3. LLM-based decoders (2024–2025) report comparable or lower values. The table row "Transformer (2022)" repeats the error.
   **Fix:** Cite a 2023–2025 hybrid CTC/attention or LLM-decoder result, with its year, test set and reported WER as given in its source. Update the M06 table cell to match. VTP can stay as the sub-word example.

3. **Sentences:** "36 confirmed works use it on non-audio input: none prior or concurrent, 35 later" (M06, verdict "standard"); "18 confirmed works use the curriculum: none prior or concurrent, 17 later" (M03, verdict "standard"); "M11 is its lasting contribution" (Verdict) against the M11 table verdict "not reported".
   **What is wrong:** The review's own ledger shows no prior or concurrent non-audio use of either M06 or M03. That is the evidence pattern for `ahead`, yet both are labelled `standard` without a stated rule. M03 gives no reason at all; M06 gives only "carried over from ASR". M11 is called the paper's lasting contribution in the Verdict, but its slot verdict is "not reported", which reads as a contradiction. M12 has the same mismatch.
   **Fix:** For M06 and M03, either assign `ahead` with the ledger count, the deciding priors and the repeated effect, or add one clause each giving the verdict rule that makes them `standard`. For example: "standard: imported unchanged from audio ASR (LAS; curriculum from ASR training), so not new to the field's method stock." For M11 and M12, either change the verdict or define "not reported" in a short note so it does not contradict "lasting contribution".

4. **Sentence:** "**\"Lips help on clean audio\"** rests on 17.7% to 13.9% WER, but retrained Kaldi reaches 16.8% on audio alone; noisy tests (62.9% to 42.0% at 0 dB) reuse the training SNRs with the noise type unstated."
   **What is wrong:** 13.9% is still below the stronger Kaldi audio-only 16.8%, so the claim's direction survives. The weak audio baseline inflates only the size of the gain. As written, the bullet implies the claim fails.
   **Fix:** "**\"Lips help on clean audio\"** holds in direction (13.9% WER against 16.8% for retrained Kaldi), but the reported 3.8-point gain is measured against a weaker 17.7% audio-only baseline; noisy tests (62.9% to 42.0% at 0 dB) reuse the training SNRs with the noise type unstated."

5. **Sentence:** "LRS is the first in-the-wild sentence set (17,428 words) of five confirmed."
   **What is wrong:** This is a novelty claim, but the sentence before it names concurrent Miao and Metze [12], who used in-the-wild YouTube sentence video. The deciding distinction is not stated: a lip-reading benchmark with mouth crops versus AVSR data without them, and size. Earlier broadcast-TV visual speech corpora are not ruled out by name.
   **Fix:** "LRS is the first in-the-wild sentence set built for visual-only lip reading (mouth-cropped, 17,428 words) of five confirmed; Miao and Metze [12] used YouTube sentences for AVSR without mouth crops." Name any earlier broadcast sentence corpus the ledger contains.

6. **Sentence:** "CVF §5.1 text gives CER 16.2% to 13.3%, Table 5 10.4% to 7.9%; CER is defined over words; Table 3 gives LRW 400,000 (arXiv v2) or 450,000 (CVF) utterances."
   **What is wrong:** "CER is defined over words" is unclear. A reader cannot tell whether the paper's formula normalises character edits by word count, or whether the text confuses CER with WER. The point the review draws from it is also not stated.
   **Fix:** State the exact defect with its locator. For example: "the CER formula in §5 normalises character edits by the number of words in the ground truth, so CER and WER are not on comparable scales." If that is not what the source says, quote the definition.

7. **Sentence (reference 11):** "*Proc. Asian Conference on Computer Vision (ACCV 2016), LNCS 10111*, 2016, 87–103. doi:10.1007/978-3-319-54184-6_6."
   **What is wrong:** The DOI prefix 978-3-319-54184-6 belongs to ACCV 2016 Part II, which is LNCS 10112. LNCS 10111 is Part I. (Confidence: medium.)
   **Fix:** Change to "LNCS 10112" after confirming against the DOI landing page.

8. **Sentence:** "**State of the art:** VTP [5] (2022) keeps only sub-sequence augmentation and states the gain comes from it, not from ordering." (also in the Verdict: "later attributed to sub-sequence augmentation [5]")
   **What is wrong:** This attribution carries the M03 verdict, but the review gives no locator. The evaluator's recollection is that VTP still trains with a length-based schedule over sub-sequences, so "keeps only augmentation" may overstate what VTP says. A design choice in one later paper is also not a state-of-the-art training result.
   **Fix:** Quote VTP's sentence with its section number. If VTP does not explicitly credit augmentation over ordering, write: "VTP [5] (2022) trains on random sub-sequences and the target itself suggests the curriculum 'presumably' acts as augmentation (§3.1); no work has separated the two." Then soften the Verdict sentence to match.

## Scores

- Procedure: 6/10. The components are compared against the field, and absence claims name counts. However, verdict labels do not follow from the review's own absence evidence, and the M06 state of the art is out of date.
- Final text: 6/10. The text is precise and well located on the target's numbers and inconsistencies. One central sentence attributes a multi-factor gap to the decoder, one bullet overstates, and one sentence is unclear.

Strengths (brief): the human-comparison critique is careful and well located; the vocabulary-overlap computation is a useful and checkable point; the version differences (arXiv v2 vs CVF) are documented.
