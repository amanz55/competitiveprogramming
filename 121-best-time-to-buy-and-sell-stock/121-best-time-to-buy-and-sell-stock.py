class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxim = prices[-1]
        
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] < maxim:
                profit = max(profit, maxim - prices[i])
            else:
                maxim = prices[i]
                
        return profit
        