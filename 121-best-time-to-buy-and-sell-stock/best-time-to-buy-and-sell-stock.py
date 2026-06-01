class Solution(object):
    def maxProfit(self, prices):
        #  brute force
        '''
        n = len(prices)
        maxprofit = 0
        for i in range(n):
            for j in range(i+1, n):
                profit = prices[j] - prices[i]
                maxprofit = max(maxprofit, profit)
        return maxprofit
        '''
        maxprofit = 0
        minprice = float("inf")
        for i in prices:
            if i < minprice:
                minprice = i
            profit = i - minprice
            maxprofit = max(maxprofit, profit)
        return maxprofit










       