class Solution(object):
    def maxProfit(self, prices):
        '''
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j]- prices[i]
                max_profit = max(max_profit, profit)
        return max_profit
        '''
        """
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right]- prices[left]
                if profit > max_profit:
                    max_profit = profit
            else:
                left = right
            right = right+1
        return max_profit
        """

        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit

        
       