import json

filename = r"C:\Users\DELL\Desktop\data.txt"
with open(filename,"r") as file:
  data = json.load(file)

print("name: ",data['name'])
print("city: ",data['city'])