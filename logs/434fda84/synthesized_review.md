# Review: Erase or Hide? Suppressing Spurious Unlearning Neurons for Robust Unlearning

## Summary
The paper investigates the fragility of current machine unlearning methods, arguing that they achieve "shallow alignment" by generating "spurious unlearning neurons" that negatively suppress target knowledge rather than truly erasing it. The authors propose SSIUU, a method intended to regularize negative attributions and prevent them from increasing during the unlearning process, thereby improving robustness against benign and harmful retraining attacks. 

While the conceptual framing and attribution-based analysis of why unlearning fails are insightful, the paper suffers from critical mathematical flaws in its proposed method and severe internal contradictions in its empirical evaluation.

## Strengths
- **Conceptual Insight**: The use of positive and negative attribution variations to explain the "obfuscation" effect of unlearning (i.e., identifying that models learn new negative weights to hide knowledge rather than erasing positive ones) provides a compelling mechanistic explanation for recent findings in the literature.
- **Logit Lens Analysis**: The layer-wise evaluation of knowledge removal (Figure 4) provides good qualitative evidence of the depth of unlearning alignment.

## Critical Weaknesses

**1. Mathematical Flaw in the Regularization Objective**
The core algorithmic contribution is fundamentally broken. The paper repeatedly claims to "constrain the negative attribution values to remain at their original levels" (Section 1, Section 5). However, Equation 3 and Algorithm 1 (Lines 11-12) define the regularization penalty as the squared difference between the attribution at the *current* optimization step and the *previous* step ($||A_{\theta_{t-1}} - A_{\theta_t}||^2$). This is a step-wise smoothing/damping term—effectively a gradient penalty—not an anchor to the original pre-unlearning model ($A_{\theta_0}$). Consequently, the attributions can drift arbitrarily over time. The method mathematically fails to guarantee the retention of original negative influences as claimed.

**2. Disconnect Between Analysis and Method**
The paper builds its conceptual argument around "neurons" (activations, $h_{i,k}$) and computes their attribution via $\frac{\partial P}{\partial h}$ (Equation 1). Yet, in Section 5, the SSIUU method abandons this and regularizes *parameter* attribution ($\phi_{t,i} \cdot \frac{\partial P}{\partial \phi_{t,i}}$) for computational efficiency. A parameter (e.g., a weight matrix element) is not a neuron (the resulting hidden state). Regularizing parameter updates is conceptually and mathematically distinct from regularizing activation attributions, breaking the link between the paper's analysis and its proposed solution.

**3. Internal Contradiction in Empirical Results**
Section 6.1 explicitly states that for the FaithUn dataset, the unlearning process is early-stopped "when accuracy for the forget set reaches 0.33 (random sampling from three options)". However, Table 1 and Figure 2 report that the Forgetting Score (accuracy) prior to attacks is exactly 0.0 for all methods. Achieving 0.0 accuracy on a 3-choice MCQA dataset means the model actively avoids the correct answer 100% of the time. This indicates extreme over-unlearning and the heavy presence of "spurious unlearning neurons"—the exact phenomenon the authors claim to have solved. This blatant contradiction invalidates the primary dataset's baseline results.

**4. Missing Control Baselines**
Because the flawed SSIUU objective essentially acts as a step-wise drag force on parameter updates, its apparent robustness might simply stem from it forcing the model to take smaller effective steps than vanilla GD, distorting representations less. The authors failed to provide control baselines (e.g., standard L2 parameter regularization, or early-stopped GD matched to the exact parameter norm change of SSIUU) to prove that the *attribution-guided* nature of the penalty is actually responsible for the empirical gains.

## Conclusion
The observation that unlearning acts via negative suppression is valuable, but the proposed method is mathematically flawed and operates on different principles than the analysis suggests. The severe contradictions in the reported results make the empirical claims untrustworthy. 

## Scoring Breakdown
- **Impact:** 3.5 / 10 (The fundamental flaws in the methodology preclude any real-world adoption, though the analytical framing may garner niche citations.)
- **Technical Soundness:** 2.0 / 10 (Critical mathematical mismatch between the stated claims and the step-wise regularization objective, exacerbated by the parameter vs. neuron disconnect.)
- **Experimental Rigor:** 3.0 / 10 (The contradiction between the 0.33 early stopping criterion and the reported 0.0 accuracy invalidates the primary dataset's results. Lack of proper control baselines.)
- **Novelty:** 5.0 / 10 (Moderate. The specific attribution lens is a nice mechanistic addition to the already established finding that unlearning relies on obfuscation.)

**Formula:** Empirical Paper
`score = (4.0 * 3.5 + 2.0 * 2.0 + 2.0 * 3.0 + 2.0 * 5.0) / 10`
`score = (14.0 + 4.0 + 6.0 + 10.0) / 10 = 34.0 / 10 = 3.4`

**Final Score: 3.4**