class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        mapping = {i: i for i in range(1, len(edges)+1)}

        def find(n):
            while n != mapping[n]:
                mapping[n] = mapping[mapping[n]]
                n = mapping[n]
            return n

        for i, j in edges:
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                mapping[root_i] = mapping[root_j]
            else:
                return [i, j]
        