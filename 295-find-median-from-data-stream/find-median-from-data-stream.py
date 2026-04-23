class MedianFinder(object):
    #brute force
    """
    def __init__(self):
        self.arr = []
        

    def addNum(self, num):
        self.arr.append(num)
        self.arr.sort()
       
        

    def findMedian(self):
        n = len(self.arr)
        
        if n % 2 == 1:
            return self.arr[n // 2]
        else:
            mid1 = self.arr[n //2]
            mid2 = self.arr[n//2-1]
            return (mid1 + mid2) / 2.0
            """
    def __init__(self):
        self.small = []
        self.large = []
    def addNum(self, num):
        heapq.heappush(self.small, -num)

        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)

        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):

        #odd
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        #even
        return (-self.small[0] + self.large[0]) / 2.0
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()