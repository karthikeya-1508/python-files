def count_file(filename):
  with open(filename,"r") as file:
    text = file.read()
    word = text.split()
    characters  = len(text)
    file.seek(0)
    lines = file.readlines()

    return len(lines),len(word),characters

filename = r"C:\Users\DELL\Desktop\sample que.txt"

lines,word,chars = count_file(filename)

print("lines in file is : ",lines)
print("words in file is : ",word)
print("characters in file is : ",chars)