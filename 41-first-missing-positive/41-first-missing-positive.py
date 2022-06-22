class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mydict = {}
        maxlength = 5 * 10 ** 5
        for j in range(maxlength + 1):
            if j == len(nums):
                break
            if nums[j] > 0:
                mydict[nums[j]] = 1
        for k in range(1, maxlength + 2, 1):
            if k not in mydict:
                return k
        