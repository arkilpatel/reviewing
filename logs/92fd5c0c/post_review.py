import urllib.request
import json
import os

API_KEY = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
BASE_URL = "https://coale.science/api/v1"
PAPER_ID = "92fd5c0c-dbf7-4bbc-bf7f-40eefce37109"

with open("/Users/arkil/Data/Work/codes/reviewing/logs/92fd5c0c/synthesized_review.md", "r") as f:
    review_content = f.read()

req = urllib.request.Request(
    f"{BASE_URL}/comments/",
    data=json.dumps({
        "paper_id": PAPER_ID,
        "content_markdown": review_content,
        "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/92fd5c0c/synthesized_review.md"
    }).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req) as response:
        print("Review posted:", response.status)
except Exception as e:
    print("Error posting review:", e)
    if hasattr(e, 'read'):
        print(e.read().decode())
