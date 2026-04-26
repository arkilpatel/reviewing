# Review: RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents

This paper identifies a critical issue when applying Group Relative Policy Optimization (GRPO) to multi-turn tool-calling LLMs: when initialized with a strong Supervised Fine-Tuning (SFT) policy, the model exhibits a "paradox of perfection," generating nearly identical rollouts. This lack of within-group variance causes the group-normalized advantages to vanish, stalling reinforcement learning updates. To solve this, the authors propose RC-GRPO, which fine-tunes a Reward-Conditioned Trajectory Policy (RCTP) using mixed-quality data with special reward tokens (`<|high reward|>` and `<|low reward|>`), and then applies GRPO while explicitly sampling these diverse tokens. This guarantees variance within the rollout group, yielding a robust learning signal.

### Novelty
The paper identifies a critical failure mode in standard GRPO training for agents, termed the "paradox of perfection" or variance collapse, where a strong supervised fine-tuning (SFT) initialization reduces rollout diversity and causes group-relative advantages to vanish. The authors propose RC-GRPO (Reward-Conditioned Group Relative Policy Optimization), which combines a Reward-Conditioned Trajectory Policy (RCTP) with group-relative policy optimization using diverse reward-token conditioning. The problem of low variance after strong SFT is a known issue in reinforcement learning, and recent concurrent works have identified similar local optima in multi-turn LLMs. The core mechanism of conditioning on a reward token stems directly from Decision Transformers and Upside-Down RL. The novelty lies in the specific algorithmic synthesis. While neither return-conditioned generation nor GRPO is entirely new, applying Decision Transformer-style conditioning specifically to maintain within-group variance for GRPO in multi-turn environments is a non-obvious, pragmatic solution to a concrete optimization bottleneck. The contribution is a solid, incremental methodological improvement.

### Technical Soundness
The paper is technically very sound and internally consistent. The authors make the conceptual claim that SFT causes vanishing updates in standard GRPO due to low within-group reward variance, and back this up with both theoretical bounds and empirical logs. Proposition 4.2 models how a peaked reference policy leads to identical rollouts and zero variance, while Proposition 4.3 proves that RC-GRPO provides a theoretical lower bound on within-group variance if the conditional expectations of rewards are separated. While the theoretical model relies on an extreme assumption (that the reference policy perfectly approaches a Dirac delta optimal policy), the authors are transparent about this, using it as a "minimal variance-based explanation." The empirical logs perfectly corroborate the theory: RC-GRPO maintains advantage spread without relying on increased policy entropy, unlike standard temperature scaling.

### Experimental Rigor
The experimental evaluation is cleanly designed but suffers from a narrow scope. The baselines are highly appropriate; the authors perform a factorial ablation by including SFT+GRPO, RCTP+GRPO, and SFT+RC-GRPO, which precisely isolates the contribution of the two-stage pipeline. The ablations confirm that both the initialization and the conditioning during RL are necessary. However, the evaluation is conducted entirely on a single dataset: the Berkeley Function Calling Leaderboard (BFCLv4) multi-turn split. Claiming a general algorithmic improvement for "Multi-Turn Tool Calling Agents" but evaluating on a single environment leaves the generalizability of the method unproven. Furthermore, while the training dynamics section mentions using 4 runs, the main performance results do not report standard deviations or confidence intervals. For an RL method—where performance is notoriously sensitive to random seeds—reporting only a single point estimate is a significant rigor gap.

### Impact
The paper addresses a highly pertinent bottleneck in modern agent training: group-relative policy optimization (GRPO) is vastly more memory-efficient than PPO, but vanishing gradients on strong models cause it to stall. The performance improvements demonstrated are practically massive (e.g., an absolute gain of +36% on Qwen2.5 over SFT+GRPO). The method itself is lightweight and requires very few modifications to standard pipelines. The paper also scientifically demonstrates that relying on temperature or entropy maximization to induce exploration is brittle when the underlying model distribution is peaked, showing that controllable generation is a much more robust avenue for ensuring variance. Assuming these massive performance gains hold true beyond the single benchmark tested, this technique could readily become a standard recipe for training reasoning and tool-using agents.

---

### Scoring Breakdown

*   **Impact:** 6/10
*   **Technical Soundness:** 8/10
*   **Experimental Rigor:** 4/10
*   **Novelty:** 5/10

**Formula applied:** Standard (Empirical / Mixed) Papers
`score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`

**Calculation:**
`score = (4.0 * 6 + 2.0 * 8 + 2.0 * 4 + 2.0 * 5) / 10`
`score = (24 + 16 + 8 + 10) / 10`
`score = 58 / 10 = 5.8`

**Final Score:** 5.8