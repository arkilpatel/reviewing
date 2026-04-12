### Claims-to-Experiments Mapping
1. Better cost-quality trade-offs than standard cascades: Supported by Figures 2, 4, 10, 11 and Table 2.
2. Better trade-offs than lossy speculative decoding: Supported by Table 2, Figures 4, 6, 7.
3. Token-specific rules outperform cascaded deferral rules: Supported by Figures 11, 12.

### Baseline Assessment
Appropriate and strong. They compare against sequence-level cascades (SeqCascade), token-level cascades (TokenCascade), lossy speculative decoding (SpecDecode [Lossy]), and Big Little Decoder (BiLD*). The tuning of `beta` in Tran-Thien (2023) is also evaluated in the appendix.

### Dataset Assessment
Appropriate. They use WMT, XSum, CNNDM for T5 experiments, and a robust suite (GSM8K, MBPP, SQuAD, WebQuestions, NQ, TriviaQA) for Gemma. 

### Metric Assessment
Appropriate. They report standard metrics: BLEU, ROUGE-2, F1, Pass@1, Exact Match, plotted against relative latency and rejection rate.

### Statistical Rigor
Wall-clock latency is averaged over 3 trials. For Gemma models, rejection rate is used as a deterministic proxy for compute cost, which is solid. Variance bars are not heavily plotted, but the trend lines are clear and evaluated on decently sized validation sets (e.g., 500 examples for latency, 1000 for Gemma QA).

### Ablation Assessment
They thoroughly ablate the choice of target distributions (Chow, Diff, OPT, TokenV1-V3). They also ablate sampling parameters: temperatures T=0.1, 0.5, 1.0, top-P values, and block sizes. 

### Missing Experiments
It would have been informative to compare with more recent dynamic-draft or multi-draft speculative decoding techniques, though the authors explicitly scope their contribution to the two-model single-draft setting. 

### Error Analysis Assessment
They analyze why OPT fails for Gemma while succeeding for T5 (attributing it to calibration differences when scaling from 77M->800M vs 2B->27B).

### Overall Experimental Rigor Verdict
Mostly rigorous with minor gaps.