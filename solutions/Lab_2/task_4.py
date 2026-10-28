import gc

def f1():
    first = []
    second = []

    first.append(second)
    second.append(first)

    print("first ссылается на second:", first[0] is second)
    print("second ссылается на first:", second[0] is first)
    print(gc.isenabled())
    print("thresholds:", gc.get_threshold())
    print("stats:", gc.get_stats())
    print('First:',id(first),'Second:',id(second))
    print()

    del first
    del second
    print('Got:', gc.collect())
    
def f2():
    gc.disable()
    first = []
    second = []
    
    first.append(second)
    second.append(first)
    
    del first
    del second
    print("stats:", gc.get_stats())
    gc.collect()
    print("stats:", gc.get_stats())
    gc.enable()
    
def f3():
    gc.disable()
    a={'refA': []}
    b={'refB': []}
    c={'refC': []}
    d={'refD': []}
    print(gc.get_stats())
    
    a['refA'].append(b)
    b['refB'].append(c)
    c['refC'].append(a)
    
    print(a)
    print(b)
    print(c)
    
    del a
    del b
    del c
    gc.collect()
    print(gc.get_stats())
    print(d)
    gc.enable()
    
    
    
f1()
f2()
f3()