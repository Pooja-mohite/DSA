class Solution(object):
    def myAtoi(self, s):
        ans = 0
        i = 0
        n = len(s)
        while i < n  and s[i] == " ":
            i = i+1
        sign = 1
        if i <n:
            if s[i] == "-":
                sign = -1
                i = i+1
            elif s[i] == "+":
                i = i+1
        while i<n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")
            ans = ans * 10 + digit
            i = i+1
        ans = ans * sign
        if ans < -2147483648:
            return -2147483648
        if ans > 2147483647:
            return 2147483647
        return ans

         
        


        
       
        