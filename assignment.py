def main():
    print("Welcome to the simple calculator!")
    
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Calculate the result
    result = calculate(num1, num2, operation)

    # Print the result
    print(f"{num1} {operation} {num2} = {result}")
