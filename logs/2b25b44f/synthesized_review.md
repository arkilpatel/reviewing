# Review of "pSAE-chiatry: Utilizing Sparse Autoencoders to Uncover Mental-Health-Related Features in Language Models"

## Summary
The paper explores the internal representations of mental-health-related features (MHRFs) in the Gemma-2-2B language model using sparse autoencoders (SAEs). Specifically, the authors utilize the public GemmaScope tool via the Neuronpedia interface to search for specific terms ("sad", "suicide", "mania", "paranoia") within auto-generated feature labels across the model's 25 layers. They find features related to "sad" and "suicide" but report finding no features related to "mania" or "paranoia." They further demonstrate that a single suicide-related feature (Feature 15435, Layer 25) activates more strongly when prompted with queries about suicide compared to queries about homicide, and show that amplifying this feature causes the model to generate text about suicide.

## Strengths
- The problem domain—improving the safety of language models for users experiencing psychiatric emergencies—is of high societal importance.
- Applying mechanistic interpretability techniques to specific critical domains like mental health is a worthwhile direction.

## Weaknesses and Critical Flaws
Unfortunately, the execution of this study is fundamentally flawed, and the paper lacks the necessary technical and experimental rigor for a scientific publication. It resembles an informal blog post more than a scientific study.

**1. Flawed Methodology for Feature Discovery (Technical Soundness):**
The authors claim that the model lacks features for "mania" or "paranoia" because a keyword search for these terms in GemmaScope yielded no results. This is a critical methodological error. The text labels in GemmaScope are auto-generated descriptions (often by another LLM like GPT-4) meant to summarize the texts that activate a feature. The absence of a specific substring in these auto-generated labels does not imply the absence of the concept in the model's internal representation. The feature might be polysemantic, the labeler might have used synonyms (e.g., "delusions," "grandiosity"), or the label might simply be imprecise. Drawing sweeping conclusions about the model's handling of complex psychiatric symptoms based on this naive string-matching approach is invalid.

**2. Complete Lack of Experimental Rigor:**
The empirical evaluation is virtually non-existent.
- **Sample Size:** The authors test exactly four handcrafted prompts (two suicide-related, two homicide-related) to evaluate feature activation, and exactly one prompt to evaluate steering behavior.
- **No Datasets or Baselines:** There is no use of standard NLP mental health datasets or any structured evaluation set. There are no baselines for comparison.
- **Statistical Significance:** With $N=4$ for activation and $N=1$ for steering, no statistical conclusions can be drawn.
- **Scope:** The authors limit their manual inspection and steering to a single feature (Feature 15435 in Layer 25) out of millions, which provides anecdotal evidence at best.

**3. Minimal Novelty and Impact:**
The paper does not introduce any new methodology, framework, or dataset. The entire study consists of using an existing web interface (Neuronpedia) to search for strings and move a slider to steer a single prompt. While applying existing tools to new domains can sometimes be impactful, the insights generated here are trivial (e.g., showing that a feature labeled "suicide" activates more on a prompt about suicide than a prompt about homicide). This work does not advance the state-of-the-art in mechanistic interpretability or mental health AI safety in any meaningful way.

## Scoring Breakdown
- **Impact (40%):** 2.0 / 10
- **Technical Soundness (20%):** 2.5 / 10
- **Experimental Rigor (20%):** 1.0 / 10
- **Novelty (20%):** 2.0 / 10

**Score Calculation:** (4.0 * 2.0 + 2.0 * 2.5 + 2.0 * 1.0 + 2.0 * 2.0) / 10 = (8.0 + 5.0 + 2.0 + 4.0) / 10 = 19.0 / 10 = 1.9

**Final Score:** 1.9