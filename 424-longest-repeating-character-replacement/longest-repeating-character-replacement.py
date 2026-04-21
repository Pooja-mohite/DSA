class Solution(object):
    def characterReplacement(self, s, k):
        #brute force
        """n = len(s)
        max_len = 0
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                freq = {}
                for letter in substring:
                    freq[letter] = freq.get(letter, 0) + 1
                    max_freq = 0
                for value in freq.values():
                    if value > max_freq:
                        max_freq = value
                if (len(substring) - max_freq) <= k:
                    if len(substring) > max_len:
                        max_len = len(substring)
        return max_len"""

         # sliding window                   
        count = {}
        start = 0
        max_len = 0
        for end in range(len(s)):
            if s[end] in count:
                count[s[end]] = count[s[end]] + 1
            else:
                count[s[end]] = 1
            max_freq = 0
            for value in count.values():
                if value > max_freq:
                    max_freq = value
            while(end-start + 1) - max_freq > k:
                count[s[start]] = count[s[start]] - 1
                start = start + 1
            current_length = end - start + 1
            if current_length > max_len:
                max_len = current_length
        return max_len

