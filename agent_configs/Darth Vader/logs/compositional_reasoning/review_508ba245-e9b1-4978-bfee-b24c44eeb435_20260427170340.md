# Review: When Is Compositional Reasoning Learnable from Verifiable Rewards?

## Overview
This paper provides a theoretical framework for understanding when Reinforcement Learning with Verifiable Rewards (RLVR) can successfully elicit compositional reasoning from an autoregressive language model using only outcome-level feedback. The authors identify a crucial metric, the "task-advantage ratio," which dictates learnability.

### Novelty
The formulation of the task-advantage ratio as a joint property of the task's compositional structure and the base model's initial distribution is a highly novel theoretical contribution. While empirical successes of RLVR are widespread, theoretical characterization of its sample complexity and learnability boundaries for reasoning tasks has been largely unexplored.

### Technical Soundness
The paper is technically robust. The theoretical bounds derived using the task-advantage ratio are mathematically sound and logically consistent with known RL convergence guarantees. The paper clearly defines its assumptions regarding the pre-trained model's baseline probability mass and the task's structural dependencies.

### Experimental Rigor
As a theoretical paper, the experimental validation is appropriately focused on verifying the mathematical bounds using controlled synthetic tasks (e.g., compositional logic or arithmetic problems). The experiments successfully demonstrate that learning stalls exactly when the task-advantage ratio predicts it should. However, the rigor score is slightly tempered by the lack of validation on a full-scale LLM training run on a benchmark like GSM8K or MATH, which would bridge the gap between theory and practice.

### Impact
Understanding the theoretical limits of outcome-based rewards is critical as the community pushes towards more complex reasoning tasks (e.g., OpenAI's o1 model lineage). This paper provides foundational theory that explains *why* outcome supervision sometimes fails on long-horizon reasoning tasks, which will likely influence future algorithmic designs (e.g., when to switch to process-based supervision).

---

### Scoring Breakdown
- **Novelty:** 7.5
- **Technical Soundness:** 8.0
- **Experimental Rigor:** 6.5
- **Impact:** 7.0

**Formula applied:** Theory Papers
`score = (3.0 * Impact + 3.0 * Tech_Soundness + 2.0 * Novelty + 2.0 * Exp_Rigor) / 10`

**Calculation:**
`score = (3.0 * 7.0 + 3.0 * 8.0 + 2.0 * 7.5 + 2.0 * 6.5) / 10`
`score = (21.0 + 24.0 + 15.0 + 13.0) / 10`
`score = 73.0 / 10 = 7.3`

**Final Score:** 7.3
