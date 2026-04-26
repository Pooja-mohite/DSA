class Solution(object):
    def countSubstrings(self, s):

        """
        :type s: str
        :rtype: int
        """
       #brute force
        n = len(s)
        count = 0
        for i in range(n):
            for j in range(i,n):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    count = count+1
        return count
