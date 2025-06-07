def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"🔍 Calling `{func.__name__}` with:")
        print(f"    positional arguments: {args}")
        print(f"    keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"✅ `{func.__name__}` returned: {result}")
        return result
    return wrapper

@log_function_call
def multiply(a, b):
    return a * b

# Example usage
multiply(4, 5)
multiply(a=7, b=3)
