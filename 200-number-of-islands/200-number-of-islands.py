from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [[0,-1], [-1,0], [0,1], [1,0]]
        islands = 0
        myque = deque([])
        
        inbound = lambda row, col : 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def bfs(a, b):
            myque.append((a,b))
            visited.add((a,b))

            while myque:
                size = len(myque)

                for i in range(size):
                    loc = myque.popleft()

                    for i in directions:
                        x, y = loc[0] + i[0], loc[1] + i[1]
                        if inbound(x, y) and grid[x][y] == "1" and (x, y) not in visited:
                            bfs(x, y)
            
        
        
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    if (i, j) not in visited:
                        islands += 1
                        bfs(i, j)
                        
        return islands
                
        