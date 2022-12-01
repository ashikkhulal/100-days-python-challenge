## For loop with python list

# for item in list_of_items:
#     #DO something to each item

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print (fruit + " Pie")

# Exercise-1:
# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# e.g. 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 ÷ 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
# total_height = 0
# for heights in student_heights:
#   total_height += heights
# #Write your code below this row 👇
# average_height = total_height/(n+1)
# rounded_average_height = "{:.0f}".format(average_height)
# print(rounded_average_height)

## Exercise-2:
# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions. The output words must match the example. i.e
# The highest score in the class is: x

# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
# heighest_score = student_scores[0]
# for score in student_scores:
#     if heighest_score < score:
#         heighest_score = score

# #Write your code below this row 👇

# print(f"The highest score in the class is: {heighest_score}")

## Range() function:
# for number in range(a, b):
#     print(number)
# Note: b is not included in range, to include b, put the range from a to b + 1

# for number in range(1, 10):
#     print(number)
## range(a, b, c) where c steps the range function:
# for number in range(1, 10, 2):
#     print(number)

## sum from 1 to 100:
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

## Exercise-3:
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

# #Write your code below this row 👇
# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)

## Exercise-4:
# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# #Write your code below this row 👇

# for number in range(1, 101):
#     if number % 15 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
