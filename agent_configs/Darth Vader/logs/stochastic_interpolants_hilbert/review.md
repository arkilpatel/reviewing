# Review: Stochastic Interpolants in Hilbert Spaces

## Novelty & Originality
### Claimed Contributions
1. A rigorous mathematical framework for Stochastic Interpolants (SIs) in infinite-dimensional Hilbert spaces, circumventing the issues of Lebesgue measure dependence and isotropic noise found in finite-dimensional formulations.
2. The introduction of a Conditional Bridge SDE (CB-SDE) that enables conditional generation for arbitrarily coupled source and target distributions.
3. Proofs of well-posedness (existence and uniqueness of strong solutions) and explicit Wasserstein-2 error bounds for the proposed infinite-dimensional SI.
4. Empirical demonstration of the framework on PDE-based inverse and forward problems (Darcy flow and Navier-Stokes).

### Prior Work Assessment
- **Infinite-dimensional generative models:** Recent works have successfully extended Diffusion Models (DMs) to infinite-dimensional spaces (e.g., Pidstrigach et al., 2023; Lim et al., 2023; Yao et al., 2025). The transition from finite to infinite dimensions for SIs closely parallels the trajectory of these infinite-dimensional diffusion models.
- **Stochastic bridges in function spaces:** Works like Yang et al. (2024) and Park et al. (2024) have explored diffusion bridges and optimal control for stochastic bridges in infinite dimensions.
- **Finite-dimensional SIs with coupled data:** Albergo et al. (2023a, 2023b) introduced the foundational SI framework and its application to data-dependent couplings.

*Delta:* The paper directly translates the finite-dimensional SI framework of Albergo et al. into the infinite-dimensional setting. While the mathematical lifting is non-trivial (requiring trace-class noise and careful handling of Cameron-Martin spaces to ensure absolute continuity), the conceptual leap is highly predictable given the recent wave of infinite-dimensional DMs. The conditional bridge essentially formalizes the coupled-data approach of Albergo et al. (2023b) using function-space SDEs. The theoretical proofs are solid, but the novelty is largely methodological and mathematical rather than conceptual.

### Novelty Verdict
Incremental to Moderate

### Justification
The paper represents a natural and expected progression of the literature. With diffusion models already having been formulated in Hilbert spaces (Yao et al., 2025; Pidstrigach et al., 2023), doing the same for Stochastic Interpolants is the obvious next step. The authors tackle the necessary measure-theoretic hurdles well, but the core generative paradigm remains unchanged. The resulting application to PDEs, while successful, builds directly on existing neural operator and continuous-time generative modeling pipelines. Thus, it is a useful but predictable extension.

### Missing References
The references are generally quite comprehensive and up-to-date, covering the relevant literature on infinite-dimensional diffusions, stochastic interpolants, and operator learning.

4.0

## Technical Soundness
### Claims Inventory
- **Theoretical:** The CB-SDE correctly transports the source distribution to the conditional target (Theorem 2).
- **Theoretical:** The drift coefficient is Lipschitz continuous in the Cameron-Martin (HC) norm under specific conditions (Proposition 4).
- **Theoretical:** Strong solutions for the CB-SDE exist and are unique under specific conditions (Theorems 5 and 6).
- **Theoretical:** A time-change technique regularizes the drift singularity at the terminal time (Lemma 7).
- **Theoretical:** A Wasserstein-2 bound limits the error between the true and approximate conditional target laws (Theorem 8).
- **Empirical:** Infinite-dimensional SIs outperform or match SOTA infinite-dimensional diffusion models and finite-dimensional SIs on PDE tasks.

### Verification Results
- **CB-SDE Transport (Theorem 2):** Verified, assuming unique solvability of the infinite-dimensional Fokker-Planck equation.
- **HC-Lipschitz Drift (Proposition 4):** Verified conceptually, but reliant on exceptionally strong assumptions (Hypothesis 3).
- **Existence/Uniqueness (Theorems 5 & 6):** Unverifiable/Concern. Theorem 6 requires the target distribution to factorize along an eigenbasis of the covariance operator $C$.
- **Error Bound (Theorem 8):** Verified mathematically.
- **Empirical Claims:** Concern due to massive theory-practice gaps.

### Errors and Concerns
- **Critical Concern (Theory-Practice Gap):** The conditions required for well-posedness (Hypothesis 3 or Proposition 4ii) dictate that the target data must reside in the Cameron-Martin space of the trace-class covariance operator $C$. For an RBF kernel, this implies the data must be exceptionally smooth. However, the Darcy flow experiment uses a binary permeability field (taking values 3 and 12). Binary fields possess sharp discontinuities and absolutely do not reside in the Cameron-Martin space of an RBF kernel. This directly violates the assumptions needed for Lipschitz continuity and well-posedness, rendering the theoretical guarantees inapplicable to the presented experiments.
- **Significant Error (Unrealistic Uniqueness Assumption):** Theorem 6 (Uniqueness) assumes that the target distribution $\mu_1$ factorizes along the eigenbasis of the covariance operator $C$ (i.e., the components are mutually independent). This is an incredibly strong and unrealistic assumption for any complex functional data (like fluid vorticity or permeability), which exhibit intricate spatial correlations that will not neatly decouple across the eigenvectors of a standard isotropic RBF kernel.

### Internal Consistency Check
The authors acknowledge the underperformance on the Darcy flow task due to the binary permeability field, noting that spectral convolutions struggle with the discontinuities. However, they fail to acknowledge that this very discontinuity completely breaks their theoretical well-posedness guarantees (Proposition 4 and Theorem 5).

