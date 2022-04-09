class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i != len(grid) - 1 or j != len(grid[0]) - 1:
                    right = grid[i][j + 1] if j + 1 < n else float('inf')
                    bottom = grid[i + 1][j] if i + 1 < m else float('inf')
                    grid[i][j] += min(right, bottom)
                    
        return grid[0][0]
        
        
        
        
        
        
        
        # dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        # def inbound(row, col): 
        #     if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        #         return grid[row][col]
        #     else:
        #         return 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        # m = len(grid)
        # n = len(grid[0])
        # dp = [[0] * n for _ in range(m)]
        # dp[0][0] = grid[0][0]
        # for i in range(1, len(grid)):
        #     dp[i][0] = dp[i - 1][0] + grid[i][0]
        # for i in range(1, len(grid[0])):
        #     dp[0][i] = dp[0][i - 1] + grid[0][i]
        # print(dp)