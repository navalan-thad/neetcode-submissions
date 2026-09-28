class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        above = [1] * n # 1 way to reach each cell in first row
        for _ in range(m-1): # each row after first one
            row = [1] * n # init to 1 since first cell has 1 path
            for j in range(1, n): # iterating through each cell in row after first
                row[j] = row[j-1] + above[j] # ways = from_left + from_above
            above = row
        return above[-1]
            

        