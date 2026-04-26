### Claimed Contributions
1. **MIGRASCOPE**: A mutual-information-based retriever quality score that normalizes across lexical, dense, and graph-based ranking paradigms to quantify retrieval relevance and utility.
2. **Synergy and Redundancy Metrics**: Formulation of MI-grounded synergy and redundancy metrics to visualize how multiple retrievers interact.
3. **MI-based Ensemble Framework**: A retriever ensemble method using MI-based attribution (Shapley values) to select and weight retrievers.
4. **Comprehensive Benchmarking**: An empirical benchmark over SOTA GraphRAG and RAG retrievers, providing insights on contribution patterns and robustness.

### Prior Work Assessment
- **Contribution 1 & 2 (MI metrics for RAG)**: Prior works like Zhu et al. (2024), Liu et al. (2024), and Li et al. (2025) have utilized Information Bottleneck, Pointwise Mutual Information (PMI), and Jensen-Shannon Divergence respectively for context pruning, filtering, or internal attribution. The delta here is adapting these concepts specifically for benchmarking retrievers against a pseudo-ground-truth distribution, rather than for real-time pruning.
- **Contribution 3 (Ensembling)**: RAG ensembles have been extensively studied (e.g., Rezaei et al., Zhang et al., Chen et al.). Chen et al. (2025) even explored multi-RAG from an information-theoretic perspective. The delta is providing a specific operational recipe using Shapley values to weight and select retrievers based on their marginal information gain.
- **Contribution 4 (Benchmarking)**: Existing benchmarks focus on end-to-end RAG metrics (Recall, MRR). The delta is the direct evaluation of retriever redundancy.

### Novelty Verdict
Moderate

### Justification
The paper applies established information-theoretic concepts (MI, JSD, Shapley values) to the problem of RAG retriever evaluation. While the application is novel and yields interesting findings (especially regarding the redundancy of GraphRAG methods), the core mathematical ideas are heavily borrowed from existing statistical signal processing and recent RAG attribution literature. The transition from context-attribution to retriever-evaluation is a sensible, logical extension but not a transformative leap.

### Missing References
The authors cite most of the relevant literature, but further discussion on how their CP* estimation compares to log-probability based rerankers (e.g., UPR - Unsupervised Passage Reranking) would provide better context.

Score: 5.0