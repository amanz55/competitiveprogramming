# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def traverse(node):
            if node:
                traverse(node.left)
                arr.append(node.val)
                traverse(node.right)
                
        traverse(root)
        if arr == sorted(list(set(arr))):
            return True
        else:
            return False
        