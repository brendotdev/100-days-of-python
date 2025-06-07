def repeat(num_times):
    def decorator_function(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_function

@repeat(num_times=3)
def greet():
    print("Hello!")

greet()
