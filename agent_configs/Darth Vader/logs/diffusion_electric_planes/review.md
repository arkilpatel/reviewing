This paper tackles the complex problem of generating conceptual engineering designs for electric vertical take-off and landing (eVTOL) aircraft using Simulation-Based Inference (SBI). The authors introduce a hierarchical probabilistic model utilizing two diffusion models: `MixeDiT` for sampling discrete aircraft topologies alongside continuous observations, and `MaskeDiT` for sampling the corresponding variable-dimensional continuous parameters.

### Novelty
### Claimed Contributions
1. A hierarchical probabilistic model to generate conceptual eVTOL aircraft designs containing discrete and continuous variables.
2. `MixeDiT`: A diffusion model that jointly samples discrete topologies and continuous observations by coupling Riemannian Diffusion Language Modeling (RDLM) with continuous diffusion processes.
3. `MaskeDiT`: A masked diffusion transformer (extending the Simformer architecture) that handles continuous parameters conditioned on topology, utilizing a token masking scheme to gracefully support variable-dimensional parameter spaces depending on the selected topology.

### Prior Work Assessment
- **RDLM (Jo & Hwang, 2025):** The paper leverages this for discrete diffusion on Riemannian manifolds. The delta here is coupling this specific continuous-formulation of discrete diffusion with a standard continuous diffusion process for the observations.
- **Simformer (Gloeckler et al., 2024):** A recent transformer-based diffusion model for Simulation-Based Inference (SBI). The delta is the addition of the topology masking scheme (`M_tau`), which allows the Simformer to condition on and generate variable-length parameter sets across 144 different aircraft topologies, whereas prior SBI methods typically require a separate model per topology.
- **UWMs (Zhu et al., 2025):** Integrated independent continuous diffusion processes. The paper adapts this to couple discrete and continuous processes.

### Novelty Verdict
Substantial

### Justification
The paper demonstrates a strong "Creative Combination" and "Methodological" novelty. While the individual components (RDLM, Simformer, UWMs) exist, combining them to perform SBI over a mixed discrete-continuous and variable-dimensional space is highly non-trivial. The insight to use the continuous flow on a hypersphere (from RDLM) alongside a standard continuous diffusion process for observations allows for a unified training objective. Furthermore, the variable-dimension masking in MaskeDiT elegantly solves the problem of training one SBI model across completely different topologies (e.g., monoplane vs biplane), which previously required completely separate models. 

### Missing References
None glaringly obvious, the paper cites recent and relevant work in both SBI and diffusion modeling (up to 2025).



### Technical Soundness
### Claims Inventory
- **Methodological/Theoretical:** MixeDiT jointly models the discrete topology and continuous observations using a combined continuous diffusion framework (combining RDLM and noise-prediction score matching).
- **Methodological:** MaskeDiT can model variable-dimensional parameter distributions by utilizing a topology-based masking scheme during both attention and loss computation.
- **Empirical:** MaskeDiT achieves comparable likelihood and posterior estimation (measured via MMD and C2ST) to independent Neural Likelihood Estimation (NLE) models, while generalizing across topologies.
- **Conceptual/Physical:** The generated samples rediscover known physical laws in aircraft design (e.g., drag proportional to lift squared, increased mass leading to more wings).

### Verification Results
- **MixeDiT Formulation:** Verified. Combining the RDLM importance-sampled cross-entropy loss (Eq. 2) with the standard continuous score matching loss (Eq. 3) via a simple weighted sum (Eq. 4) is mathematically sound given they operate on conditionally independent paths during the forward process.
- **MaskeDiT Masking Scheme:** Verified. Applying the outer product of the binary topology mask to the attention matrix and normalizing the diffusion loss only over the non-masked components (Eq. 6) is a standard and robust way to handle variable-length sequences in transformers.
- **Physical Consistency:** Verified. The scatter plots in the case studies (e.g., $C_D$ vs $C_L$) clearly show the expected near-quadratic relationship ($C_D \approx C_{D,0} + K C_L^2$). The topological shifts (e.g., higher mass leading to biplane designs) are physically logical.
- **C2ST Exclusion:** Concern. The authors mention: "We remove strongly correlated observation variables whose samples collapse onto a near-linear relationship, as C2ST is not informative in these cases." This is slightly concerning as dropping dimensions can artificially inflate C2ST scores (make them closer to 0.5), but the justification is transparently stated.

### Errors and Concerns
- **Minor Concern (C2ST computation):** Dropping highly correlated variables before running the Classifier Two-Sample Test (C2ST) can be risky. While near-linear relationships can cause numerical instability in some classifiers, completely removing them means the metric isn't evaluating the full joint distribution. 

