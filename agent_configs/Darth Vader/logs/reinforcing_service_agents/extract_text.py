import fitz

doc = fitz.open('logs/reinforcing_service_agents/paper.pdf')
text = ''
for page in doc:
    text += page.get_text() + '\n'
    
with open('logs/reinforcing_service_agents/paper.txt', 'w') as f:
    f.write(text)
