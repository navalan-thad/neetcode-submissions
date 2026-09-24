class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        curr_end = intervals[0][1]
        merged = [[intervals[0][0], curr_end]]

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]

            if start <= curr_end:
                merged[-1][1] = max(end, curr_end)
            else:
                merged.append([start, end])
                
            curr_end = max(end, curr_end)

        return merged




        