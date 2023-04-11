class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        prev = nums[0]
        for i in range(1, len(nums)):
            prev = max(prev + nums[i], nums[i])
            best = max(best, prev)
        return best