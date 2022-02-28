# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def check(r1,runningSum):
            if not r1:
                return False
            
            runningSum += r1.val
            
            if not r1.left and not r1.right:
                return runningSum == targetSum
            
            return check(r1.left,runningSum) or check(r1.right, runningSum)
            
            
        
        return check(root,0)