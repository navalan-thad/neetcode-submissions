class MinStack:

    def __init__(self):
        self.main = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        
        self.main.append(val)
        if self.minStack:
            currMin = min(self.minStack[-1], val)
            self.minStack.append(currMin)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.main:
            self.main.pop()
            self.minStack.pop() 

    def top(self) -> int:
        return self.main[-1] if self.main else 0

    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else 0

        
