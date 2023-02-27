class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        prefix = [0] * 101
        
        for log in logs:
            prefix[log[0] - 1950] += 1
            prefix[log[1] - 1950] -= 1
        
        prefix = list(accumulate(prefix))
        return prefix.index(max(prefix)) + 1950