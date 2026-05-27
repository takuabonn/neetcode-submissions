"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals = sorted(intervals, key=lambda i: i.start)
        currMtg = intervals[0]
        for i in range(1, len(intervals)):
            nextMtg = intervals[i]
            if currMtg.end > nextMtg.start:
                return False
            currMtg = nextMtg
        return True
            