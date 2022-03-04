import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        if k < len(self.nums):
            while len(self.nums) > k:
                heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:
        if len(self.nums) != self.k:
            heapq.heappush(self.nums, val)
            return list(self.nums)[0]
        else:
            if list(self.nums)[0] < val:
                heapq.heappop(self.nums)
                heapq.heappush(self.nums, val)
                return list(self.nums)[0]
            else:
                return list(self.nums)[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)