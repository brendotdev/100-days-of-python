class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a noise."

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

# Instantiate objects
dog = Dog("Buddy")
cat = Cat("Whiskers")
generic = Animal("Creature")

# Demonstrate method overriding
print(dog.speak())      # Buddy says woof!
print(cat.speak())      # Whiskers says meow!
print(generic.speak())  # Creature makes a noise.
