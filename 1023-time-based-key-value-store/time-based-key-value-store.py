class TimeMap(object):
    """
    #  brute force-
    def __init__(self):
        self.store = {}
        

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))
        
        

    def get(self, key, timestamp):
        if key not in self.store:
            return ""
        result = ""
        for value, time in self.store[key]:
            if time <= timestamp:
                result = value
            else:
                break
        return result
        """
    def __init__(self):
        self.store = {}
    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))
    def get(self, key, timestamp):
        if key not in self.store:
            return ""
        values = self.store[key]
        left = 0
        right = len(values)-1
        result = ""

        while left <=  right:
            mid = (left+right)//2
            value, time = values[mid]

            if time <= timestamp:
                result = value
                left = mid + 1
            else:
                right = mid - 1
        return result
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)