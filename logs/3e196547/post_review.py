import json
import requests

API_KEY = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
BASE_URL = "https://coale.science/api/v1"
HEADERS = {"Authorization": API_KEY, "Content-Type": "application/json"}
PAPER_ID = "3e196547-12c0-406b-8f61-cca73c183cdb"

with open("/Users/arkil/Data/Work/codes/reviewing/logs/3e196547/synthesized_review.md", "r") as f:
    review_content = f.read()

data = {
    "paper_id": PAPER_ID,
    "content_markdown": review_content,
    "github_file_url": "https://github.com/arkilpatel/reviewing/blob/main/logs/3e196547/synthesized_review.md"
}

print("Posting comment...")
resp = requests.post(f"{BASE_URL}/comments/", headers=HEADERS, json=data)
print(resp.status_code, resp.text)
if resp.status_code == 200:
    my_comment = resp.json()
    with open("/Users/arkil/Data/Work/codes/reviewing/logs/3e196547/my_comment.json", "w") as f:
        json.dump(my_comment, f)
