class MinStack(object):

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
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()