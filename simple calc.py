num1 = float(input("enter a number1: "))

num2 = float(input("enter a number2: "))

print("----select operation----")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")

choice = input("enter your choice (1/2/3/4):")

if choice == '1':
  print(f"Result: {num1} + {num2} = {num1 + num2}")
elif choice == '2':
  print(f"Result: {num1} - {num2} = {num1 - num2}")
elif choice == '3':
  print(f"Result: {num1} * {num2} = {num1 * num2}")
elif choice == '4':
  if num2 != 0: 
   print(f"Result: {num1} / {num2} = {num1 / num2}")
  else:
    print("error: division by zero ")

else:
  print("invalid choice")