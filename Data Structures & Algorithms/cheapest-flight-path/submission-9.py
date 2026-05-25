from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = {}
        for i in flights:
            if i[0] in adj:
                adj[i[0]].append((i[1], i[2]))
            else:
                adj[i[0]] = [(i[1], i[2])]

        frontier = deque([(src, 0, 0)])
        min_prices = [float('inf')] * n
        min_prices[src] = 0

        while frontier:
            node, curr_price, stops = frontier.popleft()
            if stops > k or node not in adj:
                continue

            for dest, price in adj[node]:
                new_price = price + curr_price
                if new_price < min_prices[dest]:
                    min_prices[dest] = new_price
                    frontier.append((dest, new_price, stops+1))

        return min_prices[dst] if min_prices[dst] != float('inf') else -1
            






        




        