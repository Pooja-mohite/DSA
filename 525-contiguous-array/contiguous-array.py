class Solution(object):
    def findMaxLength(self, nums):
        '''
        n = len(nums)
        maxlen = 0
        for i in range(n):
            zero = 0
            one = 0
            for j in range(i,n):
                if nums[j] == 0:
                    zero = zero + 1
                else:
                    one = one +1
                if zero == one:

                    length = j -i +1
                    maxlen = max(maxlen, length)
        return maxlen'''
        
        n = len(nums)
        zero = 0
        one = 0
        hashmap = {}
        res =0
        for i in range(n):
            if nums[i] == 0:
                zero = zero+1
            else:
                one = one+1
            diff = zero - one
            if diff == 0:
                res = max(res, i+1)
                continue
            if diff not in hashmap:
                hashmap[diff] = i
            else:
                index = hashmap[diff]
                length = i - index
                res = max(res, length)
        return res

            


       
                


            
            

       