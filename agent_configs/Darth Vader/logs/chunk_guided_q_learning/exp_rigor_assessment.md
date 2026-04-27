### Claims-to-Experiments Mapping
- **Claim 1: CGQ outperforms single-step and action-chunked methods on long-horizon tasks.** Supported by Table 1 (OGBench manipulation and navigation tasks).
- **Claim 2: CGQ is a better way to blend single-step and chunked TD than alternatives.** Supported by the update design ablation (CGQ vs. CGQ-DISTILL vs. CGQ-MAX vs. CGQ-OPPOSITE).
- **Claim 3: CGQ is robust to hyperparameters.** Supported by ablations on chunk size, distillation coefficient $\beta$, and expectile $\tau$.

### Baseline Assessment
- **Appropriateness and Strength**: The baselines include strong, very recent offline RL methods (FQL, NFQL, QC-FQL, DEAS, DQC). These are the correct, state-of-the-art baselines for this specific sub-field (action chunking in offline RL).
- **Completeness**: Missing standard non-chunking offline RL baselines (e.g., CQL, IQL, TD3+BC). While FQL is a strong single-step baseline, including widely adopted standards would better ground the results for the broader community.
- **Fairness**: The authors note that DQC was evaluated under smaller, reward-based datasets rather than the large goal-conditioned datasets from its original paper, leading to lower performance. It is unclear if DQC was extensively hyperparameter-tuned for this new setting to ensure a fair comparison. 

### Dataset Assessment
The experiments utilize OGBench, a recent and highly challenging benchmark specifically designed for evaluating long-horizon, sparse-reward offline RL. The datasets are appropriate, challenging, and directly test the paper's claims regarding long-horizon error accumulation. 

### Metric Assessment
The primary metric is success rate, evaluated over 150 episodes. This is the standard and appropriate metric for these tasks.

### Statistical Rigor
- **Number of runs**: Results are aggregated across only 4 random seeds. Given the high variance often observed in offline RL, 4 seeds are on the lower end of acceptable rigor. 
- **Variance reporting**: Standard deviations are reported in Table 1.
- **Significance testing**: No statistical significance tests (e.g., Welch's t-test or stratified bootstrap) are reported, making it difficult to firmly conclude superiority on tasks where the margins and standard deviations overlap.

### Ablation Assessment
The ablation studies are a strong point of the paper. The authors isolate the specific update rule (comparing against distillation-only, max-Q, and opposite regularization), and thoroughly ablate key hyperparameters ($\beta$, chunk size $h$, expectile $\tau$). The `CGQ-DISTILL` ablation effectively isolates the contribution of adding the 1-step TD loss back into the distillation framework.

### Missing Experiments
- **Computational Cost Comparison**: Since CGQ requires training two complete sets of policies and critics (chunked and single-step), a comparison of wall-clock time and parameter count against the baselines is necessary to judge whether the performance gains justify the doubled computational cost.

### Error Analysis Assessment
The paper includes an excellent and honest error analysis of its negative results on the Navigation tasks. By analyzing why the method fails (action-chunked policies struggle in locomotion, producing a bad target that corrupts the single-step critic), the authors provide genuine insight into the limitations of their method.

### Overall Experimental Rigor Verdict
Mostly rigorous with gaps

0-10 Score: 6
