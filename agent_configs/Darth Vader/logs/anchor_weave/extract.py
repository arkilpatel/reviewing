import pypdf
import sys

def extract(pdf_path, txt_path):
    with open(pdf_path, 'rb') as f:
        reader = pypdf.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n\n"
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)

extract("/network/scratch/a/arkil.patel/reviewing/agent_configs/Darth Vader/logs/anchor_weave/paper.pdf", "/network/scratch/a/arkil.patel/reviewing/agent_configs/Darth Vader/logs/anchor_weave/paper.txt")
