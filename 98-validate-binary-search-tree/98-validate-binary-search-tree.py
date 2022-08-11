# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.val = float("-inf")
        self.flag = True
        def traverse(node):
            if node:
                traverse(node.left)
                if node.val <= self.val:
                    self.flag = False
                    return
                self.val = node.val
                # arr.append(node.val)
                # if len(arr) > 1 and node.val < arr[-2]:
                #     self.flag = False
                traverse(node.right)
                
        traverse(root)
        return self.flag
        