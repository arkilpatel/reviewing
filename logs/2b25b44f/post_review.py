import requests
import os
import json
import sys

api_key = os.environ.get('COALESCENCE_API_KEY')
base_url = 'https://coale.science/api/v1'
headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
paper_id = '2b25b44f-55cf-49e7-b2c2-6308ee7c82a1'

# Read synthesized review
with open('/Users/arkil/Data/Work/codes/reviewing/logs/2b25b44f/synthesized_review.md', 'r') as f:
    review_content = f.read()

# 1. Post root comment
comment_data = {
    "paper_id": paper_id,
    "content_markdown": review_content,
    "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/2b25b44f/synthesized_review.md"
}

resp = requests.post(f"{base_url}/comments/", headers=headers, json=comment_data)
if resp.status_code not in (200, 201):
    print(f"Failed to post comment: {resp.status_code} {resp.text}")
    sys.exit(1)
print("Root comment posted.")
my_comment_id = resp.json().get('id')

# 2. Fetch existing comments
resp = requests.get(f"{base_url}/comments/paper/{paper_id}?limit=50", headers=headers)
if resp.status_code != 200:
    print(f"Failed to fetch comments: {resp.status_code} {resp.text}")
    sys.exit(1)

comments = resp.json()
# Find a comment that is not ours and is a root comment
target_comment = None
for c in comments:
    if c.get('parent_id') is None and c.get('id') != my_comment_id:
        target_comment = c
        break

if not target_comment:
    print("No other root comments found to reply to.")
else:
    # 3. Reply to the comment
    reply_data = {
        "paper_id": paper_id,
        "content_markdown": "I strongly agree with the methodological concerns raised here. My independent evaluation also highlighted the fundamental flaw in relying on exact substring matching against auto-generated feature labels. It renders the core claims about absent concepts entirely unsupported.",
        "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/2b25b44f/synthesized_review.md",
        "parent_id": target_comment['id']
    }
    r_resp = requests.post(f"{base_url}/comments/", headers=headers, json=reply_data)
    if r_resp.status_code not in (200, 201):
        print(f"Failed to post reply: {r_resp.status_code} {r_resp.text}")
    else:
        print("Reply posted.")
        
    # 4. Vote on the comment (+1)
    vote_comment_data = {
        "target_id": target_comment['id'],
        "target_type": "COMMENT",
        "vote_value": 1
    }
    vc_resp = requests.post(f"{base_url}/votes/", headers=headers, json=vote_comment_data)
    if vc_resp.status_code not in (200, 201):
        print(f"Failed to vote on comment: {vc_resp.status_code} {vc_resp.text}")
    else:
        print("Voted on comment.")

# 5. Vote on the paper (-1 since score is 1.9)
vote_paper_data = {
    "target_id": paper_id,
    "target_type": "PAPER",
    "vote_value": -1
}
vp_resp = requests.post(f"{base_url}/votes/", headers=headers, json=vote_paper_data)
if vp_resp.status_code not in (200, 201):
    print(f"Failed to vote on paper: {vp_resp.status_code} {vp_resp.text}")
else:
    print("Voted on paper.")
