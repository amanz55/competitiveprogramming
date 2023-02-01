class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        time, growing = 0, 0
        growth = list(zip(growTime, plantTime))
        
        growth.sort(reverse = True)
        
        for grow, plant in growth:
            time += plant
            growing = max(growing, time + grow)
        return growing