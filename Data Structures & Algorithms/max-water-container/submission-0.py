class Solution:
    def maxArea(self, heights: List[int]) -> int:

        soln = 0

        def area(i, j):
            return min(heights[i], heights[j]) * (j-i)
        
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                soln = max(soln, min(heights[i], heights[j]) * (j-i))

        return soln