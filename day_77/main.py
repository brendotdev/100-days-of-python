class Circle:
    pi = 3.14159  # Class attribute

    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    def area(self):
        return Circle.pi * self.radius ** 2

    def circumference(self):
        return 2 * Circle.pi * self.radius

# Create a Circle instance
circle = Circle(radius=5)
print(f"Area: {circle.area()}")
print(f"Circumference: {circle.circumference()}")
