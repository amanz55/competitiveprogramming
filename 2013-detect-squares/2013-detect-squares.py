class DetectSquares:

    def __init__(self):
        self.pairs = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pairs[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        
        answer = 0
        
        
        for pnt in self.pairs:
            if pnt[1] == point[1] and pnt[0] != point[0]:
                
                length = abs(point[0] - pnt[0])
                
                one = (pnt[0], pnt[1] - length)
                two = (point[0], point[1] - length)
                three = self.pairs[pnt]
                
                if (one in self.pairs) and (two in self.pairs):
                    answer += (self.pairs[one] * self.pairs[two] * three)
                
                one = (pnt[0], pnt[1] + length)
                two = (point[0], point[1] + length)
                
                if (one in self.pairs) and (two in self.pairs):
                    answer += (self.pairs[one] * self.pairs[two] * three)
                    
        return answer
                    
                
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)