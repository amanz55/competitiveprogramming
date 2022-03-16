class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negatives = 0
        boom = len(grid[0])
        
        for i in range(len(grid)):
            left = 0
            right = boom - 1
            best = boom

            while left <= right:
                mid = left + (right - left) // 2

                if grid[i][mid] < 0:
                    right = mid - 1
                    best = min(best, mid)
                else:
                    left = mid + 1
                    
            negatives += boom - best
        
        
        return negatives