# Fizzbuzz program --> get input from user

n = int(input("Enter a number:"))
# using for loop through numbers from 1 to n
for num in range(1, n + 1):
    if int (num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

