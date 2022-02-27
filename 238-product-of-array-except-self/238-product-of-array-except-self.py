class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result=[]
        prefixProduct = 1
        suffixProduct = 1
        suffixArray = [None] * len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            suffixArray[i] = suffixProduct
            suffixProduct *= nums[i]
            
        for j in range(len(nums)):
            result.append(prefixProduct * suffixArray[j])
            prefixProduct *= nums[j]


            
        return result
        