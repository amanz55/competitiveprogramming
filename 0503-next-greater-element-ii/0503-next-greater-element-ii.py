class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        next_greater = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                top = stack.pop()
                next_greater[top] = nums[i]
            stack.append(i)
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                top = stack.pop()
                next_greater[top] = nums[i]
            stack.append(i)
            
        
        return next_greater
        