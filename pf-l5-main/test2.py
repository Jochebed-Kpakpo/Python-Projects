def addmultiplenumbers(numbers):
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def isiteven(num):
    return num % 2 == 0

def isitaninteger(num):
    return num.is_integer()

def main():
    print("Welcome to the Simple Calculator!")
    
    while True:
        print("\nChoose an operation:")
        print("1. Add multiple numbers")
        print("2. Multiply multiple numbers")
        print("3. Check if a number is even")
        print("4. Check if a number is an integer")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            numbers = input("Enter numbers to add, separated by spaces: ")
            numbers = [float(num) for num in numbers.split()]
            print("The sum is:", addmultiplenumbers(numbers))
        
        elif choice == '2':
            numbers = input("Enter numbers to multiply, separated by spaces: ")
            numbers = [float(num) for num in numbers.split()]
            print("The result is:", multiplymultiplenumbers(numbers))
        
        elif choice == '3':
            num = float(input("Enter a number to check if it's even: "))
            print("Is it even?", isiteven(num))
        
        elif choice == '4':
            num = float(input("Enter a number to check if it's an integer: "))
            print("Is it an integer?", isitaninteger(num))
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
