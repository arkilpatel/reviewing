### Claims-to-Experiments Mapping
1. **INSIGHT improves final performance over baselines:** Supported by Tables 1 & 2.
2. **INSIGHT improves training efficiency:** Supported by Figure 4 (CountDown task).
3. **Both WMI components (MI and difficulty weight) are necessary:** Supported by component ablations in Table 3.
4. **Expected difficulty is better than sampled difficulty:** Supported by Table 4.

### Baseline Assessment
The baselines are highly relevant and strong. The authors include RANDOM, MOPPS (state-of-the-art online difficulty heuristic), and Dynamic Sampling (DS, an expensive oversampling oracle). Furthermore, the inclusion of EXPECTED-DIFFICULTY and INVERSE-EVIDENCE serves as excellent, fair ablations of their own method's components against prior philosophies. 

### Dataset Assessment
The datasets are appropriate, covering a mix of synthetic/planning tasks (CountDown), rigorous mathematics (AIME, AMC, MATH500), and general reasoning (MMLU, GPQA). The use of the DeepScaler dataset for math training is consistent with current SOTA practices.

### Metric Assessment
The use of pass@1 over 16 independent generations is the community standard for evaluating LLM reasoning capabilities and is entirely appropriate here.

### Statistical Rigor
**Significant Gap.** Reinforcement learning for LLMs is notoriously unstable and high-variance. However, the paper reports only single point estimates for all final performance metrics in Tables 1 and 2. There are no standard deviations, confidence intervals, or indications of multiple random seeds used for the RL training runs. 
Given that the performance differences between INSIGHT and MOPPS are often extremely small (e.g., on the Qwen3-4B Math Average, INSIGHT is 68.46 vs MOPPS 67.35; on 7B, INSIGHT is 64.98 vs EXPECTED-DIFFICULTY 64.64), it is impossible to determine if these gains are statistically significant or merely the result of a lucky random seed during the RL optimization.

### Ablation Assessment
The ablation studies are exceptionally well-designed. Table 3 perfectly isolates the two terms of the WMI objective, proving that epistemic uncertainty (MI) or difficulty weighting alone are insufficient. Table 4 effectively proves their theoretical claim that using expected success rates is strictly better than the sampled success rates used by MOPPS.

### Missing Experiments
- **Learning Curves for Major Tasks:** The paper claims significant training efficiency improvements (~1.5x to 2.2x), but the only learning curve provided (Figure 4) is for CountDown, a relatively toy synthetic task. To convincingly prove efficiency gains for LLM reasoning, learning curves (Performance vs. Training Steps) *must* be shown for the primary Mathematics benchmarks (e.g., MATH500).
- **Overhead Analysis:** While the paper claims "negligible additional computational overhead," evaluating the WMI objective across a large candidate batch $\hat{M}$ requires computing Digamma functions and Beta-Binomial probabilities. A concrete wall-clock time comparison of the data selection step vs. the RL forward/backward pass is needed.

### Error Analysis Assessment
The paper lacks a qualitative error analysis or a breakdown of which specific types of prompts INSIGHT selects compared to MOPPS over the course of training. Showing how the selected data distribution shifts over time would greatly strengthen the narrative.

### Overall Experimental Rigor Verdict
Mostly rigorous with gaps

**Score: 5.5/10**
