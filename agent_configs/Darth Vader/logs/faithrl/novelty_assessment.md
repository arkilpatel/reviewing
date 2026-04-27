### Claimed Contributions
The paper introduces FaithRL, a reinforcement learning framework that optimizes for reasoning faithfulness. The core contributions are: (1) a novel optimization objective maximizing reasoning faithfulness (Objective C); (2) a geometric reward (Rgeo) based on the Truthful Helpfulness Score (THS); and (3) Faithfulness-Aware Advantage Modulation (FAAM) for step-level credit assignment.

### Prior Work Assessment
The conceptual framework heavily overlaps with existing Process Reward Models (PRMs) and step-level reinforcement learning. The paper cites factuality-driven RL but does not properly contextualize FAAM within the broader literature of dense step-level reward modulation. Masking or discounting the advantage of incorrect intermediate steps is standard practice in token-level RL. Furthermore, the Truthful Helpfulness Score (THS) and its geometric interpretation are directly inherited from CRaFT (Zhu et al., 2025). The derivation of Rgeo from THS is a straightforward algebraic manipulation rather than a conceptual breakthrough. 

### Novelty Verdict
The novelty is low. The proposed framework essentially combines an LLM-as-a-judge for step-level verification with advantage masking. The theoretical framing of Objective C rephrases the well-known goal of process supervision.

### Justification
While combining THS-based reward weighting with step-level advantage modulation is technically a new composition, the individual components are well-established. The paper dresses standard PRM techniques in theoretical language without introducing fundamentally new mechanisms.

### Missing References
- Lightman et al., 2023 ("Let's Verify Step-by-Step"): Foundational work on Process Reward Models.
- Uesato et al., 2022 ("Solving math word problems with process- and outcome-based feedback").

Score: 3