import urllib.request, json
with open('.api_key', 'r') as f: key = f.read().strip()
headers = {'Authorization': key}
pid = "c4a00dde-74ae-4dc0-9ea3-068bd4f8f04b"
req = urllib.request.Request(f"https://koala.science/api/v1/papers/{pid}", headers=headers)
with urllib.request.urlopen(req) as r:
    paper = json.loads(r.read().decode())
    with open("logs/tame/paper_info.json", "w") as out:
        json.dump(paper, out, indent=2)
