# Final Review: Evaluating MLLMs on Visual Illusions

This paper introduces VIA-Bench, a diagnostic benchmark consisting of 1,004 multiple-choice questions designed to evaluate Multimodal Large Language Models (MLLMs) on visual illusions and anomalies. By evaluating over 20 state-of-the-art MLLMs against human performance, the authors explore how current architectures process deceptive visual stimuli. The paper also investigates the role of Chain-of-Thought (CoT) prompting in these scenarios, identifying a "CoT Paradox" where text-based reasoning often degrades rather than improves performance by rationalizing faulty visual priors. 

The following sections provide an exhaustive evaluation of the paper based on four core criteria.

### Novelty

The paper introduces a solid diagnostic benchmark targeting visual illusions and anomalies across six distinct categories (color, motion, gestalt, geometric/spatial, general visual illusions, and visual anomalies). While the fundamental concept of probing multimodal models with visual illusions is not entirely new—overlapping heavily with existing datasets like GVIL, Illusory VQA, and HallusionBench—the work distinguishes itself through its systematic taxonomy and the high-quality, human-in-the-loop curation of its data. 

The most compelling novel contribution of the paper is not the benchmark itself, but the empirical insights derived from it, particularly regarding the failure modes of Chain-of-Thought (CoT) prompting in the multimodal space. The paper effectively extends recent findings about CoT's limitations on counter-intuitive text tasks into the multimodal domain, revealing that text-based reasoning often acts to reinforce and rationalize initial visual misperceptions rather than correct them. This insight exposes a critical vulnerability in how current reasoning-enhanced models ground their logic in visual evidence. However, the theoretical framing could be further strengthened by connecting this "CoT Paradox" to foundational work in multimodal shortcut learning and confirmation bias in cognitive psychology. Ultimately, the novelty is moderate, providing valuable empirical insights built upon a somewhat predictable extension of prior visual benchmarks.

### Technical Soundness

While the paper makes interesting empirical claims, its technical soundness is significantly compromised by several severe methodological flaws and internal contradictions. 

Most critically, the foundational claim that the VIA-Bench dataset is curated such that the correct option is "statistically independent of the textual priors" is demonstrably false. The authors' own blind evaluation (text-only GPT-4-Turbo) achieves 87.95% accuracy on Motion Illusions and 61.11% on Geometric and Spatial Illusions without any visual input. This proves that the ground truth for these categories is highly predictable purely from standard textual and commonsense priors (e.g., inferring that a static image cannot physically move). This fundamental theory-practice gap invalidates the claim that the benchmark isolates purely visual perception.

Furthermore, there are significant issues with the evaluation metrics and data presentation. The "Avg." column in Table 1 obfuscates true model performance by averaging a deterministic regex match score with an LLM-as-a-judge score, a highly non-standard and conceptually flawed metric combination. This leads to unexplained anomalies, such as a ~30% gap between the Match and Judge protocols for Gemini-3-pro on Motion Illusions, indicating either a failure in extraction rules or extreme judge hallucination. Additionally, there is a blatant internal contradiction regarding model performance: Figure 4 depicts Gemini-2.5-pro incorrectly predicting a 6-finger visual anomaly, while Figure 12 explicitly uses the exact same image and question to showcase the model predicting it correctly. These significant errors and inconsistencies severely undermine the reliability of the technical execution.

### Experimental Rigor

Despite the conceptual and technical flaws mentioned above, the paper's experimental design is generally quite robust and extensive. The evaluation encompasses over 20 state-of-the-art MLLMs—including the latest proprietary, open-source, and reasoning-enhanced models—evaluated under unified prompting formats. The inclusion of strong baselines is highly commendable; the use of a "Blind Evaluation" to gauge reliance on textual priors, a random choice baseline to establish the floor, and human performance to establish the ceiling ensures a comprehensive understanding of the models' capabilities. The fact that humans achieve 93.30% accuracy while the best model reaches only 69.23% proves the benchmark is demonstrably challenging and provides meaningful discriminative signal. Furthermore, running each experiment 5 times to compute the average is a rare and highly rigorous practice in expensive API-based evaluations.

The error analysis is exceptionally thorough. Rather than merely reporting aggregate numbers, the authors actively isolate the root causes of failure—identifying issues like initial visual misperception, self-negating uncertainty, and overthinking (repetitive CoT loops)—and provide qualitative case studies detailing step-by-step reasoning traces. 

However, there are notable gaps in the rigorous reporting. Despite running 5 seeds, the main tables fail to report standard deviations, error bars, or confidence intervals, making it difficult to assess the stability of the results. Additionally, there is no rigorous data contamination analysis to ensure the benchmark images were not present in the training corpora of the evaluated models. Statistical significance tests are also missing for the central claim that CoT degrades performance, which is necessary to confirm that the observed drops are statistically meaningful and not just variance.

### Significance & Impact

The paper offers a valuable diagnostic evaluation suite that highlights specific vulnerabilities in MLLMs, particularly their over-reliance on internalized canonical priors rather than raw visual evidence. However, its overall technical significance is bounded. Because it does not introduce a new method, architecture, or tool, and because the community already possesses numerous robustness benchmarks, VIA-Bench is likely to be adopted primarily by a niche subset of researchers focusing specifically on perceptual anomalies rather than becoming a general-purpose standard.

Conversely, the scientific significance of the paper is quite strong. By uncovering the "CoT Paradox" within multimodal contexts, the paper answers a critical question about how current MLLMs "think." Demonstrating that textual reasoning is brittle and insufficient for resolving perceptual conflicts without continuous visual grounding is a highly valuable insight. This finding points out a fundamental flaw in the field's current approach to multimodal CoT and is likely to inform future work proposing new architectures. Given this, the paper is projected to receive moderate citation traction within the subfields of MLLM hallucinations and reasoning, but its overall impact will be capped by its nature as a specialized diagnostic tool rather than a foundational capability breakthrough.

### Scoring Breakdown

*   **Impact:** 4.5
*   **Technical Soundness:** 4.0
*   **Experimental Rigor:** 7.0
*   **Novelty:** 5.5

**Formula applied:** `score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`

**Final Score:** 5.1