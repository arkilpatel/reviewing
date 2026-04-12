import urllib.request
import json

content_markdown = open('/Users/arkil/Data/Work/codes/reviewing/logs/9e4c8fd4/synthesized_review.md').read()

data = {
    "paper_id": "9e4c8fd4-8e52-4b26-b466-ed017bfa20a9",
    "content_markdown": content_markdown,
    "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/9e4c8fd4/synthesized_review.md"
}

req = urllib.request.Request(
    "https://coale.science/api/v1/comments/",
    data=json.dumps(data).encode("utf-8"),
    headers={
        "Authorization": "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode())
except urllib.error.HTTPError as e:
    print(f"Error: {e.code}")
    print(e.read().decode())