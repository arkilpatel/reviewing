The empirical evaluation is comprehensive and rigorously executed. 

The authors evaluate NeSyS across three highly distinct text-based environments (ScienceWorld, Webshop, and Plancraft), providing strong evidence that the framework generalizes across physical reasoning, web navigation, and game dynamics. 

The choice of backbone models (Llama 3.2 1B and Qwen3 4B) is appropriate for demonstrating that smaller, efficient models can be synergized to outperform massive baselines. The comparisons against strong closed- and open-source models (including GPT-5-mini, Qwen3-14B, and GPT-oss-20B) contextualize the difficulty of the tasks.

Crucially, the ablation studies (Tables 1 and 2) are exhaustive. By breaking down performance into Phase 1 vs. Phase 2, and evaluating the Neural WM alone, the Symbolic WM alone, and the combined NeSyS framework, the authors clearly isolate the source of the performance gains. Demonstrating that NeSyS achieves superior accuracy using only 45% of the fine-tuning data compared to standard supervised fine-tuning (SFT) is a compelling empirical validation of the rule-guided data selection strategy.

Experimental Rigor Score: 8.0
