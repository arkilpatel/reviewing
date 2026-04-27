# Comprehensive Review of "Semi-knockoffs"

The paper proposes "Semi-knockoffs," a model-agnostic conditional independence testing (CIT) method designed to avoid the train-test split requirement of typical model-X knockoff and holdout randomization test (HRT) frameworks. The method creates perturbed samples using conditional expectations with and without the response variable $Y$. The authors claim finite-sample type-I error and False Discovery Rate (FDR) control, alongside optimization stability and double-robustness guarantees for the practical algorithm.

Below is an evaluation across four core criteria.

### Novelty
**Score: 5/10**

**Claimed Contributions:**
1. Semi-knockoffs: a CIT method providing FDR control and p-values without data splitting or exact knockoff variable generation.
2. A stability result for regularized ERM trained with/without a null feature.
3. A double-robustness perspective for the conditional feature importance.

**Assessment:**
The novelty is moderate. The core idea of avoiding sample splitting by regressing the feature of interest on the remaining features (and on the response to break symmetry under the alternative) is a clever amalgamation of existing regression-based conditional sampling techniques (like CPI) and the knockoff framework. The double-robustness result is a straightforward generalization of a very recent work by Reyero Lobo et al. (2025). The approach represents a sensible and useful, but somewhat incremental, step forward in the model-agnostic CIT literature. 

### Technical Soundness
**Score: 4/10**

**Assessment:**
There is a significant gap between the claims in the title/abstract and the actual results, which raises critical concerns.
- **Theory-Practice Gap:** The title and abstract prominently claim "finite-sample guarantees." However, Theorems 3.1 and 3.2 only apply to the *Oracle* Semi-knockoffs (where the true conditional expectations $\nu_j$ and $\rho_j$ are perfectly known). For the practical algorithm, the authors rely on asymptotic convergence (Theorem 4.2 provides an $O_P(1/\sqrt{n})$ bound) and explicitly state a "conjecture" (Section 4.5) that exchangeability is preserved with high probability. Claiming finite-sample validity for the method when the practical algorithm only enjoys asymptotic bounds and heuristic double-robustness is misleading.
- **Computational Cost:** The algorithm requires estimating $\nu_j$ and $\rho_j$ for each feature $j \in [p]$, meaning $2p$ regressions must be fitted. The paper does not theoretically analyze the computational bottleneck this imposes compared to simple data-splitting or global knockoff generation.
- **Theorem Presentation:** Important regularity assumptions are deferred entirely to the appendix, and notation obscures the dependence on $j$ in the theorem statements.

### Experimental Rigor
**Score: 4/10**

**Assessment:**
The experimental validation has significant gaps, particularly given the paper's focus on high-dimensional settings.
- **Dimensionality:** The abstract emphasizes that Semi-knockoffs adapt to "high-dimensional settings by providing valid false discovery rate (FDR) control." However, all simulated experiments are run with $n=300$ and $p=50$. In the context of modern variable selection and FDR control, $p=50$ is extremely low-dimensional. There are no experiments exploring truly high-dimensional regimes ($p > n$, e.g., $p=1000, n=500$), which is exactly where knockoffs are most relevant.
- **Real Data Benchmark:** The real-world evaluation uses the Wisconsin Breast Cancer dataset, which has $p=30$. This does not constitute a rigorous evaluation of a feature selection method meant for complex, high-dimensional scientific discovery (e.g., genomics or GWAS data).
- **Missing Baselines/Ablations:** A computational time comparison against standard model-X knockoffs or HRT is missing in the main text, obscuring the practical cost of fitting $2p$ conditional models.

### Impact
**Score: 4/10**

**Assessment:**
**1. Technical Significance (70%):** The practical utility of the method is limited by its computational cost ($2p$ models) and the lack of exact finite-sample guarantees for the empirical version. While avoiding data splitting increases statistical power, practitioners requiring rigorous FDR control might prefer standard knockoffs with a well-calibrated generative model, rather than relying on the conjectural validity of Semi-knockoffs.
**2. Scientific Significance (30%):** The theoretical insights connecting optimization stability and double robustness to distribution exchangeability are valuable and may inspire further theoretical analysis in perturbation-based feature importance.
**3. The 3-Year Citation Projection:** The paper will likely be cited as an incremental method within the interpretable ML and model-X knockoff literature. However, without resolving the practical finite-sample guarantees or demonstrating scalability to $p \gg n$, widespread adoption is unlikely.

---

### Scoring Breakdown
- **Impact:** 4/10
- **Technical Soundness:** 4/10
- **Experimental Rigor:** 4/10
- **Novelty:** 5/10

**Overall Score Calculation:**
`Score = (4.0 * 4 + 2.0 * 4 + 2.0 * 4 + 2.0 * 5) / 10 = (16 + 8 + 8 + 10) / 10 = 4.2`

**Final Score: 4.2**
