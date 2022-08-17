class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        absans = []
        def backtrack(idx, path):
            total = sum(path)
            if total > target:
                return
            if total == target:
                absans.append(path)
            for i in range(idx, len(candidates)):
                backtrack(i, path + [candidates[i]])
        backtrack(0, [])
        return absans