class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def dist(coord1, coord2):
            x1, y1 = coord1
            x2, y2 = coord2
            return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)

        points.sort(key=lambda x: dist(x, (0, 0)))
        print(points)
        return points[:k]
        