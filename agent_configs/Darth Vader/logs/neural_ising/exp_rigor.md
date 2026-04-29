### Claims-to-Experiments Mapping
1. **Competitive/SOTA performance on CO tasks**: Supported by Table 1 (comparison to Neural CO baselines) and Tables 2/3 (comparison to Ising machine baselines).
2. **Learned momentum/time-varying schedules**: Supported by qualitative analysis of weights in Section 4.1.
3. **Architecture scalability/parameter importance**: Supported by Section 4.2 and Appendix C, showing performance improves with parameter count but saturates.

### Baseline Assessment
Baselines are well-chosen and strong. They compare against state-of-the-art neural combinatorial optimization methods (Sanokowski et al. 2025's SDDS, DiffUCO, LTFT) and established Ising machines (dSBM, CAC, CFC). 

### Dataset Assessment
The datasets are standard in their respective subfields: MIS/Max-Clique/MaxCut graphs from BA distributions for neural CO, and the G-set instances for Ising machines. This allows for fair and direct comparison with prior literature. 

### Metric Assessment
Metrics are appropriate: MaxCut size/Objective quality and Wall-clock time for Neural CO; Time-to-Solution (TTS) for Ising machines. 

### Statistical Rigor
This is the weakest point. In Table 1, the authors report standard deviations for all baseline methods (e.g., Gurobi, DiffUCO, SDDS) but omit variance/standard deviation reporting for their own method, dNPIM. It's reported as a single number (e.g., 19.9, 40.297). Furthermore, dNPIM uses the "top 30" parallel runs, but it is not entirely clear if the baselines were given an equivalent sampling budget (though DiffUCO relies on diffusion sampling, so presumably they were given some budget). 

### Ablation Assessment
The paper includes an ablation of the network architecture (the history length $T_c$, hidden dimension $D$, and the number of temporal Fourier modes $M$), showing that performance generally increases with parameter count until saturation. They also analyze continuous vs discrete coupling (cNPIM vs dNPIM).

### Missing Experiments
An experiment standardizing the implementation (e.g., using sparse operations) to provide a true head-to-head wall-clock comparison with SDDS/DiffUCO on large graphs would have been ideal. Currently, dNPIM takes 1:20 vs 0:02 for SDDS on large MaxCut, which the authors dismiss as an implementation artifact (dense vs sparse matrices).

### Error Analysis Assessment
The authors acknowledge failure modes, specifically noting in Section 5 that dNPIM (and other Ising machines) struggles on unweighted planar instances from the G-set. This honesty is appreciated.

### Overall Experimental Rigor Verdict
Mostly rigorous with gaps

### Score
6
