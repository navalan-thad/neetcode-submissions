import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        trips.sort(key=lambda x: x[1])

        heap = []
        heapq.heapify(heap)
        curr_cap = 0
        for ppl, start, finish in trips:

            while heap and heap[0][0] <= start:
                curr_cap -= heap[0][1]
                heapq.heappop(heap)

            curr_cap += ppl
            if curr_cap > capacity:
                return False

            heapq.heappush(heap, (finish, ppl))

        return True




        