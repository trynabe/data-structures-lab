class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        # Overload the + operator for adding two points.
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        # Overload the - operator for subtracting two points.
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        # Overload the * operator for scaling a point.
        return Point(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        # Overload the str() function for a readable representation.
        return f"Point({self.x}, {self.y})"
    
# Creating Point Objects
p1 = Point(2, 3)
p2 = Point(4, 5)

# Using overloaded + operator
p3 = p1 + p2
print(f"p1 + p2 = {p3}")

# Using overloaded - operator
p4 = p1 - p2
print(f"p1 - p2 = {p4}")

# Using overloaded * operator
p5 = p1 * 3
print(f"p1 * 3 = {p5}")