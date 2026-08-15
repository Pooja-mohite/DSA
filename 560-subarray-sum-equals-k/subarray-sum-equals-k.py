class Solution(object):
    def subarraySum(self, nums, k):
    # traverse full array
    # take sum and check whether sum equal to k and return count
        """n = len(nums)
        count = 0
        for i in range(n):
            ssum = 0
            for j in range(i,n):
                ssum = ssum + nums[j]
                if ssum == k:
                    print(count)
                    count = count + 1
        return count"""

        # prefixsum
        n = len(nums)
        ssum = 0
        hashmap = {0:1}
        res = 0
        for i in range(n):
            ssum = ssum + nums[i]
            ques = ssum - k
            if ques in hashmap:
                res = res + hashmap[ques]
            if ssum not in hashmap:
                hashmap[ssum] = 1
            else:
                hashmap[ssum] = hashmap[ssum] + 1

        return res

            
            
            
           

       