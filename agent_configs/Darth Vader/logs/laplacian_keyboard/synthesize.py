import re

def extract_score(text):
    matches = re.findall(r'Score:\s*([0-9]+(?:\.[0-9]+)?)', text, re.IGNORECASE)
    if matches:
        return float(matches[-1])
    return 5.0

folder = "logs/laplacian_keyboard"

with open(f"{folder}/novelty_assessment.md", "r") as f:
    nov_text = f.read()
    nov_score = extract_score(nov_text)

with open(f"{folder}/technical_soundness_assessment.md", "r") as f:
    tech_text = f.read()
    tech_score = extract_score(tech_text)

with open(f"{folder}/exp_rigor_assessment.md", "r") as f:
    exp_text = f.read()
    exp_score = extract_score(exp_text)

with open(f"{folder}/impact_assessment.md", "r") as f:
    imp_text = f.read()
    imp_score = extract_score(imp_text)

final_score = (4.0 * imp_score + 2.0 * tech_score + 2.0 * exp_score + 2.0 * nov_score) / 10.0

review = f"""# Comprehensive Review: The Laplacian Keyboard: Beyond the Linear Span

## Overview
This review evaluates the paper across four critical dimensions: Novelty, Technical Soundness, Experimental Rigor, and Impact. The paper proposes the **Laplacian Keyboard (LK)**, a hierarchical reinforcement learning framework that uses Laplacian eigenvectors to construct a continuous library of skills. A meta-policy dynamically composes these skills, enabling the agent to represent policies that break out of the theoretical linear span of the basis.

## Novelty
{nov_text.replace(f"Score: {nov_score}", "").replace(f"Score: {nov_score:.1f}", "").strip()}

## Technical Soundness
{tech_text.replace(f"Score: {tech_score}", "").replace(f"Score: {tech_score:.1f}", "").strip()}

## Experimental Rigor
{exp_text.replace(f"Score: {exp_score}", "").replace(f"Score: {exp_score:.1f}", "").strip()}

## Impact
{imp_text.replace(f"Score: {imp_score}", "").replace(f"Score: {imp_score:.1f}", "").replace("Impact Score:", "Score:").strip()}

## Scoring Breakdown
- **Novelty:** {nov_score}
- **Technical Soundness:** {tech_score}
- **Experimental Rigor:** {exp_score}
- **Impact:** {imp_score}
- **Formula:** `(4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10`
- **Final Calculated Score:** {final_score:.2f}
"""

with open(f"{folder}/review.md", "w") as f:
    f.write(review)

print(f"Final Score: {final_score}")
