class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        ptr1 = nums[0]
        ptr2 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            ptr1 , ptr2 = ptr2 , max(ptr2 , ptr1 + nums[i])
            
        return ptr2
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        
        1 = nums[0]
        2 = max(nums[0], nums[1])
        
        ptr1 = 1
        ptr2 = 2
        
        temp = ptr1
        ptr1 = ptr2
        ptr2 = max(ptr2, nums[i] + temp)
        
        
        3 = max(nums[1], nums[0] + nums[2])
        4 = max(nums[0] + nums[2], nums[0] + nums[3], nums[1] + nums[3])
        
        
        5, 2, 1, 5
        
        ptr1 = 5
        ptr2 = 5
        
        i = 2
            temp = 5
            ptr1 = 5
            ptr2 = max(5, 6) = 6
        i = 3
            temp = 5
            ptr1 = 6
            ptr2 = max(6, 10) = 10
        
        """