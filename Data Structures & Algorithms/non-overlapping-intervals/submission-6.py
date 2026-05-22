class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[0])
        removals = 0

        prev_end = intervals[0][1]
        i = 1
        while i < len(intervals):
            if prev_end > intervals[i][0]:
                if prev_end > intervals[i][1]:
                    prev_end = intervals[i][1]
                removals += 1
            else:
                prev_end = intervals[i][1]
            i += 1

        return removals
        