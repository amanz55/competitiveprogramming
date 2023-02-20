class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        answer = -1
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    answer = max(answer, nums[j] - nums[i])
        return answer