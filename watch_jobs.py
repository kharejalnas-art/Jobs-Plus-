import requests
import json
from pathlib import Path

URL = "https://boards-api.greenhouse.io/v1/boards/openai/jobs"

db = Path("jobs.json")

old_jobs = []

if db.exists():
    old_jobs = json.loads(db.read_text(encoding="utf-8"))

new_jobs = requests.get(URL).json()["jobs"]

old_ids = {j["id"] for j in old_jobs}

added = []

for job in new_jobs:
    if job["id"] not in old_ids:
        added.append(job)

if added:
    print("وظائف جديدة:\n")

    for job in added:
        print(job["title"])
        print(job["absolute_url"])
        print("----------------")

db.write_text(json.dumps(new_jobs), encoding="utf-8")
