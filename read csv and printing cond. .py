import pandas as pd

df = pd.read_csv(r"C:\Users\DELL\Desktop\excel prep\data.csv")

result = df[df['age'] > 30]

print(result)