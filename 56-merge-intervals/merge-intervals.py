class Solution(object):
    def merge(self, intervals):
        # create one visisted list, check all intervals using for loop, if it is not visited then add it in to list, if it is visited then skip and move forward
        # second for loop = compare each i with j intervals
        #check overlap exits or not = overlap = i[end] >= j[start] and j[end] < i[start]
        # merge overlapped intervals and add in list
        
        """n = len(intervals)
        res = []
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
        return res"""

        # first sort intervals, then check overlap(end < start)
        n = len(intervals)
        intervals.sort()
        relist = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1,n):
            s = intervals[i][0]
            e = intervals[i][1]
            if end >= s:
                end = max(end,e)
            else:
                relist.append([start,end])
                start = s
                end = e
        relist.append([start,end])
        print(relist)
        return relist



        
                
    
        

                    

        