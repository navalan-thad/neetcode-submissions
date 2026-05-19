import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def dist(coord):
            x1, y1 = coord
            return x1**2 + y1**2

        heap = []
        for i in range(k):
            heap.append((-dist(points[i]), points[i]))
        heapq.heapify(heap)

        for point in points[k:]:
            if -dist(point) > heap[0][0]:
                heapq.heappushpop(heap, (-dist(point), point))

        return [x[1] for x in heap]

        