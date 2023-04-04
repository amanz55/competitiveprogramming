class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = 0
        def checkIfVisited(i, visited):
            return visited & 1 << len(nums) - i - 1
        
        def backtrack(path = []):
            nonlocal visited
            if len(path) == len(nums):
                ans.append(path[:])
                return 
            for j in range(len(nums)):
                if not checkIfVisited(j, visited):
                    path.append(nums[j])
                    visited = visited | 1 << len(nums) - j - 1
                    backtrack(path)
                    visited = visited ^ 1 << len(nums) - j - 1
                    path.pop()
        ans = []
        backtrack()
        return ans
                    