class MinStack:

    def __init__(self):
        self.stack=[]
        self.minN=[]
    def push(self, val: int) -> None:
        
        self.stack.append(val)
        if self.minN:
            self.minN.append(min(self.minN[-1],val))
        else:
            self.minN.append(val)
        
    def pop(self) -> None:
        if self.stack:
           
            self.minN.pop()
            return self.stack.pop()
            
        
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        
        return self.minN[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
