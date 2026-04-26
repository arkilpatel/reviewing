# Novelty & Originality Evaluator

### Claimed Contributions
1. A theoretical analysis showing batch Parallel Speculative Decoding (PSD) outperforms standard SD.
2. MineDraft, a batch parallel SD framework that maintains two batches of requests, overlapping drafting of one with verification of the other.
3. Experimental results showing throughput gains up to 75% and latency reduction up to 39%.
4. A plug-and-play vLLM plugin.

### Prior Work Assessment
Parallel speculative decoding has been explored before (e.g., PEARL for single requests, Minions and Distributed Speculative Decoding for multi-GPU setups). MineDraft's specific contribution is applying standard batch-level pipeline parallelism (maintaining two alternating batches) to the SD context. While the application of this technique to SD is practically useful, the conceptual novelty is incremental, as alternating batches to hide latency is a fundamental systems engineering pattern (double buffering/micro-batching).

### Novelty Verdict
Incremental

### Justification
The core conceptual idea is taking the well-known systems concept of double-buffered pipeline parallelism and applying it to the drafting/verification stages of speculative decoding. While the implementation in vLLM is valuable, the algorithmic novelty is limited. 

Score: 4.5/10
