class Solution(object):
    def kClosest(self, points, k):
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
        
        