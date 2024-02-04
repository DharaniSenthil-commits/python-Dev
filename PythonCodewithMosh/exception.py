from timeit import timeit
try:
    with open("app.py") as f1, open("fizzbuzz.py") as f2:
        print("File will automatically close as it is has control contexting protocol")
    file = open("app.py")
    age = int(input("Age :"))
    xfactor = 10/age

# except ValueError as ex:
#     print("You didn't enter a valid age")
#     print(ex)
#     print(type(ex))
# except ZeroDivisionError:
#     print("Age cannot be  0")
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No Exception were thrown")
finally:
    file.close()
print("Excution continues")

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0  or less")
    return 10/age

try:
    calculate_xfactor(-1)
except ValueError as Error:
    pass
"""
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age

try:
    a=calculate_xfactor(-1)
    if a == None :
        pass
except ValueError as Error:
    print(Error)
"""
print("code1 : ", timeit(code1, number=10000))
print("code2 : ", timeit(code2, number=10000))
