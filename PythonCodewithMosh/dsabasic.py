from collections import deque
from array import array
# List
from collections import deque
letters = ['a', 'b', 'c']
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = letters+zeros
numbers = list(range(20))
chars = list("Hello ARA")
print(numbers, chars)
print(len(chars))

# Accessing element in list
letters = ['a', 'b', 'c']
letters[0] = 'A'
print(letters)
print(letters[::2])

print(numbers[::2])
print(numbers[::-1])

# list unpacking

numbers = list(range(10))
first, *other, last = numbers
print(first, last)
print(other)
first, second, *other = numbers
print(first, second)
print(other)

# looping over lists
for index, letter in enumerate(letters):
    print(index, letter)

# add or remove
letrs = list("abcdef")
letrs.append('g')
print(letrs)
letrs.insert(0, 'Z')
print(letrs)

letrs.pop()
print(letrs)
letrs.remove('f')
print(letrs)
del letrs[4:5]
print(letrs)
letrs.clear()
print(letrs)

# finding items
letrs = list("abcdef")
print(letrs.count("d"))
if "d" in letrs:
    print(letrs.index("d"))

# sorting list

nos = [3, 51, 2, 8, 6]
nos.sort()
print(nos)
print(sorted(nos, reverse=True))
print(nos)

items = [
    ('p1', 10),
    ('p1', 9),
    ('p1', 12),]


def sort_item(item):
    return item[1]


# items.sort(key=sort_item)
items.sort(key=lambda item: item[1])

print(items)

# Mapping function
prices = list(map(lambda item: item[1], items))
# List comprehension
prices = [item[1] for item in items]
print(prices)
# filter function
filtered = list(filter(lambda item: item[1] >= 10, items))
# List comprehension
filtered = [item for item in items if item[1] >= 10]
print(filtered)

# Zip Function
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))

# stack
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.pop()

if browsing_session:
    print(browsing_session[-1])


# queue
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")

# tuples

point = (1, 2)
print(type(point))
point = 1, 2
print(type(point))
point = 1,
print(type(point))
point = (1, 2)+(3, 4)
print(point)
point = (1, 2)*3
print(point)

point = tuple([1, 2])
print(point)
point = tuple('Dhara')
print(point)
point = (1, 2, 3)
print(point[0:])

x, y, x = point
if 1 in point:
    print("Exists")

a = 10
b = 20
a, b = b, a
print(a, b)

# Arrays

arrayNumbers = array("i", [1, 2, 3])
print(arrayNumbers)
print(arrayNumbers[0])


# Sets

setNumbers = [1, 1, 2, 3, 4]
unique = set(setNumbers)
secondSet = {1, 4}
secondSet.add(5)
secondSet.remove(5)
print(len(unique))
print(unique)

firstSet = {1, 1, 2, 3, 4}
secondSet = {1, 5}
print(firstSet | secondSet)
print(firstSet & secondSet)
print(firstSet - secondSet)
print(firstSet ^ secondSet)

if 1 in firstSet:
    print("Yes")
