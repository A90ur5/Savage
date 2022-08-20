class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.data_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        self.data_stack.append(val)
        self.min_stack.append(self.min)
        

    def pop(self) -> None:
        self.min_stack.pop()
        if len(self.min_stack) == 0:
            self.min = float('inf')
        else:
            self.min = self.min_stack[-1]
        return self.data_stack.pop()

    def top(self) -> int:
        return self.data_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()