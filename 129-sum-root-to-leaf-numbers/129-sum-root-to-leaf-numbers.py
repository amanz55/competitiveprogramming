# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.totalSum = 0
        def helper(root,string):
            if not root:
                return
            string += str(root.val)
            if not root.left and not root.right:
                self.totalSum += int(string)
                return
            helper(root.left,string)
            helper(root.right,string)
        
        helper(root, "")
        return self.totalSum