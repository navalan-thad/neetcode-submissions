class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # minimize diff = s2 - s1, where total = s1 + s2
        # diff = s2 - s1 = (total - s1) - s1 = total - 2s1
        # threshold: either pile cannot exceed target//2
        
        total = sum(stones)
        target = total // 2
        memo = {}

        def dp(i, curr_sum):
            if i == len(stones) or curr_sum == target:
                return curr_sum

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            best = dp(i+1, curr_sum) # don't add curr stone
            if curr_sum + stones[i] <= target:
                best = max(best, dp(i+1, curr_sum+stones[i]))
            
            memo[(i, curr_sum)] = best
            return best

        closest_sum = dp(0, 0)
        return total - 2*closest_sum

