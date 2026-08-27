class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        curr_sum = 0
        cum_total = {0: 1}
        count = 0

        for num in nums:
            curr_sum += num
            count += cum_total.get(curr_sum-k, 0)
            cum_total[curr_sum] = cum_total.get(curr_sum, 0) + 1
        
        return count