import requests
import pandas as pd
import json

url = "https://www.cloudflarestatus.com/api/v2/summary.json"


GROUP_ID = input("enter group id: ")
try:
  response = requests.get(url)
  response.raise_for_status()
  data = response.json()
except  requests.exceptions.RequestException as e:
  print("error fetching url:",e)
  exit()

components = data.get("components",[])

extracted_data = []

for component in components:
  if component.get("group_id") == GROUP_ID:
    extracted_data.append({
     "id":component.get("id"),
     "name":component.get("name"),
     "status":component.get("status")
   })

if extracted_data:
  df = pd.DataFrame(extracted_data)
  output_filename = 'cloudflare_status1.xlsx'

  df.to_excel(output_filename,index = False)
  print(f"successfully exported data to {output_filename}")
else:
  print("no data exported")
