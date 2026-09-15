import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        max_heap = []
        res = []

        if a != 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b != 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c != 0:
            heapq.heappush(max_heap, (-c, 'c'))

        while max_heap:
            count, char = heapq.heappop(max_heap)

            if len(res) >= 2 and res[-2] == res[-1] == char:
                if max_heap:
                    count2, char2 = heapq.heappop(max_heap)
                    res.append(char2)
                    if count2 < -1:
                        heapq.heappush(max_heap, (count2+1, char2))
                    if count < -1:
                        heapq.heappush(max_heap, (count, char))

            else:
                res.append(char)
                if count < -1:
                    heapq.heappush(max_heap, (count+1, char))

        return ''.join(res)


        