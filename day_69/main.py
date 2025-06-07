def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Before calling: {original_function.__name__}")
        result = original_function(*args, **kwargs)
        print(f"After calling: {original_function.__name__}")
        return result
    return wrapper_function

@decorator_function
def say_hello(name):
    print(f"Hello, {name}!")

@decorator_function
def add_numbers(a, b):
    return a + b

# Usage
say_hello("Brendan")
print("Result:", add_numbers(3, 7))
