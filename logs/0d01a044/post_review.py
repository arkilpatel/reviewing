import requests
import json
import sys

API_KEY = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
BASE_URL = "https://coale.science/api/v1"
PAPER_ID = "0d01a044-8645-46c4-bb23-4579b73511ec"
REVIEW_FILE = "/Users/arkil/Data/Work/codes/reviewing/logs/0d01a044/synthesized_review.md"

with open(REVIEW_FILE, "r") as f:
    content = f.read()

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 1. Post the review
payload = {
    "paper_id": PAPER_ID,
    "content_markdown": content,
    "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/0d01a044/synthesized_review.md"
}

print("Posting review...")
resp = requests.post(f"{BASE_URL}/comments/", json=payload, headers=headers)
if resp.status_code not in [200, 201]:
    print(f"Error posting review: {resp.status_code} - {resp.text}")
    sys.exit(1)
    
print("Review posted successfully!")
posted_comment = resp.json()
print("My comment ID:", posted_comment.get("id"))

# 2. Fetch existing comments
print("Fetching comments...")
resp = requests.get(f"{BASE_URL}/papers/{PAPER_ID}/comments", headers=headers)
if resp.status_code == 200:
    comments = resp.json()
    with open("/Users/arkil/Data/Work/codes/reviewing/logs/0d01a044/comments.json", "w") as f:
        json.dump(comments, f, indent=2)
    print(f"Saved {len(comments)} comments.")
else:
    print("Failed to fetch comments.")
