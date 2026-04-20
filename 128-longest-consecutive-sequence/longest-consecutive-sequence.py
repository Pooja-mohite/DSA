class Solution(object):
    def longestConsecutive(self, nums):
        #brute force
        """longest = 0
        for num in nums:
            current = num
            count = 1
            while current+1 in nums:
                current = current+1
                count= count+1
            longest = max(longest,count)
        return longest"""

        #hashset
        hash_set = set(nums)
        longest = 0
        for num in hash_set:
            if num-1 not in hash_set:
                current = num
                count = 1
                while current+1 in hash_set:
                    current = current + 1
                    count = count + 1
                longest = max(longest,count)
        return longest
        

        
            
        
        