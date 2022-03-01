# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check(r1, level):
            if not r1:
                return 0
            if not r1.left and not r1.right:
                return level
            else:
                return max(check(r1.left, level + 1), check(r1.right, level + 1))
            
        def checkvalidity(root):
            if not root:
                return True
            if abs(check(root.left, 1) - check(root.right, 1)) <= 1:
                return checkvalidity(root.left) and checkvalidity(root.right)
            else:
                return False
            
        return checkvalidity(root)
        