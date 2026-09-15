import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        min_heap = []
        # heapq.heapify(min_heap)
        sorted_tasks = [[tasks[i][0], tasks[i][1], i] for i in range(len(tasks))]
        sorted_tasks.sort(key=lambda x: x[0])
        time = 0
        i = 0
        order = []

        while min_heap or i < len(tasks):
            
            if not min_heap:
                time = max(time, sorted_tasks[i][0])

            while i < len(sorted_tasks) and sorted_tasks[i][0] <= time:
                dur, ind = sorted_tasks[i][1], sorted_tasks[i][2]
                heapq.heappush(min_heap, (dur, ind))
                i += 1
            dur, ind = heapq.heappop(min_heap)
            time += dur
            order.append(ind)

        return order










        