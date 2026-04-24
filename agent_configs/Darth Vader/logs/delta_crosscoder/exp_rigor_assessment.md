### Claims-to-Experiments Mapping
1. **Delta-Crosscoder recovers causally relevant latents:** Supported by steering and max-activation analysis on 10 model organisms spanning 4 model families.
2. **Delta-Crosscoder outperforms SAE-based baselines:** Supported by the coverage analysis (Fig 5) comparing against DSF and BatchTopK crosscoders.
3. **Delta-Crosscoder matches non-SAE baselines without interactive probing:** Supported by LLM grader evaluation against Activation Difference Lens (ADL) (Fig 7).

### Baseline Assessment
- **Appropriate:** Yes. The paper compares against state-of-the-art SAE-based diffing methods (DSF, BatchTopK) and a leading non-SAE interactive method (ADL).
- **Strong & Fairly Tuned:** The SAE baselines use similar or higher sparsity budgets (BatchTopK-200, 400). The comparison to ADL is conservative; the authors use the *best reported performance* from the ADL paper rather than reproducing it under potentially disadvantageous conditions.

### Dataset Assessment
- **Appropriate:** The use of "model organisms" (Synthetic Document Finetuning, Taboo Word Guessing, Emergent Misalignment, Subliminal Learning) is highly appropriate. These are controlled settings specifically designed to study narrow, fine-tuning induced behavioral changes.
- **Diversity:** The evaluation spans multiple LLM families (Gemma, LLaMA, Qwen) and sizes (1B-9B), ensuring the results are not architecture-specific.

### Metric Assessment
- **Appropriate:** The use of causal interventions (steering) is the gold standard for validating the functional role of features in mechanistic interpretability. The LLM grader evaluation for comparing with ADL uses the exact rubric from the ADL paper.
- **Reconstruction Metrics:** Explained variance and dead feature rates are standard metrics for SAEs and are reported comprehensively.

### Statistical Rigor
- **Variance reporting:** Not extensively reported for the LLM grader scores (Fig 7), but the qualitative and causal validation (steering across multiple organisms) provides strong evidence.
- **Null Test:** A crucial experiment is the null test (applying the method to two identical un-finetuned models), which convincingly demonstrates the method's robustness against false positives.

### Ablation Assessment
- The ablation study in Appendix F demonstrates that removing fine-tuning data from the training mixture does not degrade performance. This is a critical result validating the task-agnostic claims of the method.

### Missing Experiments
- The main missing element is a thorough quantitative analysis of the LLM grader's variance across multiple runs or random seeds, although the qualitative steering results mitigate this concern.
- The paper relies heavily on inspecting the "top-3 non-shared latents." It would be beneficial to have a more systematic evaluation of false positives among the lower-ranked non-shared latents, though the authors do discuss this briefly.

### Error Analysis Assessment
The paper discusses cases where the method produces multiple latents instead of one (e.g., Taboo Word, Emergent Misalignment) and thoroughly analyzes the distinct roles of these latents (e.g., the primary misalignment latent vs. the refusal-associated latent).

### Overall Experimental Rigor Verdict
Mostly rigorous with gaps