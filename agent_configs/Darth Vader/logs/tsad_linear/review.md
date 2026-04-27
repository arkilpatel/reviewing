# Final Review: Strong Linear Baselines Strike Back: Closed-Form Linear Models as Gaussian Process Conditional Density Estimators for TSAD

## Novelty
The paper argues that simple linear models (OLS/RRR) are highly effective for time series anomaly detection (TSAD) and connects them to Gaussian Process conditional density estimation. While the empirical finding that linear models beat complex deep models in TSAD is a valuable wake-up call for the community, the methodological novelty is Incremental. OLS and RRR are classical techniques. The GP connection, while nicely articulated, is a fundamentally known property of autoregressive models and Gaussian Processes.
**Score: 4/10**

## Technical Soundness
The paper provides a sound theoretical motivation linking GP with OLS/RRR. The derivations mapping finite-history GP conditioning to linear regression are correct and well-grounded in classical theory. The mathematical claims align well with the empirical setup. However, the paper slightly overclaims that this framework easily captures all complex anomaly types without more rigorous stress-testing on non-stationary, highly nonlinear bounds.
**Score: 6/10**

## Experimental Rigor
The authors test on a wide suite of univariate and multivariate benchmarks (AIOPS, UCR, TODS, SMD, SMAP, etc.), comparing against a massive range of baselines. The use of varied F1 metrics (point-adjusted, event-level) is appreciated. However, the evaluation relies heavily on standard benchmarks that may have saturation issues or trivial anomalies. There is limited analysis of variance, random seed robustness, and statistical significance across these runs, which is critical when claiming superiority.
**Score: 5/10**

## Impact
**1. Technical Significance (70%):** Demonstrating that simple, computationally cheap baselines outperform complex deep learning models is highly practical. It provides a highly efficient drop-in replacement that practitioners can actually use.
**2. Scientific Significance (30%):** It challenges the blind application of deep learning in TSAD, forcing the community to rethink benchmark difficulty and baseline tuning.
**3. The 3-Year Citation Projection:** This paper is highly likely to be cited frequently as a mandatory baseline and a cautionary tale in future TSAD research, similar to the "DLinear" paper in time series forecasting.
**Score: 7/10**

## Scoring Breakdown
- Impact: 7
- Technical Soundness: 6
- Experimental Rigor: 5
- Novelty: 4

**Overall Score:** (4.0 * 7 + 2.0 * 6 + 2.0 * 5 + 2.0 * 4) / 10 = (28 + 12 + 10 + 8) / 10 = 5.8 / 10
