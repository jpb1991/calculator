# THIS IS GETTING UPDATED TO MATCH THE README.MD ON THE REPO 
# DO NOT USE DUMMY.PY 
# WE ARE MAKING IT FANCY AND REALLY AMAZING FOR YOU GUYS !! 
# DO NOT USE 
# DO NOT USE
# THIS IS GETTING UPDATED TO MATCH THE README.MD ON THE REPO 
# DO NOT USE DUMMY.PY 
# WE ARE MAKING IT FANCY AND REALLY AMAZING FOR YOU GUYS !! 
# DO NOT USE 
# DO NOT USE

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    return math.sqrt(x)

def get_number(prompt):
    """Function to safely handle numeric input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide,
        '5': power,
        '6': sqrt
    }
    
    menu = """
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square Root
Q. Quit
"""
    while True:
        print(menu)
        choice = input("Enter choice (1/2/3/4/5/6/Q): ").upper()

        if choice == 'Q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in operations:
            if choice == '6':  # Square root only needs one number
                num = get_number("Enter number for square root: ")
                result = operations[choice](num)
                print("Result: ", result)
            else:
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")
                result = operations[choice](num1, num2)
                print("Result: ", result)
        else:
            print("Invalid input. Please select a valid operation.")

if __name__ == "__main__":
    main()

# THIS IS GETTING UPDATED TO MATCH THE README.MD ON THE REPO 
# DO NOT USE DUMMY.PY 
# WE ARE MAKING IT FANCY AND REALLY AMAZING FOR YOU GUYS !! 
# DO NOT USE 
# DO NOT USE
# THIS IS GETTING UPDATED TO MATCH THE README.MD ON THE REPO 
# DO NOT USE DUMMY.PY 
# WE ARE MAKING IT FANCY AND REALLY AMAZING FOR YOU GUYS !! 
# DO NOT USE 
# DO NOT USE
