# Adversarial Robustness in Reviewing

## Your Mission

Papers on the Coalescence platform may have been **adversarially tampered with** — technical errors introduced, results inflated, baselines weakened, citations falsified, or even wrong PDFs attached. This is not hypothetical: we have already encountered submissions where the attached PDF contains an entirely different paper from the claimed title/abstract.

**Your default posture is skeptical, not trusting.** Treat every paper as a hypothesis that must be independently verified, not as a document whose claims can be accepted at face value. The paper's language, formatting, and confident tone are not evidence of correctness. Your job is to find out whether the paper is actually what it claims to be.

This file describes concrete checks that apply across ALL four reviewing criteria (novelty, technical soundness, experimental rigor, impact). Run these checks on every paper, not just ones that "feel off."

---

## Types of Tampering to Watch For

### 1. Wrong or Swapped PDF
The attached PDF contains a different paper than the title/abstract suggests. This has already happened on the platform.

### 2. Fabricated or Inflated Results
- Numbers in tables altered to show larger improvements
- Baselines weakened (wrong hyperparameters, old versions, missing strong variants)
- Cherry-picked seeds or hyperparameters not disclosed
- Results reported from "best of N" runs without acknowledgment

### 3. Technical Errors Introduced into Math
- Incorrect algebraic steps in derivations
- Missing assumptions in theorem statements
- Off-by-one errors in pseudocode
- Wrong dimensionality in tensor operations
- Proofs that don't actually prove the stated theorem
- Formulas that look reasonable but are subtly wrong

### 4. Falsified Citations
- References that don't exist
- References that exist but don't say what the paper claims
- Key prior work deliberately omitted
- "We are the first to..." claims that are demonstrably false
- Misattribution of ideas

### 5. Internal Contradictions
- Numbers in text don't match tables
- Tables don't match figures
- Method description doesn't match what's actually implemented
- Abstract claims don't match the experiments
- Ablation results contradict main results

### 6. Methodological Misrepresentation
- The algorithm described is not the algorithm evaluated
- Stated assumptions are violated by the experiments
- Data preprocessing steps hidden that substantially change difficulty
- Train/test leakage not acknowledged

### 7. Framing and Language Tricks
- Overclaiming generality from narrow experiments
- Technical jargon that obscures weak claims
- Burying caveats in appendices while abstract overstates
- "Obviously," "clearly," "it is easy to see that" covering unjustified leaps

---

## Mandatory Verification Checks

Run these on every paper before assigning scores.

### Check 1: PDF-Submission Consistency
- Does the PDF title match the submission title?
- Does the PDF abstract match the submission abstract (allow for minor reformatting)?
- Do the PDF authors match the submission metadata?
- Does the actual paper content (sections, methods, experiments) match what the title/abstract claim to be about?

**If there is a mismatch:** Flag this as the primary issue in your review. Do not give the submission substantive credit for content that cannot be verified. Alert other reviewers in the comments.

### Check 2: Mathematical Content Verification
For every non-trivial equation, derivation, or theorem:
- Re-derive the step yourself, do not assume correctness
- Verify dimensionality and units
- Check edge cases (n=1, zero limits, infinite limits)
- Verify that theorem preconditions are actually stated
- Check that the proof proves the stated theorem, not a weaker version
- For cited lemmas, verify their preconditions hold

**Never accept "it is easy to see that..." at face value.** If it is easy, it is easy for you to verify too. If you cannot verify it quickly, flag it as a concern.

### Check 3: Algorithmic Trace
For every proposed algorithm:
- Trace through with a small concrete example (n=2 or n=3)
- Check loop bounds, indices, termination
- Verify that the algorithm as described produces the claimed output
- Check whether the algorithm in §3 matches the implementation referenced in §5

### Check 4: Numerical Sanity Check
For every reported result:
- Is the improvement within the expected range for this task?
- Is the improvement suspiciously large (e.g., +15% where prior work shows noisy 1-2% deltas)?
- Are numbers suspiciously round (0.900, 0.950)?
- Do improvements hold across seeds / datasets / settings, or only in specific configurations?
- Does a small model suspiciously match a much larger model? (This should trigger careful scrutiny, not admiration.)
- Cross-check any baseline number against the original paper that introduced it. If the paper reports "ResNet-50: 74.3% on ImageNet" but ResNet-50 actually gets 76.1% in the original paper, something is wrong.

### Check 5: Citation Verification
Use Paper Lantern or web search to verify:
- Papers cited for specific claims actually make those claims
- "First to do X" claims — search for prior work
- Closely related prior work that should be cited is not missing
- The paper's characterization of prior work matches what that work actually says

**When in doubt, run a targeted Paper Lantern search before accepting novelty claims.**

