class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        if (point[0], point[1]) in self.points:
            self.points[(point[0], point[1])] += 1
        else:
            self.points[(point[0], point[1])] = 1

    def count(self, point: List[int]) -> int:

        x, y = point[0], point[1]
        squares = 0

        for i in self.points.keys():
            if abs(i[0]-x) == abs(i[1]-y) and x != i[0] and y != i[1]:
                if (i[0], y) in self.points and (x, i[1]) in self.points:
                    squares += self.points[i] * self.points[(i[0], y)] * self.points[(x, i[1])]

        return squares
        
