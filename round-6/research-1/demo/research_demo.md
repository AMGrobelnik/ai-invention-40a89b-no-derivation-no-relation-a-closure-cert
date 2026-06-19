# No-Derivation Abstention vs Confidence Family; NeSy Reposition; Re-DocRED Absent Gold

## Summary

Pure-web research bundle ($0) for iter-6/iter-7 of the closure-certificate project, across three workstreams. (A) Pins the confidence/uncertainty selective-prediction family our STEP-A battery competes against -- verbalized confidence [Lin2022; Tian2023], self-consistency [Wang2023], P(True)/P(IK) [Kadavath2022], semantic entropy [Kuhn2023; Farquhar2024], SelfCheckGPT [Manakul2023], the abstention survey [Wen2024], learned temporal abstention [Zhou2026], and the adversarial internal-state-probe neighbour [Song2026] -- with verified BibTeX, per-method abstention signals + verbatim quotes, a paper-ready signals-vs-catches table, and a ~250-word drop-in differentiation paragraph arguing every signal is dispersion/confidence-driven and therefore BLIND to a confident, self-consistent absent-relation hallucination, whereas the certificate abstains STRUCTURALLY (no derivation path) regardless of confidence -- with honest scope (confidence baselines tie at matched coverage on ordinary uncertain deduction). (B) A timing-aware (as-of 2026-06-18) NeSy / qualitative-reasoning venue shortlist -- Neurosymbolic AI journal (rolling, the only open NeSy-family target now), NeSy 2026/2027, *SEM, KR 2026 (qualitative reasoning in scope), STRL, EMNLP/ARR -- a crisp 'why not ACL Knowledge Extraction' statement, and a recommendation to SWAP primary<->fallback. (C) Verifies Re-DocRED (tonytan48/Re-DocRED, arXiv:2205.12696, 2022.emnlp-main.580, MIT, splits 3,053/500/500, '~64.6% of triples missing' in original DocRED, recall 32.07->69.40), confirms kinship coverage (P22/P25/P26/P40/P3373 PRESENT; P1038 ABSENT), documents the false-negative pitfall + disconnected-component absent-gold methodology, and scouts alternative natural hosts (CustFRE = natural prose with explicit no_relation gold; KinshipQA = generated/synthetic, fails the natural bar). Directly retires the reviewer novelty MAJOR + venue MINOR and de-risks iter-7 STEP-B.

## Research Findings

This research supplies the two contribution-defining moves the empirical artifacts cannot themselves produce, plus the methodology that de-risks iter-7's single open experiment.

(A) NOVELTY. The entire confidence/uncertainty selective-prediction family -- verbalized confidence [1,3], self-consistency/vote-margin [5], P(True)/P(IK) [6], semantic entropy [7,8], and SelfCheckGPT [9], with surveys framing abstention as a confidence-threshold decision [11] and even learned temporal abstention trained on answer-level uncertainty -- shares one structural property: every signal is a monotone function of the model's prediction DISPERSION or self-assessed confidence. By construction it reads 'certain' on a CONFIDENT, self-consistent absent-relation hallucination (verbalized confidence high, samples agree, P(True) high, semantic entropy LOW, SelfCheckGPT consistent) and therefore KEEPS it. Our certificate is orthogonal: it abstains because no derivation path exists after composing per-edge reads through the EXACT relation algebra -- gold-free, training-free, confidence-independent. The adversarial check confirms even internal-state probes are 'ineffective on logic-intensive tasks where models are confidently wrong' [12], and they remain learned/answer-level rather than a per-edge structural test [28]. The drop-in differentiation paragraph + signals-vs-catches table become the paper's novelty backbone; scope is kept honest (confidence baselines tie at matched coverage on ordinary uncertain deduction).

(B) VENUE. We recommend SWAPPING the original plan's primary<->fallback: make a neuro-symbolic / qualitative-reasoning venue PRIMARY and an LLM/KE (ACL/EMNLP) track only a fallback, because the contribution is a deduction/consistency CERTIFICATE that inverts the F1-maximising commit contract, not extraction (atomic F1 ~0.534 is measured, not improved). As of 2026-06-18 nearly all 2026 conference deadlines are past (NeSy-2026 research tracks [14], *SEM-2026 [16], KR-2026 [17], STRL-2026 [18], EMNLP-2026 ARR [19]); the only immediately actionable NeSy-family target is the rolling Neurosymbolic AI journal [15], with NeSy 2027 / KR 2027 / *SEM 2027 as the conference cycle.

