"""
Simple Calculator Program
Performs basic arithmetic operations: add, subtract, multiply, divide
"""


def add(x, y):
    """Add two numbers"""
    return x + y


def subtract(x, y):
    """Subtract two numbers"""
    return x - y


def multiply(x, y):
    """Multiply two numbers"""
    return x * y


def divide(x, y):
    """Divide two numbers with error handling"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y


def main():
    """Main function to run the calculator"""
    print("=" * 40)
    print("         Simple Calculator")
    print("=" * 40)
    
    try:
        # Get user input for two numbers
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Display operation choices
        print("\nSelect an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        # Get operation choice
        choice = input("\nEnter operation (1/2/3/4): ")
        
        # Perform the selected operation
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "/"
        else:
            print("Invalid operation choice! Please enter 1, 2, 3, or 4.")
            return
        
        # Display the result
        if isinstance(result, str):  # Check if it's an error message
            print(f"\n{result}")
        else:
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        
        print("=" * 40)
    
    except ValueError:
        print("Error: Please enter valid numbers!")


if __name__ == "__main__":
    main()
