"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        import heapq

        if len(intervals) < 2:
            return len(intervals)

        intervals.sort(key=lambda x: x.start)
        rooms = [intervals[0].end]

        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end

            if start < rooms[0]:
                heapq.heappush(rooms, end)
            else:
                heapq.heappushpop(rooms, end)

        return len(rooms)

        