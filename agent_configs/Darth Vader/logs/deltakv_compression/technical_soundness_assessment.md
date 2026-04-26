The technical design of DeltaKV is sound and carefully engineered to address the specific bottlenecks of modern LLM inference. 
Crucially, the authors recognize that operating on post-RoPE (rotary position embedding) states would destroy the position-invariance needed for similarity retrieval. By performing compression on pre-RoPE key-value states, they ensure the residual calculations are mathematically sound and physically meaningful. 

The training methodology is also well-designed. Relying solely on MSE reconstruction loss often suppresses low-magnitude but attention-critical features. The authors correctly address this by employing a hybrid objective that combines MSE with a Next-Token Prediction (NTP) loss, ensuring that the end-to-end generation fidelity is preserved. The design of the strided reference set $\mathcal{T}$ and the top-$k$ retrieval provides a computationally tractable way to find reference tokens without $O(N^2)$ exhaustive search. 

Score: 8.0
