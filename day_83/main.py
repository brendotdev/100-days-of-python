def class_decorator(cls):
    """A simple class decorator to wrap and enhance a class."""
    class WrappedClass(cls):
        def __init__(self, *args, **kwargs):
            print("Initializing decorated class...")
            super().__init__(*args, **kwargs)

        def greet(self):
            print("Decorator enhancement before greet:")
            super().greet()

    return WrappedClass


@class_decorator
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, I'm {self.name}.")


p = Person("Brendan")
p.greet()
