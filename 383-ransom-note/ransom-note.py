class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        character = list(magazine)
        n = len(character)
        for char in ransomNote:
            found = False
            for i in range(n):
                if character[i] == char:
                    found = True
                    character[i] = "#"
                    break
            if found == False:
                return False
        return True


     


        
        