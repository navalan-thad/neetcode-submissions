import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        order = []
        min_heap = []

        sorted_list = [[tasks[i][0], tasks[i][1], i] for i in range(len(tasks))]
        sorted_list.sort(key=lambda x: x[0])
        time = 0
        i = 0

        while min_heap or i < len(tasks):
            if not min_heap:
                time = max(time, sorted_list[i][0])

            while i < len(sorted_list) and sorted_list[i][0] <= time:
                dur, ind = sorted_list[i][1], sorted_list[i][2]
                heapq.heappush(min_heap, (dur, ind))
                i += 1

            curr_dur, curr_ind = heapq.heappop(min_heap)
            order.append(curr_ind)
            time += curr_dur

        return order














        