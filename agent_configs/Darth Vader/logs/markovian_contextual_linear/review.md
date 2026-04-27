# Review of A Reduction Algorithm for Markovian Contextual Linear Bandits

This paper extends the framework of Hanna et al. (2023b) for contextual linear bandits, moving from an i.i.d. context assumption to a Markovian context setting. The authors demonstrate that the problem can be reduced to a standard linear bandit instance by constructing a stationary surrogate action set. To handle the non-stationary bias introduced by Markovian dependence, they employ a delayed-update mechanism, and they further propose a phased learning algorithm for unknown transition distributions.

## 1. Technical Soundness
The paper's core strength lies in its theoretical analysis. The mathematical reduction is sound and rigorous. The authors correctly adapt standard linear bandit analyses (e.g., OFUL and Phased Elimination) to absorb the bias $\Delta_t$ caused by the non-stationarity of the Markov chain. The use of uniform geometric ergodicity to bound the mixing times and the uniform control of Markov additive functionals for the phased learning algorithm are standard but executed with high technical rigor.

## 2. Novelty
Conceptually, the paper is an incremental theoretical extension. The idea of reducing stochastic settings to stationary ones is directly inherited from prior work. To address the Markovian aspect, the paper applies well-known bias-control techniques such as mixing-time delays and phased estimation. While assembling these pieces requires technical care, the overall approach—combining a known reduction with standard Markovian delay techniques—is predictable and lacks a fundamentally new paradigm or algorithmic insight.

## 3. Experimental Rigor
The empirical validation is extremely limited. The experiments consist of a single synthetic ring-graph Markov chain task, comparing only against a standard LinUCB baseline. While this perfectly illustrates the theory, it fails to rigorously validate the method's practical utility. Missing are comparisons against heuristic Markovian algorithms (e.g., sliding window or discounted UCB), evaluations of the unknown distribution setting (Algorithm 2), and any real-world datasets with temporal dependence.

## 4. Impact
While the problem setting (temporally correlated contexts) is practically motivated by recommendation systems and autonomous agents, the proposed algorithmic solution—specifically the delay mechanism—is typically too conservative for real-world deployment. Practitioners are far more likely to rely on simpler heuristics. As a pure theoretical contribution, it adds a neat building block to the online learning literature, but it is unlikely to influence broad practice or see widespread adoption, resulting in a niche impact.

---

### Scoring Breakdown
- **Impact:** 3.5 / 10
- **Technical Soundness:** 8.5 / 10
- **Experimental Rigor:** 3.0 / 10
- **Novelty:** 3.0 / 10

**Formula applied:** `score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`
**Calculated First Review Score:** 4.3
