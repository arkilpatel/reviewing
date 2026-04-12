import os
import requests

API_KEY = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
BASE_URL = "https://coale.science"
PDF_PATH = "/storage/pdfs/6185ab2c-209c-4d7e-ba6d-9fd807f8aacf.pdf"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

pdf_url = f"{BASE_URL}{PDF_PATH}"
res_pdf = requests.get(pdf_url, headers=HEADERS)
if res_pdf.status_code == 200:
    with open('/Users/arkil/Data/Work/codes/reviewing/logs/6185ab2c/paper.pdf', 'wb') as f:
        f.write(res_pdf.content)
    print("PDF downloaded.")
else:
    print(f"Error downloading PDF: {res_pdf.text}")
