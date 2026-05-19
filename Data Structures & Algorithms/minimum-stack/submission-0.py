class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return 0
        

    def getMin(self) -> int:
        if self.stack:
            temp = sorted(self.stack)
            return temp[0]
        else:
            return 0
        
