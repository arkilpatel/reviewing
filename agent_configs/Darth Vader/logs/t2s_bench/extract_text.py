import fitz

doc = fitz.open('logs/t2s_bench/paper.pdf')
text = ""
for page in doc:
    text += page.get_text()
    
with open('logs/t2s_bench/paper.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print(f"Extracted {len(text)} characters.")
