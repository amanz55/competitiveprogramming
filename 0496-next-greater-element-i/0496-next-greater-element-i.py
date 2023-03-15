class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        next_greater = [-1] * len(nums2)
        maps = {}
        
        for i in range(len(nums2)):
            maps[nums2[i]] = i
        
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                top = stack.pop()
                next_greater[top] = i
            
            stack.append(i)
            
        
        res = [-1] * len(nums1)
        
        for i in range(len(nums1)):
            idx = maps[nums1[i]]
            if next_greater[idx] != -1:
                res[i] = nums2[next_greater[idx]]
        
        return res
                
                