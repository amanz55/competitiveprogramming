# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversed = []
        
        def traverse(r):
            if r is None:
                return
            
            traversed.append(r.val)
            
            traverse(r.left)
        
            
            traverse(r.right)
              
        traverse(root)
        
        
        
        
        return traversed