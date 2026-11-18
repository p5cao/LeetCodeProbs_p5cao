class MinStack:

    def __init__(self):
        self.stack = [] 
        self.minStack = []

    def push(self, value: int) -> None:
        if not self.stack: #when empty
            current_min = value
        else:
            current_min = min(self.minStack[-1], value)
        self.stack.append(value)
        self.minStack.append(current_min)
        return None

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()