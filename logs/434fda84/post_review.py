import json
import urllib.request
import urllib.error

with open("/Users/arkil/Data/Work/codes/reviewing/logs/434fda84/synthesized_review.md", "r") as f:
    content = f.read()

url = "https://coale.science/api/v1/comments/"
headers = {
    "Authorization": "Bearer cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ",
    "Content-Type": "application/json"
}

data = {
    "paper_id": "434fda84-5b86-4efd-a807-d6af3a1367b9",
    "content_markdown": content,
    "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/434fda84/synthesized_review.md"
}

req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method="POST")

try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"Error: {e.code}")
    print(e.read().decode('utf-8'))
