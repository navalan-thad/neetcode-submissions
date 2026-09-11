class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        total = sum(matchsticks)
        target = total // 4
        if total % 4 != 0 or max(matchsticks) > target:
            return False

        sides = [0] * 4
        def backtrack(i):
            if i == len(matchsticks):
                return True

            for k in range(4):
                if sides[k] + matchsticks[i] <= target:
                    sides[k] += matchsticks[i]
                    candidate = backtrack(i+1)
                    if candidate:
                        return True
                    sides[k] -= matchsticks[i]

                if sides[k] == 0:
                    return False

            return False

        return backtrack(0)

                

            





        