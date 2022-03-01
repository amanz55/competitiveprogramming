# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def check(r1, level):
            if not r1:
                return 0
            if not r1.left and not r1.right:
                return level
            else:
                return max(check(r1.left, level + 1), check(r1.right, level + 1))
            
        self.absmax = 0
            
        def finalise(r):
            if r is None:
                return self.absmax
            leftwing = check(r.left, 1)
            rightwing = check(r.right, 1)
            if leftwing + rightwing > self.absmax:
                self.absmax = leftwing + rightwing
            
            if leftwing > rightwing:
                return finalise(r.left)
            elif rightwing > leftwing:
                return finalise(r.right)
            else:
                return self.absmax
            
        finalise(root)
            
        return self.absmax
                
            
        
        
        
        