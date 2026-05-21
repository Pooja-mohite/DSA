class Solution(object):
    def longestPalindrome(self, s):
        hashmap = {}
        for char in s:
            if char in hashmap:
                hashmap[char] = hashmap[char]+1
            else:
                hashmap[char] = 1
            length = 0
            odd = False

        for count in hashmap.values():
            #even count
            if count % 2 == 0:
                length = length + count
            # odd count
            else:
                length = length + (count - 1)
                odd = True
        if odd == True:
            length = length + 1
        return length



            