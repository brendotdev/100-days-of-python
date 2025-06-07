def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1, 2, 3))           # Output: 6
print(add(10, 20, 30, 40))    # Output: 100
