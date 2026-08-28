class MyQueue:

    def __init__(self):
        self.receive = []
        self.temp = []

    def push(self, x: int) -> None:
        self.receive.append(x)

    def pop(self) -> int:
        self.peek()
        return self.temp.pop()

    def peek(self) -> int:
        if not self.temp:
            while self.receive:
                self.temp.append(self.receive.pop())
        return self.temp[-1]

        
    def empty(self) -> bool:
        return not self.receive and not self.temp
        
