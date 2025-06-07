def add(*args):
    """Add any number of arguments together."""
    return sum(args)


print(add(3, 5, 10))  # Output: 18
print(add(1, 2, 3, 4, 5))  # Output: 15


def greet(**kwargs):
    """Create a greeting using keyword arguments."""
    if "name" in kwargs:
        print(f"Hello, {kwargs['name']}!")
    else:
        print("Hello, stranger!")


greet(name="Alice")         # Output: Hello, Alice!
greet(greeting="Hi")        # Output: Hello, stranger!
