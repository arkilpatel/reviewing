import os, requests, json

API_KEY = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
BASE_URL = "https://coale.science/api/v1"
PAPER_ID = "bd905a52-5873-4935-aeae-c81aaaa19f04"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

r = requests.get(f"{BASE_URL}/papers/{PAPER_ID}", headers=HEADERS)
r.raise_for_status()
paper_data = r.json()
with open("/Users/arkil/Data/Work/codes/reviewing/logs/bd905a52/paper.json", "w") as f:
    json.dump(paper_data, f, indent=2)

pdf_url = f"{BASE_URL}/papers/{PAPER_ID}/content"
r_pdf = requests.get(pdf_url, headers=HEADERS)
r_pdf.raise_for_status()
with open("/Users/arkil/Data/Work/codes/reviewing/logs/bd905a52/paper.pdf", "wb") as f:
    f.write(r_pdf.content)

print("Downloaded successfully")
