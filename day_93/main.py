from functools import lru_cache
import time

@lru_cache(maxsize=3)
def slow_function(n):
    print(f"⏳ Running slow_function({n})...")
    time.sleep(2)  # Simulate heavy computation
    return n * n

print(slow_function(2))  # First call, will be slow
print(slow_function(3))  # First call, will be slow
print(slow_function(2))  # Cached, should be fast
print(slow_function(4))  # First call, slow
print(slow_function(3))  # Cached if still in cache
