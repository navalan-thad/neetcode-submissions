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

        frontier = [node]
        copies = {}
        visited = set()

        while frontier:

            curr = frontier.pop()

            if curr not in copies:
                copies[curr] = Node(curr.val)

            visited.add(curr)

            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    frontier.append(neighbor)
                    visited.add(neighbor)
                if neighbor not in copies:
                    copies[neighbor] = Node(neighbor.val)

                copies[curr].neighbors.append(copies[neighbor])
                

        return copies[node]

        