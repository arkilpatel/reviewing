### Claimed Contributions
1. Empirical evaluation of LLM-generated citation graphs (GPT-4o, Claude 4.5) versus human ground-truth citation graphs.
2. Demonstration that purely structural (topological) features of these citation graphs are insufficient to reliably distinguish LLM-generated references from human ones.
3. Demonstration that semantic embeddings (title/abstract textual features), particularly when combined with Graph Neural Networks (GNNs), can reliably detect LLM-generated bibliographies with high accuracy (>93%).

### Prior Work Assessment
- The paper directly builds upon prior works (e.g., Algaba et al., 2024; Mobini et al., 2025; Algaba et al., 2025) that evaluated the coarse bibliometric and local graph-structural regularities of LLM-generated bibliographies.
- The delta between prior work and this paper is the framing of a distinct detection task, leveraging a systematic machine learning pipeline (Random Forests and multiple GNN architectures) to show the stark contrast in discriminative power between structure and semantics. 

### Novelty Verdict
Moderate to Substantial.

### Justification
The paper asks a timely and interesting question about what LLMs internalize regarding scientific citations. While earlier work already hinted that LLMs match coarse structural properties but may differ in content (e.g., recency bias), this paper formalizes the detection problem. The use of GNNs to fuse structure and text is standard in graph ML, so the methodological novelty is minimal. However, the conceptual and empirical novelty—proving that detection tools *must* rely on semantic fingerprints because the topology is too perfectly mimicked—is a substantial empirical insight for the community.

### Missing References
None apparent. The paper cites the most relevant and very recent concurrent work on LLM bibliometrics.