import time

file_name =  input("enter output file name :  ")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")



timestamp = time.strftime("%Y-%m-%d %H:%M:%S")


if choice == '1':
    result = f"{num1} + {num2} = {num1 + num2}"
elif choice == '2':
    result = f"{num1} - {num2} = {num1 - num2}"
elif choice == '3':
    result = f"{num1} * {num2} = {num1 * num2}"
elif choice == '4':
    if num2 != 0:
        result = f"{num1} / {num2} = {num1 / num2}"
    else:
        result = "Error: Division by zero!"
else:
    result = "Invalid choice!"


print(result)


with open(file_name, "a") as f:
    f.write(f"[{timestamp}]  {result}\n")

print(f"Result saved to {file_name}")
