# ...existing code...
print("Welcome to the Calculator Program!")
print("You can perform addition, subtraction, multiplication, and division.")
print("What operation would you like to perform?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Enter the number corresponding to the operation (1-4): ").strip()
while operation not in ('1', '2', '3', '4'):
    print("Invalid operation selected. Please choose 1-4.")
    operation = input("Enter the number corresponding to the operation (1-4): ").strip()

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid number entered. Restart the program and enter numeric values.")
    exit()

if operation == '1':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")

if operation == '2':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")

if operation == '3':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")

if operation == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Error: Division by zero is not allowed.")
# ...existing code...