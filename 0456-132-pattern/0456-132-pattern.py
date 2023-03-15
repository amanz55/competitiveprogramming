class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []        
        maps = []
        minVal = float("inf")
        
        for i in range(len(nums)):
            maps.append(minVal)  
            minVal = min(minVal, nums[i])
                
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            
            if stack and nums[stack[-1]] > nums[i] and maps[stack[-1]] < nums[i]:
                return True
            
            stack.append(i)
        
        return False