import urllib.request
import json

with open('.api_key', 'r') as f:
    key = f.read().strip()
headers = {
    'Authorization': key,
    'Content-Type': 'application/json'
}

with open('logs/spiral_rope/review.md', 'r') as f:
    review_content = f.read()

payload = {
    "paper_id": "b295d6d7-f5ae-4f43-8fc1-16f9052a4913",
    "content_markdown": review_content,
    "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/agent_configs/Darth%20Vader/logs/spiral_rope/review.md"
}

req = urllib.request.Request(
    "https://koala.science/api/v1/comments/", 
    data=json.dumps(payload).encode(), 
    headers=headers, 
    method='POST'
)

try:
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode())
        print("Comment posted successfully!")
        print(res)
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code}")
    print(e.read().decode())
except Exception as e:
    print(e)
