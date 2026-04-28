### Claims-to-Experiments Mapping
1. **Retry plus compensation recovers task success**: Mapped to RQ1 and real-world benchmarks (WebArena, OSWorld, tau-bench). Supported.
2. **Frontier-gated commit prevents speculative contamination**: Mapped to RQ2 and controlled microbenchmark (Speculative Execution). Supported.
3. **Transactional boundaries preserve state and gate irreversible actions**: Mapped to RQ3, Multi-agent contention, and Irreversible Effect Gate microbenchmarks. Supported.

### Baseline Assessment
The authors acknowledge that directly porting existing systems (AgentGit, AIOS) was infeasible due to differing assumptions and lacking fault-injection hooks. Instead, they implemented 4 progressive configuration modes: No-Tx, No-Frontier, CR (Checkpoint-Rollback, matching AgentGit's mechanism), and Tx-Full. This is an elegant, fair, and mathematically controlled baseline setup because it evaluates the exact architectural mechanisms in isolation under identical conditions.

### Dataset Assessment
They use WebArena, OSWorld, and tau-bench, which are standard, highly challenging real-world environments for agentic tool use. Furthermore, they constructed specialized controlled microbenchmarks to isolate specific transactional properties (speculation, contention, irreversible gates). The use of synthetic fault injection (fp=0.3) is well-justified to ensure sufficient fault events per run.

### Metric Assessment
The metrics align perfectly with the claims: Task Success (with eval=1.0 criterion for WebArena), number of faults, number of retries, and recovered faults. For microbenchmarks, they measure transient/end-state contamination and leaked irreversible effects. These are exactly the right metrics.

### Statistical Rigor
The experiments report 95% confidence intervals over n=30 tasks for the real-world benchmarks. Statistical significance is explicitly noted via non-overlapping CIs. This is robust given the cost and complexity of running these benchmarks on real infrastructure.

### Ablation Assessment
The 4-mode methodology is effectively an extensive ablation study. Furthermore, they ran a specific mock ablation (Tx-NoFrontier+Retry) to cleanly isolate retry from frontier gating, proving that frontier gating provides isolation rather than fault recovery. This is rigorous component isolation.

### Missing Experiments
The empirical validation covers all bases. One minor missing aspect is the scalability of the frontier-tracking mechanism (latency overhead) under high concurrency, although they note that with real tool latencies (~100ms), the overhead is negligible.

### Error Analysis Assessment
They provide a clear breakdown of where components fail: No-Frontier fails on any scenario involving concurrent writes, and CR leaks irreversible actions. The error cases for each baseline perfectly motivate the full system.

### Overall Experimental Rigor Verdict
Rigorous

Score: 8.5
