from functools import reduce

nums = [9,4,6,3,5,8,4,2]

evens = list(filter(lambda n : n%2 == 0,nums))

doubles = list(filter(lambda n : n*2,nums))

sum = filter(lambda a,b : a+b , doubles)


print(evens)
print(doubles)
print(sum)