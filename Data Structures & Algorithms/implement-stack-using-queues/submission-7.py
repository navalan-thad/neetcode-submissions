from collections import deque

class MyStack:

    def __init__(self):
        self.first = deque()
        self.second = deque()
        
    def push(self, x: int) -> None:
        self.first.append(x)

    def pop(self) -> int:
        while len(self.first) > 1:
            self.second.append(self.first.popleft())
        val = self.first.popleft()
        self.first, self.second = self.second, self.first

        return val

    def top(self) -> int:
        while len(self.first) > 1:
            self.second.append(self.first.popleft())
        val = self.first.popleft()
        self.second.append(val)
        self.first, self.second = self.second, self.first

        return val

    def empty(self) -> bool:
        return len(self.first) == 0 and len(self.second) == 0
        