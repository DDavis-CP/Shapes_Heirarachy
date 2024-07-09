# Problem Statement:
# You are tasked with creating a class hierarchy to represent various shapes, such as circles,
# rectangles, and triangles. Each shape should have properties and methods specific to its type,
# while also inheriting common attributes and behaviors from a base shape class.
# Requirements:
# 1. Design a base class called Shape with the following attributes and methods:
# - Attributes:
# - color (string): The color of the shape
class Shape():
    # - Methods:
    # - __init__(self, color): Constructor to initialize the shape with the given color
    def __init__(self, color: str) -> None:
        self.color = color

    # - calculate_area(self): Abstract method to calculate the area of the shape (raises NotImplementedError)
    def calculate_area(self):
        raise NotImplemented("Sub Class must implement")

    # - calculate_perimeter(self): Abstract method to calculate the perimeter of the shape (raises NotImplementedError)
    def calculate_perimeter(self):
        raise NotImplemented("Sub Class must implement")

    # - get_color(self): Method to retrieve the color of the shape
    def get_color(self):
        return self.color

    # - set_color(self, color): Method to set the color of the shape
    def set_color(self, color):
        self.color = color

# 2. Design derived classes for specific shapes that inherit from the Shape class:
# - Circle class:
class Circle(Shape):
    # - Attributes:
    # - radius (float): The radius of the circle
    # - __init__(self, color, radius): Constructor to initialize the circle with the given color and radius
    def __init__(self, color: str, radius: float) -> None:
        super().__init__(color)
        self.radius = radius

    # - Methods:
    # - calculate_area(self): Overrides the base class method to calculate the area of the circle (πr²)
    def calculate_area(self):
        return 3.14 * self.radius ** 2

    # - calculate_perimeter(self): Overrides the base class method to calculate the perimeter
    def calculate_perimeter(self):
        # (circumference) of the circle (2πr)
        return 3.14 * self.radius * 2

# - Rectangle class:
class Rectangle(Shape):
    # - Attributes:
    # - length (float): The length of the rectangle
    # - width (float): The width of the rectangle
    # - __init__(self, color, length, width): Constructor to initialize the rectangle with the given color, length, and width
    def __init__(self, color: str, length: float, width: float) -> None:
        super().__init__(color)
        self.length = length
        self.width = width

    # - Methods:
    # - calculate_area(self): Overrides the base class method to calculate the area of the rectangle (length * width)
    def calculate_area(self):
        return self.length * self.width

    # - calculate_perimeter(self): Overrides the base class method to calculate the perimeter of the rectangle (2 * (length + width))
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# - Triangle class:
class Triangle(Shape):
    # - Attributes:
    # - side1 (float): The length of the first side of the triangle
    # - side2 (float): The length of the second side of the triangle
    # - side3 (float): The length of the third side of the triangle
    # - __init__(self, color, side1, side2, side3): Constructor to initialize the triangle with the given color and side lengths
    def __init__(self, color: str, side1: float, side2: float, side3: float) -> None:
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # - Methods:
    # - calculate_area(self): Overrides the base class method to calculate the area of the triangle using Heron's formula
    def calculate_area(self):
        area = (self.side1 + self.side2 + self.side3) / 2
        return (area * (area - self.side1) * (area - self.side2) * (area - self.side3)) ** 0.5

    # - calculate_perimeter(self): Overrides the base class method to calculate the perimeter of the triangle (side1 + side2 + side3)
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
