class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        answer = 0
        nums_length = len(nums)
        
        for i in range(nums_length):
            for j in range(nums_length):
                if j == i:
                    continue
                if nums[i] + nums[j] == target:
                    answer += 1
        return answer