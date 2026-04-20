class Solution(object):
        def topKFrequent(self, nums, k):
            """freq = []
            for element in nums:
                count = 0
                for x in nums:
                    if x == element:
                        count = count + 1
                freq.append((element,count))
            unique = list(set(freq))
            unique.sort(key = lambda x:x[1], reverse = True)
            result = []
            for i in range(k):
                result.append(unique[i][0])
            return result"""

        # Hashmap
            """freq = {}
            for element in nums:
                freq[element] = freq.get(element,0)+1
                sorted_element = sorted(freq.items(), key = lambda x: x[1], reverse = True)
                result = []
            for i in range(k):
                result.append(sorted_element[i][0])
            return result"""
 
    # Sort(bucket sort)
           #frequency map
            freq = {}
            for element in nums:
                freq[element] = freq.get(element, 0)+1
                # create buckets
            bucket = [[] for _ in range(len(nums)+1)]
            #fill buckets
            for element, freq in freq.items():
                bucket[freq].append(element)
            # collect result
            result = []
            for i in range(len(bucket)-1, -1, -1):
                for element in bucket[i]:
                    result.append(element)
                    if len(result) == k:
                        return result

    
                    
                    
           