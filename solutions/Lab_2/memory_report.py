import sys
import tracemalloc

print("List")
tracemalloc.start()
numbers = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("Length:", len(numbers))
print("Size:", sys.getsizeof(numbers))
print("Current mem(KB):", current/1024)
print("Peak mem(KB):", peak/1024)

del numbers

print("Range")
tracemalloc.start()
numbers = range(100_000)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("Length:", len(numbers))
print("Size:", sys.getsizeof(numbers))
print("Current mem(KB):", current/1024)
print("Peak mem(KB):", peak/1024)