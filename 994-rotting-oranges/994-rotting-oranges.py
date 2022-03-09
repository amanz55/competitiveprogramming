from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque([])
        fresh = set()
        directions = [[0,-1], [-1,0], [0,1], [1,0]]
        minutes = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    rotten.append((i,j))
                    
        inbound = lambda row, col : 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        while fresh:
            size = len(rotten)
            if size == 0:
                return -1
            
            for i in range(size):
                tup = rotten.popleft()
                for i in directions:
                    a, b = tup[0] + i[0], tup[1] + i[1]
                    if inbound(a, b) and grid[a][b] == 1:
                        grid[a][b] = 2
                        fresh.discard((a, b))
                        rotten.append((a, b))
            minutes += 1
            
        return minutes
        
            
        