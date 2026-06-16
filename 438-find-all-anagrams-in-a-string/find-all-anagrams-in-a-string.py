class Solution(object):
    def findAnagrams(self, s, p):
        #Brute force
        '''
        answer = []
        n = len(s)
        m = len(p)
        pattern = {}
        for char in p:
            if char in pattern:
                pattern[char] = pattern[char] + 1
            else:
                pattern[char] = 1
        for i in range(n-m + 1):
            current = {}
            for j in range(i, i+m):
                char = s[j]
                if char in current:
                    current[char] = current[char]+1
                else:
                    current[char] = 1
            if current == pattern:
                answer.append(i)
        return answer
        '''
        #optimized (hashmap + sliding window)
        answer = []
        n = len(s)
        m = len(p)

        # if pattern is bigger than string :
        if m > n:
            return answer
        #pattern frequency
        pattern = {}
        for char in p:
            if char in pattern:
                pattern[char] = pattern[char]+1
            else:
                pattern[char]= 1
        #current window frequncy
        current = {}
        #lrft pointer
        left = 0

        #right pointer
        for right in range(n):
            char = s[right]
            if char in current:
                current[char] = current[char]+1
            else:
                current[char]=1
            
            # window size becomes bigger
            if right - left + 1 >m:
                remove_char = s[left]
                current[remove_char]= current[remove_char] - 1
                if current[remove_char] == 0:
                    del current[remove_char]
                left = left + 1

            #compare both frequencies
            if current == pattern:
                answer.append(left)
        return answer



       
        