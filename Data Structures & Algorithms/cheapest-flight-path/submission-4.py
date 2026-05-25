from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        neighbors = {}
        for spot, dest, price in flights:
            if spot in neighbors:
                neighbors[spot].append((dest, price))
            else:
                neighbors[spot] = [(dest, price)]

        min_cost = [float('inf')] * n
        min_cost[src] = 0
        frontier = deque([(src, 0, 0)])

        while frontier:
            node, curr_price, stops = frontier.popleft()
            if stops > k or node not in neighbors:
                continue
            
            for nb, price in neighbors[node]:
                new_price = price + curr_price
                if new_price < min_cost[nb]:
                    min_cost[nb] = new_price
                    frontier.append((nb, new_price, stops+1))

        return min_cost[dst] if min_cost[dst] != float('inf') else -1






        




        