import math

print("Hello World !")
print("=" * 10)

students_count = 1000
rating = 4.99
is_published = False
course_name = 'python'
course_name = "python in double quotes"
course_name = """
python
in 
Multiple
lines
"""
x, y = 1, 2
x = y = 1


age: int = 23
# age = "test"
print(age)
# string
course = "Python Programming"
print(course[0])
print(course[-1])
print(course[0:3])
print(course[:3])
print(course[0:])
print(course[:])

print(id(course))
print(id(course[0]))

# Escape Sequence
message = "python \"programming"
print(message)
message = "python \\programming"
print(message)

message = "python \nprogramming"
print(message)

message = """python
programming"""
print(message)

# formatted String
first = "Dharani"
last = "E S"
full = first + " " + last
print(full)
full = f"{first} {last}"
print(full)
full = f"{len(first)} {last}"
print(full)
full = f"{first} {2+2}"
print(full)


# String usefull methods

test = " python Programming"

print(test.upper())
print(test.lower())
print(test.title())
print(test.strip())  # rstrip,lstrip
print(test.find("Pro"))
print(test.replace("p", "-"))
print("Pro" in test)
print("Pro" not in test)

# numbers

x = 10

x = 0b10
print(x)
print(bin(x))

x = 0x12c
print(x)
print(hex(x))

# complex number a+bi
x = 10+20j
print(x)

# numbers

x = 10+3
x = 10-3
x = 10*3
x = 10/3
x = 10//3
x = 10 % 3
x = 10**3

x = x+1
x += 1

# working with number
PI = -3.14  # indicating constant variable , so that other developer will know it

print(round(PI))
print(abs(PI))
print(math.floor(PI))

# type conversion
x = input("X: ")
print(int(x))
print(float(x))
print(bool(x))

# Conditional Statement

ageOfguy = 22
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("child")
print("All Done !")

# logical operator

name = " "
if not name.strip():
    print("Name is empty")
age = 24
if age >= 18 and age < 65:
    print("Eligibleee")
if 18 <= age < 65:
    print("Elligible")


# Ternary Operator

y = 10
message = ">= 10" if y >= 10 else "<10"
print(message)

# for loop
for i in "python":
    print(i)

for i in ['1', 'a']:
    print(i)

for i in range(0, 10, 2):
    print(i)

print(type(range(5)))
print([1, 2, 3])

names = ["john", "Mosh"]
for name in names:
    if name.startswith('j'):
        print("Found")
        break
else:
    print("not found")

# while loop
answer = 5
guess = 0

while guess != answer:
    guess = int(input("Guess : "))
else:
    pass

# function


def increment(number: int, by: int = 1) -> tuple:
    return (number, number+by)


print(increment(5))


# arguments xargs

def multiply(*list) -> int:
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# arguments xxargs


def save_user(**user) -> str:
    return (user["id"])


print(save_user(id="1", name="Mosh"))


# scope

message = "a"


def greet():
    global message
    message = "b"
    if True:
        msg = "aa"
    print(msg)


greet()
print(message)
