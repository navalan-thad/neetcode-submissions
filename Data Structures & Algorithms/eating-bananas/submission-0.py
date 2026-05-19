import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        L = 1
        R = max(piles)

        while L <= R:
            mid = (L + R) // 2
            time = sum(math.ceil(pile/mid) for pile in piles)
            if time > h:
                L = mid + 1
            elif time <= h:
                R = mid - 1
            
        return L
        
        
        




        