import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        print(f"⏳ Running {func.__name__}...")
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"✅ Finished {func.__name__} in {duration:.4f} seconds")
        return result
    return wrapper

@timer
def slow_addition(a, b):
    time.sleep(2)
    return a + b

@timer
def count_to(limit):
    for i in range(limit):
        pass
    return limit

print(slow_addition(4, 5))
print(count_to(10000000))
