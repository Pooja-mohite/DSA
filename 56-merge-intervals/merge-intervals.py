class Solution(object):
    def merge(self, intervals):
        '''
        #brute force
        result = intervals[:]
        while True:
            n = len(result)
            merged = False
            for i in range(n):
                for j in range(i+1,n):
                    a = result[i]
                    b = result[j]
                    if a[1] >= b[0] and b[1] >= a[0]:
                        newstart = min(a[0],b[0])
                        newend= max(a[1], b[1])

                        result.pop(j)
                        result.pop(i)
                        result.append([newstart, newend])
                        merged = True
                        break
                if merged:
                        break
            if not merged:
                    break
        return result
        '''

        #optimized
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if len(merged) == 0:
                merged.append(interval)
            else:
                prev_interval = merged[-1]

                if interval[0] <= prev_interval[1]:
                    prev_interval[0] = min(prev_interval[0], interval[0])
                    prev_interval[1] = max(prev_interval[1], interval[1])
                else:
                    merged.append(interval)
        return merged

                
    
        

                    

        