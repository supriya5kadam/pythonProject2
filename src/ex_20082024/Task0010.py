# Program that classifies a  triangle based on side lengths

print("Input lengths of the triangle sides:")
x= int(input("x:"))
y= int(input("y:"))
z= int(input("z:"))
if x==y==z:
    print("Equilateral triangle")
elif x==y or y==z or z==x:
    print("Isosceles triangle")
else:
    print("scalene triangle")


