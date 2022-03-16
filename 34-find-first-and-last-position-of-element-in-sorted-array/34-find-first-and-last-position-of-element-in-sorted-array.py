class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        self.first = len(nums)
        self.last = 0
        check = True
        
        def goleft(right, left, target):
            print(right,left,target)
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    self.first = min(self.first, mid)
            return
            
        def goright(right, left, target):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    left = mid + 1
                    self.last = max(self.last, mid)
            return
            
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                goleft(mid, 0, target)
                goright(len(nums) - 1, mid, target)
                check = False
                break
        if check == False:
            return [self.first, self.last]
        else:
            return [-1, -1]