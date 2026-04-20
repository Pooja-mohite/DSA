class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #brute force
        """n = len(s)
        max_length = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                max_length = max(max_length, j-i + 1)
        return max_length"""

        # sliding window
        char_set = set()
        start = 0
        max_length = 0
        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start = start + 1
            char_set.add(s[end])
            max_length = max(max_length, end-start + 1)
        return max_length
            