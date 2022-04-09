class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[-1], dp[-2] = cost[-1], cost[-2]
        for i in range(n - 3, -1, -1):
            dp[i] = min(dp[i + 1], dp[i + 2]) + cost[i]
        return min(dp[0], dp[1])