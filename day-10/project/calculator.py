import os
from art import logo, bye

# Add
def add(n1, n2):
    return n1 + n2

# Subract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

def clear():
    os.system('cls')

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    is_Continue = True

    while is_Continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        restart = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or 'exit' to exit calculator: ").lower()

        if restart == 'y':
            num1 = answer
        elif restart == 'n':
            is_Continue = False
            clear()
            calculator()
        elif restart == 'exit':
            is_Continue = False
            print("Ok bye...")
            print(bye)
        else:
            print("Wrong input entered! Calculaor will exit...")
            is_Continue = False

calculator()