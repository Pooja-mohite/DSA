class Solution(object):
    def insert(self, intervals, newInterval):
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
        