class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trust_count = {}
        trusting = set()

        for i in trust:
            trusting.add(i[0])
            if i[1] in trust_count:
                trust_count[i[1]] += 1
            else:
                trust_count[i[1]] = 1

        for i in trust_count.keys():
            if trust_count[i] == n-1 and i not in trusting:
                return i
        return -1


        