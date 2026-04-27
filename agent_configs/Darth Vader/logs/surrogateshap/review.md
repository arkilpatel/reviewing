# Comprehensive Review of "SurrogateSHAP: Training-Free Contributor Attribution for Text-to-Image (T2I) Models"

This paper tackles the highly relevant and computationally challenging problem of assigning Shapley value-based data attribution to contributors in Text-to-Image (T2I) diffusion models. To overcome the combinatorial explosion and retraining costs inherent in Shapley estimation, the authors propose SurrogateSHAP. This framework introduces a training-free "proxy game" that estimates a subset's utility by adjusting the test-time label frequencies of a fully pre-trained model. To further reduce subset queries, they fit a gradient-boosted tree (GBT) surrogate and compute the final Shapley values analytically via TreeSHAP. The method is evaluated across multiple datasets and utility metrics, demonstrating strong alignment with counterfactual retraining in their tested regimes.

While the problem domain is crucial and the proposed efficiency optimizations are appealing, a deep technical analysis reveals a fundamental, structural flaw in the method that invalidates its primary claim as a general "data attribution" framework. SurrogateSHAP does not evaluate the quality or influence of the *training data*; it solely evaluates the utility of *conditioning labels* present in a frozen model. 

Below is the detailed evaluation across the four criteria.

## Novelty
The paper creatively combines Shapley values with two distinct approximations to bypass the prohibitive costs of T2I retraining: (1) a proxy game that uses a test-time distribution mixture of conditional generators, and (2) TreeSHAP applied over a GBT surrogate to reduce sample complexity. Utilizing tree-based surrogates to accelerate Shapley estimation is an interesting variance-reduction adaptation for dataset valuation. However, the novelty is severely undermined by the proxy game itself. By substituting the retrained conditional $p_{\theta_S}(x|c)$ with the fully trained target conditional $p_\theta(x|c)$, the proxy inherently shifts the task from true data attribution to prompt/concept ablation. While the combination of these techniques is new to this domain, the resulting mechanism solves the wrong problem, diminishing the scientific contribution of the work.

**Score: 4/10**

## Technical Soundness
The technical soundness of SurrogateSHAP is fatally compromised by the core mathematical formulation of its proxy game (Equation 5). The proxy utility assumes that the retrained model's conditional distribution can be perfectly approximated by the fully-trained model's conditional, meaning a subset's utility is evaluated purely by altering the mixing weights (class frequencies) $P_S(y)$ of the *frozen* optimal conditionals. 

This introduces a catastrophic flaw: SurrogateSHAP evaluates the importance of a label/prompt rather than the specific data samples provided by a contributor. If two contributors provide data for the exact same prompt (e.g., "a dog"), but one provides high-quality, perfectly framed images and the other provides noisy, irrelevant images, SurrogateSHAP will assign them identical marginal utility (assuming equal sample counts). The proxy game is structurally incapable of evaluating intra-class data quality or capturing the representation drift that occurs when high-quality data is removed. 

The theoretical bound (Proposition 4.2) and the low representation drift observed in the paper only hold because the experimental design artificially sidesteps this flaw. The proxy game only "works" if we assume that removing data does not degrade the model's ability to generate that concept—an assumption that contradicts the fundamental premise of deep learning.

**Score: 2/10**

## Experimental Rigor
At first glance, the experimental section appears rigorous. The authors evaluate their method across three distinct datasets (CIFAR-20, ArtBench, Fashion-Product) using multiple appropriate metrics (IS, FID, LPIPS, Aesthetics, Diversity) and compare it against a vast array of baselines (TRAK variants, DAS, sFT). They also provide computationally expensive counterfactual retraining curves.

However, the experimental design contains a critical blind spot that masks the method's fundamental flaw: in every setup, there is a strict 1-to-1 mapping between a contributor and a unique conditioning label (e.g., unique fine-grained classes in CIFAR, unique artists in ArtBench, unique brands in Fashion-Product). By rigidly defining "Player = Condition," the authors ensure that removing a player removes the entire condition from the prompt mixture, which minimizes the intra-class representation drift that their proxy game cannot handle. The experiments entirely fail to evaluate the method in a realistic scenario where multiple independent contributors provide data for the same condition. Without demonstrating the ability to differentiate data quality among contributors sharing a prompt, the empirical validation of the framework as a "data marketplace" valuation tool is invalid.

**Score: 4/10**

## Impact
The motivation of the paper—enabling fair compensation in data marketplaces and sustainable revenue sharing for generative AI—is of paramount importance to the ICML community. Unfortunately, because SurrogateSHAP functionally performs concept ablation rather than true data attribution, it cannot be safely deployed for its intended use case. Valuing data based purely on its label frequency rather than its content would create perverse incentives in data marketplaces, rewarding low-effort, low-quality data dumps as long as they match high-utility prompts. 

While the method demonstrates some utility as a tool for auditing discrete concepts (as shown in the clinical spurious correlation case study), its framing as a general data valuation framework is deeply misleading. Deploying this in real-world creative workflows would fail to fairly compensate high-quality contributors, actively undermining the goal of sustainable data marketplaces.

**Score: 3/10**

## Scoring Breakdown
- Impact: 3
- Tech_Soundness: 2
- Exp_Rigor: 4
- Novelty: 4

Overall Score = (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10
Overall Score = (4.0 * 3 + 2.0 * 2 + 2.0 * 4 + 2.0 * 4) / 10 = (12 + 4 + 8 + 8) / 10 = 3.2