### Internal Consistency Check
The paper is highly consistent. The claims made in the methodology regarding the ability to sample across topologies are directly supported by Case Study B and C, which show smooth transitions and comparisons between monoplane and biplane configurations.

### Theory-Practice Gap Assessment
The models are trained on a finite dataset of 144 topologies and their simulated observations. The experimental conditions perfectly match the claims of Simulation-Based Inference (SBI) for conceptual design.

### Overall Technical Soundness Verdict
Sound with minor issues



### Experimental Rigor
### Claims-to-Experiments Mapping
- *Claim:* MixeDiT accurately models the marginal distribution of topologies. -> *Experiment:* Figure 3 compares KL divergence between test data marginals and MixeDiT samples.
- *Claim:* MaskeDiT matches the performance of topology-specific models. -> *Experiment:* Table 1 compares MaskeDiT against NLE using MMD and C2ST.
- *Claim:* The hierarchical model captures complex physical trends. -> *Experiment:* Case Studies A-D (Figures 6-11).

### Baseline Assessment
- **MixeDiT:** Only compared against a uniform distribution. A stronger baseline would be a discrete Markov-chain based diffusion model (like D3PM) to prove that the RDLM continuous-relaxation approach is actually superior for this task.
- **MaskeDiT:** Compared against Neural Likelihood Estimation (NLE). This is an appropriate and strong baseline, as NLE represents standard SBI practice. The fact that NLE requires separate models for each topology while MaskeDiT uses one unified model makes this a very fair comparison.

### Dataset Assessment
The dataset consists of simulations from SUAVE for 144 distinct eVTOL topologies. It is highly relevant to the paper's claims and domain.

### Metric Assessment
The authors use MMD and C2ST for likelihood comparison, which are standard for evaluating generative models in SBI. However, their decision to exclude "strongly correlated observation variables" from the C2ST computation (using a Pearson correlation threshold of >0.9) weakens the metric's completeness.

### Statistical Rigor
- **Variance reporting:** Table 1 reports standard deviations across the 10 most frequent topologies, which is good.
- **Number of runs:** The paper lacks explicit details on the number of random seeds used for the training of the models themselves. The case studies generate samples, but the robustness of the model training is not statistically quantified.

### Ablation Assessment
There is a notable lack of ablation studies. The paper proposes a hierarchical combination (MixeDiT + MaskeDiT), but does not ablate this design. For example:
- What if the topology and parameters were sampled jointly in a single flat MaskeDiT model?
- What is the sensitivity of the loss weighting parameter $\gamma$ in Eq. 4?
These missing ablations prevent us from knowing which components are strictly necessary.

### Missing Experiments
1. Comparison of MixeDiT against standard discrete diffusion (D3PM).
2. Ablation on the $\gamma$ weighting parameter between discrete and continuous losses.
3. A baseline showing a single flattened diffusion model (without the explicit hierarchy) to prove the hierarchy is needed.

### Error Analysis Assessment
The paper does not explicitly analyze failure cases. It shows that the model successfully recovers physical trends (Case Studies A-D), but it doesn't characterize instances where the diffusion model generates physically impossible aircraft or violates constraints.

### Overall Experimental Rigor Verdict
Mostly rigorous with gaps



### Impact
### Impact Assessment

**1. Technical Significance (70%):**
The technical utility of this paper is quite high within the specific domain of engineering design and Simulation-Based Inference (SBI). Being able to amortize the cost of multi-physics simulators over a highly variable, mixed discrete-continuous design space (like aircraft topologies) is a major practical challenge. The introduction of MaskeDiT to handle variable-dimensional parameter spaces via topological masking is an elegant solution that could easily be adopted in other fields requiring SBI over graphs or topologies (e.g., molecule design, structural engineering). 

**2. Scientific Significance (30%):**
Scientifically, the paper provides a solid proof-of-concept that Riemannian Diffusion Language Modeling (RDLM) can be seamlessly coupled with continuous diffusion to jointly sample discrete structural choices and continuous observations. It doesn't necessarily overturn any existing paradigms, but it bridges the gap between discrete and continuous diffusion for practical SBI applications. 

**3. The 3-Year Citation Projection:**
This paper sits at the intersection of generative AI and aerospace engineering. While the methodology is sound, the direct application to eVTOL design might limit its immediate visibility in the broader core ML community. However, researchers working in AI for Science, physical simulations, and combinatorial design spaces will find the variable-dimension masking technique highly useful. I expect this paper to accrue around 20-40 citations in the next 3 years as a strong applied ML paper.



### Scoring Breakdown
- **Impact:** 6.0
- **Technical Soundness:** 8.0
- **Experimental Rigor:** 6.0
- **Novelty:** 7.0

**Formula:** `(4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`
**Final Score:** 6.6
