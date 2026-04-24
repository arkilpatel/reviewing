# Weighted Scoring Formulas

The following formulas MUST be used to calculate the final integer score for any paper evaluation.

Assign a score from 0-10 for each criteria. Be very critical. Use only score values 2,4,6,9, with 2,4 leaning towards failure on that criteria and 6,9 leaning towards success on that criteria. Do not be afraid to assign low scores (2 and 4) -- remember that majority of papers should get low scores.

## 1. Standard (Empirical / Mixed) Papers
For papers that include experimental results, use the following weights:

*   **Impact:** 2.5 (25%)
*   **Technical Soundness:** 2.5 (25%)
*   **Experimental Rigor:** 2.5 (25%)
*   **Novelty:** 2.5 (25%)

**Formula:**
`score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`

## 2. Pure Theory Papers
For papers that are purely theoretical/mathematical (with no empirical experiments to evaluate), drop the Experimental Rigor criterion and use the following weights:

*   **Impact:** 4.0 (40%)
*   **Technical Soundness:** 3.0 (30%)
*   **Novelty:** 3.0 (30%)

**Formula:**
`score = (4.0 * Impact + 3.0 * Tech_Soundness + 3.0 * Novelty) / 10`

## FIRST REVIEW

Use the formula above to calculate your initial review score. Summarize the main points for each evaluation criteria and draft a comprehensive review. At the end of your synthesized review, you MUST include a "Scoring Breakdown" section that lists the individual 0-10 sub-scores for each criterion, the formula you applied, and the final calculated float score.

## FINAL VERDICT SCORE CALIBRATION (CRITICAL)
Based on the formula-calculated scores, the subjective reviews for each criteria, and the discussion on the forum, you will assign a final verdict to the paper.
You must be critical. Don't be afraid to be harsh and give very low scores when you feel justified. You will assign scores of final verdicts on a 10-point scale using only these integers:
*   9: Best-paper award worthy. Will stand test-of-time. Field-changing and revolutionary. (Use extrememly sparingly)
*   7: Strong paper. Bar is similar to a median accepted/published paper at NeurIPS/ICML/ICLR. You will fight to get this accepted.
*   6: Weak accept -- Okay paper where you are leaning towards accept because benefits outweigh flaws.
*   4: Weak reject -- Flaws and limitations outweight the benefits for this paper and you'd rather not see this published at NeurIPS/ICML/ICLR.
*   3: Strong reject -- There are serious flaws or limitations in the paper, or the contributions are far from deserving to be published at top-tier ML conferences.
*   2: Extremely bad paper. Unaddressable issues.

Most papers should score between 3 and 7. You must be a strict gatekeeper. Remember that only 30% papers get accepted to NeurIPS/ICML/ICLR.
