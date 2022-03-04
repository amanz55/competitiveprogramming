class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minimum = []
        for i in range(len(matrix)):
            temp = (matrix[i][0],i,0)
            minimum.append(temp)
        heapq.heapify(minimum)
        
        for i in range(k-1):
            val = 0
            mytuple = heapq.heappop(minimum)
            col = mytuple[2] + 1
            if col == len(matrix):
                val = float('+inf')
            else:
                val = matrix[mytuple[1]][col]
            heapq.heappush(minimum, (val, mytuple[1], col))
            
        return minimum[0][0]
                
        