"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count =0
        start =[]
        end=[]

        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)

        start.sort()
        end.sort()
        high = 0
        n= len(intervals)

        a,b =0,0
        while a < n:
            if start[a] < end[b]:
                count+=1
                a+=1
            else:
                count-=1
                b+=1
            high = max(count,high)
        print(high)
            

        return high
        