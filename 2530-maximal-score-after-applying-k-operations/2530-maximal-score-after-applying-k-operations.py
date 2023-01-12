class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: - x, nums))
        heapq.heapify(nums)
        total = 0
        while k:
            curr = heapq.heappop(nums)
            total += -curr
            heapq.heappush(nums, -(math.ceil( - curr / 3)))
            k -= 1
        return total