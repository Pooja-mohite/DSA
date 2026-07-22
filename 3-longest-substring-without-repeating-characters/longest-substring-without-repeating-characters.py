class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        max_len = 0
        for i in range(n):
            sset = set()
            for j in range(i,n):
                if s[j] not in sset:
                    sset.add(s[j])
                else:
                    break
                leng = j-i+1
                max_len= max(max_len,leng)
                
        return max_len

