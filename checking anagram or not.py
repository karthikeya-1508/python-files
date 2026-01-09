str1 = input("enter a string1 : ")
str2 = input("enter a string2 : ")

str1 = str1.replace(" ","").lower()
str2 = str2.replace(" ","").lower()

if sorted(str1) == sorted(str2):
  print("two strings are anagrams.")
else:
  print("two strings are not anagrams.")