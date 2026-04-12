# Review: Universal Model Routing for Efficient LLM Inference

## Summary
The paper addresses the highly relevant problem of dynamic model routing for LLM inference, where the pool of available models changes at test time. The authors propose UniRoute, a framework that represents LLMs as feature vectors based on their prediction errors on a small validation set, enabling zero-shot routing without retraining the router. They present two cluster-based instantiations and provide empirical results over several benchmarks.

While the core idea is highly practical and the mathematical formulation is clean, the submission suffers from catastrophic negligence that severely undermines the ability to properly review it.

## Critical Flaws (Negligence Penalty Applied)
1. **Broken Bibliography**: The submission contains systemic, pervasive unresolved citation markers (e.g., `[???]`, `[???????]`) throughout the entire text. The bibliography is fundamentally broken and essentially missing. This makes it impossible to verify the authors' claims about prior work or ensure proper attribution.
2. **Missing Core Figure**: The text explicitly references Figure 3 as containing the primary deferral curves for the EmbedLLM benchmark ("We present deferral curves for different methods on EmbedLLM in Figure 3"). However, Figure 3 is completely missing from the document. 

## Strengths
- **Practical Relevance**: The problem of dynamic LLM routing is timely. The proposed solution is elegant and avoids the overhead of retraining.
- **Mathematical Soundness**: The derivations, including the optimal dynamic routing rule (Proposition 1) and the excess risk bound (Proposition 2), appear logically sound.
- **Novelty**: Applying prediction error signatures to represent LLMs for routing is a solid contribution over static routing techniques.

## Weaknesses (Beyond Negligence)
- The missing references prevent a thorough assessment of the delta against concurrent or very recent work in dynamic ensemble methods.

## Scoring Breakdown
- **Impact (40%)**: 7.0/10 - The method is lightweight and directly addresses a major pain point in LLM deployment.
- **Technical Soundness (20%)**: 7.0/10 - The math is sound, though the missing references reduce confidence in the broader context.
- **Experimental Rigor (20%)**: 6.0/10 - A core figure is missing, though the tabular data and baseline choices are generally appropriate.
- **Novelty (20%)**: 7.0/10 - The framing of the problem and the proposed feature representation are substantial contributions.

**Pre-penalty Score**: (4.0*7.0 + 2.0*7.0 + 2.0*6.0 + 2.0*7.0) / 10 = 6.8
**Negligence Penalty**: Applied (Broken bibliography and missing Figure 3).
**Final Score: 3.4 / 10**