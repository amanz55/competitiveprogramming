class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pospeed = []
        before = []
        for i in range(len(position)):
            pospeed.append([position[i],speed[i]])
        pospeed.sort()
        
        for i in range(len(pospeed) - 1,-1,-1):
            t = (target - pospeed[i][0]) / pospeed[i][1]
            if len(before) == 0:
                before.append(t)
            elif t > before[-1]:
                before.append(t)
                
        return len(before)
                
                
        
        
        
        
        