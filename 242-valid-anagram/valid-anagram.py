class Solution(object):
    def isAnagram(self, s, t):
        #brute force
        sorts = sorted(s)
        sortt = sorted(t)
        if sorts == sortt:
            return True
        return False

        

        