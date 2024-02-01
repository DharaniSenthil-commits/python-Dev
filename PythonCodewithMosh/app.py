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
