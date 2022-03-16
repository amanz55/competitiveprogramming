class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def is_valid(val):
            result = sum(map( lambda x : math.ceil(x / val), nums ))

            return False if result > threshold else True
        
        
        low, high = 1, 1000000
        
        best_answer = float('inf')
        while low <= high:
            mid = (low + high) // 2

                
            if is_valid(mid):
                best_answer = min(best_answer, mid)
                high = mid - 1
            else:
                low = mid + 1
        
#         nums.sort()
#         binary = []
#         for i in range(nums[-1]):
#             binary.append(i + 1)
        
        
#         left = 0
#         right = len(nums) - 1
#         best = n
        
#         while left <= right:
#             sums = 0
#             mid = left + (right - left) // 2
            
#             for i in nums:
#                 sums.append(i + )
            
#             if binary[mid] > target:
#                 right = mid - 1
#             elif binary[mid] < target:
#                 left = mid + 1
#             else:
#                 return mid
            
        return best_answer
        