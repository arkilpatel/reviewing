# Experimental Rigor Assessment: Rethinking Personalization in Large Language Models at the Token Level

## Breadth of Evaluation
The experimental section is quite comprehensive:
- **Datasets:** LongLaMP (3 tasks: PAG, PRW, PTW), ALOE (multi-turn dialogue), and LaMP (short-text tasks). This covers a wide range of personalization scenarios.
- **Models:** Qwen3-4B, Qwen3-14B, and Llama3-8B-Instruct. This demonstrates scalability and cross-model applicability.
- **Metrics:** ROUGE-L, METEOR, and LLM-as-a-Judge (G-Eval style). The inclusion of LLM-as-a-Judge is important for personalization where word-overlap metrics often fail.

## Comparison and Baselines
- The authors compare against Standard CE, LossCE (Lin et al., 2024a), and EntCE (Wang et al., 2025). These are relevant and strong baselines for token-weighting strategies.
- The results (Table 1) show PerCE consistently outperforming all variants on PRW and PTW tasks, often by large margins.

## Transferability and Generalization
- **Cross-Task Transfer:** Table 3 shows that training on one task (e.g., PRW) and evaluating on others (e.g., PAG, PTW) works better with PerCE than CE.
- **Cross-Scenario Transfer:** Evaluation on ALOE (Table 4) shows that models trained with PerCE on LongLaMP generalize well to distinct dialogue scenarios, even when persona information is not explicitly provided in the same format.

## Robustness Analysis
- **Learning Rate:** Table 2 shows PerCE is more stable across different learning rates compared to standard CE, which crashed/degraded at higher LRs.
- **Clipping Thresholds:** Table 12 explores the sensitivity to $m$ and $M$, showing the method is relatively stable.
- **Synthetic Experiment:** Appendix A (Page 12) provides a controlled experiment to validate that PIR actually identifies personal tokens correctly, outperforming word-matching and LLM-as-a-judge baselines.

## Potential Weaknesses in Rigor
- The improvements on PAG (Personalized Abstract Generation) are marginal or even negative in some cases. The authors attribute this to the task being more constrained, which is a reasonable explanation, but it highlights a limitation.
- The "extra forward pass" cost is mentioned as minimal, but a more detailed breakdown of training time vs. performance gain would be beneficial (though Table 6 shows the persona-removed context is 10x shorter, which supports the claim).

Overall, the experimental rigor is excellent and follows ICML standards for thoroughness.