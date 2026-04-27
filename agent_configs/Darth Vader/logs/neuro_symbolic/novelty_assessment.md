This paper introduces Neuro-Symbolic Synergy (NeSyS), a framework for interactive world modeling in text-based environments. The core challenge addressed is that Large Language Models (LLMs), while excellent at capturing semantic priors and stochastic dynamics, often struggle with strict deterministic rules and constraints required for world modeling.

The primary novelty of NeSyS is twofold:
1. **Probability Modification via Executable Rules:** Instead of the standard approach of prepending symbolic rules to the LLM's context prompt (which relies heavily on the LLM's instruction-following capabilities and context window), NeSyS directly evaluates candidate transitions using Python functions and modifies the LLM's output probability distribution via an energy-based shifting factor.
2. **Rule-Guided Data Selection:** The authors introduce a complementary training paradigm where the neural WM is fine-tuned only on trajectories that the symbolic rules fail to explain (i.e., cases where no rules fire). This focuses the LLM on capturing complex, intuitive dynamics rather than memorizing deterministic rules, reducing the required training data by over 50%.

The automated pipeline for rule induction—clustering LLM errors and using a stronger model to synthesize and iteratively refine Python rules—is well-engineered. While neuro-symbolic approaches are common, the specific integration via logit modification coupled with complementary data selection is highly novel and practical.

Novelty Score: 8.0
