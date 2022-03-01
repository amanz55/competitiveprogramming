# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.totalSum = 0
        def summer(root):
            if not root:
                return
            if root.left and  root.left.left == root.left.right == None:
                self.totalSum += root.left.val
                
            summer(root.left)
            summer(root.right)
            
        summer(root)
        
        return self.totalSum