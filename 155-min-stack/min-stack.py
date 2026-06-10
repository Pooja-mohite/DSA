class MinStack(object):
    
    #  Brute Force
    '''

    def __init__(self):
        self.stack = []   

    def push(self, val):
        self.stack.append(val)
       
    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        minimum = self.stack[0]
        for num in self.stack:
            if num < minimum:
                minimum = num
        return minimum 
        '''
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, val):
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            current_min = min(val, self.minstack[-1])
            self.minstack.append(current_min)
    def pop(self):
        self.stack.pop()
        self.minstack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minstack[-1]








        
       

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()