class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for i in range(1 << len(nums)):
            temp = []
            count = 0
            while i:
                if i & 1 == 1:
                    temp.append(nums[len(nums) - count - 1])
                i >>= 1
                count += 1
            answer.append(temp)
        return answer