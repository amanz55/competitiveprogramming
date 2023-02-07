class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        offset = 10000
        dp = [0 for i in range(2 * offset + 2)]
        
        for num in nums:
            dp[num + offset] += 1
        count = 0    
        for i in range(2 * offset + 1, -1, -1):
            if dp[i] > 0:
                count += dp[i]
                
            if count >= k:
                return i - offset