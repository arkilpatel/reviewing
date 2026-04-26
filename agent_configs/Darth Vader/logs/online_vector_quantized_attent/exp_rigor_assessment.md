### Claims-to-Experiments Mapping
1. **Long-context recall matching full attention:** Supported by Basic ICR and Positional ICR tasks up to 64k tokens.
2. **Long in-context learning outperforming linear attention:** Supported by Linear Regression ICL task up to 128 functions.
3. **Language modeling efficiency:** Supported by PG19 evaluation.
4. **Short-context preservation:** Supported by PIQA, HellaSwag, Wino, ARC benchmarks.

### Baseline Assessment
The chosen baselines are conceptually strong: full self-attention (`sw-nope`), original `sw-vq` (VQ-attention), and leading linear attention / SSM models (`Mamba2`, `Mesa-Net`, `GDN`). However, all baselines and the proposed model are strictly evaluated at extremely small parameter scales (ranging from 70M to 480M parameters). 

### Dataset Assessment
The synthetic datasets (ICR and ICL) are highly appropriate for explicitly stressing memory capacity and isolated sequence mixing abilities. PG19 is a standard and acceptable long-context language modeling benchmark. Extrapolation up to 64k sequence lengths provides a solid testbed.

### Metric Assessment
The metrics—per-token accuracy for synthetic tasks and cross-entropy for language modeling—are direct and appropriate indicators of performance.

### Statistical Rigor
The experiments heavily report single-run accuracy curves (e.g., Figures 4, 5, 6, 8). Variance and standard deviations are only reported for the short-context benchmarks (Table 1) across checkpoints. Given the known variance in small-scale training runs, relying on single-seed runs for the primary long-context evaluations introduces statistical uncertainty. 

### Ablation Assessment
The paper includes well-designed ablations validating core design choices. They isolate the spread-maximizing centroid initialization (versus random assignment), dictionary growth schedule (plateauing versus linear), and learning rate adaptation (adaptive versus constant). This thoroughly justifies the algorithmic specifics of the OVQ update rule.

### Missing Experiments
1. **Wall-Clock Profiling:** This is the most glaring omission. A core motivation for the paper is computational efficiency. Reporting theoretical $O(N)$ asymptotic memory and linear compute without a single throughput (tokens/sec) or peak memory (MB) benchmark on actual hardware is unacceptable. Sparse `scatter`/`gather` operations often suffer severe hardware bottlenecks.
2. **Model Scale:** Evaluating exclusively under 500M parameters leaves it entirely unknown whether OVQ-attention scales competitively to modern 7B+ parameter sizes where representational dynamics shift drastically.

### Error Analysis Assessment
The paper does not provide qualitative error analysis or deeply investigate failure modes beyond plotting accuracy-vs-length curves.

### Overall Experimental Rigor Verdict
Significant gaps. The lack of wall-clock profiling and the extremely small scale of the models undermine the strong claims of efficiency and competitiveness.

**Score: 4/10**