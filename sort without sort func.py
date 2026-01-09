list = [4,7,2,6,5]

print("original list", list)

for i in range(len(list)):
  for j in range(i+1,len(list)):
    if list[i] > list[j]:
      list[i],list[j] = list[j],list[i]


print("sorted list is: ",list)