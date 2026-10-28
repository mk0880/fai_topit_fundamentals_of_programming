import sys

def f1():
    data = [1, 2, 3]
    print("После создания:", sys.getrefcount(data))

    alias = data
    print("После создания alias:", sys.getrefcount(data))

    container = [data]
    print("После помещения в контейнер:", sys.getrefcount(data))

    del alias
    print("После del alias:", sys.getrefcount(data))

    container.clear()
    print("После очистки контейнера:", sys.getrefcount(data))
    
import weakref


class Record:
    pass

def f2():
    record = Record()
    weak_record = weakref.ref(record)

    print(weak_record())
    del record
    print(weak_record())
    
def f3():
    r1=Record()
    r2=Record()
    r3=Record()
    a1=r1
    a2=r2
    dict = weakref.WeakValueDictionary()
    dict[1] = r1
    dict[2] = r2
    dict[3] = r3
    print(list(dict.items()))
    
    del r3
    print(list(dict.items()))
    
    del a2
    print(list(dict.items()))
    
    del r1
    print(list(dict.items()))


f1()
f2()
f3()