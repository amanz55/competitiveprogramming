class Solution:
    def reversee(self, row):
        left, right = 0, len(row) - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1
        
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            self.reversee(row)