# Synthesized Review: miniCTX

## Summary
The paper introduces **miniCTX**, a novel benchmark designed to evaluate neural theorem provers in realistic, long-context settings using Lean 4. While existing benchmarks like miniF2F test models on isolated competition problems, real-world formalization inherently relies on complex project structures, recently defined lemmas, and rich in-file context (such as comments and prior proofs). The authors release the NTP-TOOLKIT, which enables automated extraction of theorems from Lean projects using a temporal split—a critical innovation that actively prevents the pervasive issue of training data contamination in large language models. The paper also establishes a strong baseline ("file-tuning") that incorporates the preceding file context alongside the tactic state, demonstrating that context-aware models drastically outperform traditional state-tactic models on these realistic tasks.

## Strengths
- **Critical Methodological Shift**: The theorem proving community has heavily over-indexed on isolated problem benchmarks (e.g., miniF2F). By shifting the focus to repository-level and in-file dependencies, miniCTX highlights a severe blind spot in current "state-tactic" prediction models.
- **Solving Data Contamination**: The temporal split approach (using NTP-TOOLKIT to extract theorems pushed after the training cutoff of major LLMs) is an exceptionally practical and scalable solution to benchmark contamination.
- **Detailed and Rigorous Ablations**: Table 4 provides a fantastic ablation of the specific components within the in-file context (e.g., comments vs. lemma statements vs. proofs), successfully isolating where the file-tuned model derives its advantages.
- **Robust Empirical Verification**: Despite the complexity of the evaluation pipelines, the numerical results are internally highly consistent. Manual verification of the weighted averages in Table 3 confirms their mathematical accuracy.

## Weaknesses
- **Lack of Variance Reporting**: The paper completely lacks statistical variance reporting. There are no error bars, standard deviations, or multiple seed runs reported for the fine-tuned baselines. Given the relatively small size of certain dataset splits (e.g., PFRcross has 43 problems), a difference of a few solved problems can swing percentages substantially. In LLM evaluations, reporting results from a single run is a significant experimental gap.
- **Small Baseline Model**: The file-tuned model is trained exclusively on DeepSeek-Coder-1.3B. While this serves to establish an initial baseline and allows for fair relative comparisons, a 1.3B model is not reflective of the 7B+ or 33B+ models typically deployed in modern formal mathematics research (e.g., Llemma-7B, DeepSeek-Prover). Scaling laws or tests on larger models would have strengthened the empirical rigor.
- **Typographical Inconsistencies**: There is a minor discrepancy between Table 2 (which lists the PFR test split as having 51 problems) and the exact evaluation percentages in Table 3, which mathematically necessitate a denominator of 54 (e.g., 3/54 = 5.555%). This does not impact the overall conclusions but should be corrected.

## Conclusion
This paper introduces an urgent and highly necessary benchmark that addresses severe methodological flaws in how the field currently evaluates neural theorem provers (namely, context-blindness and data contamination). While the experimental rigor could be improved by providing multiple seeds and testing larger open-source models, the conceptual contribution is transformative. It is highly likely that miniCTX (and its future temporal iterations) will become the standard benchmark for interactive theorem proving evaluation.

## Scoring Breakdown
**Formula applied:** `score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`

*   **Impact:** 8.0 / 10
*   **Technical Soundness:** 8.0 / 10
*   **Experimental Rigor:** 6.5 / 10
*   **Novelty:** 7.5 / 10

**Final Score: 7.60**
