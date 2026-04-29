### Claimed Contributions
1. **SQUAD Framework:** A novel inference scheme that integrates early-exit neural networks (EENNs) with distributed ensemble learning. It utilizes a quorum-based stopping criterion that evaluates both "horizontally" (across ensemble learners invoked sequentially by computational cost) and "vertically" (across early exit layers) using a t-test for consensus reliability.
2. **Hierarchical Diversity:** The conceptual formalization of diversity not just at the final output of an ensemble, but at every intermediate early-exit gate, ensuring complementary representations at all depths.
3. **QUEST (Quorum Ensemble Search Technique):** A Neural Architecture Search (NAS) approach based on SVGD-RD and Joint Training Loss to automatically discover ensemble architectures that optimize both individual accuracy and hierarchical diversity.

### Prior Work Assessment
- **Ensembles of Early Exits:** The idea of combining ensembles with early exits has been explored previously, as acknowledged by the authors with citations to EE-ensemble (Qendro et al., 2021) and QUTE (Ghanathe & Wilton, 2025). However, these prior works primarily focus on uncertainty quantification. SQUAD's specific execution strategy—sequentially invoking learners by complexity until a quorum is reached—adds a meaningful systems-efficiency perspective.
- **NAS for Ensembles and Early Exits:** NESBS (Shu et al., 2022) performs NAS for static ensembles, while NACHOS (Gambella et al., 2025) and CNAS search for single early-exit models. Combining SVGD-RD to optimize for "hierarchical diversity" across multiple exits is a non-trivial algorithmic synthesis. The delta here is substantial, as extending diversity metrics to intermediate representations in a NAS framework addresses a genuine bottleneck in EENN reliability.

### Novelty Verdict
Substantial

### Justification
While the core components (Early Exits, Ensembles, NAS) are heavily researched, their intersection in this paper is well-executed and conceptually fresh. The identification of calibration failures at intermediate layers of single models is accurate, and proposing "hierarchical diversity" as the solution is structurally novel. The paper effectively bridges the gap between efficiency (via early exits) and robustness (via ensembles), which constitutes a substantial methodological advancement over the independent prior work in these subfields.

### Missing References
The authors have adequately referenced the most directly overlapping recent works (e.g., QUTE, EE-ensemble, NACHOS).

## Novelty Score: 7