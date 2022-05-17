# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        self.nod = None
        
        def dfs(node):
            if not node:
                return
            elif node.val == target.val:
                self.nod = node
            else:
                dfs(node.left)
                dfs(node.right)
        dfs(cloned)
                
        return self.nod