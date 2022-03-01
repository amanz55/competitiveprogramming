# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if not root:
                return
            
            root.left, root.right = invert(root.right), invert(root.left)
            return root
        
        return invert(root)