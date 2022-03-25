class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sums = 0
        for i in range(len(nums)):
            mini = nums[i]
            maxi = nums[i]
            for j in range(i + 1, len(nums)):
                mini = min(mini, nums[j])
                maxi = max(maxi, nums[j])
                sums += maxi - mini
        return sums