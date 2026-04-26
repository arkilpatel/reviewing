### Significance & Impact Assessment

Boolean neural networks (not to be confused with 1-bit quantized neural networks like Binarized Neural Networks or BitNet, which still rely on floating-point or integer accumulators) operate purely on logic gates (AND, OR, XOR). They hold immense promise for ultra-low-power edge computing, IoT, and hardware acceleration (FPGAs, ASICs). 

However, the field has struggled with the combinatorial explosion of logic synthesis and the inefficiency of continuous relaxations. By demonstrating how to drastically reduce the operation count (up to 37x) while simultaneously increasing accuracy, this paper marks a significant step toward making Boolean networks practically viable. 

The impact is currently bounded by the niche nature of the subfield and the limitation to small-scale vision tasks (CIFAR-10). Scaling these techniques to ImageNet or language modeling tasks remains an open challenge, largely due to the destructive nature of the input encoding (thermometer encoding) as noted by the authors themselves. Nevertheless, within its domain, it is a highly impactful paper.

Score: 6.0