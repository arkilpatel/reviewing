import os
import re

scores = {}
contents = {}
for crit in ['novelty', 'technical_soundness', 'exp_rigor', 'impact']:
    with open(f"logs/anchor_weave/{crit}_assessment.md", "r") as f:
        text = f.read()
        contents[crit] = text
        # Find score: Look for something like "Score: 6.0" or "Score: 6" or just the number at the end
        match = re.search(r'(?:Score:?\s*|Score.*?)(\d+(?:\.\d+)?)', text[-200:])
        if match:
            scores[crit] = float(match.group(1))
        else:
            scores[crit] = 0.0

nov = scores.get('novelty', 6.0)
tech = scores.get('technical_soundness', 7.0)
exp = scores.get('exp_rigor', 6.5)
imp = scores.get('impact', 6.5)

final_score = (4.0 * imp + 2.0 * tech + 2.0 * exp + 2.0 * nov) / 10.0

review = f"""# Comprehensive Review: AnchorWeave: World-Consistent Video Generation with Retrieved Local Spatial Memories

## Impact
{contents['impact']}

## Technical Soundness
{contents['technical_soundness']}

## Experimental Rigor
{contents['exp_rigor']}

## Novelty
{contents['novelty']}

## Scoring Breakdown
- **Impact:** {imp}
- **Technical Soundness:** {tech}
- **Experimental Rigor:** {exp}
- **Novelty:** {nov}

**Formula:** (4.0 * Impact + 2.0 * Tech_Soundness + 2.0 * Exp_Rigor + 2.0 * Novelty) / 10
**Final Score:** {final_score:.2f}
"""

with open("logs/anchor_weave/review.md", "w") as f:
    f.write(review)

print(f"Synthesized review with score {final_score:.2f}")
