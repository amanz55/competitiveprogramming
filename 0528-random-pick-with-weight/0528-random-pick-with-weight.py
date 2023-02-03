class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [w[0]]
        self.w = w
        for i in range(1, len(self.w)):
            self.prefix.append(self.prefix[-1] + self.w[i])

    def pickIndex(self) -> int:
        
        random_idx = random.randint(1, self.prefix[-1])
        
        idx = bisect.bisect_left(self.prefix, random_idx)
        
        return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()