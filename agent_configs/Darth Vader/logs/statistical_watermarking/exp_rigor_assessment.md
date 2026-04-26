### Claims-to-Experiments Mapping
1. **Log-growth optimality & Stopping time**: Supported by synthetic experiments (Fig 1 and 2).
2. **Superior sample efficiency & anytime validity on LLMs**: Supported by real-data experiments (Table 1).

### Baseline Assessment
- The baselines include the state-of-the-art anchor-based method (SEAL) and several others. 
- **Fairness concern**: The paper adapts fixed-horizon p-value baselines to the sequential setting by applying a strict Bonferroni correction ($p_k < \alpha / (k(k+1))$). This is an extremely conservative union bound that heavily penalizes the baselines, requiring them to achieve astronomically small p-values to stop early. A more rigorous evaluation would compare against stronger sequential adaptations (e.g., converting the baseline test statistics into martingales or using alpha-spending functions), or compare fixed-horizon performance fairly to ensure the e-value approach doesn't lose power overall.

### Dataset Assessment
- The MarkMyWords benchmark is appropriate and well-established for this task. However, evaluating on only 300 outputs is somewhat small for a rigorous statistical evaluation.
- The synthetic experiments are restricted to a vocabulary size of $n=2$. This is far too simple and fails to test the method in a regime resembling language modeling ($n \gg 10,000$).

### Metric Assessment
Metrics (Quality via LLM-as-a-judge and Size/Tokens to detect) are standard and appropriate for anytime-valid watermarking.

### Statistical Rigor
- The synthetic stopping time experiments correctly run 10,000 iterations to estimate expectations.
- For the real-data experiments, reporting the median number of tokens is helpful, but the paper lacks reporting on the variance or standard deviation across the 300 generations. 

### Ablation Assessment
- There are no ablation studies on the robustness parameter $\delta$. 
- How sensitive is the method to the choice of $\delta$? What happens when the true distribution shift exceeds the assumed $\delta$? The lack of this ablation makes it impossible to know if the theoretical robust optimization actually provides practical robustness.

### Missing Experiments
1. **Synthetic experiments at scale**: Testing with vocabulary sizes $n = 10,000+$ with heavy-tailed distributions to match the LLM setting.
2. **Ablation of $\delta$**: Showing how performance scales as $\delta$ varies in the Llama2-7B experiments.
3. **Handling of low-probability tokens**: An experiment or explanation detailing how the method avoids numerical instability or infinite e-values when $p_0(s) \to 0$.

### Error Analysis Assessment
The paper lacks a failure mode analysis. There is no discussion on when the anytime-valid stopping criteria fails or causes false alarms under severe distribution shifts.

### Overall Experimental Rigor Verdict
Significant gaps

Score: 3.5