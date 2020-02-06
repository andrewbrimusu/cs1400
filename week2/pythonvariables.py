print("Hello")

age = 38
height = 77

age, height = 18, 71

print("age, height: ",age,height)

xvar = 10
yvar = 20

print("xvar, yvar: ",xvar,yvar)

tmp = xvar
xvar = yvar
yvar = tmp

print("xvar, yvar: ",xvar,yvar)

xvar, yvar = yvar,  xvar

print("xvar, yvar: ",xvar,yvar)

gpa1, gpa2, gpa3 = eval(input("enter gpa for 3 classes, and I'll compute the overall: "))
totgpa = (gpa1 + gpa2 + gpa3) / 3
print("totgpa: ",totgpa)

name, major, favColor = input("enter your stats: ").split(",")
print("name, major, favColor: ",name, major, favColor)

PI = 3.14159265358979323846
radius = eval(input("enter the radius and i will compute the area of a circle: "))
area = PI * radius * radius
area = PI * radius ** 2
print("area: ",area)

print(7//2)
print(7/2)
print(7%2)