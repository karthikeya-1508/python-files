from collections import Counter
filename = r"C:\Users\DELL\Desktop\sample que.txt"

with open(filename,"r") as file:
  text = file.read()
words = text.split()
word_count = Counter(words)
top_5 = word_count.most_common(5)

print("top 5 most frequent words:")

for word,count in top_5:
  print(word , ":" , count)
   