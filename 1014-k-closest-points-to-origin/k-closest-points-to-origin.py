import heapq
class Solution(object):
    def kClosest(self, points, k):
        #  brute fore:
        """
        arr = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = x * x + y * y
            arr.append((distance, point))
        arr.sort()
        result = []
        for i in range(k):
            result.append(arr[i][1])
        return result
        """
        # optimized (heap)
        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = x * x + y * y
            heapq.heappush(heap, (distance, point))
        result = []
        for i in range(k):
            distance,point = heapq.heappop(heap)
            result.append(point)
        return result
            
                            

        
        