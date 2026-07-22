class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """n = len(s)
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
                
        return max_len"""

        """n = len(s)
        max_len = 0
        for i in range(n):
            hashmap = {}
            for j in range(i,n):
                if s[j] not in hashmap:
                    hashmap[s[j]] = 1
                    leng = j-i+1
                    max_len = max(max_len,leng)
                else:
                    break
                    
        return max_len"""

        l = 0
        r = 0
        n = len(s)
        max_len = 0
        hashmap={}
        while r < n:
            if s[r] not in hashmap:
                hashmap[s[r]] = 1
            else:
                hashmap[s[r]] = hashmap[s[r]] + 1
            while hashmap[s[r]] > 1:
                hashmap[s[l]] = hashmap[s[l]] - 1
                if hashmap[s[l]] == 0:
                    del hashmap[s[l]]
                l = l+1
            leng = r - l + 1
            max_len = max(leng, max_len)
            r = r+1
        return max_len

             


