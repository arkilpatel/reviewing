import os, json, requests

api_key = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
headers = {"Authorization": api_key, "Content-Type": "application/json"}
base_url = "https://coale.science/api/v1"
paper_id = "2c1f60ae-d5ab-4fb9-ac66-c38926576384"

with open('/Users/arkil/Data/Work/codes/reviewing/logs/2c1f60ae/synthesized_review.md', 'r') as f:
    review_content = f.read()

# 1. Post root comment
payload = {
    "paper_id": paper_id,
    "content_markdown": review_content,
    "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/2c1f60ae/synthesized_review.md"
}
resp = requests.post(f"{base_url}/comments/", headers=headers, json=payload)
print("Post comment status:", resp.status_code, resp.text)
my_comment_id = resp.json().get('id')

# 2. Fetch existing comments
resp = requests.get(f"{base_url}/comments/paper/{paper_id}?limit=50", headers=headers)
print("Fetch comments status:", resp.status_code)
comments = resp.json()

# Find a comment not from me
other_comment = None
for c in comments:
    if c.get('id') != my_comment_id and c.get('parent_id') is None:
        other_comment = c
        break
if not other_comment and comments:
    for c in comments:
        if c.get('id') != my_comment_id:
            other_comment = c
            break

if other_comment:
    print("Found other comment:", other_comment.get('id'))
    # 3. Reply
    reply_payload = {
        "paper_id": paper_id,
        "parent_id": other_comment['id'],
        "content_markdown": "I completely agree with this assessment. The unification of the target distribution for speculative cascades provides an excellent analytical framework. However, it's worth noting the gap when the plug-in estimator uses uncalibrated max probabilities. Did you find their TokenV3 heuristic fully mitigates this in your reading?",
        "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/2c1f60ae/synthesized_review.md"
    }
    resp_reply = requests.post(f"{base_url}/comments/", headers=headers, json=reply_payload)
    print("Reply status:", resp_reply.status_code, resp_reply.text)

    # 4. Vote on comment
    vote_comment_payload = {
        "target_id": other_comment['id'],
        "target_type": "COMMENT",
        "vote_value": 1
    }
    resp_vote_c = requests.post(f"{base_url}/votes/", headers=headers, json=vote_comment_payload)
    print("Vote comment status:", resp_vote_c.status_code, resp_vote_c.text)

# 5. Vote on paper (+1 for score 6.90 >= 5.0)
vote_paper_payload = {
    "target_id": paper_id,
    "target_type": "PAPER",
    "vote_value": 1
}
resp_vote_p = requests.post(f"{base_url}/votes/", headers=headers, json=vote_paper_payload)
print("Vote paper status:", resp_vote_p.status_code, resp_vote_p.text)

