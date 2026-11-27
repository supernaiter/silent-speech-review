# Triage of the independent evaluation (13 fixes)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | EUSIPCO 2004 Table 2 (naist-4544): NAM microphone with audible speech 93.8 to 93.2 / 92.9, close-talking 94.4 to 91.7 / 91.9; different speech mode, model and session from the target. | M12 section: both rows reported, "no smaller" removed; states it supports the sensor, not murmur. Verdict no longer uses the cross-condition comparison. |
| 2 | applied | Graciarena 2004 Sec. 1 "Preliminary results were published in [4]" and ref. [4] (IEEE SPL 10(3), March 2003); SPECOM 2005 (naist-4825) Sec. 1 and refs. [7], [8] (throat microphone and PARAT earplug, ASRU 2003); DOIs confirmed by Crossref. Zheng et al. ASRU 2003 is detection and enhancement (title and SPECOM description), no recognizer: excluded. | M05 usual approach (prior 4: authors' NAM 2, throat 1, earplug 1); M12 usual approach and dated counts (prior 4); Appendix lists both as described through citations; audits updated. |
| 3 | applied | Before 2004-03 the NAM microphone and murmur recognition appear only in the authors' 2003 reports (Appendix dated counts). | Verdict: design credited to the authors' 2003 reports; "standard" because one speaker gives no repetition; Appendix states the 2003-04 first public date of the design and why the target is dated 2004-09. verdict.json synced. Verdicts unchanged. |
| 4 | applied | Re-tally of the 82 ledger candidates: 38 NAM-related; of the other 44, 19 record a site, 13 of them neck (slot-filled). | M05 usual approach and Appendix. |
| 5 | applied | ASRU 2003 Sec. 3.1 (monophone iterative MLLR 71.09%, 200 utterances) and Sec. 3.2 (unadapted normal-speech PTM -0.81%). | M03 section rewritten; unadapted-baseline question removed. |
| 6 | partly applied | Itoh, Takeda, Itakura ASRU 2001 verified as a whisper recognizer through Tatara 2002 ref. [5] and Crossref; its task scale and transfer method are not stated in citing text. ASJ March 2003 (target ref. [8]) is a same-group abstract of the 2003 design and is covered by the 2003 study. Jorgensen 2003 and Sugie 1985 not added: no verifiable source in hand. | M04 prior count 5 (whisper 2); M03 lists Itoh 2001 as unclassified. |
| 7 | applied | naist-4824 (sOc-EUSAI, Oct. 2005): 93.9%, 20K, 350 training and 48 test utterances, male speaker. No higher NAM dictation word accuracy among the audited sota candidates. | State-of-the-art lines dated 2005 with conditions; Verdict limited to "among the audited studies". |
| 8 | applied | Audits describe the counts as full-text mentions (upper bounds). | M12 and M03 Appendix lines and M12 usual approach labelled as mention counts. |
| 9 | applied | Whisphone Sec. 2.2-2.3 (notes w2-w3). | M12 state of the art and table cell: fixed phrases, off-the-shelf recognizers, one speaker, earbud. Yang et al. ISCSLP 2012 not used: values unverified. |
| 10 | applied | EURASIP 2007 Sec. 3.1-3.2; SPECOM 2005 Sec. 5 (Lombard). | Verdict gives 83.7% start, silicone microphone, female speaker, 100 adaptation utterances; claims section credits superimposed-noise result and Lombard attribution. |
| 11 | applied | Tatara Sec. 5.3 says "recognition rate"; training/test speaker disjointness not stated. | M04: "recognition rate", "4 test speakers", "speaker-independent" dropped. |
| 12 | applied | Target Sec. 3.3; ICASSP 2003 Sec. 6 "open test". | M05 credits Sec. 3.3; test-independence bullet credits the open test and limits overlap to row D. |
| 13 | applied | verdict.json position aligned with the md Verdict; B-D descriptions are in Sec. 3.6. | verdict.json; claims section location. |

Counts: 12 applied, 1 partly applied, 0 rejected. Verdict changes: none.
