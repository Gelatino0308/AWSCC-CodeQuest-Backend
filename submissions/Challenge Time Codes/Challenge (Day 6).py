limit = int(input("Enter the limit for the range of numbers to be printed in FizzBuzz game: "))

print(f"\nLimit: {limit}\n")
for i in range(1, limit + 1):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz!")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
