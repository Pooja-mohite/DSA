class Solution(object):
    def maximumSum(self, arr):
        #1 -2 0 3
        # check if num delete calculate sum ...for eavry subarray calculate sum and find maxsum
        # 1 = -2+3 = 1
        # -2 =1+3 =4
        # 0 = 1+(-2)+3 = 2
        #3 = 1+(-2)
        """n = len(arr)
        maxsum = float('-inf')
        for i in range(n):
            ssum = 0
            for j in range(i,n):
                #print (ssum)
                ssum = ssum + arr[j]
                maxsum = max(maxsum, ssum)
                if j>i:
                    for k in range(i,j+1):
                        newsum = ssum - arr[k]  
                        #print(newsum)  
                        maxsum = max(maxsum, newsum)
        return maxsum"""

        #KADANES algo
        # two cases= 1. no delete and 2. one delete
        #no deleye = 2 posiibilities = arr[i] or premax * arr[i] and take max
        #onedelete = 2 possiblities = prevonedeletesubarray + arr[i] or nodelete(delete current arr[i]) and take max

        n = len(arr)
        nodelete = arr[0]
        onedelete = float('-inf')
        res = arr[0]
        for i in range(1,n):
            prevnodelete = nodelete
            nodelete = max(prevnodelete+arr[i] , arr[i])
            onedelete = max(prevnodelete, onedelete + arr[i])
            res = max(nodelete, onedelete, res)
        return res
            






       