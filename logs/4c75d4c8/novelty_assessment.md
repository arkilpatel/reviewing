### Novelty & Originality Assessment

**Claimed Contributions:**
1. Formulating the "functional retargeting" problem for learning dexterous manipulation from human hand-object demonstrations.
2. DexMachina: A curriculum-based RL algorithm using virtual object controllers (VOCs) to guide early-stage exploration.
3. A simulation benchmark containing 6 dexterous hands and 5 articulated objects from the ARCTIC dataset.

**Prior Work Assessment:**
- *Functional Retargeting / Learning from Video:* Learning from human hand demonstrations is a well-explored area (e.g., DexCap, AnyTeleop). Prior works like ObjDex [35] and ManipTrans [36] have explored similar bimanual retargeting tasks. The problem formulation itself is an incremental formalization of existing efforts.
- *Curriculum Learning with Virtual Controllers:* Curriculum learning by relaxing physics is known (e.g., reducing gravity or friction, as in [36]). However, applying explicit Virtual Object Controllers (PD controllers driving the object along the demonstration trajectory) and decaying their gains as the policy learns is a neat, task-specific adaptation for object manipulation. This effectively sidesteps the immense exploration challenge in long-horizon dexterous manipulation. While standard in concept (similar to trajectory tracking or guided exploration), its specific application here is effective.
- *Benchmark & Cross-Embodiment Evaluation:* Evaluating 6 diverse hands in a unified simulation (Genesis) on complex bimanual tasks is a significant artifact contribution. Most prior works focus on a single hand or much simpler tasks (e.g., single-hand grasping).

**Novelty Verdict:** Substantial

**Justification:**
While the individual components (RL with dense rewards, curriculum learning, human demonstrations) are well-known, the specific mechanism of using decaying Virtual Object Controllers to bootstrap bimanual manipulation of articulated objects is a clever and non-trivial methodological contribution. Furthermore, the artifact novelty of providing a unified benchmark across 6 different dexterous hands elevates the paper's contribution significantly, enabling new types of hardware-comparative research.