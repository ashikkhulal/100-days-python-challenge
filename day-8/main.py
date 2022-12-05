## Functions with inputs:

# def my_function():
#     #Do something

# my_function()

## Greet function:

# def greet():
#     print("Hello")
#     print("Hope you are doing well!")
#     print("Isn't the weather lovely today?")

# greet()

# def my_function(something):
#     #Do something with something

# my_function(123)

# def greet_with_name(name):
#     print(f"Hello, {name}")
#     print("Hope you are doing well!")
#     print(f"{name}, isn't the weather lovely today?")

# greet_with_name("Ashik")
# greet_with_name("Suvendu")

# Positional vs keyword argument:
# Functions with more than 1 input:

def greet_with_name_and_location(name, location):
    print(f"Hello, {name}")
    print(f"Are you from {location}?")
    print(f"{name}, how is the weather in {location}?")

# Positional argument:: 
# greet_with_name_and_location("Ashik", "Nepal")

# Keyword argument::
# greet_with_name_and_location(name="Ashik", location="Nepal")
# OR
# greet_with_name_and_location(location="Nepal", name="Ashik")

## Exercise-1:
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height x wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 * 4) / 5
#                            = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

# #Write your code below this line 👇
# import math

# def paint_calc(height, width, cover):
#     number_of_cans = (height * width) / cover
#     rounded_number_of_cans = math.ceil(number_of_cans)
#     print(f"You'll need {rounded_number_of_cans} cans of paint.")

# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

## Exercise-2:

# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# https://en.wikipedia.org/wiki/Prime_number
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# #Write your code below this line 👇
# def prime_checker(number):
#     is_prime = True
#     if number <= 2:
#         is_prime = True
#     else:
#         for num in range(2, number):
#             if number % num == 0:
#                 is_prime = False
#                 break
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")      

# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

# #Caesar Cipher Part 1 - Encryption:

# alphabet = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
# ]

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(text, shift):
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     #e.g.
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     cipher_text = ""
#     for letter in text:
#         index = alphabet.index(letter)
#         shifted_index = index + shift
#         if shifted_index >= 26:
#             new_shifted_index = shifted_index - 26
#         else:
#             new_shifted_index = shifted_index
#         shifted_letter = alphabet[new_shifted_index]
#         cipher_text += shifted_letter

#     print(f"Here is the encoded result: {cipher_text}")

#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# if direction == "encode":
#     encrypt(text, shift)

# #Caesar Cipher Part 2 - Decryption:

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"Here is the encoded result: {cipher_text}")

# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(plain_text, shift_amount):
#     decipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         if new_position < 0:
#             formatted_new_position = 26 + new_position
#         else:
#             formatted_new_position = new_position
#         decipher_text += alphabet[formatted_new_position]
#     print(f"Here is the decoded result: {decipher_text}")

#   #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#   #e.g. 
#   #cipher_text = "mjqqt" || "ejgwf"
#   #shift = 5 || 5
#   #plain_text = "hello" || "zebra"
#   #print output: "The decoded text is hello"


# #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(plain_text=text, shift_amount=shift)
# else:
#     print("Wrong input entered!")

# #Caesar Cipher Part 3 - Reorganizating our code:

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"Here is the encoded result: {cipher_text}")

# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(plain_text, shift_amount):
#     decipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         if new_position < 0:
#             formatted_new_position = 26 + new_position
#         else:
#             formatted_new_position = new_position
#         decipher_text += alphabet[formatted_new_position]
#     print(f"Here is the decoded result: {decipher_text}")

#   #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#   #e.g. 
#   #cipher_text = "mjqqt" || "ejgwf"
#   #shift = 5 || 5
#   #plain_text = "hello" || "zebra"
#   #print output: "The decoded text is hello"


# #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(plain_text=text, shift_amount=shift)
# else:
#     print("Wrong input entered!")