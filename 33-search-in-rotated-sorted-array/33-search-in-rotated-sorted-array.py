class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        best = len(nums)
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid 
            if nums[mid] >= nums[0]:
                left = mid + 1
            elif nums[mid] <= nums[0]:
                right = mid - 1
                best = min(best, mid)
                if right == 0:
                    break
        print(best)
         #now i got my minimum index
        if best == len(nums):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return -1
                
        elif target >= nums[best] and target <= nums[-1]:
            left = best
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return -1
        else:
            left = 0
            right = best

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return -1
            