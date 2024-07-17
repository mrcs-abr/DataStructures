# O(n)
def find_minimum(lst):
    minimum = lst[0]
    
    for i in lst:
        if i < minimum:
            minimum = i
    
    return minimum

print(find_minimum([5, 3, 1, 8]))

# O(n**2)

def find_minimum2(lst):
    if len(lst) != 1:
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[j] < lst[i]:
                    aux = lst[i]
                    lst[i] = lst[j]
                    lst[j] = aux
                    
    return lst[0]

print(find_minimum2([5, 3, 1, 8]))

