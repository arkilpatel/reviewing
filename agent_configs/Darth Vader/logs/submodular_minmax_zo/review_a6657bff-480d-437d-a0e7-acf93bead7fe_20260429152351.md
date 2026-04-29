# Final Review

## Novelty

The paper formalizes and addresses a new problem class: mixed-integer min-max and max-min optimization problems where the objective function is submodular with respect to the discrete minimizer and concave (possibly non-smooth) with respect to the continuous maximizer. To solve this, the authors propose a zeroth-order extragradient algorithm (ZO-EG) that relies on the subgradient of the Lovász extension for the submodular variable and a Gaussian smoothing random oracle for the concave variable.

The paper successfully identifies a useful and previously unstudied specific problem setting (submodular-concave min-max optimization). However, the proposed algorithmic solution (ZO-EG) is highly predictable and represents a straightforward synthesis of existing tools rather than introducing fundamentally new algorithmic insights. It is a direct concatenation of existing, standard techniques: using the Lovász extension to convexify the discrete variable (Lovász, 1983; Hazan & Kale, 2012), estimating the gradient of the continuous variable via Gaussian smoothing (Nesterov & Spokoiny, 2017), and updating both using the standard extragradient method. The novelty lies primarily in framing the problem and combining these established tools. Thus, the methodological novelty is moderate.

## Technical Soundness

The paper presents several significant theoretical claims regarding the convergence and complexity of the proposed algorithm in both offline and online settings. Unfortunately, a thorough analysis reveals critical mathematical flaws that invalidate the primary theoretical guarantees.

*   **Invalid Interchange of Expectation and Supremum (Critical Error):** In the proof of Theorem 3.2 (offline convergence), the authors attempt to bound the expected duality gap. They correctly define the gap using a supremum over $z \in Z$, but then substitute an upper bound on the expected value for a *fixed* $z$ directly into the supremum. This incorrectly assumes $\mathbb{E}[\sup_{z} X_k(z)] \le \sup_{z} \mathbb{E}[X_k(z)]$, violating Jensen's inequality. Because $z$ acts as the maximizer for the duality gap, it is highly correlated with the noise injected into the iterates. This probabilistic fallacy completely breaks the proof of convergence to an $\epsilon$-saddle point.
*   **Vacuous Bound for Online Duality Gap (Critical Error):** In Theorem 3.5, the online expected duality gap is bounded by $O(\sqrt{N \bar{P}_N})$, where $\bar{P}_N$ is the path length of the sequence of optimal best-response decisions. Because these best responses depend on the iterates (which are subject to random noise) and because minimizing the piecewise-linear Lovász extension causes the minimizer to jump discontinuously between hypercube vertices, the distance between consecutive best responses will frequently be lower-bounded by a constant. This leads to $\bar{P}_N = \Omega(N)$ even in a static environment, yielding an average regret bound of $O(1)$. The bound does not converge to zero and is theoretically vacuous.
*   **Incorrect Query Complexity Scaling (Significant Error):** The paper claims an $O(m^2 \epsilon^{-2})$ query complexity to reach an $\epsilon$-saddle point. However, computing the subgradient of the Lovász extension and evaluating it for the zeroth-order oracle both require $O(n)$ evaluations of the original set function. The true query complexity must be $O(n m^2 \epsilon^{-2})$; dropping the linear dependence on the combinatorial dimension $n$ is misleading.

These fundamental flaws mean the theoretical foundation of the paper is broken. While the algorithm may converge in practice, the provided theory fails to rigorously prove why.

## Experimental Rigor

The experimental validation exhibits significant gaps and relies on an inadequate methodology that fails to demonstrate real-world applicability or proper comparative performance.

*   **Trivial Synthetic Datasets:** The method is evaluated entirely on toy datasets, such as 50x50 synthetic noisy grayscale images for segmentation and a 50-point subset of the "Two-Moons" dataset for clustering. There is no evaluation on real-world images, complex videos, or standard benchmarks, meaning the method's scalability and practical usefulness remain unproven.
*   **Lack of Appropriate Baselines:** For the offline settings, there are absolutely no baselines provided. For the online setting, the proposed optimization algorithm is compared against supervised and semi-supervised U-Nets (deep neural networks) that were trained offline *without* adversaries. This "apples-to-oranges" comparison against an unrobustified neural network on a toy problem does not constitute a rigorous evaluation of an optimization algorithm. There is a glaring absence of comparisons against first-order subgradient descent-ascent methods or other robust optimization baselines.
*   **Missing Statistical Rigor and Ablations:** Although the text mentions results are averaged over 10 runs, no standard deviations or error bars are included in the tables or plots. Furthermore, there are no ablation studies isolating the impact of key algorithmic parameters (like the number of Gaussian samples or the smoothing parameter), nor computational efficiency (wall-clock time) comparisons.

These experiments serve as a basic proof-of-concept for the math rather than a rigorous empirical validation of the proposed machine learning algorithm.

## Significance & Impact

The paper tackles a novel problem formulation and connects concepts from zeroth-order optimization, min-max games, and submodular set functions. However, the scientific contribution is incremental, and its impact is severely hampered by fundamental flaws in the theoretical analysis and extremely weak empirical validation.

Because the theoretical proofs contain critical errors and the experiments are restricted to 50x50 synthetic toy problems without proper baselines, the paper fails to deliver a reliable, scalable, or theoretically sound solver that practitioners or theoreticians can confidently build upon. It is unlikely to be adopted by applied researchers due to the lack of evidence for scalability. While it may generate some discussion within the theoretical optimization community regarding robust combinatorial problems, the core mathematical errors must be addressed before the work can be considered a solid contribution.

## Scoring Breakdown
*   **Impact:** 3.5
*   **Technical Soundness:** 2.0
*   **Experimental Rigor:** 3.0
*   **Novelty:** 5.0

**Formula Applied:** `score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`
**Final Score:** 3.4