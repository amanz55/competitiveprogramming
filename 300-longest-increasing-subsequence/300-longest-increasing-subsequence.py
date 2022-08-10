class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        absmax = -1
        for i in range(len(nums) -1, -1, -1):
            memo[nums[i]] = 1
            j = i + 1
            maxim = 0
            while j < len(nums):
                if nums[j] > nums[i]:
                    maxim = max(maxim, memo[nums[j]])
                j += 1
            memo[nums[i]] += maxim
            absmax = max(absmax, memo[nums[i]])
            
        return absmax