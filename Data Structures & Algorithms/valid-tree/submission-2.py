class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        mapping = {i:i for i in range(n)}

        def find(n):
            while n != mapping[n]:
                mapping[n] = mapping[mapping[n]]
                n = mapping[n]
            return n
        
        num_edges = 0
        for i in range(len(edges)):
            x = find(edges[i][0])
            y = find(edges[i][1])

            if x != y:
                num_edges += 1
                mapping[x] = mapping[y]
            else:
                return False

        if num_edges == n-1:
            return True

        return False


        
        
        