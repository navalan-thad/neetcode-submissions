class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        total_length = sum(matchsticks)
        target = total_length // 4
        if total_length % 4 != 0 or max(matchsticks) > target :
            return False

        target = total_length // 4

        # matchsticks.sort(reverse=True)
        buckets = [0] * 4

        def dfs(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if buckets[j] + matchsticks[i] <= target:
                    buckets[j] += matchsticks[i]
                    cand = dfs(i+1)
                    if cand:
                        return True
                    buckets[j] -= matchsticks[i]

                if buckets[j] == 0:
                    break

            return False 

        return dfs(0)




        