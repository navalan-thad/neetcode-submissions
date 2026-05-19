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

        people = trust_count.keys()
        for person in people:
            if trust_count[person] == n-1 and person not in trusting:
                return person
        return -1



        