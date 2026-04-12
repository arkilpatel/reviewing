import requests
import os
import json

api_key = os.environ.get('COALESCENCE_API_KEY')
paper_id = '2b25b44f-55cf-49e7-b2c2-6308ee7c82a1'
base_url = 'https://coale.science/api/v1'

headers = {'Authorization': f'Bearer {api_key}'}

# Get paper metadata
resp = requests.get(f'{base_url}/papers/{paper_id}', headers=headers)
if resp.status_code == 200:
    paper_data = resp.json()
    with open('/Users/arkil/Data/Work/codes/reviewing/logs/2b25b44f/paper_info.json', 'w') as f:
        json.dump(paper_data, f, indent=2)
    pdf_url = paper_data.get('pdf_url')
    if pdf_url:
        if pdf_url.startswith('/'):
            pdf_url = 'https://coale.science' + pdf_url
        print(f"Downloading PDF from {pdf_url}")
        pdf_resp = requests.get(pdf_url)
        with open('/Users/arkil/Data/Work/codes/reviewing/logs/2b25b44f/paper.pdf', 'wb') as f:
            f.write(pdf_resp.content)
        print("PDF downloaded.")
    else:
        print("No PDF URL found.")
else:
    print(f"Failed to fetch paper: {resp.status_code} {resp.text}")
