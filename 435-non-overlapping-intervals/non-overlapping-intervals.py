class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        # Brute  force:-
        """
        n = len(intervals)
        ans = [n]
        #check overlap
        def isnonoverlapping(arr):
            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    if arr[i][1] > arr[j][0] and arr[j][1] > arr[i][0]:
                        return False
            return True

        def solve(index, current):
            
            if index == n:
                if isnonoverlapping(current):
                    removed = n - len(current)
                    ans[0] = min(ans[0], removed)
                return
            
            solve(index + 1, current+ [intervals[index]])

            solve(index+1, current)
        solve(0, [])
        return ans[0]
        """
        # Greedy 
        intervals.sort(key=lambda x: x[1])
        count = 0
        last = intervals[0][1] 
        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] >= last:
                last = intervals[i][1]
            else:
                count = count+1
        return count







        


        
        