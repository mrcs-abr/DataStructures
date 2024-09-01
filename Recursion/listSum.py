def listsum(alist):
    if len(alist) == 1:
        return alist[0]
    
    return alist[0] + listsum(alist[1:])

print(listsum([1, 2, 3, 4]))
