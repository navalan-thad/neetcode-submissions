"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        copies = {}
        frontier = [node]
        visited = set()

        while frontier:
            curr = frontier.pop()
            if curr in visited:
                continue
            
            visited.add(curr)
            if curr not in copies:
                copies[curr] = Node(curr.val)

            for n in curr.neighbors:
                
                if n not in copies:
                    copies[n] = Node(n.val)
                    frontier.append(n)
                
                copies[curr].neighbors.append(copies[n])
                        
        return copies[node]

        