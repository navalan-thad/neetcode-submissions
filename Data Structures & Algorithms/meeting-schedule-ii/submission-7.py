"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) < 2:
            return len(intervals)

        intervals.sort(key=lambda x: x.start)
        end_times = [intervals[0].end]

        for i in range(1, len(intervals)):
            if intervals[i].start < end_times[0]:
                heapq.heappush(end_times, intervals[i].end)
            else:
                heapq.heappushpop(end_times, intervals[i].end)
        
        return len(end_times)

            
        