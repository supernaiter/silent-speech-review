# Evaluation: Decoding speech perception from non-invasive brain recordings

Date: 2026-11-16. Independent evaluator, one pass. Inputs: the compact review and its claim table only. No source was re-opened; checks are against the claim-table quotes and locations, the review's internal consistency, and the evaluator's own knowledge of the literature (marked "knowledge").

## Claim check

| # | Claim (section, first words) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Verdict, "The paper [1] changes the decoding objective..." | Claim 1 quote (Abstract) | correct | Abstract names contrastive objective, pretrained speech representations, common subject architecture, 175 volunteers. |
| 2 | Verdict, "M06 and M03 were ahead of the field: no earlier M/EEG study in the ledger has either design" | M06 section, claim 5; knowledge | wrong | The M06 section itself names an earlier EEG contrastive study [7]. Known earlier EEG designs that discriminate matched vs mismatched speech segments exist (match/mismatch paradigm). Subject embeddings were used earlier in MEG by the same group (see fixes 1, 2). |
| 3 | Verdict, "both effects repeat across four datasets and three seeds" | Claims 6, 11 quotes | wrong | Brennan: base 6.0 ± 0.9 vs +CLIP 8.0 ± 4.8 (within noise). Broderick: without subject layer 20.2, above the 17.7 of the full model in Table 2. No quote supports "three seeds". |
| 4 | Verdict, "on EEG the pretrained target beats a learned Mel encoder by less than one standard deviation" | Claim 15 quote | wrong | True for Brennan (25.7 ± 2.9 vs 24.7 ± 3.2) only; Broderick is 17.7 ± 0.6 vs 15.4 ± 1.6, a gain larger than either SD. |
| 5 | Verdict, "every test participant is also in training" | Claim 26 quote; M12 section | insufficient evidence | Plausible (segment-level splits), but the code location (bm/dataset.py) has no claim-table row and no quote. |
| 6 | M06 usual approach, 538 studies, classification 98, regression 71 | Claims 3, 28 | correct (ledger count, not re-checked) | Out of scope for count audit. |
| 7 | M06 state of the art, 70.7% top-10 of 1,363 on Gwilliams | Claim 4 quote | correct | Numbers match Table 1 and Table 2. "2022" is the dataset/preprint year; the paper is 2023. "Remains the reference" is not backed by any search statement. |
| 8 | M06 SOTA, [later] 2024 76.0% top-10 of 512 with 175 h EEG [6] | Claim 14 quote | correct | 76.0 in quote; "512" and "calls this paper the prior EEG state of the art" have no quote. |
| 9 | M06, "the one dated earlier contrasts EEG trials of six fixed words" [7] | Claim 5 quote | correct for [7] | But "the one" implies a single earlier contrastive study, contradicting row 2 framing; match/mismatch EEG–speech work predates the target (knowledge). |
| 10 | M06, "contrastive loss alone lifts top-10 from 12.4% to 55.1%" on Gwilliams | Claim 6 quote | correct | Third column. |
| 11 | M06, "[later] cross-subject work keeps the same loss [8]" | Claim 7 quote | insufficient evidence | Quote shows wav2vec targets, not the loss. |
| 12 | M03 usual approach: per-subject 90, subject layers 34, "the earliest being this paper" | Claims 8, 32; knowledge | wrong (novelty) | Subject embeddings in a pooled MEG deep model predate the target: Chehab et al., "Deep Recurrent Encoder", arXiv:2103.02339 (2021). |
| 13 | M03, closest earlier design pooled subjects, LOSO [9] | Claim 9 quote | correct | [9] is motor imagery, not speech; the review should say so. |
| 14 | M03 SOTA: 61.3/43.0/39.9 vs 17.4/20.8/17.7 [8] | Claim 10 quotes | correct | Both triples are in the quotes. |
| 15 | M03, "Removing the subject layer costs 14.4 top-10 points on average" | Claim 11 quote | correct | 14.4 is in the row; per-dataset effect is not uniform (row 3). |
| 16 | M03, "no enrolment is defined (§2.2.2)" | Claim 12 quote | insufficient evidence | §2.2.2 quote only defines the subject layer; an absence claim needs a statement of what was searched. |
| 17 | M03, "with 2.9 h from one participant ... 10.5% top-10 of 190 segments [6]" | Claim 12 quote | wrong / insufficient | Quote gives 10.5% of 190 and 1.40% of 1,842, but not "2.9 h", "one participant" or "top-10". 190 and 1,842 are the Brennan and Broderick test sets, which are multi-participant. |
| 18 | M02 SOTA: wav2vec 2.0 76.0 vs Encodec 60.4 vs Whisper 52.9 [6] | Claim 14 quote | correct | |
| 19 | M02 verdict standard, based on lip reading [2], [3] | Claims 2, 13 | judgment weak | The M/EEG usual approach the section states is Mel/envelope; "standard" rests on a different modality. Acceptable only if stated as such. |
| 20 | M12 usual approach: LOSO in 75, "at least three earlier than this paper [9]" | Claim 16 | insufficient evidence | Only one work cited, and it is motor imagery. |
| 21 | M12 verdict "behind" | M03 and M12 counts | wrong (internal contradiction) | Review's own counts: per-subject models (90) outnumber LOSO (75); within-participant testing is the usual design, so "behind" does not follow. |
| 22 | M12 SOTA: 21 of 47 subjects above chance [8] | Claim 17 quote | correct | |
| 23 | Outrun, §1 reports 72.5% of 1,594 and 19.1% of 2,604 | Claims 18, 19, 25 | correct, framing incomplete | Numbers match §1 quote. These are the figures of the arXiv v1 abstract (2022) (knowledge); the likely explanation is a carry-over from v1, which the review should say instead of "no dataset matches" alone. |
| 24 | Outrun, "EEG is quoted without chance (Table 2)" | Claim 20 quote | wrong | The quote itself is Table 2's "Random model" row (5.3, 0.5, 0.7, 0.8). Chance is in Table 2. Ratios 4.8x and ~35x are arithmetically fine (17.7/0.5; with exact 10/1,842 = 0.54% it is ~33x). |
| 25 | Outrun, words absent from training (A.7); "Zero-shot holds for MEG only" | Claim 21 quote | partly wrong | Numbers match. Schoffelen MEG (73.4 to 61.6) omitted. EEG unseen-word accuracy remains above chance (Brennan 9.7 vs 5.3; Broderick 8.0 vs 0.5), so "holds for MEG only" overstates. |
| 26 | Outrun, clamping: "top-10 falls to 0.5% on Broderick" | Claim 24 quote | wrong | 0.5 is the first column, which is Brennan (same column order as 25.7 Brennan / 17.7 Broderick). Broderick without clamping is 14.1. |
| 27 | Outrun, matched MEG–EEG 30.3/31.7 and invasive 72.5 vs 74 | Claims 22, 23 | correct | Both are caveats the authors concede; the review attributes them, which is fair, but the Verdict then lists "parity with invasive decoders" as an overclaim the authors did not fully make. |

