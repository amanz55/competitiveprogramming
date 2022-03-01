# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversed = []
        
        def traverse(r):
            if r is None:
                return
            
            traverse(r.left)
        
            traversed.append(r.val)
            
            traverse(r.right)
              
        traverse(root)
        
        
        
        
        return traversed
        