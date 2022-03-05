# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
            
        def checkneeded(r):
            
            if r is None:
                return 0

            if not r.left and not r.right:
                self.moves += abs(r.val - 1)
                return r.val - 1
            else:
                left = checkneeded(r.left) 
                right = checkneeded(r.right)
                self.moves += abs(left + right + r.val - 1)
                return left + right + r.val - 1
            
        checkneeded(root)
        return self.moves
            
            
            
            