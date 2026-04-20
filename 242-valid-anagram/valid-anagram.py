class Solution(object):
    def isAnagram(self, s, t):
        #brute force
        """ss = sorted(s)
        st = sorted(t)
        if ss == st:
            return True
        return False"""

        #hashmap
        if len(s)!= len(t):
            return False
        count = {}
        for letter in s:
            count[letter] = count.get(letter,0) + 1
        for letter in t:
            if letter not in count:
                return False
            count[letter] -= 1
            if count[letter] < 0:
                return False
        return True
        
            
       
        
        