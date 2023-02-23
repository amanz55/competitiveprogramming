class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        length = len(nums)
        answer = 0
        
        for i in range(-500, 501):
            ranges = defaultdict(int)
            last = -1
            for num in nums:
                ranges[num] = ranges[num-i] + 1
                last = max(last, ranges[num])
            
            answer = max(last, answer)
        
        return answer