# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, rot: Optional[TreeNode]) -> int:
        self.totSum = 0
        def tilt(root):
            if not root:
                return 0
            elif not root.left and not root.right:
                return root.val
            else:
                left = tilt(root.left)
                right = tilt(root.right)
                val = abs(left - right)
                self.totSum += val
            
                return left + right + root.val
        tilt(rot)
            
        return self.totSum
        