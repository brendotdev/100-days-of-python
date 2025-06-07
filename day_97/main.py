from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_list = [repr(a) for a in args]
        kwargs_list = [f"{k}={v!r}" for k, v in kwargs.items()]
        all_args = ", ".join(args_list + kwargs_list)
        print(f"🔍 Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"✅ {func.__name__} returned {result!r}")
        return result
    return wrapper

@debug
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

@debug
def add(a, b):
    return a + b

print(greet("Brendan"))
print(add(5, b=7))
