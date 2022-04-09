class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [-1] * n
        dp[-1] = 0
        memo = prices[-1]
        for i in range(n - 2, -1, -1):
            if memo <= prices[i]:
                dp[i] = 0
                memo = prices[i]
            else:
                dp[i] = memo - prices[i]
        return max(dp)