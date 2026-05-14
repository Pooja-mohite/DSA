class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #  brute Force
        '''
        n = len(s)
        length = 0 
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                length = max(length, j-i +1)
        return length
        '''
        #sliding windoe

        i = 0
        length = 0
        seen = set()
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i = i+1
            seen.add(s[j])
            length = max(length, j-i+1)
        return length




        
        