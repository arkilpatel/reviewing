# Experimental Rigor & Evaluation Evaluator

### Claims-to-Experiments Mapping
The paper claims throughput gains and latency reductions. These are supported by comprehensive evaluations across multiple datasets (Arena, ShareGPT, Spec-Bench, Tough) using Qwen3-32B with various draft models.

### Baseline Assessment
The primary baseline is standard Speculative Decoding. The authors also compare against state-of-the-art adaptive drafting strategies like EAGLE and TETRIS, showing MineDraft is orthogonal and complementary. Baselines appear strong and appropriately tuned.

### Dataset Assessment
Datasets are standard for LLM serving benchmarks (ShareGPT, LMSYS Chatbot Arena). They are appropriate and cover diverse prompt distributions.

### Metric Assessment
Metrics are standard for inference systems: generation throughput (tokens/s) and end-to-end latency (ms). 

### Statistical Rigor
The experiments are systems benchmarks. Variance is not explicitly reported, which is common but not ideal in systems papers. However, the magnitude of improvements (e.g., 40-75% throughput gain) makes the results robust to minor variance.

### Ablation Assessment
Ablations are thorough. The authors analyze the impact of draft model scale, number of sequences per request, and batch size. They successfully isolate the behavior of their batching mechanism under different loads.

### Missing Experiments
An analysis of the system under continuous, highly bursty request arrival distributions (e.g., Poisson arrivals with high variance) would better test the robustness of the load-balancing mechanism and the fallback to standard SD.

### Error Analysis Assessment
The authors explicitly discuss the limitation of workload imbalance (e.g., when chunked prefill causes one batch to have fewer requests) and the fallback mechanism.

### Overall Experimental Rigor Verdict
Mostly rigorous with gaps

Score: 7.0/10
