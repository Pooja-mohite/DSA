class Solution(object):
    def totalFruit(self, fruits):
        # brute firce
        """n = len(fruits)
        max_fruits = 0
        for i in range(n):
            uniquetype = set()
            for j in range(i,n):
                uniquetype.add(fruits[j])
                if len(uniquetype) <= 2:
                    leng = j-i+1
                    max_fruits = max(leng, max_fruits)
                else:
                    break
        return max_fruits"""


        """n = len(fruits)
        max_fruits = 0
        for i in range(n):
            hashmap = {}
            for j in range(i,n):
                if fruits[j] not in hashmap:
                    hashmap[fruits[j]] = 1
                if len(hashmap) <= 2:
                    leng = j-i+1
                    max_fruits = max(leng, max_fruits)
        return max_fruits"""

        n= len(fruits)
        maxfruits = 0
        left = 0 
        right = 0
        hashmap = {}
        while right < n:
            if fruits[right] not in hashmap:
                hashmap[fruits[right]] = 1
            else:
                hashmap[fruits[right]] = hashmap[fruits[right]] +1
            while len(hashmap) > 2:
                hashmap[fruits[left]] = hashmap[fruits[left]] - 1
                
                if hashmap[fruits[left]] == 0:
                    del hashmap[fruits[left]]
                left = left + 1
            leng = right - left+1
            maxfruits = max(maxfruits,leng)
            right = right + 1
        return maxfruits








                    

            