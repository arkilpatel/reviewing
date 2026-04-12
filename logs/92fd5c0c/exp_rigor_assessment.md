### Claims-to-Experiments Mapping
The paper claims UniRoute works for >30 unseen LLMs. The experiments map to this claim using EmbedLLM, RouterBench, Math+Code, and SPROUT datasets.

### Baseline Assessment
Baselines include ZeroRouter, K-NN, and Oracle MLP. The baselines are appropriate for evaluating dynamic routing, particularly comparing against K-NN which is the closest viable dynamic baseline.

### Dataset Assessment
Datasets span general NLP, Math, Code, and routing benchmarks. This is a diverse and appropriate set.

### Metric Assessment
The deferral curve (Area under curve, Area 50%, QNC) is a standard and robust way to evaluate cost-quality tradeoffs.

### Statistical Rigor
Results are aggregated over multiple trials (e.g., 400 trials) with statistical significance reported.

### Missing Experiments
Figure 3, which is supposed to show the main deferral curves on EmbedLLM, is entirely missing from the document.

### Overall Experimental Rigor Verdict
Significant gaps (due to the missing Figure 3 which is a core result).
