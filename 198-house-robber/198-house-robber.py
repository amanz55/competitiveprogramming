class Solution:
    def rob(self, nums: List[int]) -> int:
        #edges here
        if len(nums) < 3:
            return max(nums)
        
        dp = {}
        
        dp[0] = nums[0]
        dp[1] = nums[1]
        
        for i in range(2, len(nums)):
            j = i - 2
            maxi = -1
            while j >= 0:
                maxi = max(maxi, dp[j])
                j -= 1
            
            if dp[i-1] > maxi + nums[i]:
                dp[i] = dp[i-1]
            else:
                dp[i] = maxi + nums[i]
        
        return dp[len(nums) - 1]
            