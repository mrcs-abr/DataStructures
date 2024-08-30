def binarySearch(alist, item):
    midpoint = len(alist) // 2
    
    if len(alist) == 0:
        return False
    else:
        if item == alist[midpoint]:
            return True
        
        if item < alist[midpoint]:
            return binarySearch(alist[:midpoint], item)
        else:
            return binarySearch(alist[midpoint + 1:], item)

print(binarySearch([1, 2, 3, 4], 3))
print(binarySearch([1, 2, 3, 4], 5))
    
