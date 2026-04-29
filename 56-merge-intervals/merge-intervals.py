class Solution(object):
    def merge(self, intervals):

        # Brute Force=
      
        intervals.sort(key=lambda x: x[0])

        result = []

        for interval in intervals:
            if len(result) == 0:
                result.append(interval)

            else:
                last = result[-1]

                #  check overlap
                if interval[0] <= last[1]:
                    #merge
                    last[0] = min(last[0],interval[0])
                    last[1] = max(last[1],interval[1])
                
                else:
                    result.append(interval)
        return result


                    

        