### Theory-Practice Gap Assessment
The gap between the theory and practice is immense. The rigorous mathematical framework relies on strict smoothness assumptions (data residing in the Cameron-Martin space) and independence assumptions (factorization along the eigenbasis). The real-world PDE experiments violate these assumptions (e.g., using binary fields). Thus, the paper presents a theoretical framework for a highly idealized setting, but runs experiments in a setting where the theory is unsupported.

### Overall Technical Soundness Verdict
Significant concerns

3.0

## Experimental Rigor
### Claims-to-Experiments Mapping
- *Claim:* The time-change technique resolves singularities and is crucial for numerical stability. Supported by 1D Darcy flow ablations (Table 1).
- *Claim:* Infinite-dimensional SIs achieve competitive/SOTA results on PDE inference. Supported by 2D Darcy and Navier-Stokes experiments (Table 2).

### Baseline Assessment
The baselines are appropriate and strong. The authors compare against FunDPS (a state-of-the-art infinite-dimensional diffusion model), DiffusionPDE (a finite-dimensional approach), and finite-dimensional SIs. However, it is unclear if the same extensive hyperparameter tuning budget was allocated to the finite-dimensional SI baseline as to the proposed method.

### Dataset Assessment
The datasets (1D Darcy, 2D Darcy, 2D Navier-Stokes) are standard and appropriate for evaluating infinite-dimensional generative models and neural operators.

### Metric Assessment
The primary metric used is the relative L2 error. While standard for PDE surrogate modeling, generative models should ideally also be evaluated on distributional metrics (e.g., Wasserstein distances of the generated ensemble, or functional Fréchet Inception Distances if applicable) rather than just pixel-wise/point-wise L2 error, which only captures the mean behavior and fails to evaluate the quality of the generated distribution's variance and diversity.

### Statistical Rigor
**Fundamentally flawed.** The paper reports point estimates (single percentages like 1.9% or 2.7%) for all experiments in Tables 1, 2, and 3. There is absolutely no reporting of variance, standard deviations, confidence intervals, or error bars. There is no mention of how many random seeds were used for training or inference. In an evaluation of stochastic generative models, failing to report variance makes it impossible to determine if the 0.4% improvement on Navier-Stokes over FunDPS is statistically significant or merely an artifact of a lucky seed.

### Ablation Assessment
The authors provide a good ablation on the time-change schedule $\theta(t)$ (Table 1), effectively demonstrating that slowing down time near the boundaries improves numerical stability.

### Missing Experiments
- **Length Scale Sensitivity:** The authors mention in Appendix E.3 a "sweet spot" tradeoff regarding the roughness of the noise (controlled by the RBF length scale $\ell$). However, they simply set $\ell = 0.02$ without showing an ablation or empirical demonstration of this tradeoff curve. 
- **Sample Diversity:** Since this is a stochastic generative model, experiments demonstrating the diversity of the generated posterior samples (e.g., plotting the variance of the generated ensemble against the true posterior) are conspicuously absent.

### Error Analysis Assessment
The paper provides qualitative visual residuals (Figure 2), but lacks a systematic quantitative error analysis (e.g., analyzing failure cases on high-frequency vs. low-frequency components).

### Overall Experimental Rigor Verdict
Significant gaps

2.5

## Significance & Impact
### Impact Assessment
**1. Technical Significance (70%):** 
The technical utility of the paper is moderate. While extending Stochastic Interpolants to infinite-dimensional spaces provides a flexible framework for operator learning and PDE inverse problems, the empirical gains over existing methods (like infinite-dimensional diffusion models, e.g., FunDPS) are marginal (e.g., an improvement from 2.8% to 1.0% on the forward Navier-Stokes task, but a regression from 1.9% to 2.3% on Darcy flow). Furthermore, the restrictive smoothness assumptions required for the framework to be mathematically well-posed (data must reside in the Cameron-Martin space) may limit its adoption in practical engineering applications that frequently feature discontinuous data (e.g., binary permeability fields, shockwaves).

**2. Scientific Significance (30%):** 
Scientifically, the paper contributes a clear articulation of the measure-theoretic challenges involved in translating flow-matching/interpolant methods to Hilbert spaces (e.g., the lack of a Lebesgue reference measure and the need for trace-class noise). The proofs of well-posedness and the Wasserstein-2 bounds are rigorous contributions to the theoretical understanding of infinite-dimensional generative models. However, the highly restrictive assumption required for strong uniqueness (factorization along the covariance eigenbasis) highlights that our theoretical understanding of these processes remains quite fragile and disconnected from practical data distributions.

**3. The 3-Year Citation Projection:** 
This paper is likely to receive a moderate number of citations (approximately 20-40 over the next 3 years). It will be cited primarily by researchers working at the intersection of generative modeling, neural operators, and Bayesian inverse problems, likely as a theoretical reference point for flow matching in infinite dimensions. However, because it does not introduce a substantially new paradigm or a massively disruptive empirical capability, it is unlikely to become a foundational, highly-cited pillar of the field.

**Impact Score: 3.5 / 10**

3.5

## Scoring Breakdown
- **Novelty:** 4.0
- **Technical Soundness:** 3.0
- **Experimental Rigor:** 2.5
- **Impact:** 3.5

**Formula applied:** `score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`
**Final Score:** 3.3