## Required fixes (ordered by impact)

1. Sentence: "M06 and M03 were ahead of the field: no earlier M/EEG study in the ledger has either design (Appendix), and both effects repeat across four datasets and three seeds."
   What is wrong: the M06 section names an earlier EEG contrastive study [7], so "no earlier M/EEG study has either design" contradicts the review. Earlier EEG work already discriminated matched from mismatched speech segments (match/mismatch paradigm, e.g. Monesi et al., ICASSP 2020, "An LSTM based architecture to relate speech stimulus to EEG"; Accou et al., 2021, dilated-convolution match/mismatch). The "repeat" clause is wrong too (fix 3).
   Fix: narrow the novelty to "contrastive alignment of M/EEG with a pretrained speech representation over open candidate sets", name [7] and the match/mismatch priors as the deciding earlier designs, and say why they differ (binary match/mismatch with envelope vs ranking >1,000 segments).

2. Sentence: "subject-specific layers appear in 34, the earliest being this paper."
   What is wrong: a pooled MEG deep model with a learned subject embedding predates the target (Chehab et al., "Deep Recurrent Encoder: an end-to-end network to model magnetoencephalography at scale", arXiv:2103.02339, 2021, same group).
   Fix: drop "the earliest being this paper", cite the earlier subject-embedding work, and either downgrade M03 from "ahead" or state what is new (a per-subject linear layer after spatial attention at 175-participant scale).

3. Sentence: "both effects repeat across four datasets and three seeds."
   What is wrong: on Brennan the contrastive loss moves top-10 from 6.0 ± 0.9 to 8.0 ± 4.8 (within noise); on Broderick, removing the subject layer gives 20.2, higher than the full model's 17.7 in Table 2. No quote supports "three seeds".
   Fix: "both effects are clear on the two MEG datasets; on EEG they are small or absent (Brennan for the loss, Broderick for the subject layer)", and drop "three seeds" unless a quote is added.

4. Sentence: "Verdict: behind." (M12) and the table row "LOSO (75) ... behind".
   What is wrong: the review's own counts show per-subject models (90) are more common than LOSO (75), so within-participant testing is the usual design; "behind" does not follow from the evidence given.
   Fix: change to "standard" and keep the limitation ("no participant-disjoint test, so the subject layer was never tested on a new person") as a weakness, not as a lag behind the field.

