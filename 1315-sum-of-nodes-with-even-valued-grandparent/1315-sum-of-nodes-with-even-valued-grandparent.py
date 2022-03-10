# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def dfs(rt, parent, grand, sums=0):
            if not rt:
                return sums
            if grand and grand.val % 2 == 0:
                sums += rt.val
                
            sums += dfs(rt.left, rt, parent) + dfs(rt.right, rt, parent)
            
            return sums
            
        return dfs(root, None, None, 0)
        
        