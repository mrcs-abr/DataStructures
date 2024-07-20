class Stack:

    def __init__ (self):
        self.items = []
    
    def isEmpty (self):
        return self.items == []
    
    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    
