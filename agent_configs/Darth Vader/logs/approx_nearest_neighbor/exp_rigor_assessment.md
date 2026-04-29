### Claims-to-Experiments Mapping
- **Superior QPS-recall and indexing time:** Supported by evaluations on 6 modern and 6 legacy datasets (Figures 3, 4, 16-19).
- **Scalability to high dimensionality:** Supported by results on DBpedia3072 and DataCompDr (d=1536).
- **Robustness to retrieval size:** Supported by evaluations at K=10, K=100, and K=1000.
- **Online insertion support:** Supported by interleaved search and insertion workload experiments (Figure 8).
- **Component effectiveness:** Supported by ablation studies explicitly testing PRT, TFB, and PES (Figures 9, 10).

### Baseline Assessment
The baselines are exceptionally strong and appropriate. The authors compare against the state-of-the-art in graph-based methods (HNSW, Vamana), quantization-based methods (ScaNN, IVFPQFS, RaBitQ+), and combined methods (SymQG). Crucially, they also include an ablation ("PRT only") which effectively serves as a comparison to the immediate prior work (KS2), isolating the exact benefits of their new contributions (TFB and PES). 

### Dataset Assessment
The dataset selection is a major strength of this evaluation. Rather than relying solely on saturated, outdated benchmarks like SIFT and GIST, the authors evaluate on a wide array of modern, high-dimensional datasets utilizing state-of-the-art embeddings (OpenAI-1536, OpenAI-3072, CLIP, DINOv2). The datasets are sufficiently challenging and highly representative of modern AI workloads.

### Metric Assessment
The metrics—QPS-Recall, Indexing time, Peak memory usage—are the gold standard for Approximate Nearest Neighbor Search evaluation and perfectly match the claims made in the paper. 

### Statistical Rigor
The evaluation follows standard ANN-Benchmarks protocols (single-threaded search over a large set of queries). While variance and confidence intervals are not reported, this is standard practice in the ANNS subfield, as deterministic graph traversals over thousands of queries typically yield negligible variance. The inclusion of 12 total datasets significantly reduces any risk of cherry-picking.

### Ablation Assessment
The ablations are perfectly designed. Figures 9 and 10 build the proposed method incrementally (PRT only -> PRT+TFB -> PRT+TFB+PES), clearly isolating the QPS-recall improvements and indexing time costs of each novel component.

### Missing Experiments
None. The evaluation is exhaustive, covering different retrieval sizes, dataset modalities, dimensionalities, and even online insertion workloads. 

### Error Analysis Assessment
While the paper does not extensively categorize "failure cases" (e.g., querying specifically hard vectors), failure in ANNS is typically captured comprehensively by the recall metric across the diverse query set. 

### Overall Experimental Rigor Verdict
Rigorous

**Score: 8.0 / 10**