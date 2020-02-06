import math
from math import factorial

# if i just "import math" then I need to reference the math module like below
print(math.factorial(5))

# if i use "from math import factorial", I have imported the function defition
# and I don't need to use math.factorial, I can just use factorial like below
print(factorial(5))




print("hello" + " friends" )

print(3 + 5)

print(+4)
howMuchFunImHaving = 1
howMuchFunImHaving = -howMuchFunImHaving

print(-4)
print(howMuchFunImHaving)

# lower camel case
carTopSpeed = 140

# age, height = eval(input("Enter your age and height in inches: "))

# print("age, height: ", age, height)

#this code will break, with a too many values to unpack error
# age, height = "38, 77"

#multiple assignment
x = y = z = 10

print("x, y, z: ", x, y, z)

age = 38.51

print(round(age), age)

#round does not change the variable, it just returnsit
#to change it, re-assign the variable with the returned value
age = round(age)

print("age: ", age)


# id() and type()
print(id(age)) #memory location

print(type(age)) #what type of data is in the object

#see formatting.py

