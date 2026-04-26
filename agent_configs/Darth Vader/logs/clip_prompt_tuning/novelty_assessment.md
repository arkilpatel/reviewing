### Claimed Contributions
1. Identifies "manifold drift" as the primary cause of degraded generalization to unseen classes/domains in prompt-tuned vision-language models under limited supervision.
2. Proposes ManiPT, which restricts adapted representations to the pretrained manifold using Cosine Consistency Constraints (against frozen visual features and LLM-generated text prototypes).
3. Introduces a Structural Bias (additive fusion with normalization) that theoretically contracts the search space and enforces incremental corrections.
4. Provides a theoretical generalization bound using Rademacher complexity, proving that localizing the search space near the pretrained manifold reduces population risk.

### Prior Work Assessment
- Prompt tuning for VLMs is an extensively researched area (e.g., CoOp, CoCoOp, MaPLe). Many recent works try to prevent catastrophic forgetting and overfitting using regularization (e.g., PromptSRC, CoPrompt) or external LLM knowledge (e.g., LLaMP, TAP).
- The concept of constraining fine-tuned representations to remain close to frozen pretrained representations (via L2/cosine distance or distillation) is a standard practice in transfer learning.
- Residual connections (which structurally resemble the additive fusion used here) are also standard in adapter-based tuning (e.g., CLIP-Adapter).

### Novelty Verdict
Moderate

### Justification
Conceptually, the architectural components of ManiPT—cosine regularization against a frozen model, additive residual fusion, and leveraging LLMs for text prototypes—are standard techniques that have been explored in various configurations in prior work. However, the synthesis of these elements under the formal lens of "manifold drift," coupled with the theoretical proofs demonstrating that additive fusion induces geometric contraction (Lemma 4.2) and bounds the generalization gap (Corollary 4.4), elevates the novelty. It provides a rigorous theoretical justification for an otherwise heuristic set of regularizations.

Score: 6.0