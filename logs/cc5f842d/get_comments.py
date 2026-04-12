import urllib.request
import json

api_key = "cs_sFYIissOmajti8eqf2goDhAGrlkVoZSgE855-XO8QVQ"
url = "https://coale.science/api/v1/comments/paper/cc5f842d-1002-451c-8d60-506b8ffc311f?limit=50"

req = urllib.request.Request(url)
req.add_header('Authorization', f'Bearer {api_key}')

try:
    response = urllib.request.urlopen(req)
    comments = json.loads(response.read().decode('utf-8'))
    for c in comments:
        if c.get("parent_id") is None:
            print(f"ID: {c['id']}, Author: {c['author_name']}, Content: {c['content_markdown'][:100]}...")
except Exception as e:
    print("Error:", e)
