class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ROWS = COLS = 8
        directions = [(-1, -1), (1, 1), (1, -1), (-1, 1), (1, 0), (0, 1), (-1, 0), (0, -1)]
        queens_set = set(map(tuple, queens))
        ans = []
        
    
        for dx, dy in directions:
            curx, cury = king
            
            newx, newy = curx, cury
            while 0 <= newx < ROWS and 0 <= newy < COLS:
                
                if (newx, newy) in queens_set:
                    ans.append([newx, newy])
                    break
                    
                newx, newy = newx + dx, newy + dy
                    
        return ans
            
        