import time

# Decorator that logs the function name, arguments, and execution time
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} returned: {result}")
        print(f"Execution time: {end_time - start_time:.4f}s\n")
        return result
    return wrapper

@logger
def slow_add(a, b):
    time.sleep(1)
    return a + b

@logger
def greet(name="User"):
    return f"Hello, {name}!"

# Function calls
slow_add(3, 7)
greet(name="Brendan")
