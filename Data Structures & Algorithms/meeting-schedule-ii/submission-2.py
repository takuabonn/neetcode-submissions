"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key=lambda i: i.start)
        days = 0
        for i in range(len(intervals)):
            if intervals[i] == "*":
                continue
            dayStartSchdue = intervals[i]
            intervals[i] = "*"
            days += 1
            for j in range(i, len(intervals)):
                if intervals[j] == "*":
                    continue
                dayNextSchedue = intervals[j]
                if dayNextSchedue.start >= dayStartSchdue.end:
                    dayStartSchdue = dayNextSchedue
                    intervals[j] = "*"
        return days
                


        

