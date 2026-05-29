class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(intervals)):
            start, end = intervals[i]
            if end < newInterval[0]:
                res.append([start, end])
            elif newInterval[1] < start:
                res.append(newInterval)
                res += intervals[i:]
                return res
            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]

        res.append(newInterval)
        return res
