class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums)) - (sorted(nums)[0] == 0)