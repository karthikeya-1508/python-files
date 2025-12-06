import requests
import json

url = "https://www.cloudflarestatus.com/api/v2/scheduled-maintenances/upcoming.json"

response = requests.get(url)
data = response.json()

print(json.dumps(data, indent=2))
