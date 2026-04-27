### Claimed Contributions
1. **Paradigm Shift:** The paper introduces an offline learning paradigm utilizing Direct Preference Optimization (DPO) instead of the standard Online RL (e.g., REINFORCE/PPO) to train Neural Combinatorial Optimization (NCO) solvers.
2. **Architecture Shift:** The paper proposes using a Mamba-based architecture (Selective State Space Model) rather than Transformers to achieve linear $O(N)$ computational and memory complexity, enabling scaling to massive instances.
3. **Progressive Bootstrapping:** The paper introduces a heuristic-based bootstrapping mechanism that integrates a Local Search (LS) operator to generate high-quality preference pairs for DPO, mitigating the reward sparsity in standard self-play.

### Prior Work Assessment
- **Mamba for NCO:** Using Mamba instead of Transformers is a relatively straightforward architectural substitution. However, in the context of NCO, where the $O(N^2)$ bottleneck of Transformers severely limits scalability beyond $N=1000$, this substitution is non-trivial and highly beneficial.
- **Offline DPO for NCO:** While DPO is currently ubiquitous in LLM alignment, applying it to Combinatorial Optimization is an interesting reframing. Previous works have explored offline RL for NCO, but replacing the reward formulation with pairwise preference optimization over trajectories is a neat adaptation.
- **Bootstrapping with Local Search:** Using local search operators to refine solutions and generate training signals is a well-explored concept in NCO (e.g., AlphaGo-style approaches, neuro-symbolic methods). Combining it specifically to create "winner/loser" pairs for DPO is a sensible, albeit expected, extension.

### Novelty Verdict
Moderate to Substantial. 

### Justification
The paper's core novelty lies in the creative combination of existing techniques (Mamba, DPO, Local Search) tailored to a specific domain (Combinatorial Optimization) to solve a very real problem (scalability and efficiency bottlenecks). While no single component is fundamentally groundbreaking, their synthesis to achieve linear complexity and high throughput in NCO constitutes a solid and substantial engineering and methodological contribution.

Score: 6.0