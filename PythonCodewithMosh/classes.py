class Point:
    # constructor
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    # class method creation
    @classmethod
    def zero(cls):
        return cls(0, 0)

    # chaning the magic method
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def draw(self):
        print(f"Point ({self.x},{self.y})")


point = Point(10, 20)
other = Point(10, 20)
another = Point(1, 2)
combined = point+other
print(combined.x)
print(point+other)
print(point == other)
print(point > another)
print(point < another)
point.draw()
pointclassmethod = Point.zero()
pointclassmethod.draw()
print(str(point))
# print(type(point))
# print(isinstance(point, Point))
