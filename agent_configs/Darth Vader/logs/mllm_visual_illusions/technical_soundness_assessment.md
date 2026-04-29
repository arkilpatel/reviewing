### Claims Inventory

**Theoretical & Conceptual Claims**
1. The question-answer pairs in VIA-Bench are curated such that the correct option is statistically independent of the textual priors in the question.
2. Dealing with visual illusions and anomalies forces MLLMs to consciously weigh visual evidence against internal knowledge, exposing failure modes missed by standard evaluations.
3. Purely text-based CoT is insufficient for resolving visual illusions because, without continuous visual grounding, it tends to reinforce perceptual errors or rely on ungrounded textual shortcuts.

**Empirical Claims**
4. SOTA MLLMs lag substantially behind humans on VIA-Bench (humans achieve 93.30%, while the best MLLM reaches 69.23%).
5. Text-only GPT-4-Turbo demonstrates surprisingly high accuracy on motion and geometric illusions without visual input.
6. CoT reasoning often degrades performance on VIA-Bench instead of improving it, as it tends to rationalize deceptive priors.
7. No single model performs uniformly well across all categories, and performance does not scale consistently with parameter count.

### Verification Results
1. **Textual prior independence**: **Error Found**.
2. **Visual illusions expose failure modes**: **Verified**.
3. **CoT is insufficient**: **Verified**.
4. **MLLMs lag behind humans (69.23% best)**: **Verified** (though the average metric calculation is highly irregular).
5. **Text-only GPT-4-Turbo high accuracy**: **Verified** (matches Table 1).
6. **CoT degrades performance**: **Verified** (supported by Table 2).
7. **No uniform performance / scaling**: **Verified**.

### Errors and Concerns

**1. Claim of Textual Prior Independence is False (Severity: Significant Error)**
The paper claims in Section 2.2 that "the question-answer pairs are curated such that the correct option y is statistically independent of the textual priors in q." However, the authors' own blind evaluation contradicts this. Text-only GPT-4-Turbo achieves an 87.95% accuracy on Motion Illusions (MI) and 61.11% on Geometric and Spatial Illusions (GSI). This proves that the ground truth for these categories is highly predictable purely from textual and commonsense priors (e.g., inferring that a static "image" cannot physically be "moving"). The dataset fails its own criteria for statistical independence from textual priors, as text alone is sufficient to solve nearly 90% of the MI category.

**2. Obfuscated Average Metric in Table 1 (Severity: Significant Error)**
The `Avg.` column in Table 1 is calculated by taking the macro-average of the 6 categories for the `Match` protocol, the macro-average for the `Judge` protocol, and then averaging those two averages together. Mixing a deterministic regex match score with an LLM-as-a-judge score into a single unified metric is conceptually flawed and highly non-standard. This obfuscates the actual model performance, and the methodology for calculating this specific column is never disclosed in the text.

**3. Massive Match/Judge Discrepancy for Gemini-3-pro (Severity: Concern)**
In Table 1, Gemini-3-pro scores 69.87% on MI under the `Match` protocol, but 99.36% under the `Judge` protocol. A ~30% gap between a regex matcher and an LLM judge indicates a severe failure in either the extraction rules or extreme hallucination by the judge. The paper does not acknowledge or investigate this massive discrepancy.

**4. Typo in Table 1 Formatting (Severity: Minor Error)**
The row for Gemini-3-pro in Table 1 merges the rank and the first score: `143.51` instead of `1 43.51`. 

### Internal Consistency Check

**1. Contradiction between Figure 4 and Figure 12 (Severity: Significant Error)**
There is a blatant internal contradiction regarding Gemini-2.5-pro's performance on the 6-finger visual anomaly task.
* In **Figure 4**, the model response visualization shows Gemini-2.5-pro incorrectly predicting option **C (5 fingers)**.
* In **Figure 12**, using the exact same image and question as a positive case study, the text explicitly shows Gemini-2.5-pro correctly predicting option **A (6 fingers)**.

**2. Missing Content and Contradictions in Appendix H / Figure 7 (Severity: Minor Error)**
The caption for Figure 7 describes the reasoning traces of three models (InternVL-3.5-8B, Qwen3-VL-30B, and Gemini-2.5-pro), but the figure only contains two text blocks. Furthermore, the caption claims Gemini-2.5-pro "preserves a readable and well-structured reasoning process," which directly contradicts the text in Appendix H immediately preceding it, which states: "The proprietary model Gemini-2.5-pro does not explicitly expose its reasoning chain."

### Theory-Practice Gap Assessment
While the paper is primarily empirical, there is a distinct gap between the theoretical design of the dataset (intended to measure purely visual perception uninfluenced by text) and the practical reality of the data. Because visual illusions often involve impossible physical states (like a static image moving), standard textual commonsense perfectly predicts the "intrinsic truth" of the image, bypassing the need for visual intelligence entirely. The authors acknowledge the text-only baseline's success but fail to recognize that this fundamentally invalidates their claim of having curated a text-independent benchmark.

### Overall Technical Soundness Verdict
Significant concerns

4
