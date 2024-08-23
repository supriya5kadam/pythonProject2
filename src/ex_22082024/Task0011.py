# Factorial of a given number using for loop

n = int(input("Enter the number: "))
if n == 0 or 1:
    print("Factorial is 1 : ")
else:
    f = 1

for i in range(2,n+1):
    f *= i
    print("Factorial of {} is:{}".format(n, f))

