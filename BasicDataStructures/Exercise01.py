from Implementations.queue1 import Queue

def filacetamol(s):
    q1 = Queue()
    res = ""
    for c in s:
        if c == "*":
            res += q1.dequeue()
        else:
            q1.enqueue(c)
    
    return res

usr_input = input()

print(filacetamol(usr_input))
