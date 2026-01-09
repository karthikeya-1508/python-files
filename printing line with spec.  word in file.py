filename = r"C:\Users\DELL\Desktop\sample que.txt"

word = input("enter a word to be search: ")

with open(filename,"r") as file:
  for line in file:
    if word in line:
      print(line.strip())