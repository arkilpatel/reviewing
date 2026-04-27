### Claimed Contributions
1. The paper proposes Mutual Information Preference Optimization (MIPO), a self-training method based on data augmentation and Direct Preference Optimization (DPO). MIPO does not require external data or verifiable rewards.
2. The authors demonstrate that generating a positive response from a given prompt and a negative response from a random prompt (or missing context), and then applying DPO, effectively maximizes the pointwise mutual information between the context and the model's output.
3. For personalization tasks, MIPO achieves a 3-40% improvement in win rates over strong personalized prompting baselines.
4. For general reasoning tasks (like math and multiple-choice questions), MIPO provides a 1-18% improvement on top of instruction-finetuned models, without any task-specific reward signals.

### Prior Work Assessment
- **Contrastive Learning and Mutual Information**: The idea of maximizing mutual information via contrastive learning is foundational (e.g., InfoNCE by van den Oord et al., 2019). Recently, applying this to language models for self-supervised alignment without preference labels has been explored directly by Fränken et al. (2024), which the authors cite. The delta here is primarily the formulation of this objective using the DPO framework rather than the standard InfoNCE loss.
- **DPO Data Augmentation**: Generating negative samples to pair with model-generated chosen samples is an active area of research. Samokhin et al. (2025) use random examples from a dataset as negatives. Yin et al. (2024) expand preference pairs across diverse prompts. The delta is Moderate. The authors provide a clean theoretical justification (mutual information maximization) for why pairing correct prompts with random prompts as negatives works within DPO.
- **Personalization**: Personalization via conditioning on user profiles is well established. The idea of dropping the user context to create a negative pair for contrastive learning is a clever, albeit straightforward, application of conditional mutual information. The delta is Substantial for the application to personalization, but Incremental theoretically.

### Novelty Verdict
Moderate

### Justification
The paper's core theoretical contribution—linking the InfoNCE mutual information bound to the DPO objective—is mathematically sound and provides a nice unifying perspective. However, the practical algorithm (using responses to random/missing prompts as negatives for DPO) is very similar to existing data augmentation heuristics for contrastive learning in LLMs. The application to personalization by contrasting a user-conditioned response with a generic response is the most novel and interesting aspect of the paper, as it effectively captures the goal of in-context steerability. Overall, the combination of these ideas is a solid, moderate step forward, but it does not represent a transformative paradigm shift, as it builds heavily on the very recent wave of contrastive RLHF literature.

### Missing References
The paper does a decent job covering the concurrent literature, including Fränken et al. (2024). It could benefit from discussing the theoretical equivalence between DPO and contrastive learning more broadly, such as in "The hidden link between RLHF and contrastive learning" (Lv et al., 2025), which the authors do cite but mainly as a passing reference for energy re-weighting.

4.0