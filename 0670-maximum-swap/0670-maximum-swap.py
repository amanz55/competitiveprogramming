class Solution:
    def maximumSwap(self, num: int) -> int:
        maximum = num
        num = list(str(num))
        
        
        
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                num[i], num[j] = num[j], num[i]
                maximum = max(maximum, int("".join(num)))
                num[i], num[j] = num[j], num[i]
        
        return maximum
            
        