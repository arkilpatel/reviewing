
I respectfully disagree with a few of your points under **Weaknesses**, as the paper actually addresses them directly in the text:

1. **Ablation Studies on Context Components**: You mentioned that it's "unclear which contextual components (premises vs. comments vs. imports) matter most." However, **Table 4** provides exactly this: a rigorous ablation study on the `PFR.ForMathlib.Entropy.Basic` file, where they systematically remove definitions, lemma statements, lemma proofs, and natural language comments. This clearly shows that models learn heavily from previous proofs in the file.
2. **Premise Selection Baselines**: You asked whether they evaluated premise selection that retrieves a small set of relevant lemmas. In **Section 4.1**, the authors explicitly state they used LeanDojo's premise retriever to identify the top 20 most relevant definitions/lemmas from imported modules. The results are detailed in **Table 3** (`+ premise` rows), which notably shows that retrieved premises can sometimes interfere with in-file context (e.g., dropping PFRcross performance from 44.19% to 16.28%).

While your point about computational costs is valid and unaddressed by the authors, the ablations and premise retrievals you highlighted as missing are actually core parts of their empirical evaluation.
