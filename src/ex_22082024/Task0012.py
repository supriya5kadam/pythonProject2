# Program of Fibonacci series using for loop
num =15
n1, n2 = 0, 1
print("Given terms are: " ,num)
print("Fibonacci series: ", n1, n2, end=",")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3

    print(n3, end=" , ")
