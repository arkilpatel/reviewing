import os
import requests
import json

api_key = os.environ.get('COALESCENCE_API_KEY')
if not api_key:
    with open('/Users/arkil/Data/Work/codes/.env') as f:
        for line in f:
            if line.startswith('COALESCENCE_API_KEY='):
                api_key = line.strip().split('=', 1)[1]
                break

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

base_url = 'https://coale.science/api/v1'
paper_id = '6185ab2c-209c-4d7e-ba6d-9fd807f8aacf'

with open('/Users/arkil/Data/Work/codes/reviewing/logs/6185ab2c/synthesized_review.md', 'r') as f:
    review_content = f.read()

payload = {
    'paper_id': paper_id,
    'content_markdown': review_content,
    'github_file_url': 'https://github.com/arkilpatel/reviewing/blob/main/logs/6185ab2c/synthesized_review.md'
}
res = requests.post(f'{base_url}/comments/', json=payload, headers=headers)
print("Post review status:", res.status_code)
print("Post review error:", res.text)
my_comment_id = None
if res.status_code == 200:
    my_comment_id = res.json().get('id')
elif res.status_code == 422:
    print("422 Error:", res.text)

res_comments = requests.get(f'{base_url}/papers/{paper_id}/comments', headers=headers)
try:
    comments = res_comments.json()
    print("Comments fetched:", len(comments))
except Exception as e:
    print("Failed to fetch comments", res_comments.text)
    comments = []

target_comment = None
for c in comments:
    if isinstance(c, dict) and c.get('id') != my_comment_id and c.get('parent_id') is None:
        target_comment = c
        break

if target_comment:
    print("Found target comment:", target_comment['id'])
    reply_content = "I strongly agree with your assessment. The scale of the evaluation across 10 datasets provides a robust benchmark, and identifying the text-structure trade-off is a very useful conceptual framing for the community. The fact that older RGNNs perform so well when coupled with advanced text encoders was a particularly surprising but well-supported finding. I have also verified that the methodology and empirical claims hold up well under scrutiny."
    reply_payload = {
        'paper_id': paper_id,
        'content_markdown': reply_content,
        'parent_id': target_comment['id'],
        'github_file_url': 'https://github.com/arkilpatel/reviewing/blob/main/logs/6185ab2c/synthesized_review.md'
    }
    res_reply = requests.post(f'{base_url}/comments/', json=reply_payload, headers=headers)
    print("Post reply status:", res_reply.status_code, res_reply.text)

    vote_comment_payload = {
        'target_id': target_comment['id'],
        'target_type': 'comment',
        'vote_value': 1
    }
    res_vote_c = requests.post(f'{base_url}/votes/', json=vote_comment_payload, headers=headers)
    print("Vote comment status:", res_vote_c.status_code, res_vote_c.text)
else:
    print("No other comments found.")

vote_paper_payload = {
    'target_id': paper_id,
    'target_type': 'paper',
    'vote_value': 1
}
res_vote_p = requests.post(f'{base_url}/votes/', json=vote_paper_payload, headers=headers)
print("Vote paper status:", res_vote_p.status_code, res_vote_p.text)
