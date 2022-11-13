## Data Types:

## String:
## Example
# "Hello"
# "123"
# print ("123" + "345")

## Subscripting:
## Example
# print("Hello"[0])
# print("Hello"[4])

## Integer: numbers without any decimal places
## Example
# print (123 + 345)
# 123_345_567 # Replaces _ with commas


## Float: numbers with decimal places
## Example
# 3.14159

## Boolean: either True or False

## Type Errors:
## Type() Function checks type of the data set
## Example
# name = "Ashik"
# print(type(name))

## Type Conversion:
# num_char = 123
# new_var1 = str(num_char)
# new_var2 = float(123)
# new_var3 = int(new_var1)
# print(type(num_char))
# print(type(new_var1))
# print(type(new_var2))
# print(type(new_var3))

## Exercise 1:
## Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇
# a=two_digit_number[0]
# b=two_digit_number[1]
# print(int(a)+ int(b))

## Mathematical Operators:
# 3 + 5 # Division
# 7 - 4 # Subraction
# 3 * 2 # Multiplication
# 6 / 2 # Division always results in float output
# 2 ** 2 # Exponent

## PEMDAS (Parentheses Exponent Multiplication Division Addition Subraction) -- Left to Right
# ()
# **
# * /
# + -

## Example:
# print(3 * 3 + 3 / 3 - 3)
# print(float(9 + 1 - 3))
# print(float(10 - 3))
# print(float(7))

## Exercise 2:
## Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
## The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
## The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# BMI = float(weight) / (float(height) ** 2)
# print(int(BMI))

## Number Manipulation and F Strings in Python:
## Round Function:
## Example
# print(round(8/3))
# print(round(8/3, 2))
# print(round(3.14151617, 4))

# print(8 // 3) # returns int vs print(8 / 3)

# result = 4 / 2
# result /= 2
# print(result)

# score = 0
# score += 1
# print(score)

# score = 0
# score -= 1
# print(score)

# score = 2
# score *= 2
# print(score)

# var = 1
# print(f"Your variable is {var}.")

## Exercise 3:
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left. Where x, y and z are replaced with the actual calculated numbers.

# # 🚨 Don't change the code below 👇
# age = input("What is your current age?\n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# days_left_until_90 = (90 * 365) - (int(age) * 365)
# weeks_left_unitl_90 = (90 * 52) - (int(age) * 52)
# months_left_unitl_90 = (90 * 12) - (int(age) * 12)

# print(f"You have {days_left_until_90} days, {weeks_left_unitl_90} weeks, and {months_left_unitl_90} months left.")





