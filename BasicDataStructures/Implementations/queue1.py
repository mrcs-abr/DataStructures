class Queue:

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        return self.items.append(item)
    
    def dequeue(self):
        if self.isEmpty():
            return "No items to be removed"
        
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.isEmpty():
            return "No items at the moment"
        
        return self.items[0]
