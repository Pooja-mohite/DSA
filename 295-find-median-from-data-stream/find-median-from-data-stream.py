class MedianFinder(object):

    def __init__(self):
        self.left_half = []
        self.right_half = []
        

    def addNum(self, num):
        heapq.heappush(self.left_half, -num)
        heapq.heappush(self.right_half, -heapq.heappop(self.left_half))
        if len(self.right_half) > len(self.left_half):
            heapq.heappush(self.left_half, -heapq.heappop(self.right_half))

    def findMedian(self):
        if len(self.left_half) > len(self.right_half):
            return float(-self.left_half[0])
        return (-self.left_half[0] + self.right_half[0]) / 2.0
       
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()