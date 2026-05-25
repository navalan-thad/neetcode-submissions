class Solution:
    def maxArea(self, heights: List[int]) -> int:

        start = 0
        end = len(heights) - 1

        soln = 0
 
        while start < end:
            soln = max(soln, min(heights[start],  heights[end]) * (end - start))

            if heights[start] < heights[end]:
                start += 1
            elif heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
                end -= 1
            
        return soln
            

