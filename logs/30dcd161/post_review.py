import os
import json
import urllib.request

api_key = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
paper_id = "30dcd161-e9f1-40ea-ae9b-1694ea337dc7"

with open("/Users/arkil/Data/Work/codes/reviewing/logs/30dcd161/synthesized_review.md", "r") as f:
    content = f.read()

payload = {
    "paper_id": paper_id,
    "content_markdown": content,
    "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/30dcd161/synthesized_review.md"
}

req = urllib.request.Request(
    "https://coale.science/api/v1/comments/",
    data=json.dumps(payload).encode('utf-8'),
    headers={
        "Authorization": api_key,
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    response = urllib.request.urlopen(req)
    print("Post comment success:", response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Post comment error:", e.read().decode('utf-8'))
