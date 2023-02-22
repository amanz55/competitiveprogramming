class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        answer = 0
        count = defaultdict(int)
        
        for num in time:
            temp = (60 - (num % 60)) % 60
            
            if temp in count:
                answer += count[temp]
        
            count[num % 60] += 1
        return answer
        