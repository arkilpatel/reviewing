### Claims-to-Experiments Mapping
- **Claim 1**: The superiority of Wasserstein Variational Inference (WVI) over Black-Box Variational Inference (BBVI) in previous literature stems from the gradient estimator used (Price's estimator), not the Bures-Wasserstein geometry.
  - *Supported*: The experiments clearly map to this claim by evaluating SPGD (BBVI) and SPBWGD (WVI) with both Price's and the reparametrization gradient estimators.
- **Claim 2**: BBVI and WVI with Price's gradient estimator significantly outperform their counterparts that use the reparametrization gradient.
  - *Supported*: Evaluated across 12 datasets, demonstrating that Price's gradient allows for convergence over a wider range of step sizes and achieves better or equal free energy.
- **Unsupported Claim**: In Section 4, the text explicitly states: "For the empirical evaluation, we will compare the performance of VI with SPGD, SPBWGD, and NGVI with the reparametrization and Price estimators." However, NGVI is entirely missing from all results, plots, and appendices.

### Baseline Assessment
The baseline design is highly appropriate and factorized. The authors compare against SPGD + Reparam (the standard BBVI baseline) and SPBWGD + Price (the standard WVI baseline from recent literature). Evaluating all methods across a dense grid of step sizes ensures that the baselines are fairly tuned and that peak performance is captured for all methods. However, the promised Natural Gradient Variational Inference (NGVI) baseline is missing. Given that NGVI is a leading state-of-the-art method for Gaussian VI, its omission represents a gap in establishing completeness.

### Dataset Assessment
The datasets are highly appropriate. The authors utilize 12 diverse models from the PosteriorDB benchmark suite, which is the gold standard for Bayesian inference tasks. The models cover a wide range of types (logistic regression, HMMs, Lotka-Volterra, mixed-effects models) and dimensionalities (from 3 to 237). Because the task is optimization (minimizing variational free energy on fixed target posteriors), there are no data contamination concerns.

### Metric Assessment
The primary metric used is the Variational Free Energy ($F$) evaluated at the end of training. This is exactly the objective function the algorithms are designed to minimize, making it perfectly aligned with the claims. Reporting performance as a function of the step size is a robust and standard way to evaluate stochastic optimization algorithms, as it captures both the minimum achieved energy and the algorithm's sensitivity to hyperparameters.

### Statistical Rigor
The statistical rigor of this paper is exceptionally high and stands out positively. All results are averaged over 32 independent random seeds. The plots include 95% bootstrap confidence intervals for all curves. The gradient estimation uses a fixed 8 Monte Carlo samples, and the final evaluation uses $2^{12}$ samples to ensure low variance in the metric itself. This level of rigor leaves very little room for cherry-picking or statistical noise.

### Ablation Assessment
The experimental design fundamentally acts as a $2 \times 2$ ablation study: Geometry (Parameter Space via SPGD vs. Measure Space via SPBWGD) $\times$ Gradient Estimator (Price vs. Reparametrization). This perfectly isolates the contribution of the novel component (introducing Price's gradient to SPGD) and proves the central thesis that the gradient estimator, not the geometry, drives the performance improvements.

### Missing Experiments
1. **NGVI Evaluation**: As noted, the paper promises an evaluation against NGVI but fails to include it.
2. **Wall-Clock Time / Computational Cost**: In the discussion, the authors note that Price's gradient estimator requires $O(d^3)$ operations per step, whereas the reparametrization gradient only requires $O(d^2)$. While Price's gradient improves iteration complexity, it is crucial to see if it actually improves *wall-clock time* convergence. A plot of Free Energy vs. Wall-Clock Time or FLOPs is severely needed, especially for the higher-dimensional models (e.g., `Birds`, $d=237$), to determine if the proposed estimator is practically useful or if the cubic cost outweighs the iteration savings.

### Error Analysis Assessment
The authors perform adequate qualitative error analysis. They identify a specific failure mode in the `Rats` problem, where methods using the reparametrization gradient fail to converge entirely, and where SPBWGD + Price requires much smaller step sizes than SPGD + Price. They provide a plausible mathematical hypothesis for this divergence (the extra $C^{-T}$ scaling in the SPBWGD estimator making it noisier).

### Overall Experimental Rigor Verdict
Mostly rigorous with gaps

7