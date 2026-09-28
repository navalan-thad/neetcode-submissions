class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        total = sum(stones)
        target = total // 2

        dp = {0}
        for s in stones:
            new_sums = set()
            for cur in dp:
                if cur + s <= target:
                    new_sums.add(cur + s)

            for val in new_sums:
                dp.add(val)

        return total - 2 * max(dp)
        