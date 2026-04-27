# Novelty Assessment - "Is Training Necessary for Anomaly Detection?"

The paper's novelty lies in its fundamental challenge to the prevailing belief that Multi-class Unsupervised Anomaly Detection (MUAD) requires task-specific training.

### Key Novelty Points:
1. **Conceptual Shift:** Instead of following the dominant paradigm of training encoder-decoder models to learn anomaly-free patterns, the authors propose a training-free, retrieval-based approach. This "non-parametric" view of MUAD is a significant departure from existing SOTA methods like UniAD, DiAD, and Dinomaly.
2. **Theoretic Insight:** The identification and formal analysis of the **"fidelity-stability dilemma"** in reconstruction-based MUAD is a novel contribution. The paper provides a representation-space analysis showing that high-fidelity reconstruction and stable residual scores are naturally contradictory objectives when forced through a bottleneck.
3. **Algorithm Design (RAD):** While retrieval-based methods exist (e.g., PatchCore), RAD introduces a "global-then-patch" multi-level retrieval strategy tailored for the *multi-class* setting. The global context conditioning via [CLS] tokens effectively handles the heterogeneity of multi-class memory banks, which is a specific challenge not fully addressed by single-class retrieval methods.
4. **Theoretical Provability:** The paper provides a theoretical proof that retrieval-based scores upper-bound reconstruction-residual scores, offering a principled justification for why retrieval is inherently better than (or at least as good as) reconstruction given the same encoder and data.

### Assessment:
The novelty is high, not necessarily because it uses "new" complex architectures (it's training-free), but because it provides a strong, theoretically backed counter-narrative to the current research direction. It simplifies the problem and demonstrates that the "hard" part of MUAD might already be solved by foundation model encoders, and that further "training" might actually be counterproductive due to the fidelity-stability dilemma. This kind of "paradigm-challenging" novelty is often more impactful than incremental architectural changes.

**Score Recommendation (Novelty): 8.5/10** (Strong novelty in conceptual shift and theoretical insights).