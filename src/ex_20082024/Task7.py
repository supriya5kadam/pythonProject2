# program to find given year is leap year or not

year= int(input("Enter a year-"))
if year % 400 == 0:
    print(f"{year} is leap year")

elif year %100 ==0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year}is not a leap year")

