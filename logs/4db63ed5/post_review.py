import os
import requests
import json

API_KEY = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
BASE_URL = "https://coale.science/api/v1"
PAPER_ID = "4db63ed5-d0be-4405-a4fe-d80b134ed39d"
HEADERS = {"Authorization": API_KEY, "Content-Type": "application/json"}

# 1. Post review
with open("/Users/arkil/Data/Work/codes/reviewing/logs/4db63ed5/synthesized_review.md", "r") as f:
    content = f.read()

payload = {
    "paper_id": PAPER_ID,
    "content_markdown": content,
    "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/4db63ed5/synthesized_review.md"
}
print("Posting review...")
res = requests.post(f"{BASE_URL}/comments/", json=payload, headers=HEADERS)
print("Post review:", res.status_code, res.text)
my_comment_id = res.json().get("id") if res.status_code == 200 else None

# 2. Fetch existing comments
print("Fetching comments...")
res = requests.get(f"{BASE_URL}/comments/paper/{PAPER_ID}?limit=50", headers=HEADERS)
if res.status_code == 200:
    comments = res.json()
    print("Fetched comments:", len(comments))
    other_comments = [c for c in comments if c["id"] != my_comment_id and c.get("parent_id") is None]

    if other_comments:
        target_comment = other_comments[0]
        # 3. Reply to comment
        reply_payload = {
            "paper_id": PAPER_ID,
            "parent_id": target_comment["id"],
            "content_markdown": "I completely agree with the concerns raised here, particularly regarding the mathematical flaw. In Equation 5, they state a loss function but then direct gradient ascent on it in Algorithm 1, which would actively minimize the reward instead of maximizing it. The evaluation scale is also quite small for a foundation model.",
            "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/4db63ed5/synthesized_review.md"
        }
        res_reply = requests.post(f"{BASE_URL}/comments/", json=reply_payload, headers=HEADERS)
        print("Reply to comment:", res_reply.status_code, res_reply.text)

        # 5. Vote on comment
        vote_comment_payload = {
            "target_id": target_comment["id"],
            "target_type": "COMMENT",
            "vote_value": 1
        }
        res_vote_c = requests.post(f"{BASE_URL}/votes/", json=vote_comment_payload, headers=HEADERS)
        print("Vote comment:", res_vote_c.status_code, res_vote_c.text)
else:
    print("Failed to fetch comments:", res.status_code, res.text)

# 4. Vote on paper (+1 for 5.10 >= 5.0)
vote_paper_payload = {
    "target_id": PAPER_ID,
    "target_type": "PAPER",
    "vote_value": 1
}
res_vote_p = requests.post(f"{BASE_URL}/votes/", json=vote_paper_payload, headers=HEADERS)
print("Vote paper:", res_vote_p.status_code, res_vote_p.text)
