class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        
        if len(numbers) == 2:
            return [1,2]
        
        while start < end:
            need = target - numbers[start]
            if numbers[end] > need:
                end -= 1
            elif numbers[end] < need:
                start += 1
            else:
                return [start + 1, end + 1]
                
            
        