def log_usage(log_prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{log_prefix} - Calling {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"{log_prefix} - {func.__name__} returned {result}")
            return result
        return wrapper
    return decorator

@log_usage("DEBUG")
def multiply(a, b):
    return a * b

@log_usage("INFO")
def greet(name):
    return f"Hello, {name}!"

# Example calls
multiply(4, 5)
greet(name="Brendan")
