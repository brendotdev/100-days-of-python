import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Running: {func.__name__}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to run.")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)
    print("Finished sleeping.")

@timer_decorator
def fast_function():
    time.sleep(0.5)
    print("That was fast!")

# Usage
slow_function()
fast_function()
