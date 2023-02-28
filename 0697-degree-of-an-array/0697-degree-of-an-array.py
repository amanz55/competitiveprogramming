class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        large = max(count.values())
        first_last = {}
        answer = inf
        
        
        for i, val in enumerate(nums):
            if count[val] == large:
                if val in first_last:
                    first_last[val][1] = i
                else:
                    first_last[val] = [i, i]
        for key in first_last:
            first, last = first_last[key]
            answer = min(answer, last - first + 1)
                
        return answer