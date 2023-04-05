class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        for i in range(1, n + 1):
            nums.append(i)
        visited = 0
        def checkIfVisited(i, visited):
            return visited & 1 << len(nums) - i - 1
        
        def backtrack(idx, path = []):
            nonlocal visited
            if len(path) == k:
                ans.append(path[:])
                return 
            for j in range(idx + 1, len(nums)):
                if not checkIfVisited(j, visited):
                    path.append(nums[j])
                    visited = visited | 1 << len(nums) - j - 1
                    backtrack(j, path)
                    visited = visited ^ 1 << len(nums) - j - 1
                    path.pop()
        ans = []
        backtrack(-1)
        return ans