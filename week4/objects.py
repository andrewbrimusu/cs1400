import random

name = "Andy Brim"
print(name.upper())
name = name.upper()

print(name)

name = name.lower()
print(name)

print(name.strip())

phrase = " a man a plan a canal panama \t \t \t \t \n \n \n \n "

print(phrase)
print(phrase.strip())

print(phrase.rstrip())
print(phrase.lstrip())

print(format(3.1415926,"10.3f"))
print(format(10.1234,"10.3f"))
print(format(123413.01,"10.3f"))
print(format(4567.56,"10.3f"))
print("---scientific notation---")
print(format(57.467657, "10.2e"))
print(format(0.0033923, "10.2e"))
print(format(57.4, "10.2e"))
print(format(57, "10.2e"))

# 3.14e+6

print(format(3141592.6,"10.2e"))

x = int("beef", 16)
print("x: ",x)
# 11*4096 + 14*256 + 14*16 + 15*1 = 48879

bored = False
password = 1234

if bored == True:
    print("You're bored because you're boring!!! Go find something to do!")
else:
    print("You are awesome!")
    
print(int(False))
print(int(True))

password = 1234
if password == 1234:
    print("correct password!")
else:
    print("wrong try again")
    
    
print(random.randint(1, 6))

print(random.randint(1,2))
print(random.randint(1,100))