# # try:
# # except: bad dewa
#     #error handling (try, except)
# cgpa = input(" Enter your CGPA: ")
# try:
#    print(cgpa + 1)
# except TypeError:
#     print("Input a number")
# print("this is the line")
#
# sum = 0
# number = 10
# while number < 15:
#     print(sum + number)
#     number += 1
#
#     break #
#     continue #
# number = 0
# while True:
#     print(number)
#     if number == 3:
#         continue
#         print(number)
#     if
#     number += 1
# print("this is the last line")

# Guess the number between 1 and 100:

import random

computer_guessed_number = random.randint(1,100)

while True:
    try:
        user_guessed = int(input("Guess the number within 1 to 100: "))
        if user_guessed not in range(1,100):
            print("Enter a number within 1 to 100")
            continue
        if computer_guessed_number > user_guessed:
            print("Your guess is lower than the computer guessed number")
        elif computer_guessed_number < user_guessed:
            print(" your guess is higher than the computer guessed number")
        else:
            print("Congratulation!! You have guessed successfully")
            break
    except ValueError:
        print("Enter a valid number")











