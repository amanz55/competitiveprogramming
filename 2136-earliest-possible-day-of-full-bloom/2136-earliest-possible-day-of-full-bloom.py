class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        num_plants = len(plantTime)
        time = list(zip(growTime, plantTime))
        
        time.sort(reverse = True)
        early_time = 0
        cur_time = 0
        
        for grow_time, plant_time in time:
            cur_time += plant_time
            early_time = max(early_time, cur_time + grow_time)
        
        return early_time