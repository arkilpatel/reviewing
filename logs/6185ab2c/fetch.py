import os
import requests
import json

API_KEY = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
BASE_URL = "https://coale.science/api/v1"
PAPER_ID = "6185ab2c-209c-4d7e-ba6d-9fd807f8aacf"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# Fetch paper details
res = requests.get(f"{BASE_URL}/papers/{PAPER_ID}", headers=HEADERS)
if res.status_code != 200:
    print(f"Error fetching paper: {res.text}")
    exit(1)
    
paper_data = res.json()
with open('/Users/arkil/Data/Work/codes/reviewing/logs/6185ab2c/paper.json', 'w') as f:
    json.dump(paper_data, f, indent=2)
    
print("Paper details saved.")

# Download PDF
pdf_url = f"{BASE_URL}/papers/{PAPER_ID}/pdf"
res_pdf = requests.get(pdf_url, headers=HEADERS)
if res_pdf.status_code == 200:
    with open('/Users/arkil/Data/Work/codes/reviewing/logs/6185ab2c/paper.pdf', 'wb') as f:
        f.write(res_pdf.content)
    print("PDF downloaded.")
else:
    print(f"Error downloading PDF: {res_pdf.text}")

