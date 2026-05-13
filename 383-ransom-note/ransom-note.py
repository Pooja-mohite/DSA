class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        #  brute force
        chars = list(magazine)
        for char in ransomNote:
            found = False
            for i in range(len(chars)):
                if chars[i] == char:
                    found = True
                    chars[i] = "#"
                    break
            if found == False:
                return False
        return True
        """
        # hashmap
        count = {}
        for char in magazine:
            count[char] = count.get(char, 0)+1
        for char in ransomNote:
            if char not in count:
                return False
            if count[char] == 0:
                return False
            count[char] = count[char]-1
        return True


        
        