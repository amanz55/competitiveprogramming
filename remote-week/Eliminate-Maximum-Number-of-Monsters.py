class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        timeLeft=[]
        for i in range(len(dist)):
            timeLeft.append(dist[i]/speed[i])
        timeLeft.sort()
        print(timeLeft)
        for j in range(len(timeLeft)):
            if timeLeft[j]<=j:
                return j
        return len(timeLeft)    
