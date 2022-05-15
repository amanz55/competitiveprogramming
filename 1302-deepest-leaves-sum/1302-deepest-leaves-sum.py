# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.sums = 0
        self.maxlevel = 0
        def getdepth(roo, maxlevel):
            if not roo:
                self.maxlevel = max(maxlevel, self.maxlevel)
            else:
                getdepth(roo.left, maxlevel + 1)
                getdepth(roo.right, maxlevel + 1)
            
            
            
        def dfs(node, level):
            if not node.left and not node.right:
                if level == self.maxlevel:
                    self.sums += node.val
            elif not node.right:
                dfs(node.left, level + 1)
            elif not node.left:
                dfs(node.right, level + 1)
            else:
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)
                
        getdepth(root, 0)
        dfs(root, 1)
        return self.sums