import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        trips.sort(key = lambda x: x[1])

        heap = []
        heapq.heapify(heap)
        curr = 0

        for people, start, finish in trips:
            while heap and heap[0][0] <= start:
                curr -= heap[0][1]
                heapq.heappop(heap)

            curr += people
            if curr > capacity:
                return False
            heapq.heappush(heap, (finish, people))

        return True

            



            










        




        