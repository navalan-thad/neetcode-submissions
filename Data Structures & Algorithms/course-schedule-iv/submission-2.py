from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adjList = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adjList[b].append(a)

        prereqMap = {}

        def dfs(c):
            if c in prereqMap:
                return prereqMap[c]
            prereqMap[c] = set()

            for prereq in adjList[c]:
                prereqMap[c].add(prereq)
                prereqMap[c].update(dfs(prereq))
            
            return prereqMap[c]

        for course in range(numCourses):
            dfs(course)

        answer = []
        for u, v in queries:
            answer.append(u in prereqMap[v])

        return answer