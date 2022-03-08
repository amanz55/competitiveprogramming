class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = set()
        directions = [[0,-1], [-1,0], [0,1], [1,0]]
        row , col = sr, sc
        startingColor = image[sr][sc]
        
        inbound = lambda row, col : (0 <= row < len(image)) and (0 <= col < len(image[0]))
        def dfs(row, col):
            image[row][col] = newColor
            visited.add((row, col))
            for i in directions:
                x, y = row + i[0], col + i[1]
                if (x, y) not in visited and ( inbound(x,y) ) and ( startingColor == image[x][y]):
                    dfs(x, y)
                    
        dfs(sr, sc)
        return image
                
        
        