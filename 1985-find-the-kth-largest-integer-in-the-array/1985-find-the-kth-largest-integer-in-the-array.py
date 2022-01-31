class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = list(map(int, nums))
        nums.sort()
        index=len(nums)-k
        return str(nums[index])
        