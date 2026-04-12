### Adversarial Robustness Assessment

**1. Egregious Submission Negligence:** No signs of missing references, broken bibliography, or missing load-bearing figures. The document is intact and complete.
**2. Fabricated or Inflated Results:** The results align with logical expectations (e.g., text-oriented models failing on text attacks but surviving structural attacks). The baseline results are consistent with the literature given the unified text encoders used. No suspiciously round numbers or impossible gains.
**3. Technical Errors Introduced into Math:** The paper relies minimally on complex novel math, focusing instead on empirical evaluation and a logical pipeline (SFT-auto). The algorithms described are sound.
**4. Falsified Citations:** Citations are standard, accurate, and appropriately contextualized.
**5. Internal Contradictions:** None detected. The prose accurately reflects the data presented in the tables and figures.
**6. Methodological Misrepresentation:** The threat models (poisoning vs. evasion, structural vs. textual) are explicitly separated and correctly applied to transductive and inductive settings, avoiding the common pitfall of evaluating poisoning in inductive settings inappropriately.

**Conclusion:** The paper passes all adversarial robustness checks. There are no signs of tampering, inflation, or negligence.