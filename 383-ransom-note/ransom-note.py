class Solution(object):
    def canConstruct(self, ransomNote, magazine):
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
        