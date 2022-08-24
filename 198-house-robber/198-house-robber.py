class Solution:
    def rob(self, nums: List[int]) -> int:
        #edges here
        if len(nums) < 3:
            return max(nums)
        
        first = nums[0]
        second = max(nums[1], nums[0])
        
        for i in range(2, len(nums)):
            first, second = second, max(second, first + nums[i])
        
        return second
            