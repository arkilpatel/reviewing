### Claimed Contributions
1. A large-scale empirical comparison of LLM-generated vs human-generated citation networks.
2. Demonstration that global structural properties of LLM-generated reference lists are indistinguishable from human ones, yet both are distinct from random baselines.
3. Demonstration that semantic embeddings, particularly when combined with graph structure via GNNs, can reliably distinguish LLM from human reference lists.
4. Robustness checks across multiple LLMs (GPT-4o, Claude) and embedding models (OpenAI, SPECTER).

### Prior Work Assessment
There is existing work showing that LLM-generated bibliographies look structurally plausible (e.g., Algaba et al., 2024; Mobini et al., 2025). However, this paper pushes the boundary by formalizing this into a detection task, utilizing Graph Neural Networks, and rigorously proving that while topology fails as a discriminator, semantic embeddings succeed. The application of GNNs to this specific problem (detecting LLM-generated reference lists by treating them as text-attributed graphs) is a novel conceptual and methodological combination.

### Novelty Verdict
Substantial. The paper takes a known concern (LLMs generating fake or biased references) and provides a rigorous, large-scale, novel framing (graph-level topological vs semantic detection).

### Justification
The transition from qualitative observations about LLM bibliographies to a quantitative, predictive detection framework using GNNs is a substantial step forward. The finding that structural mimicry is nearly perfect while semantic fingerprints remain is a strong empirical insight.