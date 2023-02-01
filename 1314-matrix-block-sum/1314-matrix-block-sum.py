class Solution:
    def findTotal(self, row, col, m, n, k):
        br_row = min(row + k, m)
        br_col = min(col + k, n)
        tl_row = max(row - k - 1, 0)
        tl_col = max(col - k - 1, 0)
        return br_row, br_col, tl_row, tl_col
        
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        prefix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                prefix[row][col] = prefix[row - 1][col] + prefix[row][col - 1] + mat[row - 1][col -1] - prefix[row - 1][col -1]
        
        for row in range(m):
            for col in range(n):
                brow, bcol, trow, tcol = self.findTotal(row + 1, col + 1, m, n, k)
                mat[row][col] = prefix[brow][bcol] - prefix[trow][bcol] - prefix[brow][tcol] + prefix[trow][tcol]
                
        return mat