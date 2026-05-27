class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        combs = [] 
        cand = []

        def dfs(i, total):

            if total == target:
                combs.append(cand.copy())
                return

            if i == len(candidates) or total > target:
                return

            cand.append(candidates[i])
            dfs(i+1, total+candidates[i])
            cand.pop()

            # skip dupes
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i+1, total)


        dfs(0, 0)

        return combs


        