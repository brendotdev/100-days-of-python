class Circle:
    pi = 3.14159  # Class variable

    def __init__(self, radius):
        self.radius = radius  # Instance variable

    def area(self):  # Instance method
        return Circle.pi * self.radius ** 2

    @classmethod
    def unit_circle(cls):  # Class method
        return cls(1)

    @staticmethod
    def degrees_to_radians(degrees):  # Static method
        return degrees * (Circle.pi / 180)


# Create an instance using the constructor
c1 = Circle(3)
print(f"Area of circle with radius 3: {c1.area()}")

# Create an instance using the class method
c2 = Circle.unit_circle()
print(f"Area of unit circle: {c2.area()}")

# Use static method
angle_in_radians = Circle.degrees_to_radians(180)
print(f"180 degrees in radians: {angle_in_radians}")
