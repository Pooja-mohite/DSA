class Solution(object):
    def longestOnes(self, nums, k):
        # given array of 1's and 0
        # count zero
        # count of zero >k, then break
        #esle calculate lenght

        """n = len(nums)
        max_len = 0
        for i in range(n):
            count = 0
            for j in range(i,n):
                if nums[j] == 0:
                    count = count+1
                if count > k:
                    break
                else:
                    leng = j - i+1
                    if leng > max_len:
                        max_len = leng
        return max_len"""

        # left = 0, right = 0
        # if num == 0, increase count of zero, if not increase right
        # if count > k, then increase left and check if num is 0 then decrease count
        # if count < k, then find length of array

        n = len(nums)
        left=0
        count =0
        max_len = 0
        for right in range(n):
            if nums[right] == 0:
                count = count + 1
            while count > k:
                if nums[left] == 0:
                    count = count-1
                left = left +1
            leng = right - left+1
            max_len = max(leng, max_len)
            right = right + 1
        return max_len


                
       