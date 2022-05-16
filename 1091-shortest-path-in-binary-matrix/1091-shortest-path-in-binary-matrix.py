from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, image: List[List[int]]) -> int:
        n = len(image)
        if image[0][0] != 0 or image[n - 1][n - 1] != 0:
            return -1
        
        directions = [[0,-1], [-1,0], [0,1], [1,0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        
        self.abscount = float("+inf")
        
        inbound = lambda row, col : (0 <= row < n) and (0 <= col < n)
        
        myque = deque([(0, 0, 1, set((0, 0)))])
        
        
        while myque:
            res = myque.popleft()

            if res[0] == res[1] == n - 1:
                self.abscount = min(self.abscount, res[2])
            else:
                for i in directions:
                    x, y = res[0] + i[0], res[1] + i[1]
                    if (x, y) not in res[3] and ( inbound(x,y) ) and ( 0 == image[x][y]):
                        res[3].add((x, y))
                        myque.append((x, y, res[2] + 1, res[3] ))

                    
        return self.abscount if self.abscount != float("+inf") else -1
        
        
            