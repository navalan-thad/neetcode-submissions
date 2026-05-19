import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks, n):

        freq = {}
        for i in tasks:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        heap = [-v for _, v in freq.items()]
        heapq.heapify(heap)

        time = 0
        cooldown = deque()

        while heap or cooldown:

            time += 1
            if cooldown and cooldown[0][0] == time:
                _, rem = cooldown.popleft()
                heapq.heappush(heap, rem)

            if heap:
                rem = heapq.heappop(heap)
                if rem != -1: # negative form of 1 remaining
                    cooldown.append((time+n+1, rem+1))

        return time