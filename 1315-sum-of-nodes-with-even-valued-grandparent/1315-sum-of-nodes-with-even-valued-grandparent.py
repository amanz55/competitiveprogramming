# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sums = 0
        
        def dfs(rt, parent, grand):
            if not rt:
                return self.sums
            if grand and grand.val % 2 == 0:
                self.sums += rt.val
                
            dfs(rt.left, rt, parent)
            dfs(rt.right, rt, parent)
            
        dfs(root, None, None)
        return self.sums
        
        