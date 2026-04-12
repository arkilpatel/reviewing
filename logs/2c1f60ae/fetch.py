import os, json, requests, subprocess
api_key = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
headers = {"Authorization": api_key}
paper_id = "2c1f60ae-d5ab-4fb9-ac66-c38926576384"
url = f"https://coale.science/api/v1/papers/{paper_id}"
resp = requests.get(url, headers=headers)
data = resp.json()
with open('/Users/arkil/Data/Work/codes/reviewing/logs/2c1f60ae/paper_info.json', 'w') as f:
    json.dump(data, f, indent=2)

pdf_url = data.get('pdf_url')
if pdf_url:
    if pdf_url.startswith('/'):
        pdf_url = "https://coale.science" + pdf_url
    pdf_resp = requests.get(pdf_url)
    pdf_path = '/Users/arkil/Data/Work/codes/reviewing/logs/2c1f60ae/paper.pdf'
    with open(pdf_path, 'wb') as f:
        f.write(pdf_resp.content)
    subprocess.run(['pdftotext', pdf_path])
