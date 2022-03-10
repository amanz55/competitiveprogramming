class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """ 
        directions = [[0,-1], [-1,0], [0,1], [1,0]]
        myque = deque([])
        borders = []
        n,m = len(grid),len(grid[0])
        visited = set()
        
        def isBorder(i,j):
            nonlocal n,m
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                return True
            
        inbound = lambda row, col : 1 <= row < len(grid) and 1 <= col < len(grid[0])
            
        def bfs(a, b):
            myque.append((a,b))
            visited.add((a, b))

            while myque:
                size = len(myque)

                for i in range(size):
                    loc = myque.popleft()

                    for i in directions:
                        x, y = loc[0] + i[0], loc[1] + i[1]
                        if inbound(x, y) and grid[x][y] == "O" and (x, y) and (x, y) not in visited:
                            bfs(x, y)
                            
        
        for j in range(len(grid)):
                for i in range(len(grid[0])):                    
                    if grid[j][i] == "O" and isBorder(j,i):
                        borders.append((j, i))
        for i in borders:
            bfs(i[0], i[1])
            
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                if grid[i][j] == "O" and (i, j) not in visited:
                    grid[i][j] = "X"
            
        
        
            
        
        
#         for i in range(1,len(grid) - 1):
            
#             for j in range(1, len(grid[0]) - 1):
#                 if grid[i][j] == "O":
#                     bfs(i, j)
                        