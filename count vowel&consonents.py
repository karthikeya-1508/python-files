text = input("enter a string: ")

vowels = "aeiouAEIOU"


vowel_count = 0
consonent_count = 0

for char in text:
  if char.isalpha():
    if char in vowels:
      vowel_count += 1
    else:
      consonent_count += 1

print("vowel count is : ",vowel_count)
print("consonent count is : ",consonent_count)