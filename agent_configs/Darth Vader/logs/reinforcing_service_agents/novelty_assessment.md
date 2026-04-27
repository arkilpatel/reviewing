### Claimed Contributions
The authors claim four main contributions:
1. Reframing Task-Oriented Dialogue (TOD) as a multi-granularity reinforcement learning process, moving away from static supervised fine-tuning towards closed-loop interactive learning.
2. Introducing a User-centric Interaction Framework, which serves as a persona-driven environment (simulator) for the agent to interact with.
3. Proposing Cost-aware Multi-turn Policy Optimization (CMPO), which incorporates a "Hybrid Advantage Estimation" strategy that combines session-level outcome rewards, turn-level generative process credits, and a PID-Lagrangian global cost controller.
4. Achieving state-of-the-art performance on customized service scenarios and cross-domain robustness.

### Prior Work Assessment
- **Reframing TOD as interactive RL**: The concept of training conversational or task-oriented agents using reinforcement learning via environment/user interaction is well-established. Prior work on applying RLHF to dialogue and using LLM-based user simulators (e.g., ArCHer, AgentTuning, WebGPT) already shifts the paradigm from static datasets to interactive environments. The delta here is minimal.
- **User-centric Interaction Framework**: Using LLMs prompted with personas as user simulators for training and evaluating dialogue agents is highly common in recent literature. The delta is minimal.
- **Cost-aware Multi-turn Policy Optimization (CMPO)**: The core methodological contribution is the Hybrid Advantage Estimation, which is a linear combination of outcome reward, process reward, and a cost penalty ($\lambda \cdot I$). 
  - Combining Process Reward Models (PRMs) and Outcome Reward Models (ORMs) is a standard technique in recent LLM reasoning and alignment literature (e.g., Lightman et al., 2023).
  - Constrained MDPs (CMDPs) for managing budgets or safety, specifically using PID-Lagrangian controllers, is a standard off-the-shelf technique in the RL community (e.g., Stooke et al., 2020, "Responsive Safety in Reinforcement Learning").
  - The delta is merely applying these standard techniques (PRM + CMDP/Lagrangian) simultaneously to the specific domain of customer service chatbots.

### Novelty Verdict
Incremental

### Justification
The paper represents a straightforward integration of several existing techniques—LLM user simulators, process/outcome reward modeling, and PID-Lagrangian constrained RL—applied to the domain of customer service chatbots. While the application is practically motivated, the methodological delta is minimal. The "Hybrid Advantage Estimation" is simply a linear sum of terms that the community already knows how to optimize. The paper falls into the category of "Creative Combination" but lacks the non-obvious emergence of new properties; it is essentially an engineering effort combining known best practices for a specific use case. The contribution could be easily anticipated by someone familiar with the current intersection of RL and LLMs.

### Missing References
- The paper should more explicitly acknowledge that combining PRMs and ORMs is standard practice in recent alignment literature.
- The use of PID-Lagrangian controllers for CMDPs is a standard RL technique, and its application here does not constitute a novel methodological contribution on its own.

Score: 3.5
