class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        parents = {i:i for i in range(n)}

        def find(n):
            while n != parents[n]:
                parents[n] = parents[parents[n]]
                n = parents[n]
            return n

        num_edges = 0

        for j in range(len(edges)):
            first = find(edges[j][0])
            second = find(edges[j][1])

            if first != second:
                num_edges += 1
                parents[first] = parents[second]
            else:
                return False

        if num_edges == n-1:
            return True

        return False

        

        
