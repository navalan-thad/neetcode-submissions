class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        sums = {0}

        for i in range(len(nums)):
            cands = set()
            for j in sums:
                if j+nums[i] == target:
                    return True
                cands.add(j+nums[i])
            sums = sums | cands

        return False



 






        