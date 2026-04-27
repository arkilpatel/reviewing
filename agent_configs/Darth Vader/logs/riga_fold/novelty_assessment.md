The paper introduces RIGA-Fold, a geometric framework for protein inverse folding, and its enhanced variant RIGA-Fold*, which incorporates pre-trained protein language models (ESM-2 and ESM-IF) via a dual-stream iterative refinement strategy. 

The core architectural contributions of RIGA-Fold are the Geometric Attention Update (GAU), which uses edge features directly as attention keys to strictly enforce SE(3)-invariance, and the Global Context Bridge, which uses a dual-gating mechanism to inject long-range dependencies and overcome the oversquashing bottleneck of k-NN graphs. These geometric modifications are clever and theoretically well-motivated, though they build upon existing paradigms of edge-augmented graph attention.

The RIGA-Fold* variant introduces an "Iterative Self-Correction" mechanism (recycling), feeding the predicted sequence back into the frozen ESM-2 encoder to dynamically update semantic priors. While recycling is a staple in protein structure prediction (e.g., AlphaFold2), its explicit application as a dual-stream semantic updater in inverse folding is a meaningful conceptual extension, similar to recent works like LM-Design but executed with a cleaner closed-loop feedback mechanism. 

Overall, while the individual components are largely adaptations of existing techniques (edge-attention, global pooling, PLM integration, recycling), their synthesis into a cohesive, theoretically grounded framework for inverse folding constitutes a solid incremental advance.

Novelty Score: 6.0
