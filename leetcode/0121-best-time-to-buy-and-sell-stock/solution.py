class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price  # update lowest buy price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit  # update max profit if better
        
        return max_profit

