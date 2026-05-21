class Solution(object):
    def longestPalindrome(self, s):
        used = [False] * len(s)
        length = 0
        odd = False
        for i in range(len(s)):
            if used[i] == True:
                continue
            count = 1
            used[i] = True
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    count = count + 1
                    used[j] = True
            if count % 2 == 0:
                length = length + count
            else:
                length = length + (count - 1)
                odd = True
        if odd == True:
            length = length + 1
        return length
        """
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
        """



            