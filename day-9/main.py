## Python dictionaries:

# Key: value pair
# {Key: Value}
# {
# "Bug": "An error in a program that prevents the program from running as expected",
# "X": "alphabet"
# }

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.", 
# }

# # Retrieving items from dictionary
# print(programming_dictionary["Bug"])

# # Adding new items to dictionary:
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dictionary["Loop"])

# # Creating an empty dictionary.
# empty_dictionary = {}

# # Wiping an existing dictionary
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.", 
# }
# programming_dictionary = {}

# Editing an iteam in a dictionary:
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.", 
# }
# programming_dictionary["Bug"] = "Something else."

# Looping through the dictionary:
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.", 
# }

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

## Exercise-1

# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.
# DO NOT modify lines 1-7 to change the existing student_scores dictionary.
# DO NOT write any print statements.
# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     name = key
#     score = student_scores[key]
#     if score >= 91:
#         grade = "Outstanding"
#     elif score >= 81:
#         grade = "Exceeds Expectations"
#     elif score >= 71:
#         grade = "Acceptable"
#     else:
#         grade = "Fail"
    
#     student_grades[name] = grade
    

# # 🚨 Don't change the code below 👇
# print(student_grades)

## Nesting:

# {
#     Key: [List],
#     Key2: {Dictionary}
# }

# capital = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }


# # Nesting list in a dictionary:
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# # Nesting dictionaries in a dictionary:
# travel_log = {
#     "France": {
#         "cities_visited" : ["Paris", "Lille", "Dijon"]
#     },
#     "Germany": {
#         "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"]
#     },
# }

# travel_log = {
#     "France": {
#         "cities_visited" : ["Paris", "Lille", "Dijon"], 
#         "total_visits": 12,
#     },
#     "Germany": {
#         "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
#         "total_visits": 8,
#     },
# }

# travel_log = {
#     {
#         "country": "France",
#         "cities_visited" : ["Paris", "Lille", "Dijon"], 
#         "total_visits": 12,
#     },
#     {   
#         "country": "Germany",
#         "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
#         "total_visits": 8,
#     },
# }

# Nesting dictionaries in a list:
# [{
#     "key1": "value1",
# },
# {
#     "key2": "value2"
# }
# ]

# travel_log = [
#     {
#         "country": "France", 
#         "cities_visited" : ["Paris", "Lille", "Dijon"], 
#         "total_visits": 12,
#     },
#     {   
#         "country": "Germany",
#         "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
#         "total_visits": 8,
#     },
# ]

## Exercise-2:
# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.
# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# You've visited Russia 2 times.
# You've been to Moscow and Saint Petersburg.


# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country, visits, cities):
#     global travel_log
#     new_entry = {
#         "country": country,
#         "visits": visits,
#         "cities": cities
#     }
#     travel_log.append(new_entry)

# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

