
def wordcount_in_file(filename):
  with open(filename,"r") as file:
    text = file.read()
    words = text.split()
    return len(words)
  

filename = r"C:\Users\DELL\Desktop\sample que.txt"


count_words = wordcount_in_file(filename)
print("total words in file is : ",count_words)