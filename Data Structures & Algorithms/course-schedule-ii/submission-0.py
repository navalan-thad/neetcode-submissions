class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        mapping = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            mapping[course].append(prereq)

        visiting = set()
        visited = set()

        order = []

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)

            for prereq in mapping[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            visited.add(course)
            order.append(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return order
        