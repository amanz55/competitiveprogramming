class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        idx = 0
        
        for i in nums:
            res = res ^ i
            res = res ^ idx
            idx += 1
        res = res ^ idx
        return res
        
        