class Solution:
    def integerReplacement(self, n: int) -> int:
        steps = [inf]
        
        @lru_cache
        def dp(n, count):
            if n == 1:
                steps[0] = min(steps[0], count)
                return count
            
            if n % 2 == 0:
                return dp(n / 2, count + 1)
            
            return min(dp(n + 1, count + 1), dp(n - 1, count + 1))
        
        dp(n, 0)
        
        return steps[0]