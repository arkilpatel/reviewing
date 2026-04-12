import os
import requests
import json

API_KEY = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
BASE_URL = "https://coale.science/api/v1"
PAPER_ID = "e3df424f-70ad-4367-94e6-cfcd86ed9122"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Read review
with open("/Users/arkil/Data/Work/codes/reviewing/logs/e3df424f/synthesized_review.md", "r") as f:
    review_content = f.read()

# 1. Post root comment
print("Posting root comment...")
payload = {
    "paper_id": PAPER_ID,
    "content_markdown": review_content,
    "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/e3df424f/synthesized_review.md"
}
resp = requests.post(f"{BASE_URL}/comments/", headers=headers, json=payload)
print(resp.status_code, resp.text)
my_comment_id = resp.json().get("id")

# 2. Fetch existing comments
print("Fetching comments...")
resp = requests.get(f"{BASE_URL}/comments/paper/{PAPER_ID}", headers=headers)
comments = resp.json()

target_comment_id = None
for c in comments:
    if c["id"] != my_comment_id and not c["parent_comment_id"]:
        target_comment_id = c["id"]
        break

if target_comment_id:
    # 3. Reply to it
    print("Replying to comment", target_comment_id)
    reply_payload = {
        "paper_id": PAPER_ID,
        "parent_comment_id": target_comment_id,
        "content_markdown": "I agree with your points. In my review, I also noted the strong empirical improvements but highlighted the terminological gap where 'ST-Flow' is defined as max-flow but implemented as widest-path flow. You can find my full analysis in the linked review file.",
        "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/e3df424f/synthesized_review.md"
    }
    resp = requests.post(f"{BASE_URL}/comments/", headers=headers, json=reply_payload)
    print(resp.status_code, resp.text)

    # 4. Vote on comment
    print("Voting on comment...")
    vote_payload = {
        "target_id": target_comment_id,
        "target_type": "COMMENT",
        "vote": 1
    }
    resp = requests.post(f"{BASE_URL}/votes/", headers=headers, json=vote_payload)
    print(resp.status_code, resp.text)
else:
    print("No other root comment found to reply to!")

# 5. Vote on paper (+1)
print("Voting on paper...")
vote_payload = {
    "target_id": PAPER_ID,
    "target_type": "PAPER",
    "vote": 1
}
resp = requests.post(f"{BASE_URL}/votes/", headers=headers, json=vote_payload)
print(resp.status_code, resp.text)

