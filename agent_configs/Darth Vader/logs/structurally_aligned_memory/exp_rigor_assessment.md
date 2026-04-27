# Experimental Rigor Assessment

**Research Questions & Baselines:**
The experimental design is extremely rigorous. The authors evaluate their method on the SWE-bench Verified dataset, which is the gold standard for repository-level coding tasks. The baselines are strong and fair: they compare against a Vanilla Agent (Mini SWE Agent) and a faithful reproduction of an Instance-level Memory baseline (ReasoningBank), ensuring that the gains are specifically due to the *granularity* of the memory, not just the presence of memory. 

**Metrics & Statistical Rigor:**
The authors test across four diverse and highly capable backbone models (Gemini 2.5 Flash/Pro, Claude 3.7/4.0 Sonnet), demonstrating robust generalizability. Crucially, they account for streaming order effects by running 3 independent random seeds and reporting both the mean, standard deviation, and Best@3 Pass@1 metric. They also account for token/step budgets by including the memory extraction overhead in the total step limit.

**Ablations & Error Analysis:**
The ablation studies are comprehensive and directly validate the core claims:
1. They decouple structured prompting from memory injection, proving that structural scaffolding alone is insufficient.
2. They ablate the category isolation filter, showing that global retrieval introduces noise.
3. They compare abstract insights against raw trajectories, proving the necessity of the extraction operator.
Furthermore, the paper includes excellent analysis sections on temporal dynamics (showing a clear cold-start to accelerated learning curve), task complexity distribution, and a qualitative case study that perfectly illustrates *why* instance-level memory fails and subtask memory succeeds.

Score: 9
