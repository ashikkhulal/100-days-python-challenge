## IF-ELSE Statement
## if condition:
##     do this 
## else:
##     do this 

## Example:
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster! :)")
# else:
#     print("You cannot ride the rollercoaster! :(")

## Comparision Operators:
## > Greater than
## < Less than
## >= Greater than or equal to
## <= Less than or equal to
## == equal to
#// != not equal to

## Exercise 1:
## Write a program that works out whether if a given number is an odd or even number.

# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# reminder = number % 2
# if reminder == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# Nested if and elif statements

## if condition:
##  if condition:     
##      do this
##  else:   
##      do this  
## else:
##     do this 

## Example:
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster! :)")
#     age = int(input("What is your age? "))
#     if age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("You cannot ride the rollercoaster! :(")

## Example:
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster! :)")
#     age = int(input("What is your age? "))
#     if age > 18:
#         print("Please pay $12.")
#     elif age >= 12:
#         print("Please pay $7.")
#     else:
#         print("Please pay $5.")
# else:
#     print("You cannot ride the rollercoaster! :(")

## if / elif /else

## if condition1:
##     do A
## elif condition2:
##     do B
## else:
##     do C

## Exercise-2:
## Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
## It should tell them the interpretation of their BMI based on the BMI value.
## Under 18.5 they are underweight
## Over 18.5 but below 25 they have a normal weight
## Over 25 but below 30 they are slightly overweight
## Over 30 but below 35 they are obese
## Above 35 they are clinically obese.

# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = round(weight / (height ** 2))

# if bmi <= 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi <= 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi <= 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi <=35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")

## Exercise-3:
## Write a program that works out whether if a given year is a leap year. 
## A normal year has 365 days, leap years have 366, with an extra day in February.

## This is how you work out whether if a particular year is a leap year.
## on every year that is evenly divisible by 4 
## **except** every year that is evenly divisible by 100 
## **unless** the year is also evenly divisible by 400

# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if (year % 100 == 0):
#     if (year % 4 == 0):
#         if (year % 400 == 0):
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Not leap year.")
# else:
#     if (year % 4 == 0):
#         print("Leap year.")
#     else:
#         print("Not leap year.")

## Example:
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster! :)")
#     age = int(input("What is your age? "))
#     if age > 18:
#         bill = 12
#         print(f"Adult tickets are ${bill}.")
#     elif age >= 12:
#         bill = 7
#         print(f"Youth tickets are ${bill}.")
#     else:
#         bill = 5
#         print(f"Child tickets are ${bill}.")
    
#     wants_photo = input("Do you want a photo taken? Y or N: ")
#     if wants_photo == "Y":
#         bill+=3

#     print(f"Your final bill is ${bill}.")
# else:
#     print("You cannot ride the rollercoaster! :(")

## Exercise-4:
## Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
## Based on a user's order, work out their final bill.
## Small Pizza: $15
## Medium Pizza: $20
## Large Pizza: $25
## Pepperoni for Small Pizza: +$2
## Pepperoni for Medium or Large Pizza: +$3
## Extra cheese for any size pizza: + $1

# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if size == 'S':
#     bill = 15
#     if add_pepperoni == 'Y':
#         if extra_cheese == 'Y':
#             bill += 4
#             print(f"Your final bill is: ${bill}.")
#         else:
#             bill += 3
#             print(f"Your final bill is: ${bill}.")
#     else:
#         if extra_cheese == 'Y':
#             bill += 1
#             print(f"Your final bill is: ${bill}.")
#         else:
#             bill += 0
#             print(f"Your final bill is: ${bill}.")
# elif size == 'M':
#     bill = 20
#     if add_pepperoni == 'Y':
#         if extra_cheese == 'Y':
#             bill += 4
#             print(f"Your final bill is: ${bill}.")
#         else:
#             bill += 3
#             print(f"Your final bill is: ${bill}.")
#     else:
#         if extra_cheese == 'Y':
#             bill += 1
#             print(f"Your final bill is: ${bill}.")
#         else:
#             bill += 0
#             print(f"Your final bill is: ${bill}.")
# else:
#     bill = 25
#     if add_pepperoni == 'Y':
#         if extra_cheese == 'Y':
#             bill += 4
#             print(f"Your final bill is: ${bill}.")
#         else:
#             bill += 3
#             print(f"Your final bill is: ${bill}.")
#     else:
#         if extra_cheese == 'Y':
#             bill += 1
#             print(f"Your final bill is: ${bill}.")
#         else:
#             bill += 0
#             print(f"Your final bill is: ${bill}.")

## Logical Operators:
## and, or, not
# if condition1 & condition2 & condition3:
#   do this
# else:
#   do this

## Example:
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster! :)")
#     age = int(input("What is your age? "))
#     if age >= 45 and age <= 55:
#         bill = 0
#         print("You will ride for free. Your total bill is $0.")
#     else:
#         if age > 18:
#             bill = 12
#             print(f"Adult tickets are ${bill}.")
#         elif age >= 12:
#             bill = 7
#             print(f"Youth tickets are ${bill}.")
#         else:
#             bill = 5
#             print(f"Child tickets are ${bill}.")
#         wants_photo = input("Do you want a photo taken? Y or N: ")
#         if wants_photo == "Y":
#             bill+=3

#         print(f"Your final bill is ${bill}.")
# else:
#     print("You cannot ride the rollercoaster! :(")

## Exercise-5:
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# combined_name = name1 + name2
# lower_case_combined_name = combined_name.lower()
# t = lower_case_combined_name.count("t")
# r = lower_case_combined_name.count("r")
# u = lower_case_combined_name.count("u")
# e = lower_case_combined_name.count("e")
# l = lower_case_combined_name.count("l")
# o = lower_case_combined_name.count("o")
# v = lower_case_combined_name.count("v")
# e = lower_case_combined_name.count("e")

# total_for_true = t + r + u + e
# total_for_love = l + o + v + e

# true_love = str(total_for_true)+str(total_for_love)
# if int(true_love) < 10 or int(true_love) > 90:
#     print(f"Your score is {true_love}, you go together like coke and mentos.")
# elif int(true_love) >=40 and int(true_love) <= 50:
#     print(f"Your score is {true_love}, you are alright together.")
# else:
#     print(f"Your score is {true_love}.")
