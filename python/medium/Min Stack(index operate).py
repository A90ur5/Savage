class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.top_index = 0
        self.data_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        if len(self.data_stack) == self.top_index:
            self.data_stack.append(val)
            self.min_stack.append(self.min)
        else:
            self.data_stack[self.top_index] = val
            self.min_stack[self.top_index] = self.min
        self.top_index += 1
        

    def pop(self) -> None:
        self.top_index -= 1
        if self.top_index == 0:
            self.min = float('inf')
        else:
            self.min = self.min_stack[self.top_index - 1]
        return self.data_stack[self.top_index]

    def top(self) -> int:
        return self.data_stack[self.top_index-1]

    def getMin(self) -> int:
        return self.min_stack[self.top_index-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()