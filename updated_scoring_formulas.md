# Updated Weighted Scoring Formulas

Based on the latest reviewer alignment, the following formulas MUST be used to calculate the final float score for any paper evaluation.

Each sub-score is evaluated on a strict 0-10 scale.

## 1. Standard (Empirical / Mixed) Papers
For papers that include experimental results, use the following weights:

*   **Impact:** 4.0 (40%)
*   **Technical Soundness:** 2.0 (20%)
*   **Experimental Rigor:** 2.0 (20%)
*   **Novelty:** 2.0 (20%)

**Formula:**
`score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`

## 2. Pure Theory Papers
For papers that are purely theoretical/mathematical (with no empirical experiments to evaluate), drop the Experimental Rigor criterion and use the following weights:

*   **Impact:** 4.0 (40%)
*   **Technical Soundness:** 3.0 (30%)
*   **Novelty:** 3.0 (30%)

**Formula:**
`score = (4.0 * Impact + 3.0 * Tech_Soundness + 3.0 * Novelty) / 10`

## Execution
At the end of your synthesized review, you MUST include a "Scoring Breakdown" section that lists the individual 0-10 sub-scores for each criterion, the formula you applied, and the final calculated float score.
