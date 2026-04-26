### Claimed Contributions
1. **Local Geometric Memory Paradigm**: Introducing AnchorWeave, a framework that replaces global 3D scene reconstruction (which is prone to cross-view misalignment and drift) with multiple per-frame local 3D point cloud memories.
2. **Coverage-Driven Memory Retrieval**: A retrieval algorithm that selects multiple local memories by maximizing the additional visibility coverage along the target camera trajectory.
3. **Multi-Anchor Weaving Controller**: A learned module featuring shared cross-anchor attention and pose-guided fusion to integrate the multiple retrieved anchor videos and reconcile any residual cross-view geometric inconsistencies during the generative process.

### Prior Work Assessment
- **Global 3D Memory for Video Generation**: Recent works like SPMem (Wu et al., 2025) and Gen3C (Ren et al., 2025) maintain long-term consistency by reconstructing a global 3D point cloud from historical frames and rendering it from target views. The delta here is conceptual and architectural: abandoning the error-prone global fusion process in favor of maintaining multiple independent, single-view local point clouds and shifting the fusion burden to the generative model itself. 
- **Multi-View Conditioning**: Methods like Context-as-Memory (Yu et al., 2025) and SEVA (Zhou et al., 2025) condition on multiple raw historical frames directly. AnchorWeave differs by explicitly leveraging 3D geometry (rendering local point clouds to the target view) rather than relying solely on implicit cross-attention to 2D frames, thus providing stronger geometric priors.
- **Image-Based Rendering (IBR) and Novel View Synthesis**: Using multiple local views to render a target view and blending them via a neural network is a well-established concept in the Novel View Synthesis literature (e.g., Generalizable NeRFs, Image-Based Rendering). AnchorWeave adapts this idea specifically to the autoregressive video generation setting, framing it as a solution to "memory drift" over long horizons. 

### Novelty Verdict
Moderate

### Justification
The paper identifies a very real issue with global 3D reconstruction in video generation frameworks (accumulation of pose/depth errors leading to ghosting). The solution—reverting to local views and using a neural network to blend/weave them—is sensible and effective. However, the core conceptual leap of "using multiple local views instead of a single fused global model" is heavily inspired by classical Image-Based Rendering (IBR) and recent generalizable novel view synthesis methods. The novelty is therefore primarily in the *application* and *combination* of these concepts (coverage-driven retrieval + local geometric rendering + pose-guided fusion) within the context of diffusion-based long-horizon video generation, rather than introducing a fundamentally new mathematical or generative paradigm.

### Missing References
The related work seems quite comprehensive regarding recent video generation models (2024-2025). However, the paper could benefit from discussing the rich history of Image-Based Rendering (IBR) and multi-view blending in graphics and vision, which conceptually paved the way for "weaving" local geometric views to avoid global 3D reconstruction artifacts.

### Score
6.0
