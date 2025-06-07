def calculator(*args, **kwargs):
    operation = kwargs.get("operation", "add")
    
    if operation == "add":
        return sum(args)
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == "subtract":
        if not args:
            return 0
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    elif operation == "divide":
        if not args:
            return "Error: No numbers to divide"
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "Error: Division by zero"
            result /= num
        return result
    else:
        return "Unsupported operation"

# Example usages
print(calculator(10, 5, 2, operation="add"))       # ➜ 17
print(calculator(10, 2, operation="subtract"))     # ➜ 8
print(calculator(2, 3, 4, operation="multiply"))   # ➜ 24
print(calculator(100, 5, 2, operation="divide"))   # ➜ 10.0
print(calculator(1, 2, 3))                         # ➜ 6 (default to add)