5. Sentence: "Without clamping, top-10 falls to 0.5% on Broderick (Table 3)"
   What is wrong: 0.5 is the Brennan column; Broderick without clamping is 14.1.
   Fix: "Without clamping, top-10 falls to 0.5% on Brennan and 1.5% on Gwilliams (Table 3)".

6. Sentence: "EEG is quoted without chance (Table 2): Brennan's 25.7% faces 190 candidates and 5.3% chance"
   What is wrong: Table 2 contains a Random model row (5.3, 0.5, 0.7, 0.8), which is the very quote used.
   Fix: "The EEG headline figures in the text are given without chance, although Table 2 lists it: Brennan's 25.7% faces 5.3% chance (about 4.8 times), Broderick's 17.7% faces about 0.5% (about 33 times)."

7. Sentence: "on EEG the pretrained target beats a learned Mel encoder by less than one standard deviation" (Verdict) and "Here the gain over Deep Mel is 70.7% against 64.4% on Gwilliams but 25.7 ± 2.9% against 24.7 ± 3.2% on Brennan EEG" (M02).
   What is wrong: holds for Brennan only; on Broderick EEG wav2vec 2.0 gives 17.7 ± 0.6 against 15.4 ± 1.6.
   Fix: "on Brennan EEG the gain is within one standard deviation (25.7 ± 2.9 vs 24.7 ± 3.2); on Broderick it is 17.7 ± 0.6 vs 15.4 ± 1.6", and re-justify "standard" on the lip-reading precedent alone, stating it is a cross-modal precedent.

8. Sentence: "with 2.9 h from one participant, the same pipeline gave 10.5% top-10 of 190 segments [6]."
   What is wrong: the quote supports 10.5% of 190 and 1.40% of 1,842 but not "2.9 h", "one participant" or "top-10"; 190 and 1,842 are the target's Brennan and Broderick multi-participant test sets.
   Fix: quote the passage in [6] that gives the training amount and metric, or reduce to "[6] reports 10.5% of 190 and 1.40% of 1,842 segments when its pipeline was run on the target's EEG datasets".

9. Sentence: "Zero-shot holds for MEG only; the EEG drop is about three quarters (inference)." and "'Zero-shot' here means unseen segments, not unseen people."
   What is wrong: EEG accuracy on unseen words stays above chance (Brennan 9.7 vs 5.3; Broderick 8.0 vs about 0.5), so "MEG only" overstates; the second MEG dataset (73.4 to 61.6) is omitted. No location shows the authors claimed zero-shot for unseen people, so the M12 line answers a claim the paper may not make.
   Fix: "On unseen words EEG keeps only about a quarter of its accuracy, though still above chance; MEG keeps 91% (Gwilliams) and 84% (Schoffelen)". For M12, quote where the paper uses "zero-shot" and say it refers to unseen segments/words; drop the "unseen people" contrast unless the paper implies it.

10. Sentence: "Leave-one-subject-out testing appears in 75 cross-subject studies (pattern match, Appendix), at least three earlier than this paper [9]"
    What is wrong: "at least three" is backed by one citation, and [9] is motor imagery, not speech.
    Fix: name the three earlier works, or write "including one earlier MEG/EEG motor-imagery study [9]".

11. Sentence: "§1 reports 72.5% top-10 of 1,594 segments (MEG) and 19.1% of 2,604 (EEG); Table 2 gives 70.7% of 1,363 and 17.7% of 1,842. No dataset in Tables 1–2 matches."
    What is wrong: the numbers are right, but they are the arXiv v1 (2022) abstract figures; presenting the mismatch as unexplained misses the likely cause.
    Fix: add "these are the arXiv v1 figures, retained in the journal introduction after the splits changed".

12. Sentence: "here blocks are split inside each recording (code, bm/dataset.py)" and "no enrolment is defined (§2.2.2)".
    What is wrong: the code location has no claim-table row or quote; the §2.2.2 quote only defines the subject layer and does not support an absence claim.
    Fix: add a claim-table row with the code passage that assigns splits, and either quote a passage where the paper discusses new participants or rephrase to "the paper does not describe how a new participant would be added".

## Scores

- Procedure: 6/10. Claim table is complete for most numbers, but several key statements (seeds, code split, [6] training amount) have no quote, and novelty checks did not catch same-group and match/mismatch priors.
- Final text: 5/10. Clear positions and good use of Table 3 and A.7, but a column mix-up, a contradicted "without chance" claim, two over-general EEG statements and an M12 verdict that contradicts the review's own counts.
