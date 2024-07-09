from shape_class import Circle, Rectangle, Triangle

# Create instances of different shapes with specific dimensions and colors
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 10, 5)
triangle = Triangle("Green", 3, 4, 5)

# Calculate and print area, perimeter, and color for each shape
print("Shape: Circle")
print(f"Color: {circle.get_color()}")
print(f"Area: {circle.calculate_area():.2f}")
print(f"Perimeter: {circle.calculate_perimeter():.2f}")


print("Shape: Rectangle")
print(f"Color: {rectangle.get_color()}")
print(f"Area: {rectangle.calculate_area():.2f}")
print(f"Perimeter: {rectangle.calculate_perimeter():.2f}")


print("Shape: Triangle")
print(f"Color: {triangle.get_color()}")
print(f"Area: {triangle.calculate_area():.2f}")
print(f"Perimeter: {triangle.calculate_perimeter():.2f}")
