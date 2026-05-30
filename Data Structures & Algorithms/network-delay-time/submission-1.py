import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = {i:[] for i in range(1, n+1)}

        for u, v, t in times:
            adj[u].append((v, t))

        minCosts = [float('inf')] * (n+1)
        minCosts[k] = 0
        min_heap = [[0, k]]
        
        while min_heap:
            curr_cost, curr_node = heapq.heappop(min_heap)
            for neighbor in adj[curr_node]:
                if curr_cost+neighbor[1] < minCosts[neighbor[0]]:
                    minCosts[neighbor[0]] = curr_cost+neighbor[1]
                    heapq.heappush(min_heap, (neighbor[1]+curr_cost, neighbor[0]))

        if max(minCosts[1:]) != float('inf'):
            return max(minCosts[1:])
        else:
            return -1




        
        