### Significance & Impact Assessment

Parameter-efficient fine-tuning (PEFT) and prompt tuning for Vision-Language Models is a highly saturated research area. While ManiPT achieves state-of-the-art results across 11 datasets, the absolute performance gains over the closest baselines (such as TAC, TAP, or LLaMP) are relatively marginal (e.g., +0.8% average HM in Base-to-Novel, +1.5% in Cross-Dataset transfer). 

However, the impact of this paper lies less in pushing the empirical state-of-the-art and more in providing a rigorous theoretical framework for *why* prompt tuning overfits and *how* geometric constraints alleviate it. The formulation of "manifold drift" and the Rademacher complexity bounds for normalized additive fusion offer a valuable theoretical lens that future researchers can use to analyze or design new PEFT methods. It bridges the gap between empirical heuristic regularization and formal learning theory in the context of foundation models.

Score: 6.0