class Solution(object):
    def longestPalindrome(self, s):
        #brute force
        n = len(s)
        answer = ""

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]

                if substring == substring[::-1]:
                    if len(substring) > len(answer):
                        answer = substring

        return answer
                

        