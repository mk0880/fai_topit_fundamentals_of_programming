def expA():
    a = 10
    b = a

    print(a, b)
    print(id(a), id(b))

    a += 1

    print(a, b)
    print(id(a), id(b))
    print()

def expB():
    first = [10, 20]
    second = first

    print(first, second)
    print(id(first), id(second))

    second.append(30)

    print(first, second)
    print(id(first), id(second))

    second = [10, 20, 30]

    print(first == second, first is second)
    print(first, second)
    print(id(first), id(second))

    second.append(40)

    print(first, second)
    print(id(first), id(second))
    print()
    
def expC():
    config_a = {
        "name": "Distractible",
        "participants": ["Mark", "Bob"],
        "launch_params": {"strategy": "GoNoStop", "options": ["-f", "-d"]},
        }
    print("A: ",config_a)
    print()
    
    config_b = config_a
    config_b["participants"].append("Lixian")
    assert config_a["participants"] is config_b["participants"]
    print("A: ",config_a)
    print("B: ",config_b)
    print()
    
    config_c = {
        "name": "Distractible",
        "participants": ["Mark", "Bob"],
        "launch_params": {"strategy": "GoNoStop", "options": ["-f", "-d"]},
        }
    config_c["participants"].append("Wade")
    print("C: ",config_c)
    print()
    
    assert config_c["participants"] is not config_a["participants"]
    assert config_c["name"] is config_a["name"]
    assert config_c["launch_params"] is not config_a["launch_params"]
    
expA()
expB()
expC()