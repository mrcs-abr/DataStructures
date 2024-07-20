from Implementations.stack import Stack

def filacetamol(s):
    stk = Stack()
    res = ""

    for c in s:
        if c == "*":
            res += stk.pop()
        else:
            stk.push(c)
    
    return res

usr_input = input()

print(filacetamol(usr_input))




