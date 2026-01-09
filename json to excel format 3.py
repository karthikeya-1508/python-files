import requests
import pandas as pd

url = "https://www.cloudflarestatus.com/api/v2/summary.json"


with open(r"C:\Users\DELL\Desktop\cloudflare id's.txt", "r") as file:
    region_ids = [line.strip() for line in file if line.strip()]


try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print("Error fetching URL:", e)
    exit()

components = data.get("components", [])


region_map = {
    component["id"]: component["name"]
    for component in components
    if component.get("group_id") is None
}

final_rows = []


for region_id in region_ids:
    region_name = region_map.get(region_id, region_id)

    
    final_rows.append({
        "Region": f"Region: {region_name}",
        "Name": "",
        "Status": ""
    })

    for component in components:
        if component.get("group_id") == region_id:
            final_rows.append({
                "Region": "",
                "Name": component.get("name"),
                "Status": component.get("status")
            })


    final_rows.append({
        "Region": "",
        "Name": "",
        "Status": ""
    })

df = pd.DataFrame(final_rows, columns=["Region", "Name", "Status"])


output_file = "cloudflare_regionwise_status2.xlsx"
df.to_excel(output_file, index=False)

print(f"Successfully exported data to {output_file}")
