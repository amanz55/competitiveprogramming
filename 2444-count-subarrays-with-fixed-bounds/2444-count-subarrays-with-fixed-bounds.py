class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        last_invalid = -1
        last_minimum = -1
        last_maximum = -1
        length = len(nums)
        
        
        for idx in range(length):
            if nums[idx] == minK:
                last_minimum = idx
            if nums[idx] == maxK:
                last_maximum = idx
                
            if nums[idx] > maxK or nums[idx] < minK:
                last_invalid = idx
                last_minimum = -1
                last_maximum = -1
                
            if last_minimum > -1 and last_maximum > -1:
                answer += min(last_minimum, last_maximum) - last_invalid
                
        return answer
                
            