### Adversarial Verification Checks

**Check 1 & 2: Fabricated Results & Mathematical Content Verification**
- The mathematical formulation in Eq 1 and 2 is a simple linear extrapolation. The Taylor expansion in Appendix B.2 is standard and technically correct: $R(\theta - w\alpha Pr_s)$ expands correctly to reveal a negative linear term if the inner product $s = \langle r_d, Pr_s \rangle$ is negative.
- The numbers reported in Table A.1 match the baseline numbers expected for these architectures (e.g., EDM-VP on CIFAR-10 at 1.97 FID, xAR-L at 1.28 FID). The improvements are substantial but empirically justified by the extensive grid search over CFG and merge weights. I do not see suspicious 'round numbers' or implausible claims.

**Check 3: Algorithmic Trace**
- Algorithm 1 is straightforward: sample $S$, fine-tune to $\theta_s$, return $(1+w)\theta_r - w\theta_s$. There is no complex logic to hide errors in.

**Check 4: Numerical Sanity Check**
- The FID gains (e.g., 1.28 to 1.02 for xAR-L, 3.30 to 2.01 for VAR-d16) are large but consistent with the effect of strong post-hoc guidance methods (like SIMS or DDO). The fact that precision strictly drops while recall rises gives immense credence to the results: the model isn't magically getting better at everything; it's executing a targeted trade-off that optimizes the Fréchet distance by covering dropped modes.

**Check 5: Citation Verification**
- The paper properly cites recent, highly relevant synthetic self-training work: Model Autophagy (Alemohammad et al., 2024a), Model Collapse (Shumailov et al., 2024), SIMS (Alemohammad et al., 2024b), and DDO (Zheng et al., 2025). The framing of these priors is accurate.

**Check 6: Claims-to-Evidence Trace**
- Every major claim is backed by a specific experiment (e.g., cross-architecture transfer -> Fig 8, precision-recall trade-off -> Fig 4 & 6, mode-seeking vs diversity seeking -> Toy experiment Appendix B.9).

**Check 7: Internal Consistency**
- The text, tables, and figures are internally consistent. The compute fractions calculated (<1%) mathematically align with the stated fine-tuning steps (e.g., 1-3 Mi images) relative to standard base model training budgets (hundreds to thousands of Mi images).

**Check 8: Assumption Tracking**
- The authors explicitly assume a local neighborhood (small $\epsilon$ from true data distribution) for their Taylor bounds. They test this assumption empirically in Fig 9, showing it holds even for weaker models, which is an honest and thorough way to handle theoretical assumptions.

**Check 9: Baseline Integrity**
- Baseline FIDs for xAR, VAR, and EDM match standard literature.

### Verdict
No adversarial tampering detected. The paper is methodologically transparent, mathematically sound, and empirically consistent.