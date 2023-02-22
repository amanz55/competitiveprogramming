class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
        row_len = len(self.pre)
        col_len = len(self.pre[0])
        
        for i in range(1, row_len):
            for j in range(1, col_len):
                self.pre[i][j] = self.pre[i - 1][j] + self.pre[i][j - 1] - self.pre[i - 1][j - 1] + matrix[i - 1][j - 1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1
        one = self.pre[row2][col2]  - self.pre[row1 - 1][col2] - self.pre[row2][col1 - 1] + self.pre[row1 - 1][col1 - 1]
        
        return one


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)