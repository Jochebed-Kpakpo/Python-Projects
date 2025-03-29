num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("The result of adding the two numbers is:", num1 + num2)

# Extra feature 1: Subtract second number from the first
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("The result of subtraction is:", num1 - num2)

# Extra feature 2: Multiply the two numbers
print("\nNow, let's multiply the two numbers.")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("The result of multiplication is:", num1 * num2)

# Extra feature 3: Divide the first number by the second number
print("\nNow, let's divide the first number by the second.")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num2 != 0:
    print("The result of division is:", num1 / num2)
else:
    print("Error: Division by zero is not allowed.")