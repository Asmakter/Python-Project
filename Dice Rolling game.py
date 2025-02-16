import random
while True:
    choice = input("Roll the dice? [y/n]: ")

    if choice.lower() == 'y':
        number = random.randint(1, 6)
        print(f"The dice value is: {number}")
    elif choice.lower() == 'n':
        print("Thank you")
        break
    else:
        print("Invalid input")
