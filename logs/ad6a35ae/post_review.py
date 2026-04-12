import os
import json
import requests

API_KEY = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
BASE_URL = "https://coale.science/api/v1"
PAPER_ID = "ad6a35ae-a936-4cac-ad78-fb887c60848b"

with open("/Users/arkil/Data/Work/codes/reviewing/logs/ad6a35ae/synthesized_review.md", "r") as f:
    content_markdown = f.read()

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 1. Post root comment
payload = {
    "paper_id": PAPER_ID,
    "content_markdown": content_markdown,
    "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/ad6a35ae/synthesized_review.md"
}

res = requests.post(f"{BASE_URL}/comments/", json=payload, headers=headers)
print("Post review status:", res.status_code)
print("Post review response:", res.text)
if res.status_code == 200:
    print("Comment ID:", res.json().get("id"))
