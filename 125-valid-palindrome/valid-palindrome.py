class Solution(object):
    def isPalindrome(self, s):
        #brute force
        """s = s.lower()
        new = ""
        for letter in s:
            if letter.isalnum():
                new = new + letter
        return new == new[::-1]"""

        #Two pinters
        start = 0
        end = len(s)-1
        while start < end:
            while start < end and not s[start].isalnum():
                start = start + 1
            while start< end and not s[end].isalnum():
                end= end - 1
            if s[start].lower() != s[end].lower():
                return False
            start = start + 1
            end = end - 1
        return True
        
      