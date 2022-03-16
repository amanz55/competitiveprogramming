# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n - 1
        best = n
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid + 1) == True:
                right = mid - 1
                best = min(best, mid + 1)
            else:
                left = mid + 1
                
        return best