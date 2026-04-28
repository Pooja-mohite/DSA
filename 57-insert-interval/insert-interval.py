class Solution(object):
    def insert(self, intervals, newInterval):
        #brute force=

        #add new interval
        intervals.append(newInterval)

        #sort
        intervals.sort(key=lambda x: x[0])

        result = []

        #add first interval
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            current = intervals[i]
            last = result[-1]

            #if no overlap
            if current[0] > last[1]:
                result.append(current)
            # ifoverlap
            else:
                last[0] = min(last[0], current[0])
                last[1] = max(last[1], current[1])
        return result

        
        