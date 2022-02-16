class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            minindex = i
            for j in range(i+1,len(nums)):
                if nums[j] < nums[minindex]:
                    minindex = j
            if minindex != i:
                nums[i], nums[minindex] = nums[minindex], nums[i]
        