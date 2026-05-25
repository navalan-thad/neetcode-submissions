from math import inf
from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        neighbors = {}
        for spot, dest, price in flights:
            if spot in neighbors:
                neighbors[spot].append((dest, price))
            else:
                neighbors[spot] = [(dest, price)]

        memo = {}

        def bfs(node, stops):
            if (node, stops) in memo:
                return memo[(node, stops)]
            if stops-1 > k:
                return inf 

            if node == dst:
                return 0
            else:
                if node not in neighbors:
                    return inf
                min_cost = inf
                for nb in neighbors[node]:
                    min_cost = min(min_cost, bfs(nb[0], stops+1) + nb[1])
            
            memo[(node, stops)] = min_cost
            return min_cost

        soln = bfs(src, 0)
        return -1 if soln == inf else soln


        




        