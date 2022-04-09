class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * (len(prices) + 2)
        maxxi = [0] * len(dp)
        for i in range(len(prices) - 2, -1, -1):
            best = 0
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    best = max(best, prices[j] - prices[i] + maxxi[j + 2])
            dp[i] = best
            maxxi[i] = max(dp[i:])
                
        return max(dp)