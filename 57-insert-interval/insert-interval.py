class Solution(object):
    def insert(self, intervals, newInterval):
        # add new interval in old interval and sort it and then check all the intervals, if they overlap then need to merge it and return the interval

        intervals.append(newInterval)
        intervals.sort()
        res = []
        n = len(intervals)
        visited = [False]*n
        for i in range(n):
            if visited[i]:
                continue
            start = intervals[i][0]
            end = intervals[i][1]
            for j in range(i+1,n):
                if visited[j]:
                    continue
                if not (intervals[j][1] < start or intervals[j][0] > end):
                    start = min(start, intervals[j][0])
                    end = max(end, intervals[j][1])
                    visited[j] = True
            res.append([start, end])
        return res

       


        