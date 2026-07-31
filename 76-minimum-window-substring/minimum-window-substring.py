class Solution(object):
    def fun(self, sarray, tarray):

        for i in range(256):
            if sarray[i] < tarray[i]:
                return False
        return True
    def minWindow(self, s, t):
        # store frequency : t
        # create substring
        # store frequency : s
        # add current character in substring
        #compare substring fre with t fre
        # if it contains all chars then calculate current lenght
        # return min substring

        """n = len(s)
        min_len = float("inf")
        answer = ""
        tfre = {}
        for ch in t:
            if ch not in tfre:
                tfre[ch] = 1
            else:
                tfre[ch] = tfre[ch] + 1
        for i in range(n):
            substring = ""
            sfre = {}
            for j in range(i,n):
                substring = substring +s[j]
                if s[j] not in sfre:
                    sfre[s[j]] = 1
                else:
                    sfre[s[j]] = sfre[s[j]] + 1

                for ch in tfre:
                    if ch not in sfre:
                        break
                    if sfre[ch] < tfre[ch]:
                        break
                else:
                    leng = j-i+1
                    if leng < min_len:
                        min_len = leng
                        answer = substring  
        return answer"""
       

# create frequency array for t
# store frequency of t
# left = 0, right traverse
# increase frequency of current character
# while current window is valid
# calculate length
# update minimum answer
# remove left character frequency
# move left
# return minimum substring
        n = len(s)
        sarray = [0] *256
        tarray = [0] * 256
        for ch in t:
            tarray[ord(ch)] += 1
        left = 0
        res = float("inf")
        start = 0
        for right in range(n):
            sarray[ord(s[right])] += 1
            while self.fun(sarray,tarray):
                leng = right-left+1
                if leng< res:
                    res = leng
                    start = left
                sarray[ord(s[left])] -= 1
                left += 1
        if res == float("inf"):
            return ""
        return s[start:start + res]


                

        