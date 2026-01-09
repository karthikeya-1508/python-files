file1 = r"C:\Users\DELL\Desktop\1.txt"
file2 = r"C:\Users\DELL\Desktop\sample.txt"

file3 = r"C:\Users\DELL\Desktop\merged.txt"

with open(file1,"r") as f1 , open(file2,"r") as f2 , open(file3,"w") as out:
  data1 = f1.read()
  data2 = f2.read()

  out.write(data1 + "\n" + data2)

print("merging of two files is :",file3)