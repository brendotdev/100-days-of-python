import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"Function '{func.__name__}' executed in {duration:.4f} seconds.")
        return result
    return wrapper

@timer_decorator
def long_running_task():
    print("Starting a long-running task...")
    time.sleep(2)
    print("Task completed.")

long_running_task()
