class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        def sim(k):
            return sum((pile + mid - 1) // mid for pile in piles)

        while left <= right:
            mid = (left + right) // 2
            time = sim(mid)
            if time <= h:
                right = mid-1
            else:
                left = mid + 1

        return left

        