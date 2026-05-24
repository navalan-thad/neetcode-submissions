class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        cands = []
        for i in triplets:
            a, b, c = i
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            cands.append(i)

        print(cands)

        if not cands:
            return False

        ai, bi, ci = cands[0]
        
        for cand in cands:
            aj, bj, cj = cand
            curr = [max(ai, aj), max(bi, bj), max(ci, cj)]
            if curr == target:
                return True
            ai, bi, ci = curr

        return False
            



        



        