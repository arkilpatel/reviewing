### Claimed Contributions
1. **Spatial Bit Encoding:** Moving away from temporal/rate coding, the paper encodes continuous values by mapping each bit of their IEEE-754 floating-point representation to a distinct spatial spike channel (e.g., 32 channels for FP32), achieving zero encoding error.
2. **Neuromorphic Gate Circuits:** The authors construct exact IEEE-754 arithmetic operations (addition, multiplication, and even complex non-linearities like SiLU and Softmax) purely out of Integrate-and-Fire (IF) neuron logic gates.
3. **Surrogate-Free Training:** Because the forward pass is a mathematically exact replica of floating-point arithmetic, backpropagation uses the Straight-Through Estimator (STE) as an exact identity mapping, avoiding the heuristic approximations typical in SNN training.

### Prior Work Assessment
- **SNN Coding Schemes:** Traditional SNNs rely on rate coding (spike frequency) or temporal coding (time-to-first-spike). These inherently introduce quantization and latency errors. Spatial encoding of bits is known in digital logic but is a radical, almost subversive shift within the neuromorphic community, as it abandons biological plausibility for digital precision.
- **ANN-to-SNN Conversion:** Prior conversion methods (like SpikeGPT or SpikeLLM) suffer from severe accuracy degradation due to approximation errors and the mismatch between continuous activations and discrete spikes. NEXUS bypasses this entirely.
- **The Novelty Delta:** Implementing digital logic gates (AND, OR, XOR) using IF neurons is a known theoretical property (since McCulloch-Pitts). However, scaling this up to build full IEEE-754 compliant ALUs and integrating it as a drop-in replacement for LLM training/inference within an SNN framework is a highly novel and brutally pragmatic approach to the ANN-to-SNN conversion problem.

### Novelty Verdict
Substantial.

### Justification
The approach fundamentally redefines how an SNN can operate in the deep learning era. By discarding the biological inspiration of temporal spike accumulation and instead using neurons to explicitly simulate digital logic ALUs, NEXUS provides a creative and highly effective solution to the long-standing accuracy degradation problem in SNNs.

Score: 7.5