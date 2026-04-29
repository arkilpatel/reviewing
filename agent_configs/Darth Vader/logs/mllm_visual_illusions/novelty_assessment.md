### Claimed Contributions
1. **The VIA-Bench Dataset**: A new benchmark consisting of 1,004 multiple-choice questions designed to test MLLMs on visual illusions and anomalies across six distinct categories (color, motion, gestalt, geometric/spatial, general visual illusions, and visual anomalies).
2. **Extensive Evaluation of Frontier Models**: A comprehensive benchmarking of over 20 state-of-the-art MLLMs, including recent reasoning-enhanced models, demonstrating that the best models still lag significantly behind human performance (69.23% vs. 93.30%).
3. **The "CoT Paradox" Insight**: Empirical evidence that Chain-of-Thought (CoT) reasoning often degrades rather than improves performance on these deceptive visual tasks, as models tend to use textual reasoning to rationalize their initial flawed visual perceptions.

### Prior Work Assessment
- **Contribution 1 (VIA-Bench Dataset)**: Probing MLLMs with visual illusions is not a fundamentally new idea. Closely related prior work includes GVIL (Zhang et al., 2023), which tests VLMs on color and geometric illusions; Illusory VQA (Rostamkhani et al., 2025), which builds datasets like IllusionMNIST; and HallusionBench (Guan et al., 2024), which evaluates visual illusions alongside language hallucinations. The delta here lies primarily in the benchmark's systematic categorization (expanding to motion, gestalt, and biological anomalies) and high-quality human-in-the-loop curation. The delta is **Incremental to Moderate**.
- **Contribution 2 (Extensive Evaluation)**: Benchmarking new models on challenging tasks is a standard practice. Applying the newest reasoning models (e.g., OpenAI o3, Qwen3-VL-Thinking) to visual illusions is a useful but expected empirical exercise. The delta is **Incremental**.
- **Contribution 3 (The CoT Paradox Insight)**: The phenomenon where CoT reasoning hurts performance on counter-intuitive tasks has been recently documented in text-only settings (e.g., Liu et al., 2025). This paper extends that finding to the multimodal domain, revealing that text-based reasoning acts to reinforce—rather than correct—initial visual misperceptions. This provides a meaningful insight into the "brittleness" of current visual-reasoning architectures. The delta is **Moderate**.

### Novelty Verdict
Moderate

### Justification
The paper introduces a solid and well-constructed diagnostic benchmark (VIA-Bench) targeting visual illusions and anomalies. While the concept of using visual illusions to stress-test multimodal models overlaps heavily with existing datasets like HallusionBench, GVIL, and Illusory VQA, this paper distinguishes itself through its comprehensive taxonomy and the inclusion of the latest generation of reasoning-heavy MLLMs.

The strongest novel contribution of the paper is its empirical insight into the failure modes of Chain-of-Thought (CoT) prompting in the multimodal space. By demonstrating that CoT can exacerbate errors by rationalizing flawed visual priors, the authors expose a critical limitation in how current models ground their reasoning in visual evidence. Although the dataset itself represents a somewhat predictable extension of prior visual benchmarks, the insights derived from evaluating reasoning-enhanced models on this data elevate the paper's contribution beyond a mere incremental step, earning a verdict of Moderate novelty.

### Missing References
The authors have done a good job citing directly related recent works such as GVIL, Illusory VQA, and HallusionBench. However, they could strengthen the theoretical grounding of their "CoT Paradox" by citing foundational work in multimodal shortcut learning and the "language prior" problem in VQA (e.g., Goyal et al., 2017, "Making the V in VQA Matter"). Additionally, referencing broader literature on confirmation bias in human cognitive psychology would provide a richer context for the observed model behaviors where initial faulty percepts are subsequently rationalized.

5.5