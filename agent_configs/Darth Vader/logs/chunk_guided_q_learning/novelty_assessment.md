### Claimed Contributions
1. Identifying a trade-off in offline RL between single-step TD learning (which suffers from bootstrapping error accumulation over long horizons) and action-chunked TD learning (which is stable but suboptimal due to open-loop execution restricting fine-grained stitching).
2. Proposing Chunk-Guided Q-Learning (CGQ), an algorithm that trains both a single-step critic and an action-chunked critic, and regularizes the former towards the latter using an upper-expectile distillation loss.
3. Providing theoretical results showing that this regularized learning process attains tighter critic optimality bounds than either single-step or action-chunked TD learning alone.
4. Demonstrating empirically that CGQ outperforms single-step and action-chunked methods on the OGBench manipulation tasks.

### Prior Work Assessment
- **Action Chunking and Distillation**: Prior work such as DQC (Decoupled Q-Learning for Action Chunking, Li et al., 2025a) has already recognized the suboptimality of large action chunks and proposed using a large-chunk critic to distill values into a smaller-chunk (or single-step) critic. The authors acknowledge DQC, but the algorithmic delta is extremely thin. While DQC relies entirely on the distillation loss to train the fine-grained critic, CGQ simply adds the standard 1-step TD loss back into the objective ($L_{CGQ} = L_{TD} + \beta L_{reg}$).
- **Value Regularization and N-Step Returns**: The idea of regularizing a high-variance/low-bias estimator (like single-step TD) with a lower-variance but potentially biased estimator (like n-step returns or an action-chunked critic) is mathematically equivalent to classic techniques like TD($\lambda$) or value regularization. 
- **Expectile Distillation**: The use of an asymmetric upper-expectile distillation loss to regularize value functions is directly borrowed from IQL and DQC.

### Novelty Verdict
Incremental

### Justification
The paper is an instance of "ablation-as-contribution" or "combination-as-contribution". The core idea of distilling from a chunk-based critic to a fine-grained critic was introduced by DQC. The primary novelty here is adding the standard 1-step TD loss back to the distillation objective. The authors' own ablation (`CGQ-DISTILL`) demonstrates that their method without the 1-step TD loss is effectively DQC. Adding a standard TD loss term to an existing distillation objective is a predictable, minor algorithmic tweak. Furthermore, the theoretical analysis is a standard bias-variance trade-off derivation for regularized estimators and does not yield surprising new insights.

### Missing References
The related work section covers the very recent concurrent literature well (e.g., QC-FQL, DQC, DEAS). However, broader connections to classic value regularization techniques and conservative target networks could be expanded to better contextualize the algorithmic contribution.

0-10 Score: 3
