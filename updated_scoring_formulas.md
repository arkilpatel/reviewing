# Updated Weighted Scoring Formulas

Based on the latest reviewer alignment, the following formulas MUST be used to calculate the final float score for any paper evaluation.

Each sub-score is evaluated on a strict 0-10 scale.

## SCORE CALIBRATION (CRITICAL)
You must be extremely harsh and critical. The empirical ground truth for human reviewers on this platform is:
- **Accepted Papers:** Average score of 7.82 (ranging from 6.0 to 10.0).
- **Rejected Papers:** Average score of 2.39 (ranging from 0.0 to 7.6).
- **Borderline Range:** 6.0 to 7.6.

Do NOT inflate scores. A score of 8.0+ means this is a top-tier, transformative paper with almost no flaws. If a paper has methodological gaps, missing baselines, incremental novelty, or limited real-world impact, its sub-scores must reflect that severely. Most papers should score between 3.0 and 6.5. Do not default to giving 7s or 8s just because the math looks correct. Be a strict gatekeeper.

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

**The Negligence Penalty:** If a paper contains egregious submission errors that break the scientific evaluation chain (e.g., a missing or completely broken bibliography characterized by unresolved citation markers of any format, completely missing load-bearing figures referenced in the main text, or severe formatting corruption), you must calculate the standard weighted float score as described above, and then **divide the final score by 2**. Clearly state in your review that the Negligence Penalty was applied. Do not rely on specific syntax (like `[?]` or `(?)`); instead, critically evaluate whether the document fundamentally fails to provide the necessary information (like references) to be peer-reviewed.
