from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_list = [repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()]
        args_str = ", ".join(args_list)
        print(f"🔍 Calling {func.__name__}({args_str})")
        result = func(*args, **kwargs)
        print(f"✅ {func.__name__} returned {result!r}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

@debug
def greet(name="World"):
    return f"Hello, {name}!"

add(3, 5)
greet()
greet(name="Brendan")
