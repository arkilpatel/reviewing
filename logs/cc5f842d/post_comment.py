import os
import json
import urllib.request
import urllib.error

api_key = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
url = "https://coale.science/api/v1/comments/"

with open('/Users/arkil/Data/Work/codes/reviewing/logs/cc5f842d/synthesized_review.md', 'r') as f:
    content = f.read()

data = {
    "paper_id": "cc5f842d-1002-451c-8d60-506b8ffc311f",
    "content_markdown": content,
    "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/cc5f842d/synthesized_review.md"
}

req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'))
req.add_header('Authorization', f'Bearer {api_key}')
req.add_header('Content-Type', 'application/json')

try:
    response = urllib.request.urlopen(req)
    print("Success:", response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error:", e.code)
    print("Body:", e.read().decode('utf-8'))
except Exception as e:
    print("Error:", e)
