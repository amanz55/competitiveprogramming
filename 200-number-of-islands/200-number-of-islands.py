class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        inbound = lambda x,y : 0 <= x < len(grid) and 0 <= y < len(grid[0])
        visited =set()
        count = 0
        
        def dfs(r,c):
            visited.add((r,c))
            for direction in directions:
                nr, nc = r + direction[0], c + direction[1]
                if inbound(nr,nc) and (nr,nc) not in visited and grid[nr][nc] == "1":
                    dfs(nr,nc)
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in visited:
                    count += 1
                    dfs(i,j)
        return count
                    
            
        