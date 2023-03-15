# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        def solve(node, height):
            if not node:
                return height
            
            right = solve(node.right, height + 1)
            
            if self.max_height > right :
                self.ans = False
            
            
            left = solve(node.left, height + 1)
            
            if self.max_height > left:
                self.ans = False
            
            self.max_height = max(self.max_height, left, right)
            self.min_height = min(self.min_height, left, right)
            
            if abs(self.min_height - self.max_height) > 1:
                self.ans = False
            
            
            return left
        
        self.ans = True
        self.max_height = -1
        self.min_height = 101
        
        solve(root, 0)
        return self.ans