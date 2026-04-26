import urllib.request, json
with open('.api_key', 'r') as f: key = f.read().strip()
headers = {'Authorization': key}
pid = "b295d6d7-f5ae-4f43-8fc1-16f9052a4913"
req = urllib.request.Request(f"https://koala.science/api/v1/papers/{pid}", headers=headers)
with urllib.request.urlopen(req) as r:
    paper = json.loads(r.read().decode())
    with open("logs/spiral_rope/paper_info.json", "w") as out:
        json.dump(paper, out, indent=2)
