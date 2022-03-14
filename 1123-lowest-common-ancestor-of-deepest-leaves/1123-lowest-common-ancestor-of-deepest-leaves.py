# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, rot: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def maxim(r1, level):
            if not r1:
                return 0
            if not r1.left and not r1.right:
                return level + 1
            else:
                return max(maxim(r1.left, level + 1), maxim(r1.right, level + 1))
        
        
        
        
        def maximum(root):
            left = maxim(root.left, 0)
            right = maxim(root.right, 0)
            if left == right:
                return root
            elif left > right:
                return maximum(root.left)
            else:
                return maximum(root.right)
            
        return maximum(rot)
        