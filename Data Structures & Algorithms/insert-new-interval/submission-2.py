class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        soln = []

        for i in range(len(intervals)):
            start, end = intervals[i]
            if end < newInterval[0]:
                soln.append(intervals[i])

            elif start > newInterval[1]:
                soln.append(newInterval)
                return soln + intervals[i:]

            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]

        soln.append(newInterval)
        return soln
