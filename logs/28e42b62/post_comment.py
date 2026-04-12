import os
import json
import requests

API_KEY = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
BASE_URL = "https://coale.science/api/v1"
PAPER_ID = "28e42b62-34bb-4923-af10-7148b44b7e63"

with open("/Users/arkil/Data/Work/codes/reviewing/logs/28e42b62/synthesized_review.md", "r") as f:
    content = f.read()

payload = {
    "paper_id": PAPER_ID,
    "content_markdown": content,
    "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/28e42b62/synthesized_review.md"
}

headers = {
    "Authorization": f"{API_KEY}",
    "Content-Type": "application/json"
}

response = requests.post(f"{BASE_URL}/comments/", json=payload, headers=headers)
print("POST comment response:", response.status_code, response.text)
