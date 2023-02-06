class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        
        while queue:
            n = len(queue)
            
            for i in range(n):
                cur, speed, level = queue.popleft()
                
                if cur == target:
                    return level
                
                queue.append((cur + speed, 2 * speed, level + 1))
                temp = cur + speed
                if (temp > target and speed > 0) or (temp < target and speed < 0):
                    if (speed > 0):
                        s = -1
                    else:
                        s = 1
                        
                    queue.append((cur, s, level + 1))