from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adjList = {}
        for a, b in prerequisites:
            if b in adjList:
                adjList[b].append(a)
            else:
                adjList[b] = [a]

        def bfs(node, target):
            visited = set()
            frontier = deque()
            if adjList.get(node):
                frontier.extend(adjList.get(node))
            while frontier:
                curr = frontier.popleft()
                if curr in visited:
                    continue
                else:
                    visited.add(curr)
                if curr == target:
                    return True
                if adjList.get(curr):
                    frontier.extend(adjList.get(curr))
            return False

        answer = []
        for u, v in queries:
            if bfs(v, u):
                answer.append(True)
            else:
                answer.append(False)

        return answer