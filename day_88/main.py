import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"⏱️ Starting '{func.__name__}'...")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"✅ Finished '{func.__name__}' in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    return "Done with slow task!"

@timing_decorator
def sum_numbers(n):
    return sum(range(n))

# Example calls
print(slow_function())
print(sum_numbers(1_000_000))