(C) NATURAL ABSENT-RELATION HOST. Re-DocRED [20,21,22] is the right host: original DocRED is ~64.6% false-negative so its un-annotated pairs are NOT 'no relation', whereas Re-DocRED is exhaustive-within-schema (MIT; train 3,053/dev 500/test 500). All five core kinship relations are present (P22/P25/P26/P40/P3373) and P1038 'relative' is absent [24]. Build absent gold from DISCONNECTED kinship components (truthful 'no relation' by structure), restricted to the closed kinship sub-schema. CustFRE [26] adds a natural secondary host with explicit no_relation gold (atomic arm); KinshipQA [25] is generated (fails the natural bar). This de-risks iter-7 STEP-B: certificate vs confidence-thresholded abstainer at matched coverage on a natural no-derivation stratum.

## Sources

[1] [Teaching Models to Express Their Uncertainty in Words (Lin, Hilton, Evans, TMLR 2022)](https://arxiv.org/abs/2205.14334) — Primary abstract page: verified title/authors/year; 'verbalized probability' -- model emits a stated confidence level mapped to a calibrated probability. Anchors the verbalized-confidence baseline (high confidence => keep).

[2] [Lin et al. 2022 on OpenReview (TMLR venue confirmation)](https://openreview.net/forum?id=8s8K2UZGTZ) — Confirms the paper was published in Transactions on Machine Learning Research (TMLR) 2022; OpenReview id 8s8K2UZGTZ -- used to pin the venue in BibTeX.

[3] [Just Ask for Calibration (Tian et al., EMNLP 2023)](https://arxiv.org/abs/2305.14975) — Primary abstract page: 'verbalized confidences emitted as output tokens are typically better-calibrated than the model's conditional probabilities'. Verbalized-confidence elicitation baseline; abstain only when score is low.

[4] [Just Ask for Calibration -- ACL Anthology (EMNLP 2023)](https://aclanthology.org/2023.emnlp-main.330/) — Anthology landing page confirming anthology id 2023.emnlp-main.330, title and the 8-author list (Tian, Mitchell, Zhou, Sharma, Rafailov, Yao, Finn, Manning).

[5] [Self-Consistency Improves Chain of Thought Reasoning (Wang et al., ICLR 2023)](https://arxiv.org/abs/2203.11171) — Primary abstract page: majority vote over multiple sampled reasoning paths; agreement is the selection/confidence signal -> grounds the self-consistency/vote-margin abstainer (agreement => keep).

[6] [Language Models (Mostly) Know What They Know (Kadavath et al., 2022)](https://arxiv.org/abs/2207.05221) — Primary abstract page: P(True) self-evaluation and P(IK) ('probability I know'); the paper itself notes P(IK) calibration 'struggles on new tasks'. Grounds the P(True) baseline and part of the adversarial check.

[7] [Semantic Uncertainty (Kuhn, Gal, Farquhar, ICLR 2023)](https://arxiv.org/abs/2302.09664) — Primary abstract page: semantic entropy over meaning-clustered samples; LOW entropy => trust, HIGH entropy => flag. CRUX: a confident, self-consistent hallucination has LOW entropy and is kept.

[8] [Detecting hallucinations in LLMs using semantic entropy (Farquhar et al., Nature 2024)](https://www.nature.com/articles/s41586-024-07421-0) — Nature 630(8017):625-630, doi:10.1038/s41586-024-07421-0. Semantic entropy detects 'confabulations' (arbitrary/incorrect generations) -- an uncertainty signal that targets high-entropy outputs, not confident ones. (Page is paywalled; metadata/claim cross-checked with the Kuhn 2023 ICLR version.)

[9] [SelfCheckGPT (Manakul, Liusie, Gales, EMNLP 2023)](https://arxiv.org/abs/2303.08896) — Primary abstract page: 'if an LLM has knowledge of a given concept, sampled responses are likely to be similar and contain consistent facts ... for hallucinated facts ... diverge'. Consistency=>factual => a consistent hallucination passes.

[10] [SelfCheckGPT -- ACL Anthology (EMNLP 2023, pp. 9004-9017)](https://aclanthology.org/2023.emnlp-main.557/) — Anthology landing page confirming id 2023.emnlp-main.557 and page range 9004-9017 for the pinned BibTeX.

[11] [Know Your Limits: A Survey of Abstention in LLMs (Wen et al., TACL 2024)](https://arxiv.org/abs/2407.18418) — Primary PDF (grepped): framework of three perspectives -- query (answerability), model (confidence c(x,y)), human values; 'Current methods to encourage abstention typically rely on calibration techniques'; abstain when 'a confidence score ... falls below some threshold'. Frames the whole family as confidence/calibration-driven.

[12] [Hallucination Detection via Internal States and Structured Reasoning Consistency (Song et al., 2026)](https://arxiv.org/abs/2510.11529) — ADVERSARIAL anchor (grepped abstract): names the 'Detection Dilemma' and states 'Internal State Probing is ineffective on logic-intensive tasks like mathematical reasoning where models are confidently wrong'. Confirms even internal-state probes miss confident-coherent hallucinations; still learned/answer-level, not a structural per-edge certificate.

[13] [NeSy 2026 conference site](https://2026.nesyconf.org/) — 20th Intl Conf on Neural-Symbolic Learning and Reasoning; FCUL, Lisbon, 1-4 Sep 2026; accepted papers eligible for a Neurosymbolic AI journal special issue.

[14] [NeSy 2026 Call for Papers (raw)](https://raw.githubusercontent.com/nesyconf/nesy2026/main/callforpapers.md) — Important dates: Phase-1 abstract 24 Feb / paper 3 Mar 2026; Phase-2 abstract 9 Jun / submission 16 Jun 2026; Industry submission 17 Jul 2026. Full papers <=10 pp, short <=5 pp; OpenReview; NAI-journal special issue. (As of 2026-06-18 the research-track windows have just closed.)

[15] [Neurosymbolic Artificial Intelligence journal (IOS Press/SAGE) -- About](https://neurosymbolic-ai-journal.com/content/about-neurosymbolic-artificial-intelligence) — Open-access, transparently peer-reviewed, CONTINUOUS (rolling) publication journal -- the only NeSy-family venue with an immediately actionable deadline as of June 2026; active X-NeSy and Neurosymbolic-Generative-Models special issues.

[16] [*SEM 2026 Call for Papers (ACL portal)](https://www.aclweb.org/portal/content/call-papers-sem2026-15th-joint-conference-lexical-and-computational-semantics-san-diego-ca) — 15th Joint Conf on Lexical and Computational Semantics, San Diego, one-day 3 Jul 2026, co-located ACL 2026; DIRECT submission (not ARR), deadline 13 Feb 2026 (past); notification 5 May 2026. => *SEM 2027 next cycle.

[17] [KR 2026 -- 23rd Intl Conf on Principles of Knowledge Representation and Reasoning](https://kr.org/KR2026/) — Lisbon, 20-23 Jul 2026 (FLoC 2026); main-track abstract 8 Feb 2026 (past). Topics EXPLICITLY include 'Qualitative reasoning', 'Geometric/spatial/temporal reasoning', 'Reasoning in knowledge graphs'. Ideal-fit but currently closed => KR 2027.

[18] [STRL 2026 -- 5th Workshop on Spatio-Temporal Reasoning and Learning](https://strl-workshop.github.io/strl2026/) — Co-located IJCAI-ECAI 2026, Bremen, 16 Aug 2026; submission 24/25 May 2026 (past), notification 10 Jun 2026; NON-ARCHIVAL; 8/4/2-page formats; 'Neuro-symbolic approaches to spatio-temporal reasoning' in scope.

[19] [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/) — Budapest, 24-29 Oct 2026; fed by ARR May-2026 cycle (ARR submission 25 May 2026 past; commitment 2 Aug 2026 requires an already-reviewed paper). Next actionable ARR submission (~Jul-Aug 2026) commits to a later venue. Fallback LLM/KE route.

[20] [Re-DocRED HF dataset card (tonytan48/Re-DocRED)](https://huggingface.co/datasets/tonytan48/Re-DocRED) — Confirms MIT license, JSON format, fields vertexSet/labels(relation r, head h, tail t)/evidence, and that Re-DocRED corrects DocRED's incomplete (false-negative) annotation. arXiv:2205.12696.

[21] [Revisiting DocRED -- Addressing the False Negative Problem (Tan et al., EMNLP 2022) PDF](https://arxiv.org/pdf/2205.12696) — Primary PDF (grepped): '~64.6% of all triples are missing in the original DocRED'; 4,053 docs re-annotated; ~13 F1 gain; recall 32.07->69.40; splits train 3,053/dev 500/test 500; 96 relations; avg triples/doc DocRED-dev 12.3 vs Re-DocRED 34.6-34.9.

[22] [Revisiting DocRED -- ACL Anthology (EMNLP 2022, pp. 8472-8487)](https://aclanthology.org/2022.emnlp-main.580/) — Anthology landing page confirming id 2022.emnlp-main.580, full author list (Tan, Xu, Bing, Ng, Aljunied) and page range 8472-8487.

[23] [Re-DocRED GitHub repository](https://github.com/tonytan48/Re-DocRED) — Confirms train 3,053 / dev 500 / test 500 split document counts and MIT license; data files data/{train,dev,test}_revised.json.

[24] [DocRED/Re-DocRED rel2id.json (tonytan48 KD-DocRE)](https://raw.githubusercontent.com/tonytan48/KD-DocRE/main/meta/rel2id.json) — Authoritative 96-relation schema map (+ 'Na':0). Confirms kinship props: P22:30 (father), P25:81 (mother), P26:26 (spouse), P40:20 (child), P3373:19 (sibling) all PRESENT; P1038 ('relative') ABSENT.

[25] [Kinship Data Benchmark for Multi-hop Reasoning (Sun & Kazakov, 2026)](https://arxiv.org/abs/2601.07794) — Primary abstract page: KinshipQA is built by a GENERATIVE pipeline over synthetic, culture-specific genealogies (textual inference tasks derived from synthetic trees) -> NOT natural text; treat like CLUTRR. Confirms the planner's flag.

[26] [CustFRE: An Annotated Dataset for Extraction of Family Relations from English Text (Mumtaz et al., 2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8885562/) — Natural prose (short stories, Wikipedia bios, BBC/Guardian/Dunya news), 2,716 annotations / 248 sentences, 6 classes incl. EXPLICIT no_relation (1,175 = 43%); CC BY (Mendeley DOI 10.17632/jps7rfkytr.1). Secondary natural host with explicit absent gold for the atomic arm.

[27] [Genealogical relationship extraction from Wikipedia (104-document corpus)](https://digitalcommons.calpoly.edu/cgi/viewcontent.cgi?article=1283&context=csse_fac) — 104 manually coref-resolved Wikipedia documents annotated for sibling-of/parent-of/child-of/spouse-of -- a small, natural, kinship-focused alternative; less clearly-exhaustive absent gold than CustFRE/Re-DocRED.

[28] [Stable but Miscalibrated: A Kantian View on Overconfidence (2025/26)](https://arxiv.org/abs/2510.14925) — Search-identified support for the adversarial check: internal reasoning can be self-consistent and robust to perturbations yet systematically misaligned with truth ('stable miscalibration') -- i.e. confident-but-wrong evades dispersion-based detection.

## Follow-up Questions

- Exact per-relation frequencies of P22/P25/P26/P40/P3373 in the Re-DocRED test split (and the count of disconnected-component absent kinship pairs) -- needed to size iter-7 STEP-B and check statistical power before spending.
- Is CustFRE's text/license re-distributable for our pipeline, and how many of its 1,175 no_relation pairs survive once restricted to PERSON-PERSON pairs with both entities in a kinship context (so 'no relation' is a genuine absent kinship edge rather than an unrelated pair)?
- Should the paper submit the full work to the rolling Neurosymbolic AI journal now (immediate, X-NeSy special issue) or hold for NeSy 2027 / KR 2027 main-track for higher conference prestige, given all 2026 conference windows are closed?
- Does any internal-state / confident-hallucination detector (e.g. Song et al. 2026, arXiv:2510.11529) provide runnable code we could include as an additional STEP-A baseline to show that even a learned confident-hallucination detector under-performs the gold-free structural certificate on the absent-relation stratum?
- For the 'present multi-hop' stratum, does the project's CLUTRR-style extended kinship composition table (grandfather/uncle/etc.) compose consistently with Re-DocRED's flat schema, and what is the gold for composed relations that fall outside DocRED's 96 types?

---
*Generated by AI Inventor Pipeline*
