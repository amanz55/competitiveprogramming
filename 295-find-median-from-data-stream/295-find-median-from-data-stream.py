class MedianFinder:

    def __init__(self):
        self.max_list = []
        self.min_list = []
        self.count = 0
        
    def addNum(self, num: int) -> None:
        self.count += 1
        
        if self.count %2 == 0:
            heappush(self.min_list, num)
        else:
            heappush(self.max_list, -num)
        
        if self.count > 1 and -1*self.max_list[0] > self.min_list[0]:
            temp = self.max_list[0]
            heappushpop(self.max_list,-1*self.min_list[0])
            heappushpop(self.min_list,-1* temp)

    def findMedian(self) -> float:
        
        if self.count %2 == 0:
            return (-1*self.max_list[0] + self.min_list[0])/ 2
        else:
            return -1*self.max_list[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()