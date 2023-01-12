class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        inbound = lambda x, y : 0 <= x < m and 0 <= y < n
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        start = []
        check = 1
        result = 0
        
        def dfs(row, col, visited):
            nonlocal result
            
            if grid[row][col] == -1:
                return 
            
            if grid[row][col] == 2 and len(visited) == check:
                result += 1
                return
            
            visited.add((row, col))
            for x, y in directions:
                if inbound(row + x, col + y) and (row + x, col + y) not in visited:
                    dfs(row + x, col + y, visited.copy())

        row, col = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row, col = i,j
                    
                elif grid[i][j] == 0:
                    check += 1
        start = set()
        start.add((row,col))
        dfs(row, col, start)
                           
        return result