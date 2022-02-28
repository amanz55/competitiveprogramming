# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def check(r1, level):
            if not r1:
                return float('inf')
            if not r1.left and not r1.right:
                return level
            else:
                return min(check(r1.left, level + 1), check(r1.right, level + 1))
            
        return check(root, 1)
        