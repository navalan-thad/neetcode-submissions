class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        from collections import deque, defaultdict

        def topological_sort(num_nodes):
            graph = defaultdict(list)
            indegree = [0] * num_nodes
            
            for course, prereq in prerequisites:
                graph[course].append(prereq)
                indegree[prereq] += 1
                
            # 3. Queue with nodes having 0 in-degrees
            queue = deque([i for i in range(num_nodes) if indegree[i] == 0])
            topo_order = []
            
            while queue:
                node = queue.popleft()
                topo_order.append(node)
                
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
                        
            if len(topo_order) != num_nodes:
                return False
                
            return True

        return topological_sort(numCourses)

