class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        answer = 0
        memo = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        inbound = lambda x, y: 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
        
        
        def dfs(i, j):
            
            if not inbound(i, j):
                return 0
            
            if memo[i][j]:
                return memo[i][j]
            
            maximum = 0
            
            for r, c in directions:
                row, col = i + r, j + c
                
                if not inbound(row, col) or matrix[row][col] > matrix[i][j]:
                    maximum = max(maximum, dfs(row, col))
                    
            memo[i][j] = maximum + 1  
            return maximum + 1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                answer = max(answer, dfs(i, j))
                
        return answer