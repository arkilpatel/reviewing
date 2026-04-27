import re

with open('logs/reinforcing_service_agents/paper.txt', 'r') as f:
    text = f.read()

# Try to find Abstract, Intro, Conclusion
def extract_section(text, start_keywords, end_keywords):
    start_idx = -1
    for k in start_keywords:
        match = re.search(r'\b' + k + r'\b', text, re.IGNORECASE)
        if match:
            start_idx = match.start()
            break
            
    if start_idx == -1: return ""
    
    end_idx = len(text)
    for k in end_keywords:
        match = re.search(r'\n\s*[\d\.]*\s*' + k + r'\b', text[start_idx+10:], re.IGNORECASE)
        if match:
            end_idx = start_idx + 10 + match.start()
            break
            
    return text[start_idx:end_idx]

abstract = extract_section(text, ['Abstract'], ['Introduction', '1 Introduction'])
intro = extract_section(text, ['Introduction', '1 Introduction'], ['Related Work', '2 Related Work', 'Background', 'Method'])
conclusion = extract_section(text, ['Conclusion', 'Conclusions'], ['References', 'Acknowledgments', 'Appendix'])

print("=== ABSTRACT ===")
print(abstract[:2000])
print("\n=== INTRO (first 2000 chars) ===")
print(intro[:2000])
print("\n=== CONCLUSION (first 2000 chars) ===")
print(conclusion[:2000])
