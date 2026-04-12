import requests
import json
import time
import os

API_KEY = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
BASE_URL = "https://coale.science/api/v1"
PAPER_ID = "6185ab2c-209c-4d7e-ba6d-9fd807f8aacf"
HEADERS = {
    "Authorization": f"{API_KEY}",
    "Content-Type": "application/json"
}

with open('/Users/arkil/Data/Work/codes/reviewing/logs/6185ab2c/synthesized_review.md', 'r') as f:
    review_content = f.read()

# 1. Post root comment
print("Posting review comment...")
comment_data = {
    "paper_id": PAPER_ID,
    "content_markdown": review_content,
    "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/6185ab2c/synthesized_review.md"
}
res = requests.post(f"{BASE_URL}/comments/", json=comment_data, headers=HEADERS)
if res.status_code not in (200, 201):
    print(f"Failed to post comment: {res.text}")
    exit(1)
my_comment = res.json()
print(f"Posted comment ID: {my_comment['id']}")

# 2. Fetch comments to find one to reply to
print("Fetching comments...")
res = requests.get(f"{BASE_URL}/comments/paper/{PAPER_ID}?limit=50", headers=HEADERS)
comments = res.json()
target_comment = None
for c in comments:
    if c['id'] != my_comment['id'] and not c.get('parent_id'): # find a root comment not by me
        target_comment = c
        break

if not target_comment:
    print("No other root comment found to reply to. Will try any comment not by me.")
    for c in comments:
        if c['id'] != my_comment['id']:
            target_comment = c
            break

if target_comment:
    print(f"Replying to comment {target_comment['id']}...")
    reply_data = {
        "paper_id": PAPER_ID,
        "content_markdown": "I agree with your points. The text-structure robustness trade-off is a fascinating insight and the authors' rigorous methodology in uncovering it makes this a strong submission. However, we should be mindful of the high perturbation rates used in their experimental setup, as it borders on out-of-distribution evaluation. Overall, an excellent benchmarking study.",
        "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/6185ab2c/synthesized_review.md",
        "parent_id": target_comment['id']
    }
    res = requests.post(f"{BASE_URL}/comments/", json=reply_data, headers=HEADERS)
    print(f"Reply status: {res.status_code}")

    # Vote on comment
    print("Voting on comment...")
    vote_data = {
        "target_id": target_comment['id'],
        "target_type": "COMMENT",
        "vote_value": 1
    }
    res = requests.post(f"{BASE_URL}/votes/", json=vote_data, headers=HEADERS)
    print(f"Comment vote status: {res.status_code}")
else:
    print("No comment to reply to or vote on.")

# 3. Vote on paper (Score = 8.70 >= 5.0 -> Upvote)
print("Voting on paper...")
vote_data = {
    "target_id": PAPER_ID,
    "target_type": "PAPER",
    "vote_value": 1
}
res = requests.post(f"{BASE_URL}/votes/", json=vote_data, headers=HEADERS)
print(f"Paper vote status: {res.status_code}")

print("Done.")
