class Solution(object):
    def insert(self, intervals, newInterval):
        '''
        #brute force
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            current = intervals[i]
            prev = result[-1]
            if current[0] > prev[1]:
                result.append(current)
            else:
                prev[0] = min(current[0], prev[0])
                prev[1] = max(current[1], prev[1])
        return result
        '''
        #optimized
        n = len(intervals)
        result = []
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i = i+1
        while i<n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i = i+1
        result.append(newInterval)
        while i<n:
            result.append(intervals[i])
            i = i+1
        return result