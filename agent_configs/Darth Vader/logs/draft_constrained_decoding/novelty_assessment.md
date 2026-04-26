### Claimed Contributions
1. Identifying that low feasible mass (the probability assigned to valid continuations) is the root cause of semantic distortion and trajectory bias in constrained decoding.
2. Introducing Draft-Conditioned Constrained Decoding (DCCD), a two-step inference procedure that generates an unconstrained draft and then applies constrained decoding conditioned on that draft to ensure valid formatting while preserving reasoning quality.
3. Demonstrating that DCCD improves strict structured accuracy across multiple model scales and reasoning tasks, and scales better with test-time compute compared to standard constrained decoding.

### Prior Work Assessment
The observation that strict constrained decoding (such as enforcing JSON schemas) degrades the underlying reasoning capabilities of LLMs has been well-documented in recent literature (e.g., Tam et al., "Let Me Speak Freely"; Schall et al., "Hidden Flaws of Structured Generation"). The authors acknowledge this prior work. 

The proposed solution, DCCD, fundamentally consists of a two-pass generation: first, allow the model to reason without structural constraints, and second, force the structural constraints on the output while the unconstrained reasoning is in the context. In practice, this exact pipeline (generating a free-text scratchpad or CoT, followed by a parsing/formatting LLM call) is a standard design pattern widely used by practitioners to avoid the pitfalls of direct structured generation. While the formalization using KL-divergence and "feasible mass" is a neat conceptual wrapper, the algorithmic delta over existing practitioner workflows and standard CoT-then-format strategies is very minimal.

### Novelty Verdict
Incremental

### Justification
The paper provides a formal theoretical framing (reverse-KL projection and feasible mass) for a known empirical phenomenon (constrained decoding hurts reasoning). However, the resulting method—generating an unconstrained draft and then conditioning on it for formatting—is highly predictable and already a standard workaround in the community. The method is essentially an application of Chain-of-Thought prompt engineering disguised as a novel decoding algorithm. It does not introduce a fundamentally new capability or paradigm.

### Missing References
The paper adequately cites recent work on the limitations of constrained decoding, but should also explicitly discuss the standard practitioner pipelines (e.g., two-stage reasoning and formatting agents in LangChain or LlamaIndex) which effectively implement this exact "draft-then-constrain" logic.

Score: 3.5