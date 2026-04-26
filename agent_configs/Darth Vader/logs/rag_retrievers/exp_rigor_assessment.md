### Claims-to-Experiments Mapping
- *Claim 1: MI metric aligns with Recall/MRR.* Supported by Correlation Analysis (Fig 1).
- *Claim 2: Robustness to hyperparameters.* Supported by Sensitivity Analysis (Fig 2).
- *Claim 3: Ensembles outperform single retrievers.* Supported by Perturbation and Shapley plots (Figs 3.1, 3.2, 3.3).
- *Claim 4: Redundancy spectrum of retrievers.* Supported by MDS geometric embedding (Fig 4).

### Baseline Assessment
The baselines are extensive. The authors evaluated 13 configurations, including modern GraphRAG systems (HippoRAG, LightRAG), standard RAG, and BM25. The encoder (BGE-M3) is standardized, which ensures fairness in the embedding-based comparison.

### Dataset Assessment
The paper uses HotpotQA, MuSiQue, 2WikiMultiHopQA, and TriviaQA. These are appropriate multi-hop QA benchmarks. However, the authors sampled only 1,000 QA pairs per dataset (20% train, 80% test). This subsampling is small, especially given that RAG systems can exhibit significant variance over different topics. 

### Metric Assessment
The metrics (Recall@1, MRR, Divergence) are appropriate for the retrieval stage. However, a major gap is the lack of end-to-end generation metrics. The paper argues that RAG retrievers should be selected to optimize the final generation, yet they do not report Exact Match, F1, or LLM-as-a-judge scores for the generated answers when using the ensembled retrievers.

### Statistical Rigor
- **Variance reporting**: Completely absent. None of the tables or figures report standard deviations, confidence intervals, or error bars across different random seeds or folds. 
- **Significance testing**: Missing. With only 800 test samples per dataset, small differences in MRR or Recall might not be statistically significant.

### Ablation Assessment
The hyperparameter sensitivity sweep (top-K, anchor retriever, gamma) serves as an ablation for the metric design. Figure 2 clearly isolates the effect of these choices. However, there is no ablation on the underlying LLM used to generate the CP* scores.

### Missing Experiments
- **End-to-End Generation Performance**: Does the MI-based ensemble actually lead to better downstream generation accuracy?
- **LLM Generator Variance**: Does the CP* target distribution heavily depend on the choice of the LLM?
- **Computational Cost / Latency Analysis**: Ensembling 13 retrievers or running XGB/Shapley attribution has a significant computational overhead. Is the trade-off worth it?

### Error Analysis Assessment
There is no qualitative error analysis. The paper does not show examples of where the MIGRASCOPE divergence correctly penalizes a miscalibrated retriever, nor does it present failure cases of the ensemble approach.

### Overall Experimental Rigor Verdict
Significant gaps

Score: 4.0