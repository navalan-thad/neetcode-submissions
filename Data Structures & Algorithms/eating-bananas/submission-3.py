from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        def sim(k):
            time = 0
            for pile in piles:
                time += ceil(pile / k)
            return time


        while left <= right:
            mid = (left + right) // 2
            time = sim(mid)
            if time <= h:
                right = mid-1
            else:
                left = mid + 1

        return left

        