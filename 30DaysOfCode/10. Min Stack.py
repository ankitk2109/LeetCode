class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:      
        cur_min = self.getMin()
        if(cur_min == None or cur_min>x ):
            cur_min = x
        self.stack.append((x,cur_min))
            
        
    def pop(self) -> None:
        if(self.stack != []):
            self.stack.pop()
        else:
            return None
        print(self.stack)

    def top(self) -> int:
        if(self.stack != []):
            return self.stack[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if(self.stack != []):
            return self.stack[-1][1]
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()