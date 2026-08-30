class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        def sim(k):
            return sum((pile + k - 1) // k for pile in piles)

        while left <= right:
            mid = (left + right) // 2
            time = sim(mid)
            if time <= h:
                right = mid-1
            else:
                left = mid + 1

        return left

        