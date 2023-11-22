#Create a program where it takes a numerical input and evaluates whether it is a positive number, a negative number, or zero. You may customize it however you want.

number = int(input("Enter an integer: "))

if number > 0:
    print(f"{number} is a Positive number!")
elif number == 0:
    print("That number is a Zero!")
else:
    print(f"{number} is a Negative number!")