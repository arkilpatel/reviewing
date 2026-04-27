import json

novelty = open('logs/diffusion_electric_planes/novelty.md').read()
ts = open('logs/diffusion_electric_planes/technical_soundness.md').read()
er = open('logs/diffusion_electric_planes/exp_rigor.md').read()
impact = open('logs/diffusion_electric_planes/impact.md').read()

score = (4.0 * 6.0 + 2.0 * 8.0 + 2.0 * 6.0 + 2.0 * 7.0) / 10

review = f"""This paper tackles the complex problem of generating conceptual engineering designs for electric vertical take-off and landing (eVTOL) aircraft using Simulation-Based Inference (SBI). The authors introduce a hierarchical probabilistic model utilizing two diffusion models: `MixeDiT` for sampling discrete aircraft topologies alongside continuous observations, and `MaskeDiT` for sampling the corresponding variable-dimensional continuous parameters.

### Novelty
{novelty.split('### Score')[0]}

### Technical Soundness
{ts.split('### Score')[0]}

### Experimental Rigor
{er.split('### Score')[0]}

### Impact
{impact.split('**Impact Score:')[0]}

### Scoring Breakdown
- **Impact:** 6.0
- **Technical Soundness:** 8.0
- **Experimental Rigor:** 6.0
- **Novelty:** 7.0

**Formula:** `(4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`
**Final Score:** {score:.1f}
"""

with open('logs/diffusion_electric_planes/review.md', 'w') as f:
    f.write(review)

print("Review synthesized.")
