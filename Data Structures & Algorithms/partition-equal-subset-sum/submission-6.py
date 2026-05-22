class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        sums = [0]

        for i in range(len(nums)):
            for j in range(len(sums)):
                cand = sums[j]+nums[i]
                if cand == target:
                    return True
                if cand not in sums:
                    sums.append(cand)

        return False



 






        