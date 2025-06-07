def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"🔍 Called {func.__name__} with:")
        print(f"    args: {args}")
        print(f"    kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"✅ {func.__name__} returned: {result}")
        return result
    return wrapper

@logging_decorator
def greet(name, age=None):
    greeting = f"Hello, {name}!"
    if age:
        greeting += f" You are {age} years old."
    return greeting

@logging_decorator
def add(a, b):
    return a + b

# Example usage
greet("Brendan", age=28)
add(5, 3)
