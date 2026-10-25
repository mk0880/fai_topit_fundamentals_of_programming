import copy

def out(arr):
    for i in arr:
        print(i,id(i),id(i[0]),id(i[0][1]))
    print()
            
def f1():
    original = [
        ["Python", 5],
        ["Algorithms", 4],
    ]
    alias = original
    shallow = original.copy()
    deep = copy.deepcopy(original)
    
    l=[original,alias,shallow,deep]
    out(l)
    
    original.append(["Databases", 5])
    out(l)
    
    original[0][1] = 3
    out(l)
     
def f2():
    wrong_matrix = [[0] * 3] * 3
    wrong_matrix[0][0] = 1
    
    correct_matrix = [[0] * 3 for _ in range(3)]
    correct_matrix[0][0] = 1
    
    print(wrong_matrix,id(wrong_matrix[0]),id(wrong_matrix[1]))
    print(correct_matrix,id(correct_matrix[0]),id(correct_matrix[1]))
    assert wrong_matrix[0] is wrong_matrix[1]
    assert correct_matrix[0] is not correct_matrix[1]
    
    
f1()
f2()