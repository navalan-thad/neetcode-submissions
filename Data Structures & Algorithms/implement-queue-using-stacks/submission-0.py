class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []
        
    def push(self, x: int) -> None:
        self.front.append(x)

    def pop(self) -> int:
        for i in range(len(self.front)):
            self.back.append(self.front.pop())
        top = self.back.pop()
        for i in range(len(self.back)):
            self.front.append(self.back.pop())
        return top

    def peek(self) -> int:
        if self.front:
            return self.front[0]
        
    def empty(self) -> bool:
        return len(self.front) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()