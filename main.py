import requests

url = "https://boards-api.greenhouse.io/v1/boards/openai/jobs"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Found {len(data['jobs'])} jobs")

    for job in data["jobs"][:5]:
        print(job["title"])
else:
    print("Error:", response.status_code)
