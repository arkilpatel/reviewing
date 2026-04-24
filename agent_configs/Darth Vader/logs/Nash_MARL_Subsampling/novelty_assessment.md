### Claimed Contributions
1. Formalizes a communication-constrained cooperative MARL setting with one global agent and $n$ local agents.
2. Proposes `ALTERNATING-MARL`, a framework using subsampled mean-field Q-learning for the global agent and an induced episodic MDP for local agents.
3. Proves convergence to an $\tilde{O}(1/\sqrt{k})$ approximate Nash Equilibrium with poly-log sample complexity in $n$ when $k = O(\log n)$.

### Prior Work Assessment
- Mean-field subsampling for MARL: Anand et al. (2025) proposed subsampled mean-field Q-learning but for a fully centralized setting. The current paper adapts this to an alternating best-response setting.
- The local agent's learning uses the Upper-Confidence Fixed-Horizon (UCFH) algorithm by Dann et al. (2015) as a black box.
- Delta: The paper creatively combines these tools and constructs novel reductions (like the chained MDPs) to handle the communication constraints within a Markov Potential Game framework. The delta is a non-trivial methodological combination.

### Novelty Verdict
Substantial

### Justification
While the core components (subsampled mean-field RL, UCFH, Markov Potential Games) exist, synthesizing them to solve the newly formulated communication-constrained MARL problem is highly non-trivial. The reduction to chained micro-step MDPs for local agents is a clever conceptual framing.

### Missing References
None apparent, the paper adequately cites relevant prior work on mean-field MARL, potential games, and Stackelberg games.
