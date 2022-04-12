class Solution:
    def check(self, nums: List[int]) -> bool:
        nums_initial = sorted(nums)
        if nums_initial == nums:
            return True
        length = len(nums)
        i = 1
        
        for i in range(length - 1):
            if nums[ i + 1 :] + nums[ : i + 1 ] == nums_initial:
                return True
        return False
        