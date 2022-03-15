# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        traversed = []
        def traverse(root):
            if not root:
                return
            
            traverse(root.left)
            if len(traversed) == 0:
                traversed.append(root)
            elif root.val < traversed[-1].val:
                traversed.append(root)
                i = -1
                val = 0 - len(traversed)
                while i > val and traversed[i].val < traversed[i - 1].val:
                    traversed[i].val, traversed[i - 1].val = traversed[i - 1].val, traversed[i].val
                    i -= 1
            elif root.val >= traversed[-1].val:
                traversed.append(root)
            
            traverse(root.right)
            
        traverse(root)