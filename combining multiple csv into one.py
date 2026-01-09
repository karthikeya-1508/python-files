import pandas as pd
import glob

files = glob.glob(r"C:\Users\DELL\Desktop\excel prep\files\*.csv")

combined = pd.concat((pd.read_csv(f) for f in files),ignore_index = True)

combined.to_csv("combined.csv",index = False)

print("all files are combined.")