### Experimental Rigor Assessment

1. **Extensive Benchmarking:** The empirical evaluation is highly comprehensive, covering four distinct and standard downstream settings for CLIP adaptation: unseen-class generalization (Base-to-Novel), cross-dataset transfer (ImageNet to 10 datasets), few-shot classification (1 to 16 shots), and domain generalization. 
2. **Strong Baselines:** The authors compare ManiPT against a formidable suite of modern baselines, including capacity-based methods (CoOp, CoCoOp, MaPLe), regularization-based methods (PromptSRC, CoPrompt), and LLM-assisted methods (LLaMP, TAC, TAP). This ensures the reported gains are measured against the true state-of-the-art rather than outdated models.
3. **Performance Metrics:** The results consistently show that ManiPT achieves the highest Harmonic Mean (HM) in Base-to-Novel generalization and the highest average accuracy in cross-dataset transfer. 
4. **Ablations:** The presence of extensive ablations (context length, $\lambda$ sensitivity) ensures that the hyperparameter robustness of the method is well-documented.

Score: 8.0