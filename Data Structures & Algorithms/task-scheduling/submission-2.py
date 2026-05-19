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

        maxHeap = []
        for key in freq.keys():
            heapq.heappush(maxHeap, -freq[key])

        cooldown = deque() # (available_time, remaining_count)
        time = 0

        while maxHeap or cooldown:

            time += 1

            if cooldown and cooldown[0][0] == time:
                _, count = cooldown.popleft()
                heapq.heappush(maxHeap, count)

            if maxHeap:
                count = heapq.heappop(maxHeap)

                count += 1

                if count != 0:
                    cooldown.append((time + n + 1, count))

        return time