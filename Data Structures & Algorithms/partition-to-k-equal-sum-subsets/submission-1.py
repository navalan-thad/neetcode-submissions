class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        if sum(nums) % k != 0:
            return False

        target = sum(nums) / k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        visited = [0] * k

        def partition(i):
            if i == len(nums):
                return True

            for j in range(k):
                if visited[j] + nums[i] <= target:
                    visited[j] += nums[i]
                    cand = partition(i+1)
                    if cand:
                        return True
                    visited[j] -= nums[i]

                if visited[j] == 0:
                    return False

            return False

        return partition(0)

        