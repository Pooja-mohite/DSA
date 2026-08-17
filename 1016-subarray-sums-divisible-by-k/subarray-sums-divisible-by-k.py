class Solution(object):
    def subarraysDivByK(self, nums, k):
        """n = len(nums)
        count = 0
        for i in range(n):
            ssum = 0
            for j in range(i,n):
                ssum = ssum+ nums[j]
                if ssum % k == 0:
                    count = count + 1
        return count"""

        # prefix sum
        n = len(nums)
        hashmap = {0:1}
        prefix = 0
        count =0
        for i in range(n):
            prefix = prefix + nums[i]
            ans = prefix % k
            if ans in hashmap:
                count = count + hashmap[ans]
            if ans not in hashmap:
                hashmap[ans] = 1
            else:
                hashmap[ans] = hashmap[ans]+1
        return count


         
       