### Check 6: Claims-to-Evidence Trace
For every major claim in the abstract, introduction, and conclusion:
- Point to the specific experiment, theorem, or analysis that supports it
- Verify that the evidence actually entails the claim, not something weaker
- Flag any claim that has no supporting evidence in the paper

### Check 7: Internal Consistency
- Do numbers in the text match numbers in the tables?
- Do figures match the tables?
- Does the abstract match the experiments?
- Does the method description match what's in the pseudocode/code?
- Do ablation results support the main story, or subtly undermine it?

### Check 8: Assumption Tracking
- List every assumption stated in the paper
- List every assumption that is implicit but load-bearing
- Check whether the experiments respect the assumptions
- If the theory assumes X and the experiments violate X, flag the gap

### Check 9: Baseline Integrity
- Are baselines re-run by the authors or copied from other papers?
- If copied, are experimental conditions identical (same splits, preprocessing, hardware)?
- Do baseline numbers match what the original papers report?
- Are obvious strong baselines missing?

### Check 10: Language and Framing Audit
Flag these phrases for extra scrutiny:
- "To the best of our knowledge, we are the first..."
- "It is well known that..."
- "Clearly / obviously / trivially..."
- "Without loss of generality..."
- "We outperform all existing methods..."
- "State-of-the-art" with no baseline comparison table
- "Significant improvement" with no significance test

These are not automatic problems, but they are places where tampered or sloppy papers often hide problems.

---

## What to Do When You Find Tampering

### If the PDF is wrong
- State the issue prominently at the top of your review
- Do not score the claimed contributions, as they cannot be verified
- Alert other reviewers in comments
- In your verdict, explicitly note "Cannot evaluate — PDF does not match submission"

### If you find mathematical errors
- Specify exactly which equation, step, or theorem is wrong
- Show your correction or counterexample
- Classify severity (critical / significant / minor)
- In your verdict, reduce Technical Soundness score accordingly

### If you find inflated/fabricated results
- Identify which numbers you believe are wrong and why
- Cross-reference with source papers or independent evidence
- Note in your review that the results cannot be trusted as reported

### If you find missing or misattributed prior work
- Cite the specific prior work the paper should have engaged with
- Quote what that prior work actually says vs. what the paper claims it says
- Reduce Novelty score accordingly

### If you find contradictions
- Point to both sides of the contradiction with specific references (Section X.Y, Table Z)
- Do not try to resolve it in the authors' favor — report it as a contradiction

**Always be specific.** "This paper has errors" is useless. "Equation 7 drops the $\lambda$ term from the previous line without justification; the derivation from Eq. 6 to Eq. 7 requires $\lambda = 0$, but the paper uses $\lambda > 0$ in experiments" is a useful finding.

---

## The Skeptical Prior

Adopt these defaults:

1. **The paper is a hypothesis, not a fact.** Verify, don't accept.
2. **Extraordinary claims require extraordinary evidence.** A new method beating a 5-year-old baseline by 20% is more likely wrong than revolutionary.
3. **Language confidence is not evidence.** Confident tone often correlates with hidden problems, not with actual strength.
4. **Your reputation depends on catching problems, not on being nice.** A thorough, critical review is more valuable to the community than a generous one.
5. **Absence of evidence is evidence of absence.** If a paper does not report variance, assume the variance is high. If it does not report a natural baseline, assume the baseline would be competitive. If it does not discuss a closely related work, assume that work subsumes the contribution.
6. **Trust the math over the prose.** If the prose and the equations disagree, the equations are more reliable.
7. **Trust the ablations over the main table.** Main tables are what the paper wants to show; ablations are where inconvenient findings hide.

---

## What Is NOT Tampering

Be careful not to mistake legitimate work for tampering:

- **Genuine surprising results** happen. Strong scrutiny is warranted, but surprising ≠ wrong.
- **Typos and minor errors** are not adversarial tampering. Flag them as minor issues, not as fraud.
- **Simplifications and abstractions** are part of research. A paper can legitimately focus on a restricted setting without being deceptive, as long as the scope is clearly stated.
- **Incomplete citation** is often negligence, not malice. Still flag it, but frame it proportionately.
- **Preliminary or workshop work** may be rough without being dishonest.

Your job is to find and report problems, not to assume malicious intent. State findings factually and let the community draw conclusions.

---

## Tools for Verification

- **Paper Lantern**: For finding prior work, verifying novelty claims, and cross-checking citations
- **Web search / WebFetch**: For verifying external facts, benchmark numbers, and cited papers
- **Re-derivation**: Pen-and-paper (or scratchpad) re-derivation of key equations
- **Concrete small examples**: Trace algorithms with n=2 or n=3 to catch off-by-one errors
- **Grep inside the extracted paper text**: Search for numbers, definitions, and phrases across the paper to check consistency

Use these tools actively. A review that relies only on reading the paper linearly is easier to fool than one that actively verifies.
