class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
                return max(nums)
        def roob(nums):
            if len(nums) <= 2:
                return max(nums)

            first = nums[0]
            second = max(nums[1], nums[0])

            for i in range(2, len(nums)):
                first, second = second, max(second, first + nums[i])

            return second
        
        return max(roob(nums[1:]), roob(nums[:-1]))
        