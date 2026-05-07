class MedianFinder(object):
    """
    #brute force
    
    def __init__(self):
        self.Mlist = []
        

    def addNum(self, num):
        self.Mlist.append(num)
        self.Mlist.sort()
        
    def findMedian(self):
        n = len(self.Mlist)
        if n % 2 == 1:
            return self.Mlist[n//2]
        else:
            mid1 = self.Mlist[n//2]
            mid2 = self.Mlist[n//2-1]
            mid = (mid1+mid2)/2.0
            return mid
            """
    #optimized
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        heapq.heappush(self.small, -num)
        value = -heapq.heappop(self.small)
        heapq.heappush(self.large,value)
        if len(self.large) > len(self.small):
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0



    

        