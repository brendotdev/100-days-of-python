import time
from functools import wraps

def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"⏱️ Starting '{func.__name__}'...")
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"✅ '{func.__name__}' completed in {run_time:.4f} seconds.")
        return result
    return wrapper

@timer_decorator
def slow_operation():
    time.sleep(2)
    print("...done with the slow operation.")

@timer_decorator
def fast_operation():
    print("Fast and done.")

slow_operation()
fast_operation()
