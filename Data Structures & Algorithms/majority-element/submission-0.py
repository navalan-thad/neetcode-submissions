class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = {i: 0 for i in set(nums)}

        for i in nums:
            freq[i] += 1

        for j in freq.keys():
            if freq[j] > len(nums) // 2:
                return j
        