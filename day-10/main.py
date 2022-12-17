## Functions with output:

# simple function:
# def my_function():
#     # Do something

# my_function()

# function with input:
# def my_function(x):
#     # Do something with x

# my_function(x)

# function with input and output (return):
# def my_function(x):
#     # result = Do something with x
#     return result

# my_function(x)

# def format_name(first_name, last_name):
#     formatted_first_name = first_name.title()
#     formatted_last_name = last_name.title()

#     return f"{formatted_first_name} {formatted_last_name}"

# formatted_full_name = format_name("AsHik", "KHULAL")

# print(formatted_full_name)

# Built in functions with output: len("Ashik")

## Multiple return values:

# def format_name(first_name, last_name):
#     if first_name == "" or last_name == "":
#         return "Warning: first and last names should not be empty!"
#     else:
#         formatted_first_name = first_name.title()
#         formatted_last_name = last_name.title()

#         return f"Full formatted name: {formatted_first_name} {formatted_last_name}"

# #formatted_full_name = format_name("AsHik", "KHULAL")
# formatted_full_name = format_name("", "")

# print(formatted_full_name)

## Exercise-1:

# In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.
# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
# days_in_month(year=2022, month=2)
# And it will use this information to work out the number of days in the month, then return that as the output, e.g.:
# 28
# The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return "true"
#       else:
#         return "false"
#     else:
#       return "true"
#   else:
#     return "false"

# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     is_leap_year = is_leap(year)
#     if is_leap_year == "true" and month == 2:
#         days = 29
#         return days
#     else:
#         days = month_days[month-1]
#         return days
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

## Docstrings:

# def format_name(first_name, last_name):
#     """Take a first and last name and format it to return the title
#     case version of the name."""                                                   # docstring
#     if first_name == "" or last_name == "":
#         return "Warning: first and last names should not be empty!"
#     else:
#         formatted_first_name = first_name.title()
#         formatted_last_name = last_name.title()

#     return f"Full formatted name: {formatted_first_name} {formatted_last_name}"

# formatted_full_name = format_name("AsHik", "KHULAL")
# print(formatted_full_name)


## Calculator Part-1:

# # Add
# def add(n1, n2):
#     return n1 + n2

# # Subract
# def subtract(n1, n2):
#     return n1 - n2

# # Multiply
# def multiply(n1, n2):
#     return n1 * n2

# # Divide
# def divide(n1, n2):
#     return n1 / n2

# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
# }

# def calculator():
#     num1 = int(input("What's the first number?: "))

#     for symbol in operations:
#         print(symbol)

# # operation_symbol = input("Pick an operation from the line above: ")

# # num2 = int(input("What's the second number?: "))

# # calculation_function = operations[operation_symbol]
# # answer = calculation_function(num1, num2)

# # print(f"{num1} {operation_symbol} {num2} = {answer}")

# ## Print vs Return:

# # operation_symbol = input("Pick another operation: ")

# # num3 = int(input("What's the next number?: "))

# # calculation_function = operations[operation_symbol]
# # second_answer = calculation_function(calculation_function(num1, num2), num3)

# ## While Loops, Flags and Recursion:

#     is_Continue = True

#     while is_Continue:
#         operation_symbol = input("Pick an operation: ")
#         num2 = int(input("What's the next number?: "))
#         calculation_function = operations[operation_symbol]
#         answer = calculation_function(num1, num2)
        
#         print(f"{num1} {operation_symbol} {num2} = {answer}")
        
#         restart = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()

#         if restart == 'y':
#             num1 = answer
#         elif restart == 'n':
#             is_Continue = False
#             calculator()
#         else:
#             print("Wrong input entered!")
#             is_Continue = False

# calculator()