class Solution:
    def movement(self, direction, x, y):
        finalx, finaly = x, y
        
        if direction == 'N':
            finaly += 1
        elif direction == 'S':
            finaly -= 1
        elif direction == 'E':
            finalx += 1
        elif direction == 'W':
            finalx -= 1          
        
        return finalx, finaly
        
        
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        directions = ['N', 'E', 'S', 'W']
        index = 0
        for _ in range(4):
            for inst in instructions:
                if inst == 'G':
                    x, y = self.movement(directions[index], x, y)
                elif inst == 'R':
                    index = (index + 1) % 4
                else:
                    index = (index - 1) % 4
        
        return x == 0 and y == 0