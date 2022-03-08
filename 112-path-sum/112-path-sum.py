# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def traverse(rt, runsum):
            runsum += rt.val
            if not rt.left and not rt.right:
                if runsum == targetSum:
                    return True
                else:
                    return False
            elif not rt.left:
                return traverse(rt.right, runsum)
            elif not rt.right:
                return traverse(rt.left, runsum)
            else:
                return traverse(rt.left,runsum) or traverse(rt.right, runsum)
        
        return traverse(root, 0)
        