class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        next_greater = [-1] * len(nums)
        n = len(nums)
        length = n * 2
        
        for i in range(length):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                top = stack.pop()
                next_greater[top] = nums[idx]
            stack.append(idx)
        
            
        
        return next_greater
        