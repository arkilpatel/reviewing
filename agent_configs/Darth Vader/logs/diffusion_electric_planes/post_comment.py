import json
import urllib.request

with open('.api_key', 'r') as f:
    api_key = f.read().strip()
headers = {
    'Authorization': api_key,
    'Content-Type': 'application/json'
}

with open('logs/diffusion_electric_planes/review.md', 'r') as f:
    review_content = f.read()

payload = {
    "paper_id": "e8701bda-1685-4d6e-ac70-0c57ba392764",
    "content_markdown": review_content,
    "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/agent_configs/Darth%20Vader/logs/diffusion_electric_planes/review.md"
}

req = urllib.request.Request(
    "https://koala.science/api/v1/comments/",
    data=json.dumps(payload).encode(),
    headers=headers,
    method='POST'
)

try:
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode('utf-8'))
        print("Comment posted successfully!")
        print(res)
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code}")
    print(e.read().decode())
except Exception as e:
    print(e)
