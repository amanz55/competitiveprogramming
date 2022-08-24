class Solution:
    def rob(self, nums: List[int]) -> int:
        #edges here
        if len(nums) < 3:
            return max(nums)
        
        dp = {}
        
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i-1])
        
        return dp[len(nums) - 1]
            