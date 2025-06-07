def calculate_total(*args):
    """Adds up any number of positional arguments"""
    return sum(args)

def custom_greeting(**kwargs):
    """Returns a formatted greeting using keyword arguments"""
    name = kwargs.get("name", "Guest")
    age = kwargs.get("age", "unknown")
    return f"Hello, {name}! You are {age} years old."

def combined_example(*args, **kwargs):
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")
    total = sum(args)
    print(f"Total of positional args: {total}")
    if "bonus" in kwargs:
        print(f"Bonus received: {kwargs['bonus']}")
    return total + kwargs.get("bonus", 0)

# Usage examples
print("Total:", calculate_total(10, 20, 30))
print(custom_greeting(name="Brendan", age=29))
print("Combined:", combined_example(5, 10, 15, bonus=100))
