class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

# Create a Dog object
my_dog = Dog(name="Rex", breed="German Shepherd")
print(my_dog.bark())
