import sys
import tracemalloc 

def f1():
    print(sys.getsizeof([]))
    print(sys.getsizeof([x for x in range(500,510)]))
    print(sys.getsizeof(tuple(x for x in range(500,510))))
    print(sys.getsizeof('0123456789'))
    print(sys.getsizeof(543))
    print(sys.getsizeof(None))
    
def f2():
    a=[]
    prev=0
    print(0, sys.getsizeof(a))
    for i in range(100):
        a.append(i)
        curr=sys.getsizeof(a)
        if curr != prev:
            prev = curr
            print(len(a), curr)
            
def f3():
    tracemalloc.start()
    numbers = list(range(100_000))
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(current/1024,peak/1024)
    
    tracemalloc.start()
    numbers = range(100_000)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(current/1024,peak/1024)
    
f1()
f2()
f